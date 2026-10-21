---
key: 图片生成/文生图/组件系列10-FLUX.2-Klein文生图_2058761708835008514.json
name: 组件系列10-FLUX.2-Klein文生图_2058761708835008514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/组件系列10-FLUX.2-Klein文生图_2058761708835008514.json
hash: 424cda732a7033c4
coverage: 0.8
learned_at: 2026-10-19 23:04:17
nodes: [UNETLoader, CLIPLoader, VAELoader, ConditioningZeroOut, LoraLoaderModelOnly, CLIPTextEncode, Text, Seed (rgthree), VAEDecode, SetNode, GetNode, EmptyFlux2LatentImage, PreviewImage, SaveImage, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 5}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/组件系列10-FLUX.2-Klein文生图_2058761708835008514.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/组件系列10-FLUX.2-Klein文生图_2058761708835008514.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Text`
- `Seed (rgthree)`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `EmptyFlux2LatentImage`
- `PreviewImage`
- `SaveImage`
- `KSampler` ★核心

## 关键参数

- `seed` = `0`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（12/15）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`Text`、`Seed (rgthree)`、`VAEDecode`、`EmptyFlux2LatentImage`、`SaveImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
