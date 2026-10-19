---
key: 图片生成/文生图/flux2.0_1995304483615858689.json
name: flux2.0_1995304483615858689
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/flux2.0_1995304483615858689.json
hash: 12506f00c1bc2106
coverage: 1
learned_at: 2026-10-19 21:33:12
nodes: [VAELoader, CLIPLoader, VAEDecode, KSampler, ConditioningZeroOut, FluxGuidance, EmptyFlux2LatentImage, UNETLoader, SaveImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 807171426215387, "steps": 22}
---

# 图片生成/文生图/flux2.0_1995304483615858689.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/flux2.0_1995304483615858689.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（10 个）：
- `VAELoader`
- `CLIPLoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ConditioningZeroOut`
- `FluxGuidance`
- `EmptyFlux2LatentImage`
- `UNETLoader` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `807171426215387`
- `steps` = `22`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`VAELoader`、`CLIPLoader`、`VAEDecode`、`KSampler`、`ConditioningZeroOut`、`FluxGuidance`、`EmptyFlux2LatentImage`、`UNETLoader`、`SaveImage`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、FluxGuidance
