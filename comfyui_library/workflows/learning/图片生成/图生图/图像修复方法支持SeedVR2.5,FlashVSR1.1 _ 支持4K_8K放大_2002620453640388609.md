---
key: 图片生成/图生图/图像修复方法支持SeedVR2.5,FlashVSR1.1 _ 支持4K_8K放大_2002620453640388609.json
name: 图像修复方法支持SeedVR2.5,FlashVSR1.1 _ 支持4K_8K放大_2002620453640388609
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图像修复方法支持SeedVR2.5,FlashVSR1.1 _ 支持4K_8K放大_2002620453640388609.json
hash: 152640b7ab43435e
coverage: 0.744186
learned_at: 2026-10-23 12:38:07
nodes: [SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SaveImage, Note, Note, Image Comparer (rgthree), SeedVR2LoadDiTModel, LoadImage, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, TTP_Tile_image_size, TTP_Image_Tile_Batch, LayerUtility: ImageScaleByAspectRatio V2, easy imageBatchToImageList, SeedVR2LoadVAEModel, easy imageSize, SeedVR2VideoUpscaler, easy imageListToImageBatch, ImageScale, TTP_Image_Assy, INTConstant, Image Comparer (rgthree), easy imageSizeBySide, SaveImage, SeedVR2LoadDiTModel, LoadImage, Image Comparer (rgthree), LoadImage, FlashVSRNode, Note, Fast Groups Bypasser (rgthree), Note, PreviewImage, ImageScaleToTotalPixels, INTConstant, Int, INTConstant, Int, INTConstant, Int]
patterns: []
missing: []
---

# 图片生成/图生图/图像修复方法支持SeedVR2.5,FlashVSR1.1 _ 支持4K_8K放大_2002620453640388609.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图像修复方法支持SeedVR2.5,FlashVSR1.1 _ 支持4K_8K放大_2002620453640388609.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（43 个）：
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
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
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `LoadImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `FlashVSRNode`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `PreviewImage`
- `ImageScaleToTotalPixels`
- `INTConstant`
- `Int`
- `INTConstant`
- `Int`
- `INTConstant`
- `Int`

## 知识

覆盖率 **74%**（32/43）

**有卡**：`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SaveImage`、`SeedVR2LoadDiTModel`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`easy imageSize`、`easy imageListToImageBatch`、`ImageScale`、`TTP_Image_Assy`、`INTConstant`、`easy imageSizeBySide`、`FlashVSRNode`、`ImageScaleToTotalPixels`、`Int`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、TTP_Tile_image_size、easy imageSize、easy imageSizeBySide、SaveImage
