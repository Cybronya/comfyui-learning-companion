---
key: Flux.1文生图工作流_2100500167958024193.json
name: Flux.1文生图工作流_2100500167958024193
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1文生图工作流_2100500167958024193.json
hash: 1b70424bf261db77
coverage: 1
learned_at: 2026-10-10 20:58:36
nodes: [DualCLIPLoader, VAELoader, VAEDecode, CLIPTextEncode, UNETLoader, FluxGuidance, SaveImage, CLIPTextEncode, EmptySD3LatentImage, KSampler]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 244297134688005, "steps": 30}
---

# Flux.1文生图工作流_2100500167958024193.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.1文生图工作流_2100500167958024193.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（10 个）：
- `DualCLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `FluxGuidance`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `KSampler` ★核心

## 关键参数

- `seed` = `244297134688005`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`DualCLIPLoader`、`VAELoader`、`VAEDecode`、`CLIPTextEncode`、`UNETLoader`、`FluxGuidance`、`SaveImage`、`EmptySD3LatentImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、FluxGuidance、DualCLIPLoader、SaveImage
