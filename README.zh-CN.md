<div align="center">

<img src="assets/readme/repository-banner.webp" width="100%" alt="全球森林树冠标注数据集 1.0 版本横幅">

[English](README.md) | **中文**

**一个全球性、经人工核验的森林基准数据集，联合树冠区域掩膜、树顶点和单木树冠多边形三类标注，服务于大范围森林制图与人工智能研究。**

[![版本](https://img.shields.io/badge/version-1.0-00A67E?style=for-the-badge)](#-发布状态)
[![状态](https://img.shields.io/badge/status-private%20pre--release-06251D?style=for-the-badge)](#-发布状态)
[![标注](https://img.shields.io/badge/annotation-human%20verified-00A67E?style=for-the-badge)](#️-标注生产流程)
[![范围](https://img.shields.io/badge/coverage-global-2E6EB5?style=for-the-badge)](#️-全球覆盖)
[![示例包](https://img.shields.io/badge/real%20sample%20package-12%20scenes-7357A5?style=for-the-badge)](examples/real_sample_package_v1/README.zh-CN.md)
[![论文](https://img.shields.io/badge/data%20descriptor-in%20preparation-F0A000?style=for-the-badge)](#-引用)

[项目概述](#-项目概述) · [动态演示](#-标注动态演示) · [真实示例](#-真实示例数据包) · [数据组成](#-数据集组成) · [全球覆盖](#️-全球覆盖) · [标注流程](#️-标注生产流程) · [质量控制](#-质量控制) · [贡献者](#-贡献者与机构) · [数据获取](#-数据获取) · [引用](#-引用)

</div>

## 🌍 项目概述

Global Forest Crown Annotations 汇集了三类从不同空间尺度描述森林结构的标注产品：

1. **树冠区域掩膜**：刻画树冠连续覆盖的空间范围。
2. **树顶点**：在场景尺度上标识单株树木的树顶位置。
3. **单木树冠多边形**：勾画每个可见树冠的实例边界。

这三类产品彼此互补，并不能相互替代。它们共同连接了景观尺度的树冠覆盖、单株树木位置和树冠实例几何，可用于不同地理环境下的数据集基准测试、模型研发和生态分析。

### 同一森林场景的三种视角

<table>
  <tr>
    <td width="33.33%" align="center">
      <img src="assets/readme/canopy-region-example.webp" width="100%" alt="树冠区域标注示例">
      <br><b>01 · 树冠区域</b>
      <br><sub>连续树冠覆盖范围</sub>
    </td>
    <td width="33.33%" align="center">
      <img src="assets/readme/treetop-points-example.webp" width="100%" alt="树顶点标注示例">
      <br><b>02 · 树顶点</b>
      <br><sub>单株树木位置</sub>
    </td>
    <td width="33.33%" align="center">
      <img src="assets/readme/crown-polygons-example.webp" width="100%" alt="单木树冠多边形标注示例">
      <br><b>03 · 单木树冠多边形</b>
      <br><sub>实例级树冠边界</sub>
    </td>
  </tr>
</table>

### 数据概览

| 数据组成 | 发布单元 | 已核验规模 | 标注路线 | 类别颜色 |
|:--|:--|--:|:--|:--:|
| **树冠区域掩膜** | 栅格镶嵌图 | **27 幅镶嵌图** | **100% 人工标注** | 🟢 |
| **树顶点** | 场景级点图层 | **26 个 SVG 场景中的 1,306,763 个有效标记** | **100% 人工标注** | 🔴 |
| **单木树冠多边形** | 单个树冠实例 | **6,802 幅 RGB 图像中的 459,756 个树冠** | 约 70% 直接人工勾画；约 30% 模型候选，全部经过人工修改与确认 | 🟠 |

## 🎥 标注动态演示

<table>
  <tr>
    <td width="50%" align="center">
      <a href="assets/readme/treetop-annotation-demo.mp4">
        <img src="assets/readme/treetop-annotation-demo.webp" width="100%" alt="树顶点标注动态演示">
      </a>
      <br><b>树顶点标注</b>
      <br><sub>点击动画可打开 MP4 视频。</sub>
    </td>
    <td width="50%" align="center">
      <a href="assets/readme/crown-annotation-demo.mp4">
        <img src="assets/readme/crown-annotation-demo.webp" width="100%" alt="单木树冠标注动态演示">
      </a>
      <br><b>单木树冠标注</b>
      <br><sub>点击动画可打开 MP4 视频。</sub>
    </td>
  </tr>
</table>

两个预览动画都会在 GitHub 中自动播放并循环。链接的 MP4 文件保留了更流畅的运动和更高的视觉质量。

## 🚀 真实示例数据包

仓库提供一个已经完成完整性核验的轻量示例包，包含 **12组真实样例**，可立即用于检查数据格式和开发读取程序：

| 树冠区域掩膜 | 树顶点 | 单木树冠实例 |
|:--:|:--:|:--:|
| 4个场景 | 4个场景 | 4幅影像 |
| PNG/TIFF二值掩膜 | CSV/JSON点坐标 | RGB、轮廓图、实例TIFF和面积表 |

<div align="center">

### [查看真实示例数据包 →](examples/real_sample_package_v1/README.zh-CN.md)

<sub>包含中英文说明、文件清单和SHA-256校验和。</sub>

</div>

## 🧩 数据集组成

### 1. 树冠区域掩膜

树冠区域掩膜以栅格标签表示可见树冠的空间覆盖范围，适用于树冠覆盖制图、语义分割和景观尺度森林监测等任务。

| 字段 | 说明 |
|:--|:--|
| **表示形式** | 与源影像对齐的栅格掩膜 |
| **标注单元** | 连续树冠区域 |
| **生产方式** | 完全人工勾画 |
| **当前核验规模** | 27 幅镶嵌图 |
| **典型任务** | 语义分割 / 树冠覆盖范围估计 |

### 2. 树顶点

树顶点记录人工判读的单株树木顶部位置。由于点标注本身的空间覆盖范围很小，验证时采用合理的空间容差，而不是不切实际的像素级完全一致标准。

| 字段 | 说明 |
|:--|:--|
| **表示形式** | 存储于场景级矢量图层中的点标注 |
| **标注单元** | 一个判读树顶位置 |
| **生产方式** | 完全人工放置 |
| **当前核验规模** | 26 个 SVG 场景中的 1,306,763 个有效标记 |
| **典型任务** | 点目标检测 / 树木计数 / 密度估计 |

### 3. 单木树冠多边形

单木树冠多边形在实例尺度上描述可见树冠边界。约 70% 的树冠由标注人员直接勾画，约 30% 以模型生成的候选轮廓为起点。所有保留的候选结果在纳入数据集前均经过人工修改和确认。

| 字段 | 说明 |
|:--|:--|
| **表示形式** | 实例掩膜、轮廓及树冠面积记录 |
| **标注单元** | 一个可见树冠 |
| **生产方式** | 约 70% 直接人工勾画 + 约 30% 模型候选辅助，之后全部进行人工修改 |
| **当前核验规模** | 6,802 幅 RGB 图像中的 459,756 个树冠 |
| **典型任务** | 实例分割 / 树冠勾画 / 树冠尺寸分析 |

## 🗺️ 全球覆盖

<div align="center">

<img src="assets/readme/global-distribution.svg" width="94%" alt="全球样点分布图及森林标注示例">

*已制图的卫星场景位置及代表性标注示例。地图采用 Robinson 投影，并以国家边界提供地理参照。*

</div>

本数据集旨在覆盖多样的森林外观、树冠结构和地理环境。地图展示现有卫星场景的位置；地图周边示例用于说明标注产品，并不代表不同国家或生物群系具有相同的采样密度。

## 🖼️ 代表性场景图集

<div align="center">

<img src="assets/readme/representative-scene-atlas-v3.webp" width="100%" alt="包含树冠区域、树顶点和单木树冠多边形的代表性场景图集">

</div>

场景图集展示树冠纹理、树冠密度、背景环境、影像分辨率和标注几何的多样性。该图用于直观说明数据集中的典型情况，而不是对完整数据集进行统计汇总。

## ✍️ 标注生产流程

数据标注采用以人工为核心的生产与核验流程。树冠区域掩膜和树顶点均由标注人员直接依据原始影像进行纯人工标注。单木树冠多边形约 70% 由人工直接勾画，约 30% 以模型候选结果作为起点；所有保留的树冠均须经过人工修改与确认。三类数据在发布前还需完成独立复核和自动文件级完整性检查。

| 阶段 | 树冠区域掩膜 | 树顶点 | 单木树冠多边形 |
|:--|:--|:--|:--|
| **初始标注** | 人工 | 人工 | 直接人工标注或模型候选 |
| **人工修改** | 必须 | 必须 | 每个保留树冠均必须修改确认 |
| **人工确认** | 必须 | 必须 | 必须 |
| **自动完整性检查** | 影像–掩膜配对、掩膜有效性、标识符 | 影像–点配对、坐标边界、标识符 | 影像–标注配对、多边形有效性、标识符 |
| **发布门槛** | 通过复核与完整性检查 | 通过带空间容差的复核及完整性检查 | 通过边界复核及完整性检查 |

> [!NOTE]
> 模型辅助**仅应用于约 30% 的单木树冠多边形生产流程**。树冠区域掩膜和树顶点均为完全人工标注。

## ✅ 质量控制

<div align="center">

<img src="assets/readme/technical-validation-core.webp" width="100%" alt="三项技术验证分析">

</div>

质量控制结合独立人工复核和自动文件级检查。未通过检查的样本会退回相应标注阶段，依次完成修改、重新复核和再次检查。

- **完整性与重复项：**识别缺失、空白或重复标签。
- **影像–标注配对：**确认每个标注对应正确的源影像。
- **坐标有效性：**检查树顶点和几何对象是否位于影像边界内。
- **几何有效性：**检查掩膜可读性和多边形结构。
- **边界复核：**检查树冠合并、树冠拆分和存在歧义的边界。
- **文件完整性：**验证标识符、元数据、文件可读性和发布校验和。
- **版本管理：**仅冻结通过人工核验和完整性检查的数据包。

## 📁 计划发布结构

```text
release/
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

以上为计划中的正式存档结构。在论文准备阶段，完整数据包不会提交到 GitHub 仓库。

### 计划发布的数据产品

| 产品 | 计划内容 | 状态 |
|:--|:--|:--:|
| 树冠区域影像与掩膜 | 配对源影像、栅格掩膜和场景元数据 | 🔒 发布前 |
| 树顶点影像与点标注 | 配对源场景、点图层和元数据 | 🔒 发布前 |
| 单木树冠标注 | RGB 影像、实例掩膜、轮廓和树冠面积表 | 🔒 发布前 |
| 数据集清单 | 文件清单、来源记录和校验和 | 🔒 发布前 |
| 文档 | Data Descriptor、标注指南和技术验证说明 | 🟡 准备中 |

## 🔬 预期用途

- 树冠覆盖范围与森林覆盖语义分割。
- 树顶点检测、点定位及树木数量估计。
- 单木树冠检测与实例分割。
- 跨区域迁移、域偏移及模型鲁棒性研究。
- 区域、点和实例标注之间的多粒度学习。
- 标注质量控制与地理空间视觉工作流的基准测试。

### 使用时需要考虑的局限

- 三类标注具有不同的空间单元，不应被视为可互换标签。
- 数据集覆盖全球，但空间采样并不均匀。
- 在树冠重叠、阴影及异质冠层结构下，可见树冠边界仍可能存在歧义。
- 点标注的一致性应在明确的空间容差下评估。
- 在重新分发之前，应分别核查源影像权利和标注产品许可。

## 📦 数据获取

> **数据即将发布。**

正式压缩包地址、永久标识符、版本号和数据仓库引用将在论文投稿、数据存档核验及仓库所有者批准后补充。本私有草稿不提供局部或非官方数据下载。

正式发布后，本节将提供：

- 永久数据集落地页；
- 带版本号的压缩包链接和校验和；
- 各数据组成部分的下载说明；
- 机器可读的引用文件；
- 不同资产类别的许可与来源说明。

## 📝 引用

论文最终题目、作者顺序、期刊信息、论文 DOI 和数据仓库 DOI 尚未冻结。论文和存档数据完成注册后，将在此提供可直接复制的 BibTeX 记录。

```bibtex
@dataset{global_forest_crown_annotations,
  title     = {Global Forest Crown Annotations: Canopy-Region Masks,
               Treetop Points, and Individual-Crown Polygons},
  author    = {To be finalised},
  year      = {To be finalised},
  publisher = {To be finalised},
  version   = {1.0},
  doi       = {To be finalised}
}
```

请勿将本私有仓库作为已发布数据集引用。

## ⚖️ 许可与来源

标注产品、代码和源影像将分别说明许可条款。私有草稿阶段暂不设置覆盖整个仓库的统一许可。当前资产审核状态请参阅 [`docs/DRAFT_ASSET_MANIFEST.md`](docs/DRAFT_ASSET_MANIFEST.md)。

## 🤝 贡献者与机构

<div align="center">

<h3>项目贡献者</h3>

<table>
  <tr>
    <td align="center" width="20%">
      <a href="https://github.com/njyunting">
        <img src="https://avatars.githubusercontent.com/u/78784756?v=4" width="92" alt="Ting Yun — @njyunting"><br>
        <sub><b>Ting Yun</b></sub><br>
        <sub>第一作者 · @njyunting</sub>
      </a>
    </td>
    <td align="center" width="20%">
      <img src="assets/readme/contributors/zhang-huaiqing.svg" width="92" alt="张怀清"><br>
      <sub><b>张怀清</b></sub><br>
      <sub>中国林业科学研究院</sub>
    </td>
    <td align="center" width="20%">
      <img src="assets/readme/contributors/yang-wenjie.svg" width="92" alt="杨文杰"><br>
      <sub><b>杨文杰</b></sub><br>
      <sub>项目贡献者</sub>
    </td>
    <td align="center" width="20%">
      <img src="assets/readme/contributors/bai-chenhui.svg" width="92" alt="白晨辉"><br>
      <sub><b>白晨辉</b></sub><br>
      <sub>项目贡献者</sub>
    </td>
    <td align="center" width="20%">
      <img src="assets/readme/contributors/xu-enhao.svg" width="92" alt="许恩浩"><br>
      <sub><b>许恩浩</b></sub><br>
      <sub>项目贡献者</sub>
    </td>
  </tr>
</table>

<sub>后续将在姓名、GitHub 账户、所属机构和贡献角色核验完成后继续加入其他贡献者。</sub>

<br><br>

| 南京林业大学 | 中国林业科学研究院 |
|:--:|:--:|
| **Nanjing Forestry University** | **Chinese Academy of Forestry** |

</div>

贡献者头像墙用于展示数据集构建、人工标注、质量复核、软件开发和论文撰写等工作的参与者。已经核验的 GitHub 账户可直接点击进入个人主页；暂未确认 GitHub 账户的人员仍以姓名清晰展示。详细的单位信息和 CRediT 贡献角色统一维护在 [`CONTRIBUTORS.md`](CONTRIBUTORS.md) 中。

## 🚦 发布状态

- [x] 已创建私有 GitHub 仓库。
- [x] README 已包含三类标注产品。
- [x] 已记录经过核验的数据规模。
- [x] 已说明标注流程和质量控制流程。
- [ ] 最终论文题目、作者顺序和作者单位已确认。
- [ ] 永久数据存档和 DOI 已确认。
- [ ] 影像来源和再分发权审核已完成。
- [ ] 各数据组成部分的许可已批准。
- [ ] 已添加公开下载链接和校验和。
- [ ] 仓库所有者明确批准将仓库设为公开。

在 [`docs/RELEASE_CHECKLIST.md`](docs/RELEASE_CHECKLIST.md) 中的所有必要项目完成之前，本仓库将保持私有。

---

<div align="center">

**三种标注尺度，一个全球分布的森林基准数据集。**

私有预发布 · 数据与论文准备中

</div>
