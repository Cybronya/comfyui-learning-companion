---
key: 视频生成/文生视频/Flux.2 Klein 9B文生图_2066059765985406977.json
name: Flux.2 Klein 9B文生图_2066059765985406977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Flux.2 Klein 9B文生图_2066059765985406977.json
hash: 0798d138b7e8c4aa
coverage: 0.933333
learned_at: 2026-10-11 20:21:24
nodes: [BasicGuider, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, FluxGuidance, CLIPLoader, VAELoader, Int Literal, Flux2Scheduler, VAEDecode, UNETLoader, EmptyFlux2LatentImage, SaveImage, CompressImages, CLIPTextEncode]
patterns: []
missing: [Int Literal]
discoveries: [次要节点 `Int Literal` 知识库中没有该节点类型的任何知识]
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

覆盖率 **93%**（14/15）

**有卡**：`BasicGuider`、`KSamplerSelect`、`RandomNoise`、`SamplerCustomAdvanced`、`FluxGuidance`、`CLIPLoader`、`VAELoader`、`Flux2Scheduler`、`VAEDecode`、`UNETLoader`、`EmptyFlux2LatentImage`、`SaveImage`、`CompressImages`、`CLIPTextEncode`

**缺卡**（1）：`Int Literal`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced

## 学习发现

- 次要节点 `Int Literal` 知识库中没有该节点类型的任何知识
