---
key: 图片生成/图生图/Qwen构图+SRPO_Wan2.2质感提升_1987947203429863426.json
name: Qwen构图+SRPO_Wan2.2质感提升_1987947203429863426
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen构图+SRPO_Wan2.2质感提升_1987947203429863426.json
hash: ae5ca34c3501d6f6
coverage: 0.9375
learned_at: 2026-10-23 11:22:29
nodes: [VAELoader, CLIPLoader, UNETLoader, UpscaleModelLoader, ConditioningZeroOut, UNETLoader, VAELoader, DualCLIPLoader, FluxGuidance, VAEEncode, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, KSampler, LoraLoaderModelOnly, VAELoader, CLIPTextEncode, VAEEncode, CLIPLoader, KSampler, EmptySD3LatentImage, ModelSamplingAuraFlow, CLIPTextEncode, UNETLoader, CLIPTextEncode, Text Concatenate, PathchSageAttentionKJ, ModelSamplingSD3, Text Multiline, VAEDecode, Fast Groups Bypasser (rgthree), SaveImage, VAEDecode, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, SaveImage, VAEDecode, ImageUpscaleWithModel, ImageScaleBy, SaveImage, SaveImage, Text Multiline, KSampler, Image Comparer (rgthree), LoraLoader, LoraLoader, LoraLoader, Image Comparer (rgthree)]
patterns: [lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "WAN2.2-LowNoise_SmartphoneSnapshotPhotoReality_v3_by-AI_Characters.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 45221066186065, "steps": 8, "strength_clip": 0.7000000000000002, "strength_model": 0.7000000000000002}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen构图+SRPO_Wan2.2质感提升_1987947203429863426.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen构图+SRPO_Wan2.2质感提升_1987947203429863426.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `UpscaleModelLoader`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `Text Concatenate`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `Text Multiline`
- `VAEDecode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `VAEDecode` ★核心
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `VAEDecode` ★核心
- `ImageUpscaleWithModel`
- `ImageScaleBy`
- `SaveImage`
- `SaveImage`
- `Text Multiline`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `Image Comparer (rgthree)`

**识别到的模式**：lora

## 关键参数

- `seed` = `45221066186065`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `WAN2.2-LowNoise_SmartphoneSnapshotPhotoReality_v3_by-AI_Characters.safetensors`
- `strength_model` = `0.7000000000000002`
- `strength_clip` = `0.7000000000000002`

## 知识

覆盖率 **94%**（45/48）

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`UpscaleModelLoader`、`ConditioningZeroOut`、`DualCLIPLoader`、`FluxGuidance`、`VAEEncode`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`KSampler`、`EmptySD3LatentImage`、`ModelSamplingAuraFlow`、`Text Concatenate`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`Text Multiline`、`VAEDecode`、`SaveImage`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`ImageUpscaleWithModel`、`ImageScaleBy`、`LoraLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
