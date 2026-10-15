---
key: 图片生成/图生图/Texture Restoration质感修复SeedVR2.5+图像高清修复High_2107279324872265729.json
name: Texture Restoration质感修复SeedVR2.5+图像高清修复High_2107279324872265729
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Texture Restoration质感修复SeedVR2.5+图像高清修复High_2107279324872265729.json
hash: 0b89bacde79dce49
coverage: 0.766667
learned_at: 2026-10-15 22:25:31
nodes: [TTP_Image_Tile_Batch, INTConstant, ImageScaleToTotalPixels, PreviewImage, SeedVR2VideoUpscaler, Image Comparer (rgthree), SeedVR2LoadVAEModel, LoadImage, ImageScale, easy imageListToImageBatch, TTP_Image_Assy, easy imageSize, easy imageSizeBySide, SeedVR2LoadVAEModel, TTP_Tile_image_size, SeedVR2LoadDiTModel, SeedVR2LoadDiTModel, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, SeedVR2VideoUpscaler, LayerUtility: ImageScaleByAspectRatio V2, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), SaveImage, SaveImage, easy imageBatchToImageList, INTConstant, LoadImage, Note, Note]
patterns: []
missing: []
---

# 图片生成/图生图/Texture Restoration质感修复SeedVR2.5+图像高清修复High_2107279324872265729.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Texture Restoration质感修复SeedVR2.5+图像高清修复High_2107279324872265729.json`

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
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SaveImage`
- `easy imageBatchToImageList`
- `INTConstant`
- `LoadImage`
- `Note`
- `Note`

## 知识

覆盖率 **77%**（23/30）

**有卡**：`TTP_Image_Tile_Batch`、`INTConstant`、`ImageScaleToTotalPixels`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`LoadImage`、`ImageScale`、`easy imageListToImageBatch`、`TTP_Image_Assy`、`easy imageSize`、`easy imageSizeBySide`、`TTP_Tile_image_size`、`SeedVR2LoadDiTModel`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`easy imageBatchToImageList`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、TTP_Tile_image_size、easy imageSize、easy imageSizeBySide、SaveImage
