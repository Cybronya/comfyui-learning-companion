---
key: 图片生成/图生图/SeedVR2.5 图像高清修复_2075389402867650562.json
name: SeedVR2.5 图像高清修复_2075389402867650562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SeedVR2.5 图像高清修复_2075389402867650562.json
hash: 452f6736d1af12d8
coverage: 0.766667
learned_at: 2026-10-23 11:24:57
nodes: [TTP_Image_Tile_Batch, INTConstant, ImageScaleToTotalPixels, PreviewImage, SeedVR2VideoUpscaler, Image Comparer (rgthree), SeedVR2LoadVAEModel, LoadImage, ImageScale, easy imageListToImageBatch, TTP_Image_Assy, easy imageSize, easy imageSizeBySide, SeedVR2LoadVAEModel, TTP_Tile_image_size, SeedVR2LoadDiTModel, SeedVR2LoadDiTModel, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, SeedVR2VideoUpscaler, INTConstant, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), SaveImage, SaveImage, easy imageBatchToImageList]
patterns: []
missing: []
---

# 图片生成/图生图/SeedVR2.5 图像高清修复_2075389402867650562.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SeedVR2.5 图像高清修复_2075389402867650562.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（30 个）：
- `TTP_Image_Tile_Batch`
- `INTConstant`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `SeedVR2VideoUpscaler`
- `Image Comparer (rgthree)`
- `SeedVR2LoadVAEModel`
- `LoadImage`
- `ImageScale`
- `easy imageListToImageBatch`
- `TTP_Image_Assy`
- `easy imageSize`
- `easy imageSizeBySide`
- `SeedVR2LoadVAEModel`
- `TTP_Tile_image_size`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadDiTModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `SeedVR2VideoUpscaler`
- `INTConstant`
- `Note`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SaveImage`
- `easy imageBatchToImageList`

## 知识

覆盖率 **77%**（23/30）

**有卡**：`TTP_Image_Tile_Batch`、`INTConstant`、`ImageScaleToTotalPixels`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`LoadImage`、`ImageScale`、`easy imageListToImageBatch`、`TTP_Image_Assy`、`easy imageSize`、`easy imageSizeBySide`、`TTP_Tile_image_size`、`SeedVR2LoadDiTModel`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`easy imageBatchToImageList`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、TTP_Tile_image_size、easy imageSize、easy imageSizeBySide、SaveImage
