---
key: 图片生成/文生图/三采样高质量邪修-Krea2 + Z-Image Turbo + Flux2-Klein_2071613444608057345.json
name: 三采样高质量邪修-Krea2 + Z-Image Turbo + Flux2-Klein_2071613444608057345
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/三采样高质量邪修-Krea2 + Z-Image Turbo + Flux2-Klein_2071613444608057345.json
hash: 76749e65c3c3cc22
coverage: 0.850575
learned_at: 2026-10-19 23:42:59
nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, VAEDecode, UNETLoader, CLIPLoader, SaveImage, easy cleanGpuUsed, ImageScaleBy, Image Comparer (rgthree), TTP_Image_Assy, ImageResize+, TTP_Image_Tile_Batch, SeedVR2LoadVAEModel, TTP_Tile_image_size, ImageScaleBy, easy imageSize, easy imageSize, VAELoader, KSamplerSelect, GetImageSize, LCSSharpnessCalibrate, LCSLoadData, SeedVR2VideoUpscaler, ImageResize+, Image Comparer (rgthree), SaveImage, VAELoader, easy cleanGpuUsed, VAEDecode, ConditioningZeroOut, SaveImage, KSampler, VAEEncode, easy cleanGpuUsed, Image Comparer (rgthree), TTP_Image_Assy, ImageResize+, TTP_Image_Tile_Batch, SeedVR2LoadVAEModel, TTP_Tile_image_size, ImageScaleBy, easy imageSize, easy imageSize, SeedVR2VideoUpscaler, ImageResize+, SaveImage, GetNode, Image Comparer (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadDiTModel, GetNode, UNETLoader, VAELoader, CLIPTextEncode, ConditioningZeroOut, PreviewImage, SetNode, UNETLoader, CLIPLoaderGGUF, GetNode, ImageScaleToTotalPixels, VAEEncode, ConditioningZeroOut, ReferenceLatent, ReferenceLatent, LCSColorAnchor, LCSSharpnessIntervene, CFGGuider, RandomNoise, CLIPTextEncode, Flux2Scheduler, EmptyFlux2LatentImage, SamplerCustomAdvanced, VAEDecode, ColorMatch, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), TTResolutionSelector, easy showAnything, CR Text, RH_LLMAPI_Pro_Node, ImageScaleBy]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.25, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 851726922435671, "steps": 6, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/三采样高质量邪修-Krea2 + Z-Image Turbo + Flux2-Klein_2071613444608057345.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/三采样高质量邪修-Krea2 + Z-Image Turbo + Flux2-Klein_2071613444608057345.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（87 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
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
- `KSamplerSelect` ★核心
- `GetImageSize`
- `LCSSharpnessCalibrate`
- `LCSLoadData`
- `SeedVR2VideoUpscaler`
- `ImageResize+`
- `Image Comparer (rgthree)`
- `SaveImage`
- `VAELoader`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `SaveImage`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `easy cleanGpuUsed`
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
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `PreviewImage`
- `SetNode`
- `UNETLoader` ★核心
- `CLIPLoaderGGUF`
- `GetNode`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `ReferenceLatent`
- `ReferenceLatent`
- `LCSColorAnchor`
- `LCSSharpnessIntervene`
- `CFGGuider`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `ColorMatch`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `TTResolutionSelector`
- `easy showAnything`
- `CR Text`
- `RH_LLMAPI_Pro_Node`
- `ImageScaleBy`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `851726922435671`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.25`

## 知识

覆盖率 **85%**（74/87）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`UNETLoader`、`SaveImage`、`easy cleanGpuUsed`、`ImageScaleBy`、`TTP_Image_Assy`、`ImageResize+`、`TTP_Image_Tile_Batch`、`SeedVR2LoadVAEModel`、`TTP_Tile_image_size`、`easy imageSize`、`VAELoader`、`KSamplerSelect`、`GetImageSize`、`LCSSharpnessCalibrate`、`LCSLoadData`、`SeedVR2VideoUpscaler`、`ConditioningZeroOut`、`VAEEncode`、`SeedVR2LoadDiTModel`、`CLIPLoaderGGUF`、`ImageScaleToTotalPixels`、`ReferenceLatent`、`LCSColorAnchor`、`LCSSharpnessIntervene`、`CFGGuider`、`RandomNoise`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`ColorMatch`、`LoraLoaderModelOnly`、`TTResolutionSelector`、`CR Text`、`RH_LLMAPI_Pro_Node`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
