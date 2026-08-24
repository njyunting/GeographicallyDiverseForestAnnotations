# Third-party imagery and rights notices / 第三方影像与权利说明

This register separates author-generated annotations from source imagery. A file's presence in this private repository does not establish a right to redistribute the underlying imagery.

本清单用于区分作者生成的标注与原始影像。文件出现在当前私有仓库中，并不表示已经取得公开再分发其底层影像的权利。

## Rights status by asset class

| Asset class | Examples | Annotation-data status | Source-imagery status | Public-release action |
|---|---|---|---|---|
| Canopy-region annotations | Binary masks, coverage tables | Intended CC BY 4.0 | Embedded imagery not covered | Publish masks and metadata; publish imagery only after source-level clearance |
| Treetop annotations | Point CSV/JSON | Intended CC BY 4.0 | Embedded imagery not covered | Publish coordinates and metadata; separately audit preview/source images |
| Individual-crown annotations | Instance masks, polygons, area tables | Intended CC BY 4.0 | Source JPG and imagery-bearing contour previews not covered | Publish annotations; clear, replace or omit restricted source imagery |
| README atlas and banner | `assets/readme/` composites and galleries | Annotation overlays may be author-generated | Every embedded scene requires review | Retain only assets with documented redistribution permission |
| Videos and animations | MP4/WebP demonstrations | Annotation overlays may be author-generated | Video frames may include restricted imagery | Review every source video and record provider/permission |
| Global distribution figure | Map plus representative imagery | Map symbols and layout may be author-generated | Embedded representative scenes require review | Clear each scene independently before public release |

## Required provenance fields

Before public release, each source-image family must have the following fields completed in the release manifest:

- provider or rights holder;
- product, platform or collection name;
- image or scene identifier, where available;
- acquisition or access date;
- source URL or acquisition route;
- applicable licence or terms-of-use URL;
- whether redistribution is permitted;
- required attribution wording;
- permission evidence or approval record, where required;
- resulting action: `release`, `replace`, `link only`, or `omit`.

## Important limitation

Excluding an image from [`LICENSE-DATA.md`](LICENSE-DATA.md) does not by itself make redistribution lawful. Any image for which redistribution permission cannot be documented must be removed, replaced with openly licensed imagery, or represented only through a source reference and independently releasable annotation data.

The working asset-level review is maintained in [`docs/DRAFT_ASSET_MANIFEST.md`](docs/DRAFT_ASSET_MANIFEST.md).
