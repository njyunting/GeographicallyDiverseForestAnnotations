<div align="center">

<img src="assets/readme/repository-banner.webp" width="100%" alt="Version 1.0 banner for Global Forest Crown Annotations">

**English** | [中文](README.zh-CN.md)

**A global, human-verified benchmark connecting canopy-region masks, treetop points, and individual-crown polygons across satellite —built for scalable forest mapping and AI research.**

[![Version](https://img.shields.io/badge/version-1.0-00A67E?style=for-the-badge)](#-dataset-components)
[![Annotation](https://img.shields.io/badge/annotation-human%20verified-00A67E?style=for-the-badge)](#-annotation-production)
[![Coverage](https://img.shields.io/badge/coverage-global-2E6EB5?style=for-the-badge)](#-global-coverage)
[![Samples](https://img.shields.io/badge/real%20sample%20package-12%20scenes-7357A5?style=for-the-badge)](examples/real_sample_package_v1/)

[Overview](#-overview) · [Demos](#-annotation-demos) · [Real samples](#-real-sample-package) · [Dataset](#-dataset-components) · [Coverage](#-global-coverage) · [Annotations](#-annotation-production) · [Quality control](#-quality-control) · [Contributors](#-contributors-and-institutions) · [Access](#-data-access) · [Citation](#-citation)

</div>

## 🌍 Overview

Global Forest Crown Annotations brings together three annotation products that describe forest structure at different spatial levels:

1. **Canopy-region masks** capture continuous areas occupied by tree canopy.
2. **Treetop points** identify individual treetop locations at scene scale.
3. **Individual-crown polygons** delineate the visible boundary of each tree crown.

These products are complementary rather than interchangeable. Together, they provide a bridge from landscape-scale canopy extent to tree locations and crown-level geometry, supporting dataset benchmarking, model development and ecological analysis across varied geographic contexts.

### Three views of one forest scene

<table>
  <tr>
    <td width="33.33%" align="center">
      <img src="assets/readme/canopy-region-example.webp" width="100%" alt="Canopy-region example">
      <br><b>01 · Canopy region</b>
      <br><sub>Continuous canopy extent</sub>
    </td>
    <td width="33.33%" align="center">
      <img src="assets/readme/treetop-points-example.webp" width="100%" alt="Treetop-point example">
      <br><b>02 · Treetop points</b>
      <br><sub>Individual tree locations</sub>
    </td>
    <td width="33.33%" align="center">
      <img src="assets/readme/crown-polygons-example.webp" width="100%" alt="Individual-crown polygon example">
      <br><b>03 · Crown polygons</b>
      <br><sub>Instance-level boundaries</sub>
    </td>
  </tr>
</table>

### At a glance

| Component | Released unit | Verified scale | Annotation route | Primary colour |
|:--|:--|--:|:--|:--:|
| **Canopy-region masks** | 2 km × 2 km raster scene | **27 mosaics** | **100% manual** | 🟢 |
| **Treetop points** | 2 km × 2 km point scene | **1,306,763 effective markers in 26 SVG scenes** | **100% manual** | 🔴 |
| **Individual-crown polygons** | Crown instance | **459,756 crowns in 6,802 RGB images** | ≈70% direct manual; ≈30% model candidates, all corrected and confirmed by humans | 🟠 |

## 🎥 Annotation demos

<table>
  <tr>
    <td width="50%" align="center">
      <a href="assets/readme/treetop-annotation-demo.mp4">
        <img src="assets/readme/treetop-annotation-demo.webp" width="100%" alt="Animated treetop-point annotation demonstration">
      </a>
      <br><b>Treetop-point annotation</b>
      <br><sub>Click the animation to open the MP4 video.</sub>
    </td>
    <td width="50%" align="center">
      <a href="assets/readme/crown-annotation-demo.mp4">
        <img src="assets/readme/crown-annotation-demo.webp" width="100%" alt="Animated individual-crown annotation demonstration">
      </a>
      <br><b>Individual-crown annotation</b>
      <br><sub>Click the animation to open the MP4 video.</sub>
    </td>
  </tr>
</table>

Both previews autoplay and loop on GitHub. The linked MP4 files preserve smoother motion and higher visual quality.

## 🚀 Real sample package

The repository includes a compact, integrity-checked package of **12 real examples** for immediate format inspection and loader development:

| Canopy-region masks | Treetop points | Individual-crown polygons |
|:--:|:--:|:--:|
| 4 scenes | 4 scenes | 4 images |
| Binary PNG/TIFF masks | CSV/JSON coordinates | RGB, contours, instance TIFF and area CSV |

<div align="center">

### [Explore the real sample package →](examples/real_sample_package_v1/)

<sub>Includes bilingual documentation, a file manifest and SHA-256 checksums.</sub>

</div>

## 🧩 Dataset components

### 1. Canopy-region masks

Canopy-region masks represent the spatial extent of visible tree canopy as raster labels. They are designed for tasks such as canopy-cover mapping, semantic segmentation and landscape-scale forest monitoring.

| Field | Description |
|:--|:--|
| **Representation** | Raster mask aligned with source imagery |
| **Annotation unit** | Continuous canopy region |
| **Spatial coverage per scene** | **2 km × 2 km (4 km²)** |
| **Production** | Fully manual delineation |
| **Current verified scale** | 27 mosaics |
| **Typical task** | Semantic segmentation / canopy-extent estimation |

### 2. Treetop points

Treetop points record the interpreted location of individual tree tops. Because a point occupies a very small spatial footprint, validation uses a practical spatial tolerance rather than an unrealistically strict pixel-perfect equality rule.

| Field | Description |
|:--|:--|
| **Representation** | Point annotations stored in scene-level vector layers |
| **Annotation unit** | One interpreted treetop location |
| **Spatial coverage per scene** | **2 km × 2 km (4 km²)** |
| **Production** | Fully manual placement |
| **Current verified scale** | 1,306,763 effective markers across 26 SVG scenes |
| **Typical task** | Point detection / tree counting / density estimation |

### 3. Individual-crown polygons

Individual-crown polygons describe visible crown boundaries at instance level. Approximately 70% were delineated directly by annotators; approximately 30% began as model-generated candidates. Every retained candidate was manually corrected and human confirmed before inclusion.

| Field | Description |
|:--|:--|
| **Representation** | Instance masks, contours and crown-area records |
| **Annotation unit** | One visible tree crown |
| **Production** | ≈70% direct manual + ≈30% model-candidate-assisted, followed by manual correction |
| **Current verified scale** | 459,756 crowns across 6,802 RGB images |
| **Typical task** | Instance segmentation / crown delineation / crown-size analysis |

## 🗺️ Global coverage

<div align="center">

<img src="assets/readme/global-distribution.svg" width="94%" alt="Global distribution map with representative forest annotation examples">

*Mapped satellite-scene locations and representative released annotations. Country boundaries provide geographic reference in a Robinson projection.*

</div>

The collection was assembled to capture diverse forest appearances, crown structures and geographic settings. The map reports the available mapped scenes; representative examples around the map illustrate the annotation products and are not intended to imply equal sampling density among countries or biomes.

## 🖼️ Representative scene atlas

<div align="center">

<img src="assets/readme/representative-scene-atlas-v3.webp" width="100%" alt="Representative scene atlas showing canopy masks, treetop points and individual-crown polygons">

</div>

The scene atlas highlights variability in canopy texture, crown density, background context, image resolution and annotation geometry. It is intended as a visual guide to the range of cases represented in the collection rather than a statistical summary of the complete dataset.

## ✍️ Annotation production

Annotation follows a human-centred production and verification process. Canopy-region masks and treetop points are drawn manually from the source imagery. Individual-crown polygons are produced either by direct manual delineation (approximately 70%) or from model-generated candidates (approximately 30%); every retained crown is then manually corrected and confirmed. All three components undergo independent review and automated file-level integrity checks before release.

| Stage | Canopy-region masks | Treetop points | Individual-crown polygons |
|:--|:--|:--|:--|
| **Initial annotation** | Manual | Manual | Direct manual or model candidate |
| **Human correction** | Required | Required | Required for every retained crown |
| **Human confirmation** | Required | Required | Required |
| **Automated integrity checks** | Image–mask pairing, mask validity, identifiers | Image–point pairing, coordinate bounds, identifiers | Image–annotation pairing, polygon validity, identifiers |
| **Release gate** | Pass review and integrity checks | Pass tolerant spatial review and integrity checks | Pass boundary review and integrity checks |

> [!NOTE]
> Model assistance applies **only to approximately 30% of the individual-crown polygon workflow**. Canopy-region masks and treetop points were produced entirely through manual annotation.

## ✅ Quality control

<div align="center">

<img src="assets/readme/technical-validation-core.webp" width="100%" alt="Three technical-validation analyses">

</div>

Quality control combines independent human review with automated file-level checks. Failed items return to the relevant annotation stage for correction, re-review and re-checking.

- **Completeness and duplication:** identify missing, empty or duplicated labels.
- **Image–annotation pairing:** verify that each annotation resolves to the intended source image.
- **Coordinate validity:** check that treetop locations and geometries remain within image bounds.
- **Geometry validity:** test mask readability and polygon structure.
- **Boundary review:** inspect merged crowns, split crowns and ambiguous boundaries.
- **File integrity:** validate identifiers, metadata, readable files and release checksums.
- **Versioning:** freeze only human-verified, integrity-checked data packages.

## 📁 Dataset organisation

```text
dataset/
├── canopy_region_masks/
│   ├── imagery/
│   ├── masks/
│   └── metadata/
├── treetop_points/
│   ├── imagery/
│   ├── annotations/
│   └── metadata/
├── individual_crown_polygons/
│   ├── imagery/
│   ├── instance_masks/
│   ├── contours/
│   └── crown_areas/
└── manifests/
    ├── file_inventory.csv
    ├── checksums.sha256
    └── provenance.csv
```

## 🔬 Intended uses

- Canopy-extent and forest-cover segmentation.
- Treetop detection, point localisation and tree-count estimation.
- Individual-tree crown detection and instance segmentation.
- Cross-region transfer, domain-shift and robustness studies.
- Multi-granularity learning across region, point and instance annotations.
- Benchmarking annotation quality-control and geospatial vision workflows.

### Limitations to consider

- The three annotation components have different spatial units and must not be treated as interchangeable labels.
- Geographic coverage is global but not spatially uniform.
- Visible crown boundaries can remain ambiguous under overlap, shadow and heterogeneous canopy structure.
- Point-level agreement should be evaluated with an explicit spatial tolerance.
- Source-imagery rights and annotation-product licences must be checked separately before redistribution.

## 📦 Data access

A representative package containing 12 real examples is available in [`examples/real_sample_package_v1`](examples/real_sample_package_v1/). The package includes all three annotation components, component-level documentation, a file manifest and SHA-256 checksums.

## 📝 Citation

**Global Forest Crown Annotations contributors.** *Global Forest Crown Annotations: Canopy-Region Masks, Treetop Points, and Individual-Crown Polygons*. Version 1.0 (2026).

## ⚖️ Licensing and provenance

This repository uses separate terms for different asset classes; there is no repository-wide licence covering every file.

- **Annotation data and metadata:** [CC BY 4.0](LICENSE-DATA.md).
- **Software and scripts:** [MIT License](LICENSE-CODE).
- **Third-party source imagery:** governed by source-specific terms described in the [third-party imagery notice](THIRD_PARTY_NOTICES.md).

## 🤝 Contributors and institutions

<div align="center">

<h3>Project contributors</h3>

<table>
  <tr>
    <td align="center" width="20%">
      <a href="https://github.com/njyunting">
        <img src="https://avatars.githubusercontent.com/u/78784756?v=4" width="92" alt="Ting Yun — @njyunting"><br>
        <sub><b>Ting Yun</b></sub><br>
        <sub>Lead author · @njyunting</sub>
      </a>
    </td>
    <td align="center" width="20%">
      <img src="assets/readme/contributors/zhang-huaiqing.svg" width="92" alt="Zhang Huaiqing"><br>
      <sub><b>Zhang Huaiqing</b></sub><br>
      <sub>Chinese Academy of Forestry</sub>
    </td>
    <td align="center" width="20%">
      <img src="assets/readme/contributors/yang-wenjie.svg" width="92" alt="Yang Wenjie"><br>
      <sub><b>Yang Wenjie</b></sub><br>
      <sub>Contributor</sub>
    </td>
    <td align="center" width="20%">
      <img src="assets/readme/contributors/bai-chenhui.svg" width="92" alt="Bai Chenhui"><br>
      <sub><b>Bai Chenhui</b></sub><br>
      <sub>Contributor</sub>
    </td>
    <td align="center" width="20%">
      <img src="assets/readme/contributors/xu-enhao.svg" width="92" alt="Xu Enhao"><br>
      <sub><b>Xu Enhao</b></sub><br>
      <sub>Contributor</sub>
    </td>
  </tr>
</table>

<br><br>

| Nanjing Forestry University | Chinese Academy of Forestry |
|:--:|:--:|
| **南京林业大学** | **中国林业科学研究院** |

</div>

The contributor wall recognises contributions to data curation, annotation, validation, software, visualisation and scholarly communication. Affiliations and contribution roles are listed in [`CONTRIBUTORS.md`](CONTRIBUTORS.md).

---

<div align="center">

**Three annotation levels. One globally distributed forest benchmark.**

</div>
