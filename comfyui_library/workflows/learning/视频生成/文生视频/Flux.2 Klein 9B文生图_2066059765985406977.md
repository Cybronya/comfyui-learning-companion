---
key: 视频生成/文生视频/Flux.2 Klein 9B文生图_2066059765985406977.json
name: Flux.2 Klein 9B文生图_2066059765985406977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Flux.2 Klein 9B文生图_2066059765985406977.json
hash: 0798d138b7e8c4aa
coverage: 1
learned_at: 2026-10-15 22:44:11
nodes: [BasicGuider, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, FluxGuidance, CLIPLoader, VAELoader, Int Literal, Flux2Scheduler, VAEDecode, UNETLoader, EmptyFlux2LatentImage, SaveImage, CompressImages, CLIPTextEncode]
patterns: []
missing: []
---

# 视频生成/文生视频/Flux.2 Klein 9B文生图_2066059765985406977.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Flux.2 Klein 9B文生图_2066059765985406977.json`

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
