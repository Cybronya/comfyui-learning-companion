---
key: 图片生成/图生图/人像高清放大 质感修复 SeedVR2.5+图像高清修复_2089159747038703618.json
name: 人像高清放大 质感修复 SeedVR2.5+图像高清修复_2089159747038703618
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/人像高清放大 质感修复 SeedVR2.5+图像高清修复_2089159747038703618.json
hash: 18036ae387832de2
coverage: 0.766667
learned_at: 2026-10-23 12:08:54
nodes: [TTP_Image_Tile_Batch, INTConstant, ImageScaleToTotalPixels, PreviewImage, SeedVR2LoadVAEModel, ImageScale, easy imageListToImageBatch, easy imageSize, easy imageSizeBySide, SeedVR2LoadVAEModel, TTP_Tile_image_size, SeedVR2LoadDiTModel, SeedVR2LoadDiTModel, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, SeedVR2VideoUpscaler, INTConstant, Note, Note, SaveImage, SaveImage, easy imageBatchToImageList, SeedVR2VideoUpscaler, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, TTP_Image_Assy, Image Comparer (rgthree), LoadImage, LoadImage, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 图片生成/图生图/人像高清放大 质感修复 SeedVR2.5+图像高清修复_2089159747038703618.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/人像高清放大 质感修复 SeedVR2.5+图像高清修复_2089159747038703618.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（30 个）：
- `TTP_Image_Tile_Batch`
- `INTConstant`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `SeedVR2LoadVAEModel`
- `ImageScale`
- `easy imageListToImageBatch`
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
- `SaveImage`
- `SaveImage`
- `easy imageBatchToImageList`
- `SeedVR2VideoUpscaler`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TTP_Image_Assy`
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **77%**（23/30）

**有卡**：`TTP_Image_Tile_Batch`、`INTConstant`、`ImageScaleToTotalPixels`、`SeedVR2LoadVAEModel`、`ImageScale`、`easy imageListToImageBatch`、`easy imageSize`、`easy imageSizeBySide`、`TTP_Tile_image_size`、`SeedVR2LoadDiTModel`、`LayerUtility: ImageScaleByAspectRatio V2`、`SeedVR2VideoUpscaler`、`SaveImage`、`easy imageBatchToImageList`、`TTP_Image_Assy`、`LoadImage`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、TTP_Tile_image_size、easy imageSize、easy imageSizeBySide、SaveImage
