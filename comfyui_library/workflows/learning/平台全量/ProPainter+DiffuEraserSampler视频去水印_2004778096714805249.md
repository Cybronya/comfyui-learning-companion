---
key: 平台全量/ProPainter+DiffuEraserSampler视频去水印_2004778096714805249.json
name: ProPainter+DiffuEraserSampler视频去水印_2004778096714805249
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/ProPainter+DiffuEraserSampler视频去水印_2004778096714805249.json
hash: 562b4e7535a68c39
coverage: 0.947368
learned_at: 2026-11-14 00:48:34
nodes: [PreviewImage, GrowMaskWithBlur, LoadImage, LayerUtility: CropByMask V2, VHS_LoadVideo, DiffuEraserLoader, MaskToImage, VHS_VideoInfo, GetImageRangeFromBatch, ImageToMask, RepeatImageBatch, Int, ImageGenResolutionFromImage, LayerUtility: RestoreCropBox, ProPainterInpaint, DiffuEraserSampler, MaskToImage, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/ProPainter+DiffuEraserSampler视频去水印_2004778096714805249.json

> 来源文件 `comfyui_library/workflows/平台全量/ProPainter+DiffuEraserSampler视频去水印_2004778096714805249.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（19 个）：
- `PreviewImage`
- `GrowMaskWithBlur`
- `LoadImage`
- `LayerUtility: CropByMask V2`
- `VHS_LoadVideo`
- `DiffuEraserLoader`
- `MaskToImage`
- `VHS_VideoInfo`
- `GetImageRangeFromBatch`
- `ImageToMask`
- `RepeatImageBatch`
- `Int`
- `ImageGenResolutionFromImage`
- `LayerUtility: RestoreCropBox`
- `ProPainterInpaint`
- `DiffuEraserSampler` ★核心
- `MaskToImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`GrowMaskWithBlur`、`LoadImage`、`LayerUtility: CropByMask V2`、`VHS_LoadVideo`、`DiffuEraserLoader`、`MaskToImage`、`VHS_VideoInfo`、`GetImageRangeFromBatch`、`ImageToMask`、`RepeatImageBatch`、`Int`、`ImageGenResolutionFromImage`、`LayerUtility: RestoreCropBox`、`ProPainterInpaint`、`DiffuEraserSampler`、`VHS_VideoCombine`

**用到的条目**：LoadImage、DiffuEraserSampler、ImageGenResolutionFromImage、DiffuEraserLoader、GetImageRangeFromBatch、GrowMaskWithBlur、ImageToMask、Int
