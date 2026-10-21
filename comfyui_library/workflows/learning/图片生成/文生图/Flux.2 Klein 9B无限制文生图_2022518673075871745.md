---
key: 图片生成/文生图/Flux.2 Klein 9B无限制文生图_2022518673075871745.json
name: Flux.2 Klein 9B无限制文生图_2022518673075871745
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.2 Klein 9B无限制文生图_2022518673075871745.json
hash: dccf25e68f9ae08a
coverage: 1
learned_at: 2026-10-19 22:29:40
nodes: [Int Literal, FluxGuidance, Flux2Scheduler, KSamplerSelect, BasicGuider, RandomNoise, CLIPTextEncode, CLIPLoader, VAELoader, EmptyFlux2LatentImage, SamplerCustomAdvanced, UNETLoader, CompressImages, VAEDecode, SaveImage]
patterns: []
missing: []
---

# 图片生成/文生图/Flux.2 Klein 9B无限制文生图_2022518673075871745.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.2 Klein 9B无限制文生图_2022518673075871745.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `Int Literal`
- `FluxGuidance`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `CompressImages`
- `VAEDecode` ★核心
- `SaveImage`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`Int Literal`、`FluxGuidance`、`Flux2Scheduler`、`KSamplerSelect`、`BasicGuider`、`RandomNoise`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`UNETLoader`、`CompressImages`、`VAEDecode`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
