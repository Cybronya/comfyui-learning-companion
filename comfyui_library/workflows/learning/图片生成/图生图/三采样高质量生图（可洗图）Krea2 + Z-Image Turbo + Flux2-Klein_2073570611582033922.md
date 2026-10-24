---
key: 图片生成/图生图/三采样高质量生图（可洗图）Krea2 + Z-Image Turbo + Flux2-Klein_2073570611582033922.json
name: 三采样高质量生图（可洗图）Krea2 + Z-Image Turbo + Flux2-Klein_2073570611582033922
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/三采样高质量生图（可洗图）Krea2 + Z-Image Turbo + Flux2-Klein_2073570611582033922.json
hash: c2c855136721d224
coverage: 0.850575
learned_at: 2026-10-23 12:05:04
nodes: [ConditioningZeroOut, CLIPTextEncode, EmptyLatentImage, RH_LLMAPI_Pro_Node, TTResolutionSelector, VAELoader, VAEDecode, UNETLoader, easy showAnything, VAEEncode, ConditioningZeroOut, VAEDecode, easy cleanGpuUsed, UNETLoader, KSampler, KSampler, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, LCSColorAnchor, LCSSharpnessCalibrate, VAEEncode, ReferenceLatent, ReferenceLatent, LCSSharpnessIntervene, VAEDecode, Image Comparer (rgthree), VAELoader, LCSLoadData, UNETLoader, GetNode, ImageScaleToTotalPixels, ConditioningZeroOut, GetImageSize, SamplerCustomAdvanced, easy cleanGpuUsed, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, CFGGuider, RandomNoise, GetNode, ImageScaleBy, easy imageSize, ImageResize+, TTP_Tile_image_size, SeedVR2VideoUpscaler, easy imageSize, ImageScaleBy, ImageResize+, TTP_Image_Assy, SaveImage, Image Comparer (rgthree), TTP_Image_Tile_Batch, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, easy cleanGpuUsed, easy imageSize, ImageResize+, TTP_Tile_image_size, SeedVR2VideoUpscaler, easy imageSize, ImageScaleBy, ImageResize+, Image Comparer (rgthree), TTP_Image_Tile_Batch, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, GetNode, ImageScaleBy, TTP_Image_Assy, SaveImage, Fast Groups Bypasser (rgthree), CLIPLoader, Fast Groups Bypasser (rgthree), CR Text, CLIPLoaderGGUF, CLIPTextEncode, VAELoader, SetNode, SetNode, PreviewImage, CLIPTextEncode, Image Comparer (rgthree), SaveImage, ColorMatch, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 884962027940318, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/三采样高质量生图（可洗图）Krea2 + Z-Image Turbo + Flux2-Klein_2073570611582033922.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/三采样高质量生图（可洗图）Krea2 + Z-Image Turbo + Flux2-Klein_2073570611582033922.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（87 个）：
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `RH_LLMAPI_Pro_Node`
- `TTResolutionSelector`
- `VAELoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `easy showAnything`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `LCSColorAnchor`
- `LCSSharpnessCalibrate`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `LCSSharpnessIntervene`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `VAELoader`
- `LCSLoadData`
- `UNETLoader` ★核心
- `GetNode`
- `ImageScaleToTotalPixels`
- `ConditioningZeroOut`
- `GetImageSize`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `RandomNoise`
- `GetNode`
- `ImageScaleBy`
- `easy imageSize`
- `ImageResize+`
- `TTP_Tile_image_size`
- `SeedVR2VideoUpscaler`
- `easy imageSize`
- `ImageScaleBy`
- `ImageResize+`
- `TTP_Image_Assy`
- `SaveImage`
- `Image Comparer (rgthree)`
- `TTP_Image_Tile_Batch`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `easy cleanGpuUsed`
- `easy imageSize`
- `ImageResize+`
- `TTP_Tile_image_size`
- `SeedVR2VideoUpscaler`
- `easy imageSize`
- `ImageScaleBy`
- `ImageResize+`
- `Image Comparer (rgthree)`
- `TTP_Image_Tile_Batch`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `GetNode`
- `ImageScaleBy`
- `TTP_Image_Assy`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `CLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `CR Text`
- `CLIPLoaderGGUF`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `ColorMatch`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `884962027940318`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（74/87）

**有卡**：`ConditioningZeroOut`、`CLIPTextEncode`、`EmptyLatentImage`、`RH_LLMAPI_Pro_Node`、`TTResolutionSelector`、`VAELoader`、`VAEDecode`、`UNETLoader`、`VAEEncode`、`easy cleanGpuUsed`、`KSampler`、`LoraLoaderModelOnly`、`CLIPLoader`、`LCSColorAnchor`、`LCSSharpnessCalibrate`、`ReferenceLatent`、`LCSSharpnessIntervene`、`LCSLoadData`、`ImageScaleToTotalPixels`、`GetImageSize`、`SamplerCustomAdvanced`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`KSamplerSelect`、`CFGGuider`、`RandomNoise`、`ImageScaleBy`、`easy imageSize`、`ImageResize+`、`TTP_Tile_image_size`、`SeedVR2VideoUpscaler`、`TTP_Image_Assy`、`SaveImage`、`TTP_Image_Tile_Batch`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`CR Text`、`CLIPLoaderGGUF`、`ColorMatch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
