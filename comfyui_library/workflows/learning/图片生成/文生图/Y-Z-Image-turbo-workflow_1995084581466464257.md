---
key: 图片生成/文生图/Y-Z-Image-turbo-workflow_1995084581466464257.json
name: Y-Z-Image-turbo-workflow_1995084581466464257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Y-Z-Image-turbo-workflow_1995084581466464257.json
hash: 6bbcc5f073e80128
coverage: 1
learned_at: 2026-10-19 21:32:45
nodes: [ModelSamplingAuraFlow, UNETLoader, CLIPTextEncode, ConditioningZeroOut, VAEDecode, SaveImage, CLIPLoader, EmptySD3LatentImage, KSampler, VAELoader]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 276560349160418, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Y-Z-Image-turbo-workflow_1995084581466464257.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Y-Z-Image-turbo-workflow_1995084581466464257.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（10 个）：
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPLoader`
- `EmptySD3LatentImage`
- `KSampler` ★核心
- `VAELoader`

## 关键参数

- `seed` = `276560349160418`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`ModelSamplingAuraFlow`、`UNETLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`VAEDecode`、`SaveImage`、`CLIPLoader`、`EmptySD3LatentImage`、`KSampler`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、UNETLoader、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
