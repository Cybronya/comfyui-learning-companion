---
key: 图片生成/图生图/图像放大工作流（SeedVR2.5和FlashVSR1.1放大）_2043258669537697794.json
name: 图像放大工作流（SeedVR2.5和FlashVSR1.1放大）_2043258669537697794
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图像放大工作流（SeedVR2.5和FlashVSR1.1放大）_2043258669537697794.json
hash: 31a65bd8818ec299
coverage: 0.744186
learned_at: 2026-10-23 12:38:40
nodes: [SeedVR2VideoUpscaler, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, TTP_Tile_image_size, TTP_Image_Tile_Batch, ImageScale, TTP_Image_Assy, INTConstant, easy imageSize, SeedVR2LoadVAEModel, SeedVR2LoadVAEModel, PreviewImage, ImageScaleToTotalPixels, SeedVR2VideoUpscaler, INTConstant, FlashVSRNodeAdv, Image Comparer (rgthree), VRAM_Debug, LoadImage, Note, SeedVR2LoadDiTModel, VRAM_Debug, Image Comparer (rgthree), Note, Note, LoadImage, FlashVSRInitPipe, Note, LoadImage, easy imageBatchToImageList, easy imageSizeBySide, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, SeedVR2LoadDiTModel, LayerUtility: ImageScaleByAspectRatio V2, easy imageListToImageBatch, VRAM_Debug, Fast Groups Bypasser (rgthree), Note, Note, SaveImage, SaveImage, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/图像放大工作流（SeedVR2.5和FlashVSR1.1放大）_2043258669537697794.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图像放大工作流（SeedVR2.5和FlashVSR1.1放大）_2043258669537697794.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（43 个）：
- `SeedVR2VideoUpscaler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `ImageScale`
- `TTP_Image_Assy`
- `INTConstant`
- `easy imageSize`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadVAEModel`
- `PreviewImage`
- `ImageScaleToTotalPixels`
- `SeedVR2VideoUpscaler`
- `INTConstant`
- `FlashVSRNodeAdv`
- `Image Comparer (rgthree)`
- `VRAM_Debug`
- `LoadImage`
- `Note`
- `SeedVR2LoadDiTModel`
- `VRAM_Debug`
- `Image Comparer (rgthree)`
- `Note`
- `Note`
- `LoadImage`
- `FlashVSRInitPipe`
- `Note`
- `LoadImage`
- `easy imageBatchToImageList`
- `easy imageSizeBySide`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SeedVR2LoadDiTModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy imageListToImageBatch`
- `VRAM_Debug`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `Note`
- `SaveImage`
- `SaveImage`
- `SaveImage`

## 知识

覆盖率 **74%**（32/43）

**有卡**：`SeedVR2VideoUpscaler`、`LayerUtility: ImageScaleByAspectRatio V2`、`INTConstant`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`ImageScale`、`TTP_Image_Assy`、`easy imageSize`、`SeedVR2LoadVAEModel`、`ImageScaleToTotalPixels`、`FlashVSRNodeAdv`、`VRAM_Debug`、`LoadImage`、`SeedVR2LoadDiTModel`、`FlashVSRInitPipe`、`easy imageBatchToImageList`、`easy imageSizeBySide`、`easy imageListToImageBatch`、`SaveImage`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、TTP_Tile_image_size、easy imageSize、easy imageSizeBySide、SaveImage
