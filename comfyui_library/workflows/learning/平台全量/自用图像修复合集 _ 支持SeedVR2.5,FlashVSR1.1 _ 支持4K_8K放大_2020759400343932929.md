---
key: 平台全量/自用图像修复合集 _ 支持SeedVR2.5,FlashVSR1.1 _ 支持4K_8K放大_2020759400343932929.json
name: 自用图像修复合集 _ 支持SeedVR2.5,FlashVSR1.1 _ 支持4K_8K放大_2020759400343932929
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/自用图像修复合集 _ 支持SeedVR2.5,FlashVSR1.1 _ 支持4K_8K放大_2020759400343932929.json
hash: eea6cbaf7b530cc6
coverage: 0.725
learned_at: 2026-11-14 02:31:53
nodes: [SeedVR2LoadVAEModel, ImageScaleToTotalPixels, SeedVR2VideoUpscaler, PreviewImage, SaveImage, Note, Note, Image Comparer (rgthree), SeedVR2LoadDiTModel, LoadImage, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, TTP_Tile_image_size, TTP_Image_Tile_Batch, LayerUtility: ImageScaleByAspectRatio V2, easy imageBatchToImageList, SeedVR2LoadVAEModel, easy imageSize, SeedVR2VideoUpscaler, easy imageListToImageBatch, ImageScale, TTP_Image_Assy, INTConstant, Image Comparer (rgthree), easy imageSizeBySide, SeedVR2LoadDiTModel, Image Comparer (rgthree), LoadImage, Note, INTConstant, INTConstant, INTConstant, FlashVSRNode, Note, Fast Groups Bypasser (rgthree), LoadImage, SaveImage]
patterns: []
missing: []
---

# 平台全量/自用图像修复合集 _ 支持SeedVR2.5,FlashVSR1.1 _ 支持4K_8K放大_2020759400343932929.json

> 来源文件 `comfyui_library/workflows/平台全量/自用图像修复合集 _ 支持SeedVR2.5,FlashVSR1.1 _ 支持4K_8K放大_2020759400343932929.json`

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
- `Image Comparer (rgthree)`
- `LoadImage`
- `Note`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `FlashVSRNode`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `SaveImage`

## 知识

覆盖率 **72%**（29/40）

**有卡**：`SeedVR2LoadVAEModel`、`ImageScaleToTotalPixels`、`SeedVR2VideoUpscaler`、`SaveImage`、`SeedVR2LoadDiTModel`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`easy imageSize`、`easy imageListToImageBatch`、`ImageScale`、`TTP_Image_Assy`、`INTConstant`、`easy imageSizeBySide`、`FlashVSRNode`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、easy imageSize、easy imageSizeBySide、TTP_Tile_image_size、SaveImage
