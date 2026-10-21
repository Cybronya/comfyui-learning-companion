---
key: 图片生成/文生图/Flux.2+Klein+9B无限制文生图_2028848965118070785.json
name: Flux.2+Klein+9B无限制文生图_2028848965118070785
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.2+Klein+9B无限制文生图_2028848965118070785.json
hash: 557d656cb22dad9c
coverage: 1
learned_at: 2026-10-20 23:21:34
nodes: [Int Literal, FluxGuidance, KSamplerSelect, BasicGuider, RandomNoise, CLIPTextEncode, CLIPLoader, VAELoader, SamplerCustomAdvanced, UNETLoader, SaveImage, EmptyFlux2LatentImage, Flux2Scheduler, VAEDecode, CompressImages]
patterns: []
missing: []
---

# 图片生成/文生图/Flux.2+Klein+9B无限制文生图_2028848965118070785.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.2+Klein+9B无限制文生图_2028848965118070785.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `Int Literal`
- `FluxGuidance`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `VAEDecode` ★核心
- `CompressImages`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`Int Literal`、`FluxGuidance`、`KSamplerSelect`、`BasicGuider`、`RandomNoise`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`SamplerCustomAdvanced`、`UNETLoader`、`SaveImage`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`VAEDecode`、`CompressImages`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
