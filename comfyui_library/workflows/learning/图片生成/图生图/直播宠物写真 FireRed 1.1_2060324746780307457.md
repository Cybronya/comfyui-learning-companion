---
key: 图片生成/图生图/直播宠物写真 FireRed 1.1_2060324746780307457.json
name: 直播宠物写真 FireRed 1.1_2060324746780307457
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/直播宠物写真 FireRed 1.1_2060324746780307457.json
hash: 9bbb7b570dbae916
coverage: 0.666667
learned_at: 2026-10-23 13:18:27
nodes: [CLIPLoader, LoraLoaderModelOnly, ConditioningZeroOut, KSampler, VAELoader, VAEDecode, UNETLoader, TextEncodeQwenImageEditPlusAdvance_lrzjason, Reroute, Note, Image Comparer (rgthree), SaveImage, Note, LoadImage, JjkText]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 985255412883239, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/直播宠物写真 FireRed 1.1_2060324746780307457.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/直播宠物写真 FireRed 1.1_2060324746780307457.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（15 个）：
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `Reroute`
- `Note`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Note`
- `LoadImage`
- `JjkText`

## 关键参数

- `seed` = `985255412883239`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **67%**（10/15）

**有卡**：`CLIPLoader`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`KSampler`、`VAELoader`、`VAEDecode`、`UNETLoader`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
