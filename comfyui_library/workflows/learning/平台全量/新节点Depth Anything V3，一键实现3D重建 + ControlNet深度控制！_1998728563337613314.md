---
key: 平台全量/新节点Depth Anything V3，一键实现3D重建 + ControlNet深度控制！_1998728563337613314.json
name: 新节点Depth Anything V3，一键实现3D重建 + ControlNet深度控制！_1998728563337613314
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/新节点Depth Anything V3，一键实现3D重建 + ControlNet深度控制！_1998728563337613314.json
hash: 0aa31f705f7d69d2
coverage: 0.935484
learned_at: 2026-11-14 02:12:24
nodes: [LoadImage, DownloadAndLoadDepthAnythingV3Model, DepthAnything_V3, PreviewImage, DownloadAndLoadDepthAnythingV3Model, DepthAnything_V3, SaveVideo, CreateVideo, SaveVideo, CreateVideo, DepthAnythingV3_MultiView, DepthAnythingV3_MultiView, DA3_MultiViewPointCloud, DA3_SavePointCloud, DownloadAndLoadDepthAnythingV3Model, LoadImage, LoadImage, ImageBatchMulti, DownloadAndLoadDepthAnythingV3Model, DepthAnything_V3, DA3_ToPointCloud, DA3_SavePointCloud, DownloadAndLoadDepthAnythingV3Model, DA3_ToMesh, DepthAnything_V3, Fast Groups Bypasser (rgthree), VHS_LoadVideo, LoadImage, LoadImage, Label (rgthree), Label (rgthree)]
patterns: []
missing: []
---

# 平台全量/新节点Depth Anything V3，一键实现3D重建 + ControlNet深度控制！_1998728563337613314.json

> 来源文件 `comfyui_library/workflows/平台全量/新节点Depth Anything V3，一键实现3D重建 + ControlNet深度控制！_1998728563337613314.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（31 个）：
- `LoadImage`
- `DownloadAndLoadDepthAnythingV3Model`
- `DepthAnything_V3`
- `PreviewImage`
- `DownloadAndLoadDepthAnythingV3Model`
- `DepthAnything_V3`
- `SaveVideo`
- `CreateVideo`
- `SaveVideo`
- `CreateVideo`
- `DepthAnythingV3_MultiView`
- `DepthAnythingV3_MultiView`
- `DA3_MultiViewPointCloud`
- `DA3_SavePointCloud`
- `DownloadAndLoadDepthAnythingV3Model`
- `LoadImage`
- `LoadImage`
- `ImageBatchMulti`
- `DownloadAndLoadDepthAnythingV3Model`
- `DepthAnything_V3`
- `DA3_ToPointCloud`
- `DA3_SavePointCloud`
- `DownloadAndLoadDepthAnythingV3Model`
- `DA3_ToMesh`
- `DepthAnything_V3`
- `Fast Groups Bypasser (rgthree)`
- `VHS_LoadVideo`
- `LoadImage`
- `LoadImage`
- `Label (rgthree)`
- `Label (rgthree)`

## 知识

覆盖率 **94%**（29/31）

**有卡**：`LoadImage`、`DownloadAndLoadDepthAnythingV3Model`、`DepthAnything_V3`、`SaveVideo`、`CreateVideo`、`DepthAnythingV3_MultiView`、`DA3_MultiViewPointCloud`、`DA3_SavePointCloud`、`ImageBatchMulti`、`DA3_ToPointCloud`、`DA3_ToMesh`、`VHS_LoadVideo`、`Label (rgthree)`

**用到的条目**：LoadImage、DepthAnything_V3、DownloadAndLoadDepthAnythingV3Model、DepthAnythingV3_MultiView、SaveVideo、DA3_SavePointCloud、CreateVideo、ImageBatchMulti
