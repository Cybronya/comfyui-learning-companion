---
key: 图片生成/文生图/Flux.2_Klein_9B文生图_2069068665672265729.json
name: Flux.2_Klein_9B文生图_2069068665672265729
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.2_Klein_9B文生图_2069068665672265729.json
hash: 3795550da8fe8a5a
coverage: 1
learned_at: 2026-10-19 23:21:22
nodes: [BasicGuider, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, FluxGuidance, CLIPLoader, VAELoader, Int Literal, Flux2Scheduler, VAEDecode, UNETLoader, EmptyFlux2LatentImage, SaveImage, CompressImages, CLIPTextEncode]
patterns: []
missing: []
---

# 图片生成/文生图/Flux.2_Klein_9B文生图_2069068665672265729.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.2_Klein_9B文生图_2069068665672265729.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `BasicGuider`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `FluxGuidance`
- `CLIPLoader`
- `VAELoader`
- `Int Literal`
- `Flux2Scheduler`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `EmptyFlux2LatentImage`
- `SaveImage`
- `CompressImages`
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **100%**（15/15）

**有卡**：`BasicGuider`、`KSamplerSelect`、`RandomNoise`、`SamplerCustomAdvanced`、`FluxGuidance`、`CLIPLoader`、`VAELoader`、`Int Literal`、`Flux2Scheduler`、`VAEDecode`、`UNETLoader`、`EmptyFlux2LatentImage`、`SaveImage`、`CompressImages`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
