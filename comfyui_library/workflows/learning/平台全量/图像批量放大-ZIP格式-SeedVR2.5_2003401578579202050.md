---
key: 平台全量/图像批量放大-ZIP格式-SeedVR2.5_2003401578579202050.json
name: 图像批量放大-ZIP格式-SeedVR2.5_2003401578579202050
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/图像批量放大-ZIP格式-SeedVR2.5_2003401578579202050.json
hash: de73593ab9d9f072
coverage: 0.868421
learned_at: 2026-11-14 01:53:31
nodes: [easy imageSize, ImageScaleToTotalPixels, easy clearCacheAll, easy cleanGpuUsed, SeedVR2LoadVAEModel, JoinImageWithAlpha, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, TTP_Tile_image_size, ImageScaleBy, SeedVR2LoadDiTModel, GetImageSize+, easy clearCacheAll, easy cleanGpuUsed, easy cleanGpuUsed, SeedVR2VideoUpscaler, easy clearCacheAll, KOOK_SaveJPGImage, TTP_Image_Tile_Batch, Image Comparer (rgthree), ImageScaleBy, easy showAnything, RHUploadZip_V2, easy showAnything, TTP_Image_Assy, KOOK_ImageCompression, ImageResize+, CompressImages, ImageListToBatch_, HAIGC_SaveImagesToZip, RHUploadZip_V2, SeedVR2VideoUpscaler, SaveImage, ImageResize+, GetImageSize+, easy showAnything, easy showAnything, easy int]
patterns: []
missing: []
---

# 平台全量/图像批量放大-ZIP格式-SeedVR2.5_2003401578579202050.json

> 来源文件 `comfyui_library/workflows/平台全量/图像批量放大-ZIP格式-SeedVR2.5_2003401578579202050.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（38 个）：
- `easy imageSize`
- `ImageScaleToTotalPixels`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `SeedVR2LoadVAEModel`
- `JoinImageWithAlpha`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `TTP_Tile_image_size`
- `ImageScaleBy`
- `SeedVR2LoadDiTModel`
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
- `HAIGC_SaveImagesToZip`
- `RHUploadZip_V2`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `ImageResize+`
- `GetImageSize+`
- `easy showAnything`
- `easy showAnything`
- `easy int`

## 知识

覆盖率 **87%**（33/38）

**有卡**：`easy imageSize`、`ImageScaleToTotalPixels`、`easy clearCacheAll`、`easy cleanGpuUsed`、`SeedVR2LoadVAEModel`、`JoinImageWithAlpha`、`SeedVR2LoadDiTModel`、`TTP_Tile_image_size`、`ImageScaleBy`、`GetImageSize+`、`SeedVR2VideoUpscaler`、`KOOK_SaveJPGImage`、`TTP_Image_Tile_Batch`、`RHUploadZip_V2`、`TTP_Image_Assy`、`KOOK_ImageCompression`、`ImageResize+`、`CompressImages`、`ImageListToBatch_`、`HAIGC_SaveImagesToZip`、`SaveImage`、`easy int`

**用到的条目**：SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、easy imageSize、GetImageSize+、ImageResize+、TTP_Tile_image_size、HAIGC_SaveImagesToZip
