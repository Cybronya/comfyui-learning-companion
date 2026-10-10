---
key: Qwen构图+SRPO_Wan2.2质感提升_1973197627275784193.json
name: Qwen构图+SRPO_Wan2.2质感提升_1973197627275784193
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen构图+SRPO_Wan2.2质感提升_1973197627275784193.json
hash: af0b1c4639e54178
coverage: 0.833333
learned_at: 2026-10-10 20:59:10
nodes: [VAELoader, CLIPLoader, UNETLoader, UpscaleModelLoader, ConditioningZeroOut, UNETLoader, VAELoader, DualCLIPLoader, FluxGuidance, VAEEncode, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, KSampler, LoraLoaderModelOnly, VAELoader, CLIPTextEncode, VAEEncode, CLIPLoader, KSampler, KSampler, EmptySD3LatentImage, ModelSamplingAuraFlow, CLIPTextEncode, UNETLoader, CLIPTextEncode, LoraLoader, LoraLoader, LoraLoader, Text Concatenate, PathchSageAttentionKJ, ModelSamplingSD3, Text Multiline, VAEDecode, Image Comparer (rgthree), Fast Groups Bypasser (rgthree), SaveImage, Image Comparer (rgthree), VAEDecode, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, SaveImage, VAEDecode, ImageUpscaleWithModel, ImageScaleBy, Text Multiline, SaveImage, SaveImage]
patterns: [lora]
missing: [LayerUtility: ImageReel, LayerUtility: ImageReelComposit, Text Concatenate, Text Multiline, Text Multiline]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "WAN2.2-LowNoise_SmartphoneSnapshotPhotoReality_v3_by-AI_Characters.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 724802566875783, "steps": 8, "strength_clip": 0.7000000000000002, "strength_model": 0.7000000000000002}
discoveries: [次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# Qwen构图+SRPO_Wan2.2质感提升_1973197627275784193.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen构图+SRPO_Wan2.2质感提升_1973197627275784193.json`

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
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `Text Concatenate`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `Text Multiline`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `VAEDecode` ★核心
- `ImageUpscaleWithModel`
- `ImageScaleBy`
- `Text Multiline`
- `SaveImage`
- `SaveImage`

**识别到的模式**：lora

## 关键参数

- `seed` = `724802566875783`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `WAN2.2-LowNoise_SmartphoneSnapshotPhotoReality_v3_by-AI_Characters.safetensors`
- `strength_model` = `0.7000000000000002`
- `strength_clip` = `0.7000000000000002`

## 知识

覆盖率 **83%**（40/48）

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`UpscaleModelLoader`、`ConditioningZeroOut`、`DualCLIPLoader`、`FluxGuidance`、`VAEEncode`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`KSampler`、`EmptySD3LatentImage`、`ModelSamplingAuraFlow`、`LoraLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VAEDecode`、`SaveImage`、`ImageUpscaleWithModel`、`ImageScaleBy`

**缺卡**（5）：`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`Text Concatenate`、`Text Multiline`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
