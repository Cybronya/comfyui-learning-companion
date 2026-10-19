---
key: 图片生成/文生图/Flux.2-支持中文-文生图_1993529170808471553.json
name: Flux.2-支持中文-文生图_1993529170808471553
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.2-支持中文-文生图_1993529170808471553.json
hash: 86884161214e26f8
coverage: 0.685714
learned_at: 2026-10-19 21:32:32
nodes: [FluxGuidance, VAEEncode, VAEEncode, BasicGuider, UNETLoader, CLIPLoader, RandomNoise, SamplerCustomAdvanced, CLIPTextEncode, KSamplerSelect, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, ImageScaleToTotalPixels, GetNode, GetNode, GetNode, VAELoader, ImageScaleToTotalPixels, VAEDecode, AddLabel, SaveImage, LoadImage, EmptyFlux2LatentImage, Flux2Scheduler, ReferenceLatent, ReferenceLatent, LoadImage, Int, Int, JjkText]
patterns: []
missing: []
---

# 图片生成/文生图/Flux.2-支持中文-文生图_1993529170808471553.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.2-支持中文-文生图_1993529170808471553.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `FluxGuidance`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `BasicGuider`
- `UNETLoader` ★核心
- `CLIPLoader`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `ImageScaleToTotalPixels`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAELoader`
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `AddLabel`
- `SaveImage`
- `LoadImage`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `ReferenceLatent`
- `ReferenceLatent`
- `LoadImage`
- `Int`
- `Int`
- `JjkText`

## 知识

覆盖率 **69%**（24/35）

**有卡**：`FluxGuidance`、`VAEEncode`、`BasicGuider`、`UNETLoader`、`CLIPLoader`、`RandomNoise`、`SamplerCustomAdvanced`、`CLIPTextEncode`、`KSamplerSelect`、`ImageScaleToTotalPixels`、`VAELoader`、`VAEDecode`、`AddLabel`、`SaveImage`、`LoadImage`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`ReferenceLatent`、`Int`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
