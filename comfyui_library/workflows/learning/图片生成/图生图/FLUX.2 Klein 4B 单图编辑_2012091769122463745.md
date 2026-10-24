---
key: 图片生成/图生图/FLUX.2 Klein 4B 单图编辑_2012091769122463745.json
name: FLUX.2 Klein 4B 单图编辑_2012091769122463745
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2 Klein 4B 单图编辑_2012091769122463745.json
hash: 9d2534d2f4579fb0
coverage: 1
learned_at: 2026-10-23 10:54:03
nodes: [BasicGuider, KSamplerSelect, SamplerCustomAdvanced, VAEEncode, ReferenceLatent, RandomNoise, VAEDecode, FluxGuidance, VAELoader, UNETLoader, CLIPLoader, LoadImage, CLIPTextEncode, SaveImage, EmptyFlux2LatentImage, Int Literal, Flux2Scheduler, Int Literal, Int Literal]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.2 Klein 4B 单图编辑_2012091769122463745.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2 Klein 4B 单图编辑_2012091769122463745.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `BasicGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `RandomNoise`
- `VAEDecode` ★核心
- `FluxGuidance`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `EmptyFlux2LatentImage`
- `Int Literal`
- `Flux2Scheduler`
- `Int Literal`
- `Int Literal`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`BasicGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`VAEEncode`、`ReferenceLatent`、`RandomNoise`、`VAEDecode`、`FluxGuidance`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`LoadImage`、`CLIPTextEncode`、`SaveImage`、`EmptyFlux2LatentImage`、`Int Literal`、`Flux2Scheduler`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
