---
key: 图片生成/图生图/图像批量放大-ZIP格式-SeedVR2.5（有用）_2011684011390799874.json
name: 图像批量放大-ZIP格式-SeedVR2.5（有用）_2011684011390799874
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图像批量放大-ZIP格式-SeedVR2.5（有用）_2011684011390799874.json
hash: ab6c868e8a989d1d
coverage: 0.875
learned_at: 2026-10-23 12:38:33
nodes: [easy imageSize, SeedVR2LoadVAEModel, SeedVR2LoadVAEModel, easy showAnything, TTP_Tile_image_size, ImageScaleBy, easy showAnything, ImageResize+, SeedVR2LoadDiTModel, GetImageSize+, GetImageSize+, easy clearCacheAll, easy cleanGpuUsed, easy cleanGpuUsed, SeedVR2VideoUpscaler, easy clearCacheAll, KOOK_SaveJPGImage, TTP_Image_Tile_Batch, Image Comparer (rgthree), ImageScaleBy, easy showAnything, RHUploadZip_V2, easy showAnything, TTP_Image_Assy, KOOK_ImageCompression, ImageResize+, CompressImages, ImageListToBatch_, SaveImage, easy int, HAIGC_SaveImagesToZip, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, LoadImage, easy clearCacheAll, easy cleanGpuUsed, ImageScaleToTotalPixels, JoinImageWithAlpha, RHUploadZip_V2, JoinImageWithAlpha]
patterns: []
missing: []
---

# 图片生成/图生图/图像批量放大-ZIP格式-SeedVR2.5（有用）_2011684011390799874.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图像批量放大-ZIP格式-SeedVR2.5（有用）_2011684011390799874.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（40 个）：
- `easy imageSize`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadVAEModel`
- `easy showAnything`
- `TTP_Tile_image_size`
- `ImageScaleBy`
- `easy showAnything`
- `ImageResize+`
- `SeedVR2LoadDiTModel`
- `GetImageSize+`
- `GetImageSize+`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `SeedVR2VideoUpscaler`
- `easy clearCacheAll`
- `KOOK_SaveJPGImage`
- `TTP_Image_Tile_Batch`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `easy showAnything`
- `RHUploadZip_V2`
- `easy showAnything`
- `TTP_Image_Assy`
- `KOOK_ImageCompression`
- `ImageResize+`
- `CompressImages`
- `ImageListToBatch_`
- `SaveImage`
- `easy int`
- `HAIGC_SaveImagesToZip`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `LoadImage`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `ImageScaleToTotalPixels`
- `JoinImageWithAlpha`
- `RHUploadZip_V2`
- `JoinImageWithAlpha`

## 知识

覆盖率 **88%**（35/40）

**有卡**：`easy imageSize`、`SeedVR2LoadVAEModel`、`TTP_Tile_image_size`、`ImageScaleBy`、`ImageResize+`、`SeedVR2LoadDiTModel`、`GetImageSize+`、`easy clearCacheAll`、`easy cleanGpuUsed`、`SeedVR2VideoUpscaler`、`KOOK_SaveJPGImage`、`TTP_Image_Tile_Batch`、`RHUploadZip_V2`、`TTP_Image_Assy`、`KOOK_ImageCompression`、`CompressImages`、`ImageListToBatch_`、`SaveImage`、`easy int`、`HAIGC_SaveImagesToZip`、`LoadImage`、`ImageScaleToTotalPixels`、`JoinImageWithAlpha`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、TTP_Tile_image_size、easy imageSize、GetImageSize+、ImageResize+
