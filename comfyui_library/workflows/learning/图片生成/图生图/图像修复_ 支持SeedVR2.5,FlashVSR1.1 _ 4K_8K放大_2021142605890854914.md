---
key: 图片生成/图生图/图像修复_ 支持SeedVR2.5,FlashVSR1.1 _ 4K_8K放大_2021142605890854914.json
name: 图像修复_ 支持SeedVR2.5,FlashVSR1.1 _ 4K_8K放大_2021142605890854914
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图像修复_ 支持SeedVR2.5,FlashVSR1.1 _ 4K_8K放大_2021142605890854914.json
hash: 9d3f72e2c4d21462
coverage: 0.725
learned_at: 2026-10-23 12:38:06
nodes: [SeedVR2LoadVAEModel, ImageScaleToTotalPixels, SeedVR2VideoUpscaler, PreviewImage, SaveImage, Note, Note, Image Comparer (rgthree), SeedVR2LoadDiTModel, LoadImage, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, TTP_Tile_image_size, TTP_Image_Tile_Batch, LayerUtility: ImageScaleByAspectRatio V2, easy imageBatchToImageList, SeedVR2LoadVAEModel, easy imageSize, SeedVR2VideoUpscaler, easy imageListToImageBatch, ImageScale, TTP_Image_Assy, INTConstant, Image Comparer (rgthree), easy imageSizeBySide, SeedVR2LoadDiTModel, LoadImage, Image Comparer (rgthree), LoadImage, Note, INTConstant, INTConstant, INTConstant, FlashVSRNode, Note, SaveImage, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 图片生成/图生图/图像修复_ 支持SeedVR2.5,FlashVSR1.1 _ 4K_8K放大_2021142605890854914.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图像修复_ 支持SeedVR2.5,FlashVSR1.1 _ 4K_8K放大_2021142605890854914.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（40 个）：
- `SeedVR2LoadVAEModel`
- `ImageScaleToTotalPixels`
- `SeedVR2VideoUpscaler`
- `PreviewImage`
- `SaveImage`
- `Note`
- `Note`
- `Image Comparer (rgthree)`
- `SeedVR2LoadDiTModel`
- `LoadImage`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy imageBatchToImageList`
- `SeedVR2LoadVAEModel`
- `easy imageSize`
- `SeedVR2VideoUpscaler`
- `easy imageListToImageBatch`
- `ImageScale`
- `TTP_Image_Assy`
- `INTConstant`
- `Image Comparer (rgthree)`
- `easy imageSizeBySide`
- `SeedVR2LoadDiTModel`
- `LoadImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `Note`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `FlashVSRNode`
- `Note`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **72%**（29/40）

**有卡**：`SeedVR2LoadVAEModel`、`ImageScaleToTotalPixels`、`SeedVR2VideoUpscaler`、`SaveImage`、`SeedVR2LoadDiTModel`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`easy imageSize`、`easy imageListToImageBatch`、`ImageScale`、`TTP_Image_Assy`、`INTConstant`、`easy imageSizeBySide`、`FlashVSRNode`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、TTP_Tile_image_size、easy imageSize、easy imageSizeBySide、SaveImage
