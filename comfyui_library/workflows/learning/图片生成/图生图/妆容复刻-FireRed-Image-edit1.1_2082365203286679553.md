---
key: 图片生成/图生图/妆容复刻-FireRed-Image-edit1.1_2082365203286679553.json
name: 妆容复刻-FireRed-Image-edit1.1_2082365203286679553
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/妆容复刻-FireRed-Image-edit1.1_2082365203286679553.json
hash: 2ffe53e875fc4efe
coverage: 0.974359
learned_at: 2026-10-23 12:46:50
nodes: [LoadImage, VAEEncode, KSampler, easy imageSwitch, ModelSamplingAuraFlow, FluxKontextImageScale, CLIPLoader, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, VAELoader, CFGNorm, LoadImage, EnhancedLoadDiffusionModel, LoraLoaderModelOnly, LoraLoaderModelOnly, FluxKontextImageScale, Int, LayerUtility: ImageScaleByAspectRatio V2, TextInput_, PrimitiveNode, EmptyFlux2LatentImage, ConditioningZeroOut, VAEEncode, VAELoader, CLIPLoader, CLIPTextEncode, UNETLoader, KSampler, LoraLoaderModelOnly, LayerUtility: PurgeVRAM, VAEDecode, ImageScaleBy, GetImageSize, ReferenceLatent, ReferenceLatent, VAEDecode, LayerColor: ColorAdapter, SaveImage, Float]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 294081117846109, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/妆容复刻-FireRed-Image-edit1.1_2082365203286679553.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/妆容复刻-FireRed-Image-edit1.1_2082365203286679553.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `LoadImage`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `easy imageSwitch`
- `ModelSamplingAuraFlow`
- `FluxKontextImageScale`
- `CLIPLoader`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `VAELoader`
- `CFGNorm`
- `LoadImage`
- `EnhancedLoadDiffusionModel`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `FluxKontextImageScale`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextInput_`
- `PrimitiveNode`
- `EmptyFlux2LatentImage`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `ImageScaleBy`
- `GetImageSize`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEDecode` ★核心
- `LayerColor: ColorAdapter`
- `SaveImage`
- `Float`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `294081117846109`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`LoadImage`、`VAEEncode`、`KSampler`、`easy imageSwitch`、`ModelSamplingAuraFlow`、`FluxKontextImageScale`、`CLIPLoader`、`TextEncodeQwenImageEditPlus`、`VAELoader`、`CFGNorm`、`EnhancedLoadDiffusionModel`、`LoraLoaderModelOnly`、`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextInput_`、`EmptyFlux2LatentImage`、`ConditioningZeroOut`、`CLIPTextEncode`、`UNETLoader`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`ImageScaleBy`、`GetImageSize`、`ReferenceLatent`、`LayerColor: ColorAdapter`、`SaveImage`、`Float`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
