---
key: 图片生成/文生图/Krea2 + Z-Image Turbo + Flux2-Klein三模王炸合体_2071802083606618114.json
name: Krea2 + Z-Image Turbo + Flux2-Klein三模王炸合体_2071802083606618114
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Krea2 + Z-Image Turbo + Flux2-Klein三模王炸合体_2071802083606618114.json
hash: df62e7201de2ce9b
coverage: 0.870588
learned_at: 2026-10-19 23:41:13
nodes: [CLIPLoader, EmptyLatentImage, KSampler, VAEDecode, VAEDecode, RandomNoise, SamplerCustomAdvanced, UNETLoader, CLIPLoader, VAEEncode, ReferenceLatent, ReferenceLatent, ConditioningZeroOut, easy cleanGpuUsed, ImageScaleBy, Image Comparer (rgthree), TTP_Image_Assy, ImageResize+, TTP_Image_Tile_Batch, SeedVR2LoadVAEModel, TTP_Tile_image_size, ImageScaleBy, easy imageSize, easy imageSize, VAELoader, LCSSharpnessIntervene, LCSColorAnchor, CFGGuider, Flux2Scheduler, KSamplerSelect, GetImageSize, LCSSharpnessCalibrate, LCSLoadData, ColorMatch, SetNode, SeedVR2VideoUpscaler, ImageResize+, Image Comparer (rgthree), GetNode, EmptyFlux2LatentImage, CLIPLoaderGGUF, VAELoader, easy cleanGpuUsed, VAEDecode, CLIPTextEncode, ConditioningZeroOut, ImageScaleToTotalPixels, KSampler, VAEEncode, easy cleanGpuUsed, ImageScaleBy, Image Comparer (rgthree), TTP_Image_Assy, ImageResize+, TTP_Image_Tile_Batch, SeedVR2LoadVAEModel, TTP_Tile_image_size, ImageScaleBy, easy imageSize, easy imageSize, SeedVR2VideoUpscaler, ImageResize+, SaveImage, GetNode, Label (rgthree), Image Comparer (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadDiTModel, GetNode, UNETLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, ConditioningZeroOut, PreviewImage, UNETLoader, SetNode, Fast Groups Bypasser (rgthree), CLIPTextEncode, SaveImage, SaveImage, TTResolutionSelector, CR Text, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.25, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 500501165580563, "steps": 6, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Krea2 + Z-Image Turbo + Flux2-Klein三模王炸合体_2071802083606618114.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Krea2 + Z-Image Turbo + Flux2-Klein三模王炸合体_2071802083606618114.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（85 个）：
- `CLIPLoader`
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
- `EmptyFlux2LatentImage`
- `CLIPLoaderGGUF`
- `VAELoader`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ImageScaleToTotalPixels`
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
- `Label (rgthree)`
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
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `SaveImage`
- `TTResolutionSelector`
- `CR Text`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `500501165580563`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.25`

## 知识

覆盖率 **87%**（74/85）

**有卡**：`CLIPLoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`RandomNoise`、`SamplerCustomAdvanced`、`UNETLoader`、`VAEEncode`、`ReferenceLatent`、`ConditioningZeroOut`、`easy cleanGpuUsed`、`ImageScaleBy`、`TTP_Image_Assy`、`ImageResize+`、`TTP_Image_Tile_Batch`、`SeedVR2LoadVAEModel`、`TTP_Tile_image_size`、`easy imageSize`、`VAELoader`、`LCSSharpnessIntervene`、`LCSColorAnchor`、`CFGGuider`、`Flux2Scheduler`、`KSamplerSelect`、`GetImageSize`、`LCSSharpnessCalibrate`、`LCSLoadData`、`ColorMatch`、`SeedVR2VideoUpscaler`、`EmptyFlux2LatentImage`、`CLIPLoaderGGUF`、`CLIPTextEncode`、`ImageScaleToTotalPixels`、`SaveImage`、`Label (rgthree)`、`SeedVR2LoadDiTModel`、`LoraLoaderModelOnly`、`TTResolutionSelector`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
