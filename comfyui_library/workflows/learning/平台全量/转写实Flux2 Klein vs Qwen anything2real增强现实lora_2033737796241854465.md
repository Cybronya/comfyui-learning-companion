---
key: 平台全量/转写实Flux2 Klein vs Qwen anything2real增强现实lora_2033737796241854465.json
name: 转写实Flux2 Klein vs Qwen anything2real增强现实lora_2033737796241854465
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/转写实Flux2 Klein vs Qwen anything2real增强现实lora_2033737796241854465.json
hash: 3df4a8a3192340bb
coverage: 0.888889
learned_at: 2026-11-14 02:47:37
nodes: [ReferenceLatent, ReferenceLatent, CLIPTextEncode, CLIPLoader, UNETLoader, VAEEncode, ConditioningZeroOut, LayerUtility: ImageReelComposit, PreviewImage, EmptyFlux2LatentImage, SaveImage, VAELoader, QwenEditAdaptiveLongestEdge, LoraLoaderModelOnly, LayerUtility: ImageReel, Image Comparer (rgthree), ImageScaleBy, Image Comparer (rgthree), PreviewAny, CropWithPadInfo, ConditioningZeroOut, CLIPLoader, SaveImage, CFGGuider, RandomNoise, CR Text, PrimitiveStringMultiline, LoadImage, QwenEditConfigPreparer, Flux2Scheduler, VAELoader, ImageScaleToTotalPixels, GetImageSize, SamplerCustomAdvanced, UNETLoader, TextEncodeQwenImageEditPlusCustom_lrzjason, KSampler, LoraLoaderModelOnly, VAEDecode, KSamplerSelect, easy cleanGpuUsed, LoraLoaderModelOnly, Seed Everywhere, VAEDecode, QwenEditOutputExtractor]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 1091359629774735, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/转写实Flux2 Klein vs Qwen anything2real增强现实lora_2033737796241854465.json

> 来源文件 `comfyui_library/workflows/平台全量/转写实Flux2 Klein vs Qwen anything2real增强现实lora_2033737796241854465.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `ReferenceLatent`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `LayerUtility: ImageReelComposit`
- `PreviewImage`
- `EmptyFlux2LatentImage`
- `SaveImage`
- `VAELoader`
- `QwenEditAdaptiveLongestEdge`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageReel`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `Image Comparer (rgthree)`
- `PreviewAny`
- `CropWithPadInfo`
- `ConditioningZeroOut`
- `CLIPLoader`
- `SaveImage`
- `CFGGuider`
- `RandomNoise`
- `CR Text`
- `PrimitiveStringMultiline`
- `LoadImage`
- `QwenEditConfigPreparer`
- `Flux2Scheduler`
- `VAELoader`
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `Seed Everywhere`
- `VAEDecode` ★核心
- `QwenEditOutputExtractor`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1091359629774735`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **89%**（40/45）

**有卡**：`ReferenceLatent`、`CLIPTextEncode`、`CLIPLoader`、`UNETLoader`、`VAEEncode`、`ConditioningZeroOut`、`LayerUtility: ImageReelComposit`、`EmptyFlux2LatentImage`、`SaveImage`、`VAELoader`、`QwenEditAdaptiveLongestEdge`、`LoraLoaderModelOnly`、`LayerUtility: ImageReel`、`ImageScaleBy`、`CropWithPadInfo`、`CFGGuider`、`RandomNoise`、`CR Text`、`LoadImage`、`QwenEditConfigPreparer`、`Flux2Scheduler`、`ImageScaleToTotalPixels`、`GetImageSize`、`SamplerCustomAdvanced`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`KSampler`、`VAEDecode`、`KSamplerSelect`、`easy cleanGpuUsed`、`Seed Everywhere`、`QwenEditOutputExtractor`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
