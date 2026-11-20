---
key: 平台全量/图像高清放大三大主流合集 - 支持SeedVR2.5,FlashVSR1.1 _ 支持4K_8K放大_2004023878215188481.json
name: 图像高清放大三大主流合集 - 支持SeedVR2.5,FlashVSR1.1 _ 支持4K_8K放大_2004023878215188481
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/图像高清放大三大主流合集 - 支持SeedVR2.5,FlashVSR1.1 _ 支持4K_8K放大_2004023878215188481.json
hash: 3db368bbaa3ec65b
coverage: 0.725
learned_at: 2026-11-14 01:54:05
nodes: [SeedVR2LoadVAEModel, ImageScaleToTotalPixels, PreviewImage, SaveImage, Note, Image Comparer (rgthree), SeedVR2LoadDiTModel, SaveImage, Note, LayerUtility: ImageScaleByAspectRatio V2, TTP_Tile_image_size, TTP_Image_Tile_Batch, LayerUtility: ImageScaleByAspectRatio V2, easy imageBatchToImageList, SeedVR2LoadVAEModel, easy imageSize, SeedVR2VideoUpscaler, easy imageListToImageBatch, ImageScale, TTP_Image_Assy, INTConstant, easy imageSizeBySide, SeedVR2LoadDiTModel, Image Comparer (rgthree), INTConstant, INTConstant, FlashVSRNode, Fast Groups Bypasser (rgthree), Note, INTConstant, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, Note, LoadImage, LoadImage, LoadImage, Image Comparer (rgthree), SaveImage, SeedVR2VideoUpscaler]
patterns: []
missing: []
---

# 平台全量/图像高清放大三大主流合集 - 支持SeedVR2.5,FlashVSR1.1 _ 支持4K_8K放大_2004023878215188481.json

> 来源文件 `comfyui_library/workflows/平台全量/图像高清放大三大主流合集 - 支持SeedVR2.5,FlashVSR1.1 _ 支持4K_8K放大_2004023878215188481.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（40 个）：
- `SeedVR2LoadVAEModel`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `SaveImage`
- `Note`
- `Image Comparer (rgthree)`
- `SeedVR2LoadDiTModel`
- `SaveImage`
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
- `easy imageSizeBySide`
- `SeedVR2LoadDiTModel`
- `Image Comparer (rgthree)`
- `INTConstant`
- `INTConstant`
- `FlashVSRNode`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `INTConstant`
- `Note`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SeedVR2VideoUpscaler`

## 知识

覆盖率 **72%**（29/40）

**有卡**：`SeedVR2LoadVAEModel`、`ImageScaleToTotalPixels`、`SaveImage`、`SeedVR2LoadDiTModel`、`LayerUtility: ImageScaleByAspectRatio V2`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`easy imageSize`、`SeedVR2VideoUpscaler`、`easy imageListToImageBatch`、`ImageScale`、`TTP_Image_Assy`、`INTConstant`、`easy imageSizeBySide`、`FlashVSRNode`、`LoadImage`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、easy imageSize、easy imageSizeBySide、TTP_Tile_image_size、SaveImage
