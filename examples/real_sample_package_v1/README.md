# Real sample package v1

[中文说明](README.zh-CN.md)

This compact package contains real, human-reviewed examples from the three annotation components of **Geographically Diverse Forest Annotation Dataset**. It supports format inspection, visualisation and data-loader development.

These are demonstration formats. The full dataset uses RGB PNG/JPEG canopy masks, SVG treetop markers and COCO JSON crown annotations. See the [main README](../../README.md) for the release inventory and data-access link.

## Package summary

| Component | Samples | Example image size | Included data |
|:--|--:|:--:|:--|
| Canopy-region masks | 4 | 1024 × 1024 px | Overlay previews, binary PNG/TIFF masks and coverage statistics |
| Treetop points | 4 | 1024 × 1024 px | Overlay previews and point coordinates in CSV/JSON |
| Individual-crown polygons | 4 | 512 × 512 px | RGB images, contour previews, TIFF instance masks and crown-area tables |

The canopy examples span approximately 17–93% labelled canopy coverage. The treetop examples span 50–358 independently hand-drawn points per example. The crown examples contain 163–243 manually delineated instances per image.

## Directory structure

```text
real_sample_package_v1/
├── 01_canopy_region_masks/
├── 02_treetop_points/
├── 03_individual_crown_polygons/
├── sample_index.csv
├── manifest.csv
└── checksums.sha256
```

Each component directory contains its own README and one folder per sample. `manifest.csv` records file sizes and SHA-256 hashes; `checksums.sha256` supports direct integrity verification.

## Coordinate and label conventions

- Image coordinates use a top-left origin, with `x` increasing rightward and `y` increasing downward.
- Canopy masks are binary raster labels aligned to 1024 × 1024 preview coordinates.
- Treetop coordinates are integer pixel locations in 1024 × 1024 example images.
- The manuscript's 2 km × 2 km extent describes full source scenes. This package records example pixel dimensions but does not supply a per-example geographic transform or ground footprint; do not infer ground area from preview size.
- Individual-crown TIFF masks use `0` for background and positive integer IDs for crown instances in 512 × 512 images.

## Provenance note

All annotations in this package are human-produced or human-corrected release examples. The treetop points included here were independently redrawn from scratch. Obsolete `score` and `source` fields created by the annotation web interface were deliberately omitted because they do not describe the provenance of these manual re-annotations.

## Access and licence

Binary masks, point records, instance masks, crown-area tables and package metadata are licensed under [CC BY 4.0](../../LICENSE-DATA.md). Source images and imagery-bearing overlays or previews remain governed by source-specific terms described in the [third-party imagery notice](../../THIRD_PARTY_NOTICES.md).
