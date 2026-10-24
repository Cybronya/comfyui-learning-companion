---
key: 图片生成/图生图/小红书FireRed Image Edit 1.1 超高一致性｜单图编辑｜局部重绘_2090595616262021121.json
name: 小红书FireRed Image Edit 1.1 超高一致性｜单图编辑｜局部重绘_2090595616262021121
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/小红书FireRed Image Edit 1.1 超高一致性｜单图编辑｜局部重绘_2090595616262021121.json
hash: 920d59eca98f12d7
coverage: 0.868421
learned_at: 2026-10-23 12:49:05
nodes: [UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, ConditioningZeroOut, MaskFillHoles, CFGNorm, InpaintModelConditioning, KSampler, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, 孤海注释, LoadImage, Int, UNETLoader, LoraLoaderModelOnly, ModelSamplingAuraFlow, CFGNorm, SaveImage, Image Comparer (rgthree), 孤海注释, Int, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, ConditioningZeroOut, CLIPLoader, TextEncodeQwenImageEditPlus, VAEEncode, LoadImage, CR Prompt Text, KSampler, Fast Groups Bypasser (rgthree), CR Prompt Text, Image Comparer (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 362052898356238, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/小红书FireRed Image Edit 1.1 超高一致性｜单图编辑｜局部重绘_2090595616262021121.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/小红书FireRed Image Edit 1.1 超高一致性｜单图编辑｜局部重绘_2090595616262021121.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `ConditioningZeroOut`
- `MaskFillHoles`
- `CFGNorm`
- `InpaintModelConditioning`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `孤海注释`
- `LoadImage`
- `Int`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `SaveImage`
- `Image Comparer (rgthree)`
- `孤海注释`
- `Int`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `ConditioningZeroOut`
- `CLIPLoader`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `LoadImage`
- `CR Prompt Text`
- `KSampler` ★核心
- `Fast Groups Bypasser (rgthree)`
- `CR Prompt Text`
- `Image Comparer (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `362052898356238`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（33/38）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`TextEncodeQwenImageEditPlus`、`ConditioningZeroOut`、`MaskFillHoles`、`CFGNorm`、`InpaintModelConditioning`、`KSampler`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`LoadImage`、`Int`、`VAEEncode`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
