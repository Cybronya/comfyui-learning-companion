---
key: 图片生成/图生图/电商产品贴图 FireRed 1.1_2039972727704002561.json
name: 电商产品贴图 FireRed 1.1_2039972727704002561
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/电商产品贴图 FireRed 1.1_2039972727704002561.json
hash: 6bd983db93d99fc5
coverage: 0.647059
learned_at: 2026-10-23 13:16:33
nodes: [CLIPLoader, LoraLoaderModelOnly, ConditioningZeroOut, KSampler, VAELoader, VAEDecode, TextEncodeQwenImageEditPlusAdvance_lrzjason, Image Comparer (rgthree), Note, SaveImage, Reroute, Note, UNETLoader, LoadImage, LoadImage, JjkText, Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 713325225915812, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/电商产品贴图 FireRed 1.1_2039972727704002561.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/电商产品贴图 FireRed 1.1_2039972727704002561.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（17 个）：
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `Image Comparer (rgthree)`
- `Note`
- `SaveImage`
- `Reroute`
- `Note`
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `JjkText`
- `Note`

## 关键参数

- `seed` = `713325225915812`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **65%**（11/17）

**有卡**：`CLIPLoader`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`KSampler`、`VAELoader`、`VAEDecode`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`SaveImage`、`UNETLoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
