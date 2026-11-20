---
key: 平台全量/8K图像高清超清放大修复RFMSR+SeedVR2.5+TTP分块_2082689584877629441.json
name: 8K图像高清超清放大修复RFMSR+SeedVR2.5+TTP分块_2082689584877629441
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/8K图像高清超清放大修复RFMSR+SeedVR2.5+TTP分块_2082689584877629441.json
hash: bc1f6993e29ca69f
coverage: 0.793103
learned_at: 2026-11-14 00:14:05
nodes: [ImageResize+, ImageCASharpening+, ImageConcanate, ImageResize+, Get Image Size, easy showAnything, TTP_Image_Tile_Batch, SeedVR2, LayerUtility: PurgeVRAM, TTP_Image_Assy, SaveImage, SaveImage, SaveImage, PreviewImage, ImageCASharpening+, RH_RFMSR_ModelLoader, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, PDIMAGE_LongerSize, easy cleanGpuUsed, GetImageRangeFromBatch, ImpactMinMax, RH_RFMSR_Upscale, Image Comparer (rgthree), SaveImage, Image Comparer (rgthree), Image Comparer (rgthree), LoadImage, Image Comparer (rgthree)]
patterns: []
missing: []
---

# 平台全量/8K图像高清超清放大修复RFMSR+SeedVR2.5+TTP分块_2082689584877629441.json

> 来源文件 `comfyui_library/workflows/平台全量/8K图像高清超清放大修复RFMSR+SeedVR2.5+TTP分块_2082689584877629441.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（29 个）：
- `ImageResize+`
- `ImageCASharpening+`
- `ImageConcanate`
- `ImageResize+`
- `Get Image Size`
- `easy showAnything`
- `TTP_Image_Tile_Batch`
- `SeedVR2`
- `LayerUtility: PurgeVRAM`
- `TTP_Image_Assy`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `PreviewImage`
- `ImageCASharpening+`
- `RH_RFMSR_ModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `PDIMAGE_LongerSize`
- `easy cleanGpuUsed`
- `GetImageRangeFromBatch`
- `ImpactMinMax`
- `RH_RFMSR_Upscale`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `LoadImage`
- `Image Comparer (rgthree)`

## 知识

覆盖率 **79%**（23/29）

**有卡**：`ImageResize+`、`ImageCASharpening+`、`ImageConcanate`、`Get Image Size`、`TTP_Image_Tile_Batch`、`SeedVR2`、`LayerUtility: PurgeVRAM`、`TTP_Image_Assy`、`SaveImage`、`RH_RFMSR_ModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`PDIMAGE_LongerSize`、`easy cleanGpuUsed`、`GetImageRangeFromBatch`、`ImpactMinMax`、`RH_RFMSR_Upscale`、`LoadImage`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、SeedVR2、RH_RFMSR_Upscale、Get Image Size、ImageResize+、PDIMAGE_LongerSize、SaveImage
