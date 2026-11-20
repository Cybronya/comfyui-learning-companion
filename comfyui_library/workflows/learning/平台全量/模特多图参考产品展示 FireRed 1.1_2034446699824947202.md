---
key: 平台全量/模特多图参考产品展示 FireRed 1.1_2034446699824947202.json
name: 模特多图参考产品展示 FireRed 1.1_2034446699824947202
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/模特多图参考产品展示 FireRed 1.1_2034446699824947202.json
hash: 865f28c808252284
coverage: 0.6875
learned_at: 2026-11-14 02:18:12
nodes: [CLIPLoader, LoraLoaderModelOnly, ConditioningZeroOut, KSampler, VAELoader, VAEDecode, Note, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, Image Comparer (rgthree), LoadImage, LoadImage, Note, JjkText, Note, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 254705791219393, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/模特多图参考产品展示 FireRed 1.1_2034446699824947202.json

> 来源文件 `comfyui_library/workflows/平台全量/模特多图参考产品展示 FireRed 1.1_2034446699824947202.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（16 个）：
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `Note`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoadImage`
- `Note`
- `JjkText`
- `Note`
- `SaveImage`

## 关键参数

- `seed` = `254705791219393`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **69%**（11/16）

**有卡**：`CLIPLoader`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`KSampler`、`VAELoader`、`VAEDecode`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`UNETLoader`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
