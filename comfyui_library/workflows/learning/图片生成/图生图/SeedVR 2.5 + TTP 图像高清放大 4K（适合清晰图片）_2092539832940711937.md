---
key: 图片生成/图生图/SeedVR 2.5 + TTP 图像高清放大 4K（适合清晰图片）_2092539832940711937.json
name: SeedVR 2.5 + TTP 图像高清放大 4K（适合清晰图片）_2092539832940711937
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SeedVR 2.5 + TTP 图像高清放大 4K（适合清晰图片）_2092539832940711937.json
hash: 933fe546308fd247
coverage: 0.888889
learned_at: 2026-10-21 00:44:20
nodes: [TTP_Image_Tile_Batch, ImageScale, easy imageListToImageBatch, TTP_Image_Assy, easy imageSize, easy imageSizeBySide, SeedVR2LoadVAEModel, TTP_Tile_image_size, SeedVR2LoadDiTModel, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, SeedVR2VideoUpscaler, Note, LayerUtility: ImageScaleByAspectRatio V2, easy imageBatchToImageList, INTConstant, SaveImage, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/SeedVR 2.5 + TTP 图像高清放大 4K（适合清晰图片）_2092539832940711937.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SeedVR 2.5 + TTP 图像高清放大 4K（适合清晰图片）_2092539832940711937.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（18 个）：
- `TTP_Image_Tile_Batch`
- `ImageScale`
- `easy imageListToImageBatch`
- `TTP_Image_Assy`
- `easy imageSize`
- `easy imageSizeBySide`
- `SeedVR2LoadVAEModel`
- `TTP_Tile_image_size`
- `SeedVR2LoadDiTModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `SeedVR2VideoUpscaler`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy imageBatchToImageList`
- `INTConstant`
- `SaveImage`
- `LoadImage`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`TTP_Image_Tile_Batch`、`ImageScale`、`easy imageListToImageBatch`、`TTP_Image_Assy`、`easy imageSize`、`easy imageSizeBySide`、`SeedVR2LoadVAEModel`、`TTP_Tile_image_size`、`SeedVR2LoadDiTModel`、`LayerUtility: ImageScaleByAspectRatio V2`、`SeedVR2VideoUpscaler`、`easy imageBatchToImageList`、`INTConstant`、`SaveImage`、`LoadImage`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、TTP_Tile_image_size、easy imageSize、easy imageSizeBySide、SaveImage
