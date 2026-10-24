---
key: 图片生成/图生图/SeedVR2.5+高清修复_2081656815695253506.json
name: SeedVR2.5+高清修复_2081656815695253506
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SeedVR2.5+高清修复_2081656815695253506.json
hash: b4b51aeab6128797
coverage: 0.842105
learned_at: 2026-10-23 11:24:59
nodes: [LayerUtility: ImageScaleByAspectRatio V2, TTP_Tile_image_size, TTP_Image_Tile_Batch, easy imageSize, easy imageSizeBySide, LayerUtility: ImageScaleByAspectRatio V2, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, easy imageBatchToImageList, SeedVR2VideoUpscaler, ImageScale, TTP_Image_Assy, easy imageListToImageBatch, INTConstant, Note, LoadImage, SaveImage, Image Comparer (rgthree), PreviewImage]
patterns: []
missing: []
---

# 图片生成/图生图/SeedVR2.5+高清修复_2081656815695253506.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SeedVR2.5+高清修复_2081656815695253506.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（19 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `easy imageSize`
- `easy imageSizeBySide`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `easy imageBatchToImageList`
- `SeedVR2VideoUpscaler`
- `ImageScale`
- `TTP_Image_Assy`
- `easy imageListToImageBatch`
- `INTConstant`
- `Note`
- `LoadImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `PreviewImage`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`easy imageSize`、`easy imageSizeBySide`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`easy imageBatchToImageList`、`SeedVR2VideoUpscaler`、`ImageScale`、`TTP_Image_Assy`、`easy imageListToImageBatch`、`INTConstant`、`LoadImage`、`SaveImage`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、TTP_Tile_image_size、easy imageSize、easy imageSizeBySide、SaveImage
