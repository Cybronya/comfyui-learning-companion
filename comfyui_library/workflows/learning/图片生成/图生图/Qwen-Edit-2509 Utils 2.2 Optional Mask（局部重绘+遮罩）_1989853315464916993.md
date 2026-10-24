---
key: 图片生成/图生图/Qwen-Edit-2509 Utils 2.2 Optional Mask（局部重绘+遮罩）_1989853315464916993.json
name: Qwen-Edit-2509 Utils 2.2 Optional Mask（局部重绘+遮罩）_1989853315464916993
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Edit-2509 Utils 2.2 Optional Mask（局部重绘+遮罩）_1989853315464916993.json
hash: 68e1f2b2461a186d
coverage: 0.795455
learned_at: 2026-10-23 11:15:24
nodes: [QwenEditAdaptiveLongestEdge, QwenEditAdaptiveLongestEdge, QwenEditConfigPreparer, QwenEditConfigPreparer, VAEDecode, PreviewImage, PreviewImage, CropWithPadInfo, QwenEditAdaptiveLongestEdge, QwenEditAdaptiveLongestEdge, TextEncodeQwenImageEditPlusCustom_lrzjason, PreviewImage, PreviewImage, QwenEditConfigPreparer, QwenEditConfigPreparer, SaveImage, LoraLoaderModelOnly, UNETLoader, LoadImage, LoadImage, QwenEditOutputExtractor, KSampler, ConditioningZeroOut, KSampler, QwenEditOutputExtractor, VAEDecode, ImageScaleBy, CropWithPadInfo, Image Comparer (rgthree), Image Comparer (rgthree), easy imageConcat, easy imageConcat, PreviewImage, SaveImage, ImageScaleBy, PreviewImage, LoadImage, ConditioningZeroOut, TextEncodeQwenImageEditPlusCustom_lrzjason, VAELoader, CLIPLoader, PrimitiveStringMultiline, LoraLoaderModelOnly, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 1091359629774735, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Edit-2509 Utils 2.2 Optional Mask（局部重绘+遮罩）_1989853315464916993.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Edit-2509 Utils 2.2 Optional Mask（局部重绘+遮罩）_1989853315464916993.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `QwenEditAdaptiveLongestEdge`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditConfigPreparer`
- `QwenEditConfigPreparer`
- `VAEDecode` ★核心
- `PreviewImage`
- `PreviewImage`
- `CropWithPadInfo`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditAdaptiveLongestEdge`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `PreviewImage`
- `PreviewImage`
- `QwenEditConfigPreparer`
- `QwenEditConfigPreparer`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `QwenEditOutputExtractor`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `QwenEditOutputExtractor`
- `VAEDecode` ★核心
- `ImageScaleBy`
- `CropWithPadInfo`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `easy imageConcat`
- `easy imageConcat`
- `PreviewImage`
- `SaveImage`
- `ImageScaleBy`
- `PreviewImage`
- `LoadImage`
- `ConditioningZeroOut`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `VAELoader`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`

## 关键参数

- `seed` = `1091359629774735`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **80%**（35/44）

**有卡**：`QwenEditAdaptiveLongestEdge`、`QwenEditConfigPreparer`、`VAEDecode`、`CropWithPadInfo`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`SaveImage`、`LoraLoaderModelOnly`、`UNETLoader`、`LoadImage`、`QwenEditOutputExtractor`、`KSampler`、`ConditioningZeroOut`、`ImageScaleBy`、`easy imageConcat`、`VAELoader`、`CLIPLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、SaveImage、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
