---
key: 图片生成/图生图/电商假人模特转真人+FireRed+1.1_2045761264483307521.json
name: 电商假人模特转真人+FireRed+1.1_2045761264483307521
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/电商假人模特转真人+FireRed+1.1_2045761264483307521.json
hash: 37c8c7bd861d9ee6
coverage: 0.6875
learned_at: 2026-10-23 13:16:38
nodes: [CLIPLoader, LoraLoaderModelOnly, ConditioningZeroOut, KSampler, VAELoader, VAEDecode, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, Image Comparer (rgthree), Note, SaveImage, LoadImage, Reroute, LoadImage, JjkText, Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 726862773602609, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/电商假人模特转真人+FireRed+1.1_2045761264483307521.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/电商假人模特转真人+FireRed+1.1_2045761264483307521.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（16 个）：
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader` ★核心
- `Image Comparer (rgthree)`
- `Note`
- `SaveImage`
- `LoadImage`
- `Reroute`
- `LoadImage`
- `JjkText`
- `Note`

## 关键参数

- `seed` = `726862773602609`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **69%**（11/16）

**有卡**：`CLIPLoader`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`KSampler`、`VAELoader`、`VAEDecode`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`UNETLoader`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
