---
key: 平台全量/图像批量放大ZIP上传下载-SeedVR2.5_2016381202407628801.json
name: 图像批量放大ZIP上传下载-SeedVR2.5_2016381202407628801
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/图像批量放大ZIP上传下载-SeedVR2.5_2016381202407628801.json
hash: 305e83098d236bd3
coverage: 0.871795
learned_at: 2026-11-14 01:53:33
nodes: [SeedVR2LoadVAEModel, easy showAnything, TTP_Tile_image_size, ImageScaleBy, easy showAnything, ImageResize+, SeedVR2LoadDiTModel, GetImageSize+, GetImageSize+, easy clearCacheAll, easy cleanGpuUsed, easy cleanGpuUsed, SeedVR2VideoUpscaler, easy clearCacheAll, KOOK_SaveJPGImage, TTP_Image_Tile_Batch, Image Comparer (rgthree), ImageScaleBy, easy showAnything, RHUploadZip_V2, easy showAnything, TTP_Image_Assy, KOOK_ImageCompression, ImageResize+, CompressImages, ImageListToBatch_, RHUploadZip_V2, easy int, TextBox, JoinImageWithAlpha, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, easy mathInt, easy clearCacheAll, easy cleanGpuUsed, HAIGC_SaveImagesToZip, SeedVR2VideoUpscaler, SaveImage, Int]
patterns: []
missing: []
---

# 平台全量/图像批量放大ZIP上传下载-SeedVR2.5_2016381202407628801.json

> 来源文件 `comfyui_library/workflows/平台全量/图像批量放大ZIP上传下载-SeedVR2.5_2016381202407628801.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（39 个）：
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
- `RHUploadZip_V2`
- `easy int`
- `TextBox`
- `JoinImageWithAlpha`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `easy mathInt`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `HAIGC_SaveImagesToZip`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `Int`

## 知识

覆盖率 **87%**（34/39）

**有卡**：`SeedVR2LoadVAEModel`、`TTP_Tile_image_size`、`ImageScaleBy`、`ImageResize+`、`SeedVR2LoadDiTModel`、`GetImageSize+`、`easy clearCacheAll`、`easy cleanGpuUsed`、`SeedVR2VideoUpscaler`、`KOOK_SaveJPGImage`、`TTP_Image_Tile_Batch`、`RHUploadZip_V2`、`TTP_Image_Assy`、`KOOK_ImageCompression`、`CompressImages`、`ImageListToBatch_`、`easy int`、`TextBox`、`JoinImageWithAlpha`、`easy mathInt`、`HAIGC_SaveImagesToZip`、`SaveImage`、`Int`

**用到的条目**：SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、GetImageSize+、ImageResize+、TTP_Tile_image_size、HAIGC_SaveImagesToZip、KOOK_SaveJPGImage
