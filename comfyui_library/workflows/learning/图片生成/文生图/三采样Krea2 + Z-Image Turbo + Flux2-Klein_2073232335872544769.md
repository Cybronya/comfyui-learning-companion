---
key: 图片生成/文生图/三采样Krea2 + Z-Image Turbo + Flux2-Klein_2073232335872544769.json
name: 三采样Krea2 + Z-Image Turbo + Flux2-Klein_2073232335872544769
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/三采样Krea2 + Z-Image Turbo + Flux2-Klein_2073232335872544769.json
hash: 8f2c5784361000f1
coverage: 0.869048
learned_at: 2026-10-20 00:02:12
nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, VAEDecode, VAEDecode, RandomNoise, SamplerCustomAdvanced, UNETLoader, CLIPLoader, VAEEncode, ReferenceLatent, ReferenceLatent, ConditioningZeroOut, SaveImage, easy cleanGpuUsed, ImageScaleBy, Image Comparer (rgthree), TTP_Image_Assy, ImageResize+, TTP_Image_Tile_Batch, SeedVR2LoadVAEModel, TTP_Tile_image_size, ImageScaleBy, easy imageSize, easy imageSize, VAELoader, LCSSharpnessIntervene, LCSColorAnchor, CFGGuider, Flux2Scheduler, KSamplerSelect, GetImageSize, LCSSharpnessCalibrate, LCSLoadData, ColorMatch, SetNode, SeedVR2VideoUpscaler, ImageResize+, Image Comparer (rgthree), GetNode, SaveImage, EmptyFlux2LatentImage, CLIPLoaderGGUF, VAELoader, easy cleanGpuUsed, VAEDecode, CLIPTextEncode, ConditioningZeroOut, ImageScaleToTotalPixels, SaveImage, KSampler, VAEEncode, easy cleanGpuUsed, ImageScaleBy, Image Comparer (rgthree), TTP_Image_Assy, ImageResize+, TTP_Image_Tile_Batch, SeedVR2LoadVAEModel, TTP_Tile_image_size, ImageScaleBy, easy imageSize, easy imageSize, SeedVR2VideoUpscaler, ImageResize+, SaveImage, GetNode, Image Comparer (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadDiTModel, GetNode, UNETLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, ConditioningZeroOut, PreviewImage, UNETLoader, TTResolutionSelector, SetNode, Fast Groups Bypasser (rgthree), CR Text]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.25, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1123344009098332, "steps": 6, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/三采样Krea2 + Z-Image Turbo + Flux2-Klein_2073232335872544769.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/三采样Krea2 + Z-Image Turbo + Flux2-Klein_2073232335872544769.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（84 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `SaveImage`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `Image Comparer (rgthree)`
- `TTP_Image_Assy`
- `ImageResize+`
- `TTP_Image_Tile_Batch`
- `SeedVR2LoadVAEModel`
- `TTP_Tile_image_size`
- `ImageScaleBy`
- `easy imageSize`
- `easy imageSize`
- `VAELoader`
- `LCSSharpnessIntervene`
- `LCSColorAnchor`
- `CFGGuider`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `GetImageSize`
- `LCSSharpnessCalibrate`
- `LCSLoadData`
- `ColorMatch`
- `SetNode`
- `SeedVR2VideoUpscaler`
- `ImageResize+`
- `Image Comparer (rgthree)`
- `GetNode`
- `SaveImage`
- `EmptyFlux2LatentImage`
- `CLIPLoaderGGUF`
- `VAELoader`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ImageScaleToTotalPixels`
- `SaveImage`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `Image Comparer (rgthree)`
- `TTP_Image_Assy`
- `ImageResize+`
- `TTP_Image_Tile_Batch`
- `SeedVR2LoadVAEModel`
- `TTP_Tile_image_size`
- `ImageScaleBy`
- `easy imageSize`
- `easy imageSize`
- `SeedVR2VideoUpscaler`
- `ImageResize+`
- `SaveImage`
- `GetNode`
- `Image Comparer (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadDiTModel`
- `GetNode`
- `UNETLoader` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `PreviewImage`
- `UNETLoader` ★核心
- `TTResolutionSelector`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `CR Text`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1123344009098332`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.25`

## 知识

覆盖率 **87%**（73/84）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`RandomNoise`、`SamplerCustomAdvanced`、`UNETLoader`、`VAEEncode`、`ReferenceLatent`、`ConditioningZeroOut`、`SaveImage`、`easy cleanGpuUsed`、`ImageScaleBy`、`TTP_Image_Assy`、`ImageResize+`、`TTP_Image_Tile_Batch`、`SeedVR2LoadVAEModel`、`TTP_Tile_image_size`、`easy imageSize`、`VAELoader`、`LCSSharpnessIntervene`、`LCSColorAnchor`、`CFGGuider`、`Flux2Scheduler`、`KSamplerSelect`、`GetImageSize`、`LCSSharpnessCalibrate`、`LCSLoadData`、`ColorMatch`、`SeedVR2VideoUpscaler`、`EmptyFlux2LatentImage`、`CLIPLoaderGGUF`、`ImageScaleToTotalPixels`、`SeedVR2LoadDiTModel`、`LoraLoaderModelOnly`、`TTResolutionSelector`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
