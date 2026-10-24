---
key: 图片生成/图生图/OneReward——Fill-flux-dev 局部重绘_1966159114428649474.json
name: OneReward——Fill-flux-dev 局部重绘_1966159114428649474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/OneReward——Fill-flux-dev 局部重绘_1966159114428649474.json
hash: 9f485da649994586
coverage: 1
learned_at: 2026-10-23 11:10:33
nodes: [DifferentialDiffusion, InpaintModelConditioning, DualCLIPLoader, FluxGuidance, VAELoader, VAEDecode, KSampler, UNETLoader, SaveImage, LoadImage, CLIPTextEncode, CLIPTextEncode, SaveImage, YC_SingleTextNode, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 219154996540634, "steps": 20}
---

# 图片生成/图生图/OneReward——Fill-flux-dev 局部重绘_1966159114428649474.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/OneReward——Fill-flux-dev 局部重绘_1966159114428649474.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（15 个）：
- `DifferentialDiffusion`
- `InpaintModelConditioning`
- `DualCLIPLoader`
- `FluxGuidance`
- `VAELoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `YC_SingleTextNode`
- `LoadImage`

## 关键参数

- `seed` = `219154996540634`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`DifferentialDiffusion`、`InpaintModelConditioning`、`DualCLIPLoader`、`FluxGuidance`、`VAELoader`、`VAEDecode`、`KSampler`、`UNETLoader`、`SaveImage`、`LoadImage`、`CLIPTextEncode`、`YC_SingleTextNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、DualCLIPLoader
