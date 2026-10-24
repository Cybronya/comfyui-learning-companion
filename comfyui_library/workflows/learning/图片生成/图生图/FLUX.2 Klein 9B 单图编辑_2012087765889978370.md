---
key: 图片生成/图生图/FLUX.2 Klein 9B 单图编辑_2012087765889978370.json
name: FLUX.2 Klein 9B 单图编辑_2012087765889978370
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2 Klein 9B 单图编辑_2012087765889978370.json
hash: 83e8678084fd7aff
coverage: 1
learned_at: 2026-10-23 10:54:05
nodes: [BasicGuider, KSamplerSelect, SamplerCustomAdvanced, VAEEncode, ReferenceLatent, RandomNoise, Flux2Scheduler, UNETLoader, VAEDecode, EmptyFlux2LatentImage, SaveImage, FluxGuidance, VAELoader, LoadImage, CLIPLoader, CLIPTextEncode, Int Literal, Int Literal, Int Literal]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.2 Klein 9B 单图编辑_2012087765889978370.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2 Klein 9B 单图编辑_2012087765889978370.json`

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
- `EmptyFlux2LatentImage`
- `SaveImage`
- `FluxGuidance`
- `VAELoader`
- `LoadImage`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `Int Literal`
- `Int Literal`
- `Int Literal`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`BasicGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`VAEEncode`、`ReferenceLatent`、`RandomNoise`、`Flux2Scheduler`、`UNETLoader`、`VAEDecode`、`EmptyFlux2LatentImage`、`SaveImage`、`FluxGuidance`、`VAELoader`、`LoadImage`、`CLIPLoader`、`CLIPTextEncode`、`Int Literal`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
