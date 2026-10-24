---
key: 图片生成/图生图/优秀的姿势模仿自动提示词Qwen-Image-Edit2511+AnyPose Lora_2007843959200030721.json
name: 优秀的姿势模仿自动提示词Qwen-Image-Edit2511+AnyPose Lora_2007843959200030721
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/优秀的姿势模仿自动提示词Qwen-Image-Edit2511+AnyPose Lora_2007843959200030721.json
hash: 8746b2f0fa1b30e6
coverage: 0.809524
learned_at: 2026-10-23 12:12:07
nodes: [FluxKontextMultiReferenceLatentMethod, LoraLoaderModelOnly, Text Concatenate, easy showAnything, SaveImage, CR Text, RH_Captioner, QwenEditOutputExtractor, PreviewImage, ImageScaleToTotalPixels, GetImageSize, ImpactMinMax, ImpactMinMax, GetImageSize, QwenEditConfigPreparer, QwenEditConfigPreparer, ImageConcanate, FluxKontextMultiReferenceLatentMethod, ConditioningZeroOut, KSampler, SaveImage, QwenVisionNode, Note, LoraLoaderModelOnly, ModelSamplingAuraFlow, CLIPLoader, VAELoader, VAEDecode, SetNode, SetNode, ImageConcanate, GetNode, GetNode, MarkdownNote, ImageScaleToTotalPixels, UNETLoader, LoadImage, LoraLoaderModelOnly, CFGNorm, LoraLoaderModelOnly, LoadImage, TextEncodeQwenImageEditPlusCustom_lrzjason]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 961048311057891, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/优秀的姿势模仿自动提示词Qwen-Image-Edit2511+AnyPose Lora_2007843959200030721.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/优秀的姿势模仿自动提示词Qwen-Image-Edit2511+AnyPose Lora_2007843959200030721.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `FluxKontextMultiReferenceLatentMethod`
- `LoraLoaderModelOnly` ★核心
- `Text Concatenate`
- `easy showAnything`
- `SaveImage`
- `CR Text`
- `RH_Captioner`
- `QwenEditOutputExtractor`
- `PreviewImage`
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `ImpactMinMax`
- `ImpactMinMax`
- `GetImageSize`
- `QwenEditConfigPreparer`
- `QwenEditConfigPreparer`
- `ImageConcanate`
- `FluxKontextMultiReferenceLatentMethod`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `SaveImage`
- `QwenVisionNode`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `ImageConcanate`
- `GetNode`
- `GetNode`
- `MarkdownNote`
- `ImageScaleToTotalPixels`
- `UNETLoader` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `CFGNorm`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`

## 关键参数

- `seed` = `961048311057891`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（34/42）

**有卡**：`FluxKontextMultiReferenceLatentMethod`、`LoraLoaderModelOnly`、`Text Concatenate`、`SaveImage`、`CR Text`、`RH_Captioner`、`QwenEditOutputExtractor`、`ImageScaleToTotalPixels`、`GetImageSize`、`ImpactMinMax`、`QwenEditConfigPreparer`、`ImageConcanate`、`ConditioningZeroOut`、`KSampler`、`QwenVisionNode`、`ModelSamplingAuraFlow`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`UNETLoader`、`LoadImage`、`CFGNorm`、`TextEncodeQwenImageEditPlusCustom_lrzjason`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
