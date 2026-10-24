---
key: 图片生成/图生图/Flux2 Klein 9B图像编辑+Lora-单图 浮云2.9_2020706923749842945.json
name: Flux2 Klein 9B图像编辑+Lora-单图 浮云2.9_2020706923749842945
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux2 Klein 9B图像编辑+Lora-单图 浮云2.9_2020706923749842945.json
hash: e2e84137ea8715c0
coverage: 0.891566
learned_at: 2026-10-23 10:59:05
nodes: [KSamplerSelect, KSamplerSelect, UNETLoader, CLIPLoader, VAELoader, CFGGuider, ConditioningZeroOut, CLIPTextEncode, ReferenceLatent, ReferenceLatent, CLIPLoader, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, UNETLoader, Note, ImpactSwitch, Flux2Scheduler, EmptyFlux2LatentImage, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, VAELoader, VAEDecode, easy showAnything, GetImageSize, Image Comparer (rgthree), EmptyLatentImage, ImpactInt, LoraLoaderModelOnly, ImpactSwitch, SaveImage, RH_LLMAPI_NODE, ModelSamplingAuraFlow, EmptyLatentImage, SaveImage, CFGNorm, FluxResolutionNode, SaveImage, VAEDecode, SamplerCustomAdvanced, Image Comparer (rgthree), SamplerCustomAdvanced, KSampler, CLIPLoader, VAELoader, ReferenceLatent, Flux2Scheduler, ImpactSwitch, RandomNoise, LayerUtility: ImageReelComposit, LoadImage, UNETLoader, CLIPTextEncode, ReferenceLatent, CFGGuider, ConditioningZeroOut, VAEEncode, LayerUtility: ImageReel, ImageScaleToTotalPixels, EmptyFlux2LatentImage, Text Multiline, KOOK_ImageCompression, Image Comparer (rgthree), ReferenceLatent, ConditioningZeroOut, ReferenceLatent, RandomNoise, SamplerCustomAdvanced, VAEEncode, CFGGuider, VAEDecode, GetImageSize, EmptyFlux2LatentImage, VAELoader, CLIPLoader, KSamplerSelect, Flux2Scheduler, ImageScaleToTotalPixels, UNETLoader, CLIPTextEncode, LoraLoaderModelOnly, VAEDecode, SaveImage, Image Comparer (rgthree)]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 188112630318995, "steps": 8, "width": 720}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Flux2 Klein 9B图像编辑+Lora-单图 浮云2.9_2020706923749842945.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux2 Klein 9B图像编辑+Lora-单图 浮云2.9_2020706923749842945.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（83 个）：
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CFGGuider`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `CLIPLoader`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader` ★核心
- `Note`
- `ImpactSwitch`
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `VAELoader`
- `VAEDecode` ★核心
- `easy showAnything`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `EmptyLatentImage` ★核心
- `ImpactInt`
- `LoraLoaderModelOnly` ★核心
- `ImpactSwitch`
- `SaveImage`
- `RH_LLMAPI_NODE`
- `ModelSamplingAuraFlow`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `CFGNorm`
- `FluxResolutionNode`
- `SaveImage`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `Image Comparer (rgthree)`
- `SamplerCustomAdvanced` ★核心
- `KSampler` ★核心
- `CLIPLoader`
- `VAELoader`
- `ReferenceLatent`
- `Flux2Scheduler`
- `ImpactSwitch`
- `RandomNoise`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `CFGGuider`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `LayerUtility: ImageReel`
- `ImageScaleToTotalPixels`
- `EmptyFlux2LatentImage`
- `Text Multiline`
- `KOOK_ImageCompression`
- `Image Comparer (rgthree)`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `CFGGuider`
- `VAEDecode` ★核心
- `GetImageSize`
- `EmptyFlux2LatentImage`
- `VAELoader`
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `ImageScaleToTotalPixels`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `188112630318995`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（74/83）

**有卡**：`KSamplerSelect`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CFGGuider`、`ConditioningZeroOut`、`CLIPTextEncode`、`ReferenceLatent`、`TextEncodeQwenImageEditPlus`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`FluxKontextMultiReferenceLatentMethod`、`VAEDecode`、`GetImageSize`、`EmptyLatentImage`、`ImpactInt`、`LoraLoaderModelOnly`、`SaveImage`、`RH_LLMAPI_NODE`、`ModelSamplingAuraFlow`、`CFGNorm`、`FluxResolutionNode`、`SamplerCustomAdvanced`、`KSampler`、`RandomNoise`、`LayerUtility: ImageReelComposit`、`LoadImage`、`VAEEncode`、`LayerUtility: ImageReel`、`ImageScaleToTotalPixels`、`Text Multiline`、`KOOK_ImageCompression`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
