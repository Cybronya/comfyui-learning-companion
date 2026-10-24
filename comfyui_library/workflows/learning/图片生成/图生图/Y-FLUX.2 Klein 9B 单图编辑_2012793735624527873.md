---
key: 图片生成/图生图/Y-FLUX.2 Klein 9B 单图编辑_2012793735624527873.json
name: Y-FLUX.2 Klein 9B 单图编辑_2012793735624527873
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Y-FLUX.2 Klein 9B 单图编辑_2012793735624527873.json
hash: 79cefb18bdf62fd0
coverage: 1
learned_at: 2026-10-23 11:28:39
nodes: [SamplerCustomAdvanced, BasicGuider, KSamplerSelect, VAEDecode, Flux2Scheduler, EmptyFlux2LatentImage, RandomNoise, FluxGuidance, ReferenceLatent, VAELoader, CLIPLoader, SaveImage, Int Literal, GetImageSize+, LoadImage, VAEEncode, CLIPTextEncode, UNETLoader]
patterns: []
missing: []
---

# 图片生成/图生图/Y-FLUX.2 Klein 9B 单图编辑_2012793735624527873.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Y-FLUX.2 Klein 9B 单图编辑_2012793735624527873.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `RandomNoise`
- `FluxGuidance`
- `ReferenceLatent`
- `VAELoader`
- `CLIPLoader`
- `SaveImage`
- `Int Literal`
- `GetImageSize+`
- `LoadImage`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心

## 知识

覆盖率 **100%**（18/18）

**有卡**：`SamplerCustomAdvanced`、`BasicGuider`、`KSamplerSelect`、`VAEDecode`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`RandomNoise`、`FluxGuidance`、`ReferenceLatent`、`VAELoader`、`CLIPLoader`、`SaveImage`、`Int Literal`、`GetImageSize+`、`LoadImage`、`VAEEncode`、`CLIPTextEncode`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
