---
key: 图片生成/图生图/High-Definition Zoom_Detail Enhancement 高清放大_细节增强-_2114882296372355073.json
name: High-Definition Zoom_Detail Enhancement 高清放大_细节增强-_2114882296372355073
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/High-Definition Zoom_Detail Enhancement 高清放大_细节增强-_2114882296372355073.json
hash: e0dee63e9d3ae660
coverage: 0.861111
learned_at: 2026-10-30 17:49:57
nodes: [CLIPLoader, VAELoader, ReferenceLatent, ConditioningZeroOut, CLIPTextEncode, VAEEncode, LatentUpscaleBy, KSampler, GetImageSize+, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, ImageResize+, ImageResize+, TTP_Tile_image_size, TTP_Image_Tile_Batch, GetImageSize+, ImageScaleBy, ImageScaleBy, TTP_Image_Assy, SaveImage, Image Comparer (rgthree), UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), easy cleanGpuUsed, LoadImage, VAEDecode, SaveImage, Fast Groups Bypasser (rgthree), Note, LoadImage, DownloadAndLoadDepthAnythingV2Model, DepthAnything_V2, SaveImage, Fast Groups Bypasser (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.8000000000000002, "sampler_name": "euler", "scheduler": "simple", "seed": 196688955235037, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/High-Definition Zoom_Detail Enhancement 高清放大_细节增强-_2114882296372355073.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/High-Definition Zoom_Detail Enhancement 高清放大_细节增强-_2114882296372355073.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `CLIPLoader`
- `VAELoader`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `LatentUpscaleBy`
- `KSampler` ★核心
- `GetImageSize+`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `ImageResize+`
- `ImageResize+`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `GetImageSize+`
- `ImageScaleBy`
- `ImageScaleBy`
- `TTP_Image_Assy`
- `SaveImage`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `easy cleanGpuUsed`
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `LoadImage`
- `DownloadAndLoadDepthAnythingV2Model`
- `DepthAnything_V2`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `196688955235037`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.8000000000000002`

## 知识

覆盖率 **86%**（31/36）

**有卡**：`CLIPLoader`、`VAELoader`、`ReferenceLatent`、`ConditioningZeroOut`、`CLIPTextEncode`、`VAEEncode`、`LatentUpscaleBy`、`KSampler`、`GetImageSize+`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`ImageResize+`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`ImageScaleBy`、`TTP_Image_Assy`、`SaveImage`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy cleanGpuUsed`、`LoadImage`、`VAEDecode`、`DownloadAndLoadDepthAnythingV2Model`、`DepthAnything_V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
