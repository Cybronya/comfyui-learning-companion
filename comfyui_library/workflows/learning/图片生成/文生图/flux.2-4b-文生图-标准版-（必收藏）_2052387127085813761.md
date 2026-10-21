---
key: 图片生成/文生图/flux.2-4b-文生图-标准版-（必收藏）_2052387127085813761.json
name: flux.2-4b-文生图-标准版-（必收藏）_2052387127085813761
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/flux.2-4b-文生图-标准版-（必收藏）_2052387127085813761.json
hash: cd5d71cf0109331a
coverage: 1
learned_at: 2026-10-21 02:56:48
nodes: [UNETLoader, CLIPLoader, ConditioningZeroOut, VAELoader, EmptyFlux2LatentImage, KSampler, VAEDecode, CLIPTextEncode, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1101836720805806, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/flux.2-4b-文生图-标准版-（必收藏）_2052387127085813761.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/flux.2-4b-文生图-标准版-（必收藏）_2052387127085813761.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output

**节点**（9 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `ConditioningZeroOut`
- `VAELoader`
- `EmptyFlux2LatentImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `1101836720805806`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`UNETLoader`、`CLIPLoader`、`ConditioningZeroOut`、`VAELoader`、`EmptyFlux2LatentImage`、`KSampler`、`VAEDecode`、`CLIPTextEncode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyFlux2LatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
