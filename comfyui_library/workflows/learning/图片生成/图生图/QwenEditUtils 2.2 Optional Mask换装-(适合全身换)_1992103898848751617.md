---
key: 图片生成/图生图/QwenEditUtils 2.2 Optional Mask换装-(适合全身换)_1992103898848751617.json
name: QwenEditUtils 2.2 Optional Mask换装-(适合全身换)_1992103898848751617
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QwenEditUtils 2.2 Optional Mask换装-(适合全身换)_1992103898848751617.json
hash: 444e87ef3ade6566
coverage: 0.857143
learned_at: 2026-10-23 11:20:33
nodes: [VAELoader, ConditioningZeroOut, QwenEditAdaptiveLongestEdge, UNETLoader, QwenEditAdaptiveLongestEdge, TextEncodeQwenImageEditPlusCustom_lrzjason, CLIPLoader, SaveImage, PrimitiveStringMultiline, QwenEditConfigPreparer, QwenEditOutputExtractor, CropWithPadInfo, VAEDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, Image Comparer (rgthree), KSampler, Note, LoadImage, LoadImage, QwenEditConfigPreparer]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 682, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/QwenEditUtils 2.2 Optional Mask换装-(适合全身换)_1992103898848751617.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/QwenEditUtils 2.2 Optional Mask换装-(适合全身换)_1992103898848751617.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（21 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `QwenEditAdaptiveLongestEdge`
- `UNETLoader` ★核心
- `QwenEditAdaptiveLongestEdge`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `CLIPLoader`
- `SaveImage`
- `PrimitiveStringMultiline`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor`
- `CropWithPadInfo`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `Note`
- `LoadImage`
- `LoadImage`
- `QwenEditConfigPreparer`

## 关键参数

- `seed` = `682`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`QwenEditAdaptiveLongestEdge`、`UNETLoader`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`CLIPLoader`、`SaveImage`、`QwenEditConfigPreparer`、`QwenEditOutputExtractor`、`CropWithPadInfo`、`VAEDecode`、`LoraLoaderModelOnly`、`KSampler`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、SaveImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
