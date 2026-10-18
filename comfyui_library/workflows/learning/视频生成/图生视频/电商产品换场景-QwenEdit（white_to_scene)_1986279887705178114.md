---
key: 视频生成/图生视频/电商产品换场景-QwenEdit（white_to_scene)_1986279887705178114.json
name: 电商产品换场景-QwenEdit（white_to_scene)_1986279887705178114.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/电商产品换场景-QwenEdit（white_to_scene)_1986279887705178114.json
hash: a6512837615275a4
coverage: 0.714286
learned_at: 2026-10-15 22:32:54
nodes: [PrimitiveInt, PrimitiveInt, TextEncodeQwenImageEditPlusAdvance_lrzjason, PrimitiveStringMultiline, Text Concatenate, VAELoader, Reroute, LoraLoaderModelOnly, UNETLoader, SaveImage, VAEDecode, SaveImage, ConditioningZeroOut, CLIPLoader, LoraLoaderModelOnly, KSampler, easy imageRemBg, PreviewImage, easy seed, KSampler, Image Comparer (rgthree), VAEDecode, LayerUtility: ImageReelComposit, LayerUtility: ImageReel, PreviewImage, LoadImage, PrimitiveStringMultiline, ImageResizeKJv2]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 0, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/电商产品换场景-QwenEdit（white_to_scene)_1986279887705178114.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1986279887705178114.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `PrimitiveInt`
- `PrimitiveInt`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `PrimitiveStringMultiline`
- `Text Concatenate`
- `VAELoader`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `SaveImage`
- `ConditioningZeroOut`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `easy imageRemBg`
- `PreviewImage`
- `easy seed`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageReel`
- `PreviewImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `ImageResizeKJv2`

## 关键参数

- `seed` = `0`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **71%**（20/28）

**有卡**：`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`Text Concatenate`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`SaveImage`、`VAEDecode`、`ConditioningZeroOut`、`CLIPLoader`、`KSampler`、`easy imageRemBg`、`easy seed`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`LoadImage`、`ImageResizeKJv2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
