---
key: 图片生成/文生图/FLUX.1 Dev｜PiD直出4K_2059961777689030657.json
name: FLUX.1 Dev｜PiD直出4K_2059961777689030657
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX.1 Dev｜PiD直出4K_2059961777689030657.json
hash: bd743ac8da5c6dd1
coverage: 0.866667
learned_at: 2026-10-19 23:02:20
nodes: [CLIPTextEncode, EmptySD3LatentImage, FluxGuidance, Note, CheckpointLoaderSimple, CLIPTextEncode, PiDPrepare, PiDSample, PiDFinalize, Note, SaveImage, PiDTextPrompt, SaveImage, VAEDecode, PiDKSamplerCapture]
patterns: []
missing: []
parameters: {"cfg": 1, "checkpoint": "flux1-dev-fp8.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 191166039668422, "steps": 28}
---

# 图片生成/文生图/FLUX.1 Dev｜PiD直出4K_2059961777689030657.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX.1 Dev｜PiD直出4K_2059961777689030657.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `FluxGuidance`
- `Note`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `PiDPrepare`
- `PiDSample`
- `PiDFinalize`
- `Note`
- `SaveImage`
- `PiDTextPrompt`
- `SaveImage`
- `VAEDecode` ★核心
- `PiDKSamplerCapture` ★核心

## 关键参数

- `checkpoint` = `flux1-dev-fp8.safetensors`
- `seed` = `191166039668422`
- `steps` = `28`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`CLIPTextEncode`、`EmptySD3LatentImage`、`FluxGuidance`、`CheckpointLoaderSimple`、`PiDPrepare`、`PiDSample`、`PiDFinalize`、`SaveImage`、`PiDTextPrompt`、`VAEDecode`、`PiDKSamplerCapture`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、FluxGuidance、PiDKSamplerCapture、PiDTextPrompt、SaveImage、EmptySD3LatentImage
