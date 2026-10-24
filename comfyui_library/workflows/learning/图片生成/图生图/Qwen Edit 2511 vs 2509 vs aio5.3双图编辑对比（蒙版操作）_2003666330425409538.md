---
key: 图片生成/图生图/Qwen Edit 2511 vs 2509 vs aio5.3双图编辑对比（蒙版操作）_2003666330425409538.json
name: Qwen Edit 2511 vs 2509 vs aio5.3双图编辑对比（蒙版操作）_2003666330425409538
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Edit 2511 vs 2509 vs aio5.3双图编辑对比（蒙版操作）_2003666330425409538.json
hash: 1b08a4ea38d800fb
coverage: 0.878049
learned_at: 2026-10-23 11:12:00
nodes: [VAELoader, CLIPLoader, UNETLoader, LoraLoaderModelOnly, ConditioningZeroOut, QwenEditOutputExtractor, PreviewImage, QwenEditAdaptiveLongestEdge, TextEncodeQwenImageEditPlusCustom_lrzjason, QwenEditAdaptiveLongestEdge, LoadImage, LoadImage, AddLabel, QwenEditConfigPreparer, QwenEditConfigPreparer, KSampler, CropWithPadInfo, AddLabel, ImageScaleBy, PreviewImage, VAEDecode, KSampler, CropWithPadInfo, ImageScaleBy, PreviewImage, VAEDecode, LoraLoaderModelOnly, Image Comparer (rgthree), AddLabel, PDIMAGE_LongerSize, UNETLoader, KSampler, CropWithPadInfo, ImageScaleBy, PreviewImage, VAEDecode, CheckpointLoaderSimple, AddLabel, SaveImage, CR Prompt Text, ImageConcatMulti]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v5.3.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 1091359629774735, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Edit 2511 vs 2509 vs aio5.3双图编辑对比（蒙版操作）_2003666330425409538.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Edit 2511 vs 2509 vs aio5.3双图编辑对比（蒙版操作）_2003666330425409538.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `QwenEditOutputExtractor`
- `PreviewImage`
- `QwenEditAdaptiveLongestEdge`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `QwenEditAdaptiveLongestEdge`
- `LoadImage`
- `LoadImage`
- `AddLabel`
- `QwenEditConfigPreparer`
- `QwenEditConfigPreparer`
- `KSampler` ★核心
- `CropWithPadInfo`
- `AddLabel`
- `ImageScaleBy`
- `PreviewImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CropWithPadInfo`
- `ImageScaleBy`
- `PreviewImage`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `AddLabel`
- `PDIMAGE_LongerSize`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CropWithPadInfo`
- `ImageScaleBy`
- `PreviewImage`
- `VAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `AddLabel`
- `SaveImage`
- `CR Prompt Text`
- `ImageConcatMulti`

## 关键参数

- `seed` = `1091359629774735`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v5.3.safetensors`

## 知识

覆盖率 **88%**（36/41）

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`QwenEditOutputExtractor`、`QwenEditAdaptiveLongestEdge`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`LoadImage`、`AddLabel`、`QwenEditConfigPreparer`、`KSampler`、`CropWithPadInfo`、`ImageScaleBy`、`VAEDecode`、`PDIMAGE_LongerSize`、`CheckpointLoaderSimple`、`SaveImage`、`CR Prompt Text`、`ImageConcatMulti`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
