---
key: 平台全量/Qwen2.5-VL 最强精准智能遮罩_1935163347505455105.json
name: Qwen2.5-VL 最强精准智能遮罩_1935163347505455105
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen2.5-VL 最强精准智能遮罩_1935163347505455105.json
hash: a4a6392605767f6f
coverage: 0.904762
learned_at: 2026-11-14 00:52:25
nodes: [DownloadAndLoadQwenModel, easy showAnything, DownloadAndLoadSAM2Model, LayerMask: LoadSAM2Model, QwenVLDetection, BBoxesToSAM2, preview_mask, preview_mask, GetImageSize, MaskToImage, EmptyImage, ImageConcatMulti, LayerMask: SAM2UltraV2, SaveImage, EmptyImage, GetImageSize, LoadImage, ImageConcatMulti, TextInput_, Sam2Segmentation, PreviewImage]
patterns: []
missing: []
---

# 平台全量/Qwen2.5-VL 最强精准智能遮罩_1935163347505455105.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen2.5-VL 最强精准智能遮罩_1935163347505455105.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（21 个）：
- `DownloadAndLoadQwenModel`
- `easy showAnything`
- `DownloadAndLoadSAM2Model`
- `LayerMask: LoadSAM2Model`
- `QwenVLDetection`
- `BBoxesToSAM2`
- `preview_mask`
- `preview_mask`
- `GetImageSize`
- `MaskToImage`
- `EmptyImage`
- `ImageConcatMulti`
- `LayerMask: SAM2UltraV2`
- `SaveImage`
- `EmptyImage`
- `GetImageSize`
- `LoadImage`
- `ImageConcatMulti`
- `TextInput_`
- `Sam2Segmentation`
- `PreviewImage`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`DownloadAndLoadQwenModel`、`DownloadAndLoadSAM2Model`、`LayerMask: LoadSAM2Model`、`QwenVLDetection`、`BBoxesToSAM2`、`preview_mask`、`GetImageSize`、`MaskToImage`、`EmptyImage`、`ImageConcatMulti`、`LayerMask: SAM2UltraV2`、`SaveImage`、`LoadImage`、`TextInput_`、`Sam2Segmentation`

**用到的条目**：LoadImage、GetImageSize、preview_mask、SaveImage、BBoxesToSAM2、DownloadAndLoadQwenModel、DownloadAndLoadSAM2Model、EmptyImage
