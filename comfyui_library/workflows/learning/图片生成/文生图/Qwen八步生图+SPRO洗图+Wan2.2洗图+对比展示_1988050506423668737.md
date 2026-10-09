---
key: 图片生成/文生图/Qwen八步生图+SPRO洗图+Wan2.2洗图+对比展示_1988050506423668737.json
name: Qwen八步生图+SPRO洗图+Wan2.2洗图+对比展示_1988050506423668737.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen八步生图+SPRO洗图+Wan2.2洗图+对比展示_1988050506423668737.json
hash: 932324398b86f548
coverage: 0.816327
learned_at: 2026-10-09 21:16:00
nodes: [Text Multiline, EmptySD3LatentImage, UNETLoader, DualCLIPLoader, VAELoader, UpscaleModelLoader, LoraLoaderModelOnly, CLIPTextEncode, ImageUpscaleWithModel, ImageScaleBy, FluxGuidance, ConditioningZeroOut, VAEEncode, KSampler, UNETLoader, CLIPLoader, VAELoader, Text Concatenate, LoraLoader, LoraLoader, PathchSageAttentionKJ, LoraLoader, ModelSamplingSD3, KSampler, SaveImage, SaveImage, LayerUtility: ImageReelComposit, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), Image Comparer (rgthree), Image Comparer (rgthree), VAEDecode, VAEEncode, VAEDecode, SaveImage, KSampler, CLIPTextEncode, CLIPTextEncode, VAEDecode, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, ModelSamplingAuraFlow, Text Multiline, CLIPTextEncode, CLIPTextEncode, LayerUtility: ImageReel, SaveImage]
patterns: [lora]
missing: [LayerUtility: ImageReel, LayerUtility: ImageReelComposit, Text Concatenate, Text Multiline, Text Multiline]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "WAN2.2-LowNoise_SmartphoneSnapshotPhotoReality_v3_by-AI_Characters.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 724802566875783, "steps": 8, "strength_clip": 0.7000000000000002, "strength_model": 0.7000000000000002}
discoveries: [次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen八步生图+SPRO洗图+Wan2.2洗图+对比展示_1988050506423668737.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1988050506423668737.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `Text Multiline`
- `EmptySD3LatentImage`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `UpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ImageUpscaleWithModel`
- `ImageScaleBy`
- `FluxGuidance`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Text Concatenate`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `PathchSageAttentionKJ`
- `LoraLoader` ★核心
- `ModelSamplingSD3`
- `KSampler` ★核心
- `SaveImage`
- `SaveImage`
- `LayerUtility: ImageReelComposit`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `Text Multiline`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageReel`
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

覆盖率 **82%**（40/49）

**有卡**：`EmptySD3LatentImage`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`UpscaleModelLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`ImageUpscaleWithModel`、`ImageScaleBy`、`FluxGuidance`、`ConditioningZeroOut`、`VAEEncode`、`KSampler`、`CLIPLoader`、`LoraLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`SaveImage`、`VAEDecode`、`ModelSamplingAuraFlow`

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
