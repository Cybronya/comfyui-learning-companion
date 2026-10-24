---
key: 图片生成/图生图/Flux2 Klein 超强换头换脸 2026.3.9_2024684839529619458.json
name: Flux2 Klein 超强换头换脸 2026.3.9_2024684839529619458
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux2 Klein 超强换头换脸 2026.3.9_2024684839529619458.json
hash: 3da3c9c3e032cce2
coverage: 0.808511
learned_at: 2026-10-23 10:59:24
nodes: [LoadImage, LoadImage, CLIPLoader, SeedVR2LoadVAEModel, PreviewImage, VAELoader, SeedVR2VideoUpscaler, CR Prompt Text, VAEDecode, UNETLoader, LoraLoaderModelOnly, ImpactInt, SeedVR2LoadDiTModel, ImageScaleToTotalPixels, ConditioningZeroOut, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, KSampler, VAEEncode, Note, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, SaveImage, SaveImage, Image Comparer (rgthree), easy cleanGpuUsed, PrimitiveNode, KSampler, SaveImage, RH_Captioner, CLIPTextEncode, CLIPTextEncode, ConditioningZeroOut, ModelSamplingAuraFlow, Fast Groups Bypasser (rgthree), CLIPLoader, VAELoader, UNETLoader, Note, SolidMask, easy ifElse, RembgByBiRefNet, easy isMaskEmpty, LoadRembgByBiRefNetModel, Flux2KleinEditTextEncode_EditUtils, EmptyFlux2LatentImage, PreviewImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.45000000000000007, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 1087293702412929, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Flux2 Klein 超强换头换脸 2026.3.9_2024684839529619458.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux2 Klein 超强换头换脸 2026.3.9_2024684839529619458.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `SeedVR2LoadVAEModel`
- `PreviewImage`
- `VAELoader`
- `SeedVR2VideoUpscaler`
- `CR Prompt Text`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImpactInt`
- `SeedVR2LoadDiTModel`
- `ImageScaleToTotalPixels`
- `ConditioningZeroOut`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `VAEEncode` ★核心
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `easy cleanGpuUsed`
- `PrimitiveNode`
- `KSampler` ★核心
- `SaveImage`
- `RH_Captioner`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `Fast Groups Bypasser (rgthree)`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `Note`
- `SolidMask`
- `easy ifElse`
- `RembgByBiRefNet`
- `easy isMaskEmpty`
- `LoadRembgByBiRefNetModel`
- `Flux2KleinEditTextEncode_EditUtils`
- `EmptyFlux2LatentImage`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1087293702412929`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.45000000000000007`

## 知识

覆盖率 **81%**（38/47）

**有卡**：`LoadImage`、`CLIPLoader`、`SeedVR2LoadVAEModel`、`VAELoader`、`SeedVR2VideoUpscaler`、`CR Prompt Text`、`VAEDecode`、`UNETLoader`、`LoraLoaderModelOnly`、`ImpactInt`、`SeedVR2LoadDiTModel`、`ImageScaleToTotalPixels`、`ConditioningZeroOut`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`VAEEncode`、`SaveImage`、`easy cleanGpuUsed`、`RH_Captioner`、`CLIPTextEncode`、`ModelSamplingAuraFlow`、`SolidMask`、`RembgByBiRefNet`、`easy isMaskEmpty`、`LoadRembgByBiRefNetModel`、`Flux2KleinEditTextEncode_EditUtils`、`EmptyFlux2LatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
