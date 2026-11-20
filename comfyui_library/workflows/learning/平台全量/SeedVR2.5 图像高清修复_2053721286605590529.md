---
key: 平台全量/SeedVR2.5 图像高清修复_2053721286605590529.json
name: SeedVR2.5 图像高清修复_2053721286605590529
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SeedVR2.5 图像高清修复_2053721286605590529.json
hash: 0406c45a3ffd1c17
coverage: 0.766667
learned_at: 2026-11-14 00:59:24
nodes: [TTP_Image_Tile_Batch, INTConstant, ImageScaleToTotalPixels, PreviewImage, SeedVR2VideoUpscaler, Image Comparer (rgthree), SeedVR2LoadVAEModel, LoadImage, ImageScale, easy imageListToImageBatch, TTP_Image_Assy, easy imageSize, easy imageSizeBySide, SeedVR2LoadVAEModel, TTP_Tile_image_size, SeedVR2LoadDiTModel, SeedVR2LoadDiTModel, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, SeedVR2VideoUpscaler, INTConstant, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), SaveImage, SaveImage, easy imageBatchToImageList]
patterns: []
missing: []
---

# 平台全量/SeedVR2.5 图像高清修复_2053721286605590529.json

> 来源文件 `comfyui_library/workflows/平台全量/SeedVR2.5 图像高清修复_2053721286605590529.json`

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

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、easy imageSize、easy imageSizeBySide、TTP_Tile_image_size、SaveImage
