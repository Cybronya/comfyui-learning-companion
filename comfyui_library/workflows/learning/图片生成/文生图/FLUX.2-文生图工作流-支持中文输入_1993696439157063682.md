---
key: 图片生成/文生图/FLUX.2-文生图工作流-支持中文输入_1993696439157063682.json
name: FLUX.2-文生图工作流-支持中文输入_1993696439157063682
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX.2-文生图工作流-支持中文输入_1993696439157063682.json
hash: b12377ab54f952ec
coverage: 1
learned_at: 2026-10-19 21:32:28
nodes: [EmptyFlux2LatentImage, KSampler, VAEDecode, SaveImage, CLIPLoader, ConditioningZeroOut, FluxGuidance, CLIPTextEncode, VAELoader, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 671800648513923, "steps": 22}
---

# 图片生成/文生图/FLUX.2-文生图工作流-支持中文输入_1993696439157063682.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX.2-文生图工作流-支持中文输入_1993696439157063682.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（10 个）：
- `EmptyFlux2LatentImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPLoader`
- `ConditioningZeroOut`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `UNETLoader` ★核心

## 关键参数

- `seed` = `671800648513923`
- `steps` = `22`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`EmptyFlux2LatentImage`、`KSampler`、`VAEDecode`、`SaveImage`、`CLIPLoader`、`ConditioningZeroOut`、`FluxGuidance`、`CLIPTextEncode`、`VAELoader`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、FluxGuidance
