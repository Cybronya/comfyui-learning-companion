---
key: 图片生成/图生图/Flux.2 Klein 9B单图编辑_2022512699938181122.json
name: Flux.2 Klein 9B单图编辑_2022512699938181122
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.2 Klein 9B单图编辑_2022512699938181122.json
hash: b9aa3612cfb71d27
coverage: 1
learned_at: 2026-10-23 10:58:45
nodes: [BasicGuider, KSamplerSelect, SamplerCustomAdvanced, VAEEncode, ReferenceLatent, RandomNoise, Flux2Scheduler, UNETLoader, VAEDecode, SaveImage, FluxGuidance, VAELoader, CLIPLoader, Int Literal, LoadImage, Int Literal, Int Literal, CLIPTextEncode, EmptyFlux2LatentImage]
patterns: []
missing: []
---

# 图片生成/图生图/Flux.2 Klein 9B单图编辑_2022512699938181122.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.2 Klein 9B单图编辑_2022512699938181122.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `BasicGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `RandomNoise`
- `Flux2Scheduler`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `FluxGuidance`
- `VAELoader`
- `CLIPLoader`
- `Int Literal`
- `LoadImage`
- `Int Literal`
- `Int Literal`
- `CLIPTextEncode` ★核心
- `EmptyFlux2LatentImage`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`BasicGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`VAEEncode`、`ReferenceLatent`、`RandomNoise`、`Flux2Scheduler`、`UNETLoader`、`VAEDecode`、`SaveImage`、`FluxGuidance`、`VAELoader`、`CLIPLoader`、`Int Literal`、`LoadImage`、`CLIPTextEncode`、`EmptyFlux2LatentImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
