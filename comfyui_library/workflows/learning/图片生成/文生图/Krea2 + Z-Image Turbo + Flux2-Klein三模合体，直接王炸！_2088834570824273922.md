---
key: 图片生成/文生图/Krea2 + Z-Image Turbo + Flux2-Klein三模合体，直接王炸！_2088834570824273922.json
name: Krea2 + Z-Image Turbo + Flux2-Klein三模合体，直接王炸！_2088834570824273922
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Krea2 + Z-Image Turbo + Flux2-Klein三模合体，直接王炸！_2088834570824273922.json
hash: be9b0a9106d5d2af
coverage: 0.910448
learned_at: 2026-10-20 00:58:53
nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, VAEDecode, VAEDecode, RandomNoise, SamplerCustomAdvanced, UNETLoader, CLIPLoader, VAEEncode, ReferenceLatent, ReferenceLatent, ConditioningZeroOut, easy cleanGpuUsed, ImageScaleBy, Image Comparer (rgthree), TTP_Image_Assy, ImageResize+, TTP_Image_Tile_Batch, SeedVR2LoadVAEModel, TTP_Tile_image_size, ImageScaleBy, easy imageSize, easy imageSize, VAELoader, LCSSharpnessIntervene, LCSColorAnchor, CFGGuider, Flux2Scheduler, KSamplerSelect, GetImageSize, LCSSharpnessCalibrate, LCSLoadData, ColorMatch, SeedVR2VideoUpscaler, ImageResize+, Image Comparer (rgthree), EmptyFlux2LatentImage, CLIPLoaderGGUF, VAELoader, easy cleanGpuUsed, CLIPTextEncode, ImageScaleToTotalPixels, KSampler, VAEEncode, Label (rgthree), SeedVR2LoadDiTModel, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, ConditioningZeroOut, PreviewImage, UNETLoader, SaveImage, SaveImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), VAEDecode, SetNode, CR Text, TTResolutionSelector, SaveImage, ConditioningZeroOut, UNETLoader, LoraLoaderModelOnly]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.25, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 478747904334674, "steps": 6, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Krea2 + Z-Image Turbo + Flux2-Klein三模合体，直接王炸！_2088834570824273922.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Krea2 + Z-Image Turbo + Flux2-Klein三模合体，直接王炸！_2088834570824273922.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（67 个）：
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
- `SeedVR2VideoUpscaler`
- `ImageResize+`
- `Image Comparer (rgthree)`
- `EmptyFlux2LatentImage`
- `CLIPLoaderGGUF`
- `VAELoader`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `ImageScaleToTotalPixels`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `Label (rgthree)`
- `SeedVR2LoadDiTModel`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `PreviewImage`
- `UNETLoader` ★核心
- `SaveImage`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `SetNode`
- `CR Text`
- `TTResolutionSelector`
- `SaveImage`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `478747904334674`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.25`

## 知识

覆盖率 **91%**（61/67）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`RandomNoise`、`SamplerCustomAdvanced`、`UNETLoader`、`VAEEncode`、`ReferenceLatent`、`ConditioningZeroOut`、`easy cleanGpuUsed`、`ImageScaleBy`、`TTP_Image_Assy`、`ImageResize+`、`TTP_Image_Tile_Batch`、`SeedVR2LoadVAEModel`、`TTP_Tile_image_size`、`easy imageSize`、`VAELoader`、`LCSSharpnessIntervene`、`LCSColorAnchor`、`CFGGuider`、`Flux2Scheduler`、`KSamplerSelect`、`GetImageSize`、`LCSSharpnessCalibrate`、`LCSLoadData`、`ColorMatch`、`SeedVR2VideoUpscaler`、`EmptyFlux2LatentImage`、`CLIPLoaderGGUF`、`ImageScaleToTotalPixels`、`Label (rgthree)`、`SeedVR2LoadDiTModel`、`LoraLoaderModelOnly`、`SaveImage`、`CR Text`、`TTResolutionSelector`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
