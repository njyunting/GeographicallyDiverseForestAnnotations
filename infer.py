"""Single-image or folder inference for tree-crown topflow CellposeSAM."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import cv2
import numpy as np
import tifffile
import torch

from cellpose import core, dynamics, io, plot, transforms
from tree_crown_utils import create_tree_crown_model, resolve_device, summarize_mask_classes


PROJECT_ROOT = Path(__file__).resolve().parent
DEFAULT_MODEL = PROJECT_ROOT / "models" / "tree_crown_cpsam_topflow"
DEFAULT_EXTENSIONS = ".png,.jpg,.jpeg,.tif,.tiff,.bmp"


def parse_args():
    parser = argparse.ArgumentParser(
        description="Infer tree-crown instances and conifer/broadleaf classes."
    )
    parser.add_argument("--input", required=True, type=Path, help="one image or one image directory")
    parser.add_argument("--model", type=Path, default=DEFAULT_MODEL)
    parser.add_argument("--output-dir", type=Path, default=PROJECT_ROOT / "outputs")
    parser.add_argument("--extensions", default=DEFAULT_EXTENSIONS, help="comma-separated suffixes for directory input")
    parser.add_argument("--recursive", action="store_true")
    parser.add_argument("--batch-size", type=int, default=1)
    parser.add_argument("--bsize", type=int, default=256)
    parser.add_argument("--tile-overlap", type=float, default=0.1)
    parser.add_argument("--cellprob-threshold", type=float, default=0.0)
    parser.add_argument("--flow-threshold", type=float, default=0.4)
    parser.add_argument("--min-size", type=int, default=15)
    parser.add_argument("--niter", type=int, default=200)
    parser.add_argument("--filter-min-area", type=int, default=0)
    parser.add_argument("--filter-max-aspect", type=float, default=0.0)
    parser.add_argument("--filter-min-extent", type=float, default=0.0)
    parser.add_argument("--contour-width", type=int, default=2)
    parser.add_argument("--device", choices=["auto", "cuda", "cpu"], default="auto")
    parser.add_argument("--mask-device", choices=["auto", "cuda", "cpu"], default="cpu")
    parser.add_argument("--no-save-fields", action="store_true", help="do not save cell probability and raw flow TIFFs")
    parser.add_argument("--skip-existing", action="store_true")
    return parser.parse_args()


def _resolve_images(input_path: Path, extensions: str, recursive: bool):
    input_path = input_path.resolve()
    if input_path.is_file():
        return input_path.parent, [input_path]
    if not input_path.is_dir():
        raise FileNotFoundError(f"input not found: {input_path}")
    suffixes = {
        item.strip().lower() if item.strip().startswith(".") else "." + item.strip().lower()
        for item in extensions.split(",")
        if item.strip()
    }
    iterator = input_path.rglob("*") if recursive else input_path.glob("*")
    images = sorted(path for path in iterator if path.is_file() and path.suffix.lower() in suffixes)
    if not images:
        raise FileNotFoundError(f"no images with suffixes {sorted(suffixes)} in {input_path}")
    return input_path, images


def _load_and_normalize(image_path: Path):
    image = io.imread(str(image_path))
    image = transforms.convert_image(image, channel_axis=None, z_axis=None, do_3D=False)
    if image.ndim < 4:
        image = image[np.newaxis, ...]
    return transforms.normalize_img(
        image,
        lowhigh=None,
        percentile=None,
        normalize=True,
        norm3D=True,
        sharpen_radius=0,
        smooth_radius=0,
        tile_norm_blocksize=0,
        tile_norm_smooth3D=1,
        invert=False,
    )


def _display_rgb(image_path: Path):
    image = io.imread(str(image_path))
    image = np.asarray(image)
    if image.ndim == 2:
        image = np.repeat(image[..., None], 3, axis=-1)
    elif image.ndim == 3:
        if image.shape[0] <= 4 and image.shape[-1] > 4:
            image = np.moveaxis(image, 0, -1)
        if image.shape[-1] == 1:
            image = np.repeat(image, 3, axis=-1)
        image = image[..., :3]
    else:
        raise ValueError(f"overlay supports 2D images only, got shape {image.shape}")
    image = image.astype(np.float32)
    low, high = np.percentile(image, (1, 99))
    if high <= low:
        high = low + 1.0
    return np.clip((image - low) * (255.0 / (high - low)), 0, 255).astype(np.uint8)


def _relabel(masks):
    output = np.zeros_like(masks, dtype=np.int32)
    next_id = 1
    for label_id in range(1, int(masks.max()) + 1):
        pixels = masks == label_id
        if pixels.any():
            output[pixels] = next_id
            next_id += 1
    return output


def _filter_shapes(masks, min_area: int, max_aspect: float, min_extent: float):
    if min_area <= 0 and max_aspect <= 0 and min_extent <= 0:
        return masks.astype(np.int32)
    keep = np.zeros_like(masks, dtype=bool)
    for label_id in range(1, int(masks.max()) + 1):
        yy, xx = np.nonzero(masks == label_id)
        if len(yy) == 0:
            continue
        height, width = int(yy.max() - yy.min() + 1), int(xx.max() - xx.min() + 1)
        area = int(len(yy))
        aspect = max(height / max(width, 1), width / max(height, 1))
        extent = area / max(height * width, 1)
        if min_area > 0 and area < min_area:
            continue
        if max_aspect > 0 and aspect > max_aspect:
            continue
        if min_extent > 0 and extent < min_extent:
            continue
        keep[masks == label_id] = True
    return _relabel(np.where(keep, masks, 0))


def _draw_overlay(rgb, masks, classes, contour_width: int):
    overlay = rgb.copy()
    colors = {1: np.array([0, 220, 255], dtype=np.uint8), 2: np.array([255, 210, 0], dtype=np.uint8)}
    for label_id, details in classes.items():
        pixels = masks == label_id
        color = colors[details["class_id"]]
        overlay[pixels] = (0.55 * overlay[pixels] + 0.45 * color).astype(np.uint8)
        contours, _ = cv2.findContours(pixels.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(overlay, contours, -1, color.tolist(), contour_width, lineType=cv2.LINE_AA)
    return overlay


def _write_csv(path: Path, image_path: Path, mask_path: Path, classes: dict):
    fields = [
        "image", "mask_tif", "label_id", "class_id", "class_name", "class_probability",
        "background_probability", "conifer_probability", "broadleaf_probability", "area_pixels",
    ]
    with path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for label_id, details in classes.items():
            writer.writerow({"image": str(image_path), "mask_tif": str(mask_path), "label_id": label_id, **details})


def _predict(model, image_path: Path, args, mask_device):
    image = _load_and_normalize(image_path)
    with torch.inference_mode():
        network_output, _ = core.run_net(
            model,
            image,
            batch_size=args.batch_size,
            bsize=args.bsize,
            tile_overlap=args.tile_overlap,
        )
    prediction = network_output[0]
    class_logits = prediction[..., :3].transpose(2, 0, 1)
    flow = prediction[..., -3:-1].transpose(2, 0, 1)
    cell_probability = prediction[..., -1]
    masks = dynamics.resize_and_compute_masks(
        flow,
        cell_probability,
        niter=args.niter,
        cellprob_threshold=args.cellprob_threshold,
        flow_threshold=args.flow_threshold,
        min_size=args.min_size,
        device=mask_device,
    )
    masks = _filter_shapes(masks, args.filter_min_area, args.filter_max_aspect, args.filter_min_extent)
    classes = summarize_mask_classes(masks, class_logits)
    return masks, classes, cell_probability, flow


def main():
    args = parse_args()
    if args.batch_size < 1 or not 0 <= args.tile_overlap < 1:
        raise ValueError("batch-size must be >=1 and tile-overlap must be in [0,1)")
    if args.bsize != 256:
        raise ValueError("this ViT-L checkpoint requires --bsize 256")
    if args.min_size < 0 or args.niter < 1 or args.contour_width < 1:
        raise ValueError("min-size must be >=0; niter and contour-width must be >=1")
    input_root, images = _resolve_images(args.input, args.extensions, args.recursive)
    output_root = args.output_dir.resolve()
    output_root.mkdir(parents=True, exist_ok=True)
    device = resolve_device(args.device)
    mask_device = resolve_device(args.mask_device)
    print(f"model device: {device}; mask device: {mask_device}; images: {len(images)}")
    model = create_tree_crown_model(args.model.resolve(), device=device, dtype=torch.float32)
    model.eval()

    batch_summary = []
    for index, image_path in enumerate(images, start=1):
        relative_parent = image_path.parent.relative_to(input_root) if input_root.is_dir() else Path()
        out_dir = output_root / relative_parent / image_path.stem
        summary_path = out_dir / f"{image_path.stem}_summary.json"
        if args.skip_existing and summary_path.is_file():
            print(f"[{index}/{len(images)}] skip existing {image_path}")
            batch_summary.append(json.loads(summary_path.read_text(encoding="utf-8")))
            continue
        out_dir.mkdir(parents=True, exist_ok=True)
        masks, classes, cell_probability, flow = _predict(model, image_path, args, mask_device)
        prefix = out_dir / image_path.stem
        mask_path = prefix.with_name(prefix.name + "_masks.tif")
        overlay_path = prefix.with_name(prefix.name + "_overlay.png")
        csv_path = prefix.with_name(prefix.name + "_instances.csv")
        tifffile.imwrite(mask_path, masks.astype(np.uint32), compression="zlib")
        overlay = _draw_overlay(_display_rgb(image_path), masks, classes, args.contour_width)
        cv2.imwrite(str(overlay_path), cv2.cvtColor(overlay, cv2.COLOR_RGB2BGR))
        _write_csv(csv_path, image_path, mask_path, classes)

        outputs = {"masks": str(mask_path), "overlay": str(overlay_path), "instances_csv": str(csv_path)}
        if not args.no_save_fields:
            cellprob_path = prefix.with_name(prefix.name + "_cellprob.tif")
            flow_path = prefix.with_name(prefix.name + "_flows.tif")
            flow_hsv_path = prefix.with_name(prefix.name + "_flow_hsv.png")
            tifffile.imwrite(cellprob_path, cell_probability.astype(np.float32), compression="zlib")
            tifffile.imwrite(flow_path, flow.astype(np.float32), compression="zlib")
            flow_hsv = plot.dx_to_circ(flow)
            flow_hsv[masks == 0] = 0
            cv2.imwrite(str(flow_hsv_path), cv2.cvtColor(flow_hsv, cv2.COLOR_RGB2BGR))
            outputs.update(cellprob=str(cellprob_path), flows=str(flow_path), flow_hsv=str(flow_hsv_path))

        summary = {
            "image": str(image_path),
            "model": str(args.model.resolve()),
            "num_masks": int(masks.max()),
            "num_conifer": sum(item["class_id"] == 1 for item in classes.values()),
            "num_broadleaf": sum(item["class_id"] == 2 for item in classes.values()),
            "parameters": {
                "cellprob_threshold": args.cellprob_threshold,
                "flow_threshold": args.flow_threshold,
                "min_size": args.min_size,
                "niter": args.niter,
                "filter_min_area": args.filter_min_area,
                "filter_max_aspect": args.filter_max_aspect,
                "filter_min_extent": args.filter_min_extent,
            },
            "instances": {str(key): value for key, value in classes.items()},
            "outputs": outputs,
        }
        summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
        batch_summary.append(summary)
        print(f"[{index}/{len(images)}] {image_path.name}: masks={summary['num_masks']} -> {out_dir}")

    batch_path = output_root / "batch_inference_summary.json"
    batch_path.write_text(json.dumps(batch_summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"batch summary: {batch_path}")


if __name__ == "__main__":
    main()
