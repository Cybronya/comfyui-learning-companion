---
key: 图片生成/文生图/【文生图】Flux.2.0_Klein9B_2030309405933182978.json
name: 【文生图】Flux.2.0_Klein9B_2030309405933182978
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【文生图】Flux.2.0_Klein9B_2030309405933182978.json
hash: 84f1a1ef479d1bf9
coverage: 0.9
learned_at: 2026-10-19 22:46:19
nodes: [UNETLoader, CLIPLoader, VAELoader, Anything Everywhere3, KSampler, VAEDecode, ConditioningZeroOut, SaveImage, EmptyFlux2LatentImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 671981362521023, "steps": 20}
---

# 图片生成/文生图/【文生图】Flux.2.0_Klein9B_2030309405933182978.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【文生图】Flux.2.0_Klein9B_2030309405933182978.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（10 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Anything Everywhere3`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `SaveImage`
- `EmptyFlux2LatentImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `671981362521023`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`VAEDecode`、`ConditioningZeroOut`、`SaveImage`、`EmptyFlux2LatentImage`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyFlux2LatentImage
