<div align="center">

<img src="assets/readme/repository-banner-geodiverse.webp" width="100%" alt="Geographically Diverse Forest Annotation Dataset repository banner">

**English** | [中文](README.zh-CN.md)

**Forest canopy masks, treetop points and individual tree crown polygons derived from satellite RGB imagery across 19 countries.**

[![Coverage](https://img.shields.io/badge/coverage-19%20countries-2E6EB5?style=for-the-badge)](#geographic-coverage)
[![Annotation](https://img.shields.io/badge/annotation-human%20reviewed-00A67E?style=for-the-badge)](#annotation-production)
[![Samples](https://img.shields.io/badge/examples-12%20samples-7357A5?style=for-the-badge)](examples/real_sample_package_v1/)
[![Data](https://img.shields.io/badge/data-Zenodo-1682D4?style=for-the-badge)](https://doi.org/10.5281/zenodo.22070748)

[Overview](#overview) · [Demos](#annotation-demos) · [Gallery](#scene-gallery) · [Dataset](#dataset-components) · [Coverage](#geographic-coverage) · [Annotation](#annotation-production) · [Validation](#technical-validation) · [Access](#data-access) · [Examples](#real-sample-package) · [Contributors](#contributors-and-institutions)

</div>

## Overview

**Full dataset:** [Download from Zenodo](https://doi.org/10.5281/zenodo.22070748).

This geographically diverse forest annotation dataset contains satellite colour (RGB) images from 19 countries and three types of labels:

- **Forest canopy masks:** label the area covered by forest canopy.
- **Treetop points:** mark each tree's crown apex with a color dot.
- **Individual tree crown polygons:** delineate the dripline of the individual tree crown.

### Applications and research value

- **Measure canopy cover and study forest structure.** Canopy masks can be used to calculate canopy area and cover percentage, identify gaps, and study whether canopy forms continuous cover or separate patches. Models trained on these labels can identify canopy cover in satellite images for forest cover surveys and urban tree cover landscape.
- **Locate and count trees, and study their distribution**. Treetop points can be used to train and test models that locate trees in satellite images and estimate their number, density and distribution. Researchers can also change the treetop point size and study how to train tree detection models using position markers alone, reducing the need to trace every crown.
- **Separate neighbouring crowns and measure individual crown size and shape.** Crown polygons can be used to train individual crown segmentation models, extract crown outlines, areas and shapes, and compare crown sizes within a stand. In dense areas with touching or overlapping crowns, the manual outlines help check whether a model misses crowns or merges several crowns into one.

Forests differ across regions in crown shape, density, background and imaging conditions. These labels can be used to study whether a model trained in one region still identifies trees accurately in another. They also allow comparisons across sparse trees, dense stands and complex backgrounds, helping researchers identify missed and false detections, improve recognition methods and reduce manual labelling in large-area surveys.

| Annotation type | Dataset size | Scene or image size | File format |
|:--|:--|:--|:--|
| **Forest canopy masks** | **27 masks; 108 km²** | 2 km × 2 km per scene | RGB mask images in PNG/JPEG opened by photoshop software |
| **Treetop points** | **1,648,847 points in 30 SVG files; 120 km²** | 2 km × 2 km per scene | SVG vector markers opened by Inkscape 1.0 software. |
| **Individual tree crown polygons** | **299,906 annotations in 5,061 RGB images** | 512 × 512 pixels per image | PNG/JPEG images and COCO JSON annotations |

### Image and annotation examples

<table>
  <tr>
    <td width="33.33%" align="center">
      <img src="assets/readme/canopy-region-example.webp" width="100%" alt="Source RGB forest scene"><br><b>01 · RGB image</b><br><sub>Source scene</sub>
    </td>
    <td width="33.33%" align="center">
      <img src="assets/readme/treetop-points-example.webp" width="100%" alt="Red treetop markers in the same scene"><br><b>02 · Treetop points</b><br><sub>Individual crown apices</sub>
    </td>
    <td width="33.33%" align="center">
      <img src="assets/readme/crown-polygons-example.webp" width="100%" alt="Coloured crown outlines in the same scene"><br><b>03 · Crown polygons</b><br><sub>Individual crown boundaries</sub>
    </td>
  </tr>
</table>

From left to right: the source image, crown apices marked with red dots, and the outlines of individual tree crowns.

## Annotation demos

<table>
  <tr>
    <td width="50%" align="center">
      <a href="assets/readme/treetop-annotation-demo.mp4"><img src="assets/readme/treetop-annotation-demo.webp" width="100%" alt="Treetop-point annotation demonstration"></a>
      <br><b>Treetop-point annotation</b>
    </td>
    <td width="50%" align="center">
      <a href="assets/readme/crown-annotation-demo.mp4"><img src="assets/readme/crown-annotation-demo.webp" width="100%" alt="Individual-crown annotation demonstration"></a>
      <br><b>Individual-crown annotation</b>
    </td>
  </tr>
</table>

Treetops are marked tree by tree across each **2 km × 2 km** scene. The demonstrations show details of marking crown apices and tracing individual crowns in enlarged sections of the images.

## Dataset components

### 1. Forest canopy masks

Forest canopy masks delineate the area covered by tree crowns, including isolated crowns and continuous canopy. Gaps between crowns, roads, buildings, water and bare ground are labelled as background.

**All 27 masks were delineated manually in Adobe Photoshop 2022**, with each covering **2 km × 2 km**. The full dataset stores masks as RGB PNG/JPEG images; the example package also provides binary PNG/TIFF masks.

### 2. Treetop points

Crown apices are identified from crown shape and foliage texture. In views of conifers from above, branch and foliage patterns converge towards the crown centre, indicating the apex. In angled views, the visible top of the crown is used. Annotators mark these locations with red dots in Inkscape. For broad-leaved trees and other crowns without a clear apex, they estimate and mark the crown centre from its outline and texture.

The release contains **1,648,847 points in 30 SVG files** **created using Inkscape 1.0**, each corresponding to a **2 km × 2 km** scene.

<details>
<summary>Details for reading SVG markers</summary>

Point locations are stored in SVG canvas coordinates. Convert them using the canvas extent and image dimensions, then check their alignment with the image. Red dots may be stored as circles, ellipses or paths, with colour set directly on an element or through CSS. Read all of these marker types and colour settings to avoid missing points.

</details>

### 3. Individual tree crown polygons

Each polygon traces an individual tree crown. Where neighbouring crowns touch or partly overlap, annotators use crown shape, foliage texture and local edges to identify and trace their separate outlines.

The dataset contains **5,061 RGB images and 299,906 crown annotations**. Each image is 512 × 512 pixels. Three images contain no labelled crowns and are included as training examples of background. Crown annotations are provided in COCO JSON, with one category, `tree_crown`.

<details>
<summary>COCO files and coordinate conventions</summary>

There are 4,875 PNG and 186 JPEG images; 5,058 images contain crown labels. Each annotation records image and annotation IDs, polygon coordinates, a bounding box `[x, y, width, height]`, area in square pixels, `category_id = 1` and `iscrowd = 0`. Coordinates start at the upper-left corner, with x increasing rightwards and y downwards. There are 299,895 records with one polygon and 11 with two polygons.

</details>

The crown images are split **by source scene** into training, validation and test sets. All crops from one original image stay in the same set, keeping nearby areas out of separate training and test sets.

| Split | Images | Crown annotations |
|:--|--:|--:|
| Training | 4,144 | 255,983 |
| Validation | 247 | 8,244 |
| Test | 670 | 35,679 |
| **Total** | **5,061** | **299,906** |

## Geographic coverage

<div align="center">

<img src="assets/readme/geographic-distribution.png" width="100%" alt="Geographic sampling distribution and annotation statistics">

</div>

The dataset covers **19 countries**: Angola, Australia, Austria, Brazil, Canada, China, Denmark, Finland, Germany, India, Italy, Japan, Lebanon, Russia, Spain, Sweden, Switzerland, Ukraine and the United States. It includes coniferous, broad-leaved, mixed and planted forests, with sparse trees, scattered canopy patches and dense continuous canopy, as well as trees in farmland, cities and surrounding areas.

Triangles, stars and circles mark scene locations for canopy masks, treetop points and individual crowns, respectively. The charts below the map show canopy annotation scene area, treetop point counts and individual crown counts by forest and vegetation type.

### Image sources and pixel size

RGB satellite images were obtained mainly through Google Earth Pro, including images from WorldView, QuickBird and SPOT. Image selection prioritised clear, cloud-free views acquired within the five years before annotation. Older clear images were used when recent images did not meet these requirements.

The **exported image pixel size is 0.0651–0.1237 m**, calculated from the scene extent and image dimensions in pixels. It describes the ground length represented by each exported pixel; the resolution of the original satellite image depends on its source. Acquisition dates, image sources, scene locations, image dimensions and exported pixel sizes are recorded in `scene_metadata.csv`.

## Scene gallery

<div align="center">

<img src="assets/readme/representative-scene-atlas-v3.webp" width="100%" alt="Canopy masks, treetop points and individual crown outlines across forest scenes">

</div>

The left two columns show canopy masks, the middle two show treetop points, and the right two show individual crown outlines. Green areas mark canopy cover, red dots mark crown apices, and coloured outlines distinguish individual crowns. The gallery includes sparse trees, dense stands, canopy gaps and trees near roads or buildings.

## Annotation production

Nine trained annotators completed the labels. Canopy masks were traced manually in Photoshop, and crown apices were marked with red dots in Inkscape. For individual crowns, approximately **70% of images** were annotated manually from scratch. For approximately **30% of images**, a fine-tuned Cellpose-SAM model generated initial outlines, which were then checked and corrected manually.

Annotators separated crowns that the model had merged, joined fragments of the same crown, added missing crowns, removed false detections and adjusted outlines. All crown labels were checked manually, then reviewed in batches by three reviewers. One additional lead reviewer checked the complete dataset.

Software checked that files could be read, images matched their labels, IDs were unique, coordinates stayed within image bounds and crown polygons were valid. Problems were corrected and checked again.

## Technical validation

An independent annotator labelled **214 image samples** without viewing the original labels: 59 canopy tiles, 26 treetop tiles and 129 crown images. The comparison between the two label sets is shown below.

| Annotation type | Validation sample | Matching or comparison | Agreement |
|:--|:--|:--|:--|
| Forest canopy masks | 59 tiles from 21 scenes | Pixel-wise binary-mask overlap | Mean IoU **0.914**; mean Dice **0.948** |
| Treetop points | 26 tiles from 17 scenes | One-to-one matching within **15 pixels** | Mean tile F1 **0.851**; count MAE **25.0 points/tile** |
| Individual tree crowns | 129 image patches | One-to-one matching at **IoU ≥ 0.50** | Mean image detection F1 **0.864**; median matched-crown IoU **0.807** |

IoU and Dice measure how much the two masks overlap. Treetop F1 measures whether both annotators marked the same trees, allowing a position difference of up to 15 pixels. Count MAE gives the average difference in point counts per image tile. Crown IoU measures overlap between matched outlines, while detection F1 considers matched, missed and extra crowns.

### Model evaluation

| Task | Models | Range of model results |
|:--|:--|:--|
| Canopy segmentation | U-Net, DeepLabv3+, SegFormer | Test IoU **79.49–81.74%**; Dice **88.52–89.93%** |
| Treetop localisation | U-Net, SegFormer, Mamba-UNet | Test point F1 **72.65–76.33%**; count MAE **24.65–28.47 points/tile** |
| Crown instance segmentation | Mask R-CNN, YOLOv8m-seg, Mask2Former, QueryInst, MaskDINO, StarDist-TCD | Mask AP50:95 **26.51–52.44%**; AP50 **42.73–83.84%** |

Each model was evaluated after one training run. MaskDINO had the highest AP50:95 and AP50 among the crown models compared.

## Data access

The full dataset is available through [Zenodo DOI 10.5281/zenodo.22070748](https://doi.org/10.5281/zenodo.22070748), including canopy masks, treetop SVG files, crown images and COCO annotations, scene information and documentation. Crown annotations include cropped RGB images. The full original scene images are not included.

### Full dataset files

The full dataset archive is organised as follows:

```text
dataset/
├── canopy_region/                 # 27 PNG/JPEG canopy masks
├── treetop/                       # 30 SVG point-annotation files
├── individual_crown/
│   └── images/                    # 5,061 RGB images, 512 × 512 px
├── annotations/
│   ├── instances_all.json
│   ├── instances_train.json
│   ├── instances_val.json
│   └── instances_test.json
└── scene_metadata.csv
```

## Real sample package

[`examples/real_sample_package_v1`](examples/real_sample_package_v1/) contains **12 examples** with annotation previews and the label files listed below, for exploring the labels and reading their formats.

| Component | Examples | Demonstration files |
|:--|--:|:--|
| Forest canopy masks | 4 | Overlay previews, binary PNG/TIFF masks and coverage statistics |
| Treetop points | 4 | Overlay previews and CSV/JSON coordinates |
| Individual tree crowns | 4 | RGB images, contour previews, TIFF instance masks and area CSV files |

## Usage notes and limitations

For crown segmentation, use the supplied training, validation and test sets. Match labels to images by image ID and check their alignment when reading the data.

Shadows, overlapping crowns and image edges can lead to missing labels or incomplete outlines. Neighbouring crowns in dense stands may be mistaken for one crown, while a large crown with several visible peaks may be split into several. Understorey trees hidden beneath the upper canopy are usually not visible in the images.

When comparing models, state the allowed position error for treetop localisation. For crown segmentation, check whether crowns are found correctly and completely, and compare predicted outlines with manual outlines using their overlap.

## Licences and image sources

Different terms apply to annotation data, software and imagery:

- **Annotation data and metadata:** [CC BY 4.0](LICENSE-DATA.md).
- **Software and scripts:** [MIT License](LICENSE-CODE).
- **Third-party images and their previews:** follow the use and attribution requirements of Google Earth and the image providers, as described in the [third-party imagery notice](THIRD_PARTY_NOTICES.md).

## Contributors and institutions

<div align="center">

<table>
  <tr>
    <td align="center" width="33.33%">
      <a href="https://github.com/njyunting"><img src="https://avatars.githubusercontent.com/u/78784756?v=4" width="92" alt="Yun Ting — @njyunting"><br><sub><b>Yun Ting</b></sub></a><br>
      <sub>Corresponding author · Nanjing Forestry University</sub>
    </td>
    <td align="center" width="33.33%">
      <img src="assets/readme/contributors/zhang-huaiqing.svg" width="92" alt="Huaiqing Zhang"><br><sub><b>Huaiqing Zhang</b></sub><br>
      <sub>Corresponding author · Chinese Academy of Forestry</sub>
    </td>
    <td align="center" width="33.33%">
      <img src="assets/readme/contributors/ma-lingfei.svg" width="92" alt="Lingfei Ma"><br><sub><b>Lingfei Ma</b></sub><br>
      <sub>Project contributor · East China Normal University</sub>
    </td>
  </tr>
  <tr>
    <td align="center" width="33.33%">
      <img src="assets/readme/contributors/yang-wenjie.svg" width="92" alt="Wenjie Yang"><br><sub><b>Wenjie Yang</b></sub><br>
      <sub>Co-first author · Nanjing Forestry University</sub>
    </td>
    <td align="center" width="33.33%">
      <img src="assets/readme/contributors/xu-enhao.svg" width="92" alt="Enhao Xu"><br><sub><b>Enhao Xu</b></sub><br>
      <sub>Co-first author · Nanjing Forestry University</sub>
    </td>
    <td align="center" width="33.33%">
      <img src="assets/readme/contributors/li-zhang.svg" width="92" alt="Li Zhang"><br><sub><b>Li Zhang</b></sub><br>
      <sub>Manuscript author · Nanjing Forestry University</sub>
    </td>
  </tr>
  <tr>
    <td align="center" colspan="3">
      <img src="assets/readme/contributors/bai-chenhui.svg" width="92" alt="Chenhui Bai"><br><sub><b>Chenhui Bai</b></sub><br>
      <sub>Project contributor</sub>
    </td>
  </tr>
</table>

</div>
