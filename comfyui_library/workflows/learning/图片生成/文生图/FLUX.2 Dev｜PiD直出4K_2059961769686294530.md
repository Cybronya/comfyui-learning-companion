---
key: 图片生成/文生图/FLUX.2 Dev｜PiD直出4K_2059961769686294530.json
name: FLUX.2 Dev｜PiD直出4K_2059961769686294530
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX.2 Dev｜PiD直出4K_2059961769686294530.json
hash: 77fdbb66d5e98425
coverage: 0.789474
learned_at: 2026-10-19 23:02:20
nodes: [PrimitiveNode, PrimitiveNode, CLIPLoader, UNETLoader, VAELoader, PiDPrepare, PiDSample, PiDFinalize, SaveImage, SaveImage, PiDTextPrompt, EmptyFlux2LatentImage, Note, Note, CLIPTextEncode, CLIPTextEncode, FluxGuidance, VAEDecode, PiDKSamplerCapture]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 191166039668422, "steps": 50}
---

# 图片生成/文生图/FLUX.2 Dev｜PiD直出4K_2059961769686294530.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX.2 Dev｜PiD直出4K_2059961769686294530.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `PrimitiveNode`
- `PrimitiveNode`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `PiDPrepare`
- `PiDSample`
- `PiDFinalize`
- `SaveImage`
- `SaveImage`
- `PiDTextPrompt`
- `EmptyFlux2LatentImage`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `VAEDecode` ★核心
- `PiDKSamplerCapture` ★核心

## 关键参数

- `seed` = `191166039668422`
- `steps` = `50`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **79%**（15/19）

**有卡**：`CLIPLoader`、`UNETLoader`、`VAELoader`、`PiDPrepare`、`PiDSample`、`PiDFinalize`、`SaveImage`、`PiDTextPrompt`、`EmptyFlux2LatentImage`、`CLIPTextEncode`、`FluxGuidance`、`VAEDecode`、`PiDKSamplerCapture`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、FluxGuidance、PiDKSamplerCapture、EmptyFlux2LatentImage
