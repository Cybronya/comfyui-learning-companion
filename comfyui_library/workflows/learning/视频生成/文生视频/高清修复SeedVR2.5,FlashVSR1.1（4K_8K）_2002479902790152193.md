---
key: 视频生成/文生视频/高清修复SeedVR2.5,FlashVSR1.1（4K_8K）_2002479902790152193.json
name: 高清修复SeedVR2.5,FlashVSR1.1（4K_8K）_2002479902790152193
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/高清修复SeedVR2.5,FlashVSR1.1（4K_8K）_2002479902790152193.json
hash: 90c5ec04cbaddcfe
coverage: 0.725
learned_at: 2026-10-15 22:49:08
nodes: [ImageScaleToTotalPixels, SeedVR2VideoUpscaler, PreviewImage, SaveImage, Note, Note, Image Comparer (rgthree), LoadImage, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, TTP_Tile_image_size, TTP_Image_Tile_Batch, LayerUtility: ImageScaleByAspectRatio V2, easy imageBatchToImageList, SeedVR2LoadVAEModel, easy imageSize, SeedVR2VideoUpscaler, easy imageListToImageBatch, ImageScale, TTP_Image_Assy, INTConstant, Image Comparer (rgthree), easy imageSizeBySide, SaveImage, SeedVR2LoadDiTModel, LoadImage, Image Comparer (rgthree), Note, INTConstant, INTConstant, INTConstant, FlashVSRNode, Note, LoadImage, Fast Groups Bypasser (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel]
patterns: []
missing: []
---

# 视频生成/文生视频/高清修复SeedVR2.5,FlashVSR1.1（4K_8K）_2002479902790152193.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/高清修复SeedVR2.5,FlashVSR1.1（4K_8K）_2002479902790152193.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（40 个）：
- `ImageScaleToTotalPixels`
- `SeedVR2VideoUpscaler`
- `PreviewImage`
- `SaveImage`
- `Note`
- `Note`
- `Image Comparer (rgthree)`
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
- `Note`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `FlashVSRNode`
- `Note`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`

## 知识

覆盖率 **72%**（29/40）

**有卡**：`ImageScaleToTotalPixels`、`SeedVR2VideoUpscaler`、`SaveImage`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`SeedVR2LoadVAEModel`、`easy imageSize`、`easy imageListToImageBatch`、`ImageScale`、`TTP_Image_Assy`、`INTConstant`、`easy imageSizeBySide`、`SeedVR2LoadDiTModel`、`FlashVSRNode`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、TTP_Tile_image_size、easy imageSize、easy imageSizeBySide、SaveImage
