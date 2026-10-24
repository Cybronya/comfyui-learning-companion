---
key: 图片生成/图生图/Flux.2-支持中文-图片一致性-单图编辑_1993681359214493697.json
name: Flux.2-支持中文-图片一致性-单图编辑_1993681359214493697
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.2-支持中文-图片一致性-单图编辑_1993681359214493697.json
hash: 926acb7dd108db05
coverage: 0.823529
learned_at: 2026-10-23 10:58:52
nodes: [Flux2Scheduler, BasicGuider, VAEEncode, FluxGuidance, KSamplerSelect, ReferenceLatent, EmptyFlux2LatentImage, VAEDecode, ImageScaleToTotalPixels, Note, UNETLoader, RandomNoise, CLIPLoader, MarkdownNote, SamplerCustomAdvanced, AddLabel, GetNode, GetNode, SetNode, SaveImage, LoadImage, SetNode, VAELoader, VAEEncode, ImageScaleToTotalPixels, ImageScaleToTotalPixels, VAEEncode, ReferenceLatent, ReferenceLatent, LoadImage, Int, Int, LoadImage, CLIPTextEncode]
patterns: []
missing: []
---

# 图片生成/图生图/Flux.2-支持中文-图片一致性-单图编辑_1993681359214493697.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.2-支持中文-图片一致性-单图编辑_1993681359214493697.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `Flux2Scheduler`
- `BasicGuider`
- `VAEEncode` ★核心
- `FluxGuidance`
- `KSamplerSelect` ★核心
- `ReferenceLatent`
- `EmptyFlux2LatentImage`
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `Note`
- `UNETLoader` ★核心
- `RandomNoise`
- `CLIPLoader`
- `MarkdownNote`
- `SamplerCustomAdvanced` ★核心
- `AddLabel`
- `GetNode`
- `GetNode`
- `SetNode`
- `SaveImage`
- `LoadImage`
- `SetNode`
- `VAELoader`
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `LoadImage`
- `Int`
- `Int`
- `LoadImage`
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **82%**（28/34）

**有卡**：`Flux2Scheduler`、`BasicGuider`、`VAEEncode`、`FluxGuidance`、`KSamplerSelect`、`ReferenceLatent`、`EmptyFlux2LatentImage`、`VAEDecode`、`ImageScaleToTotalPixels`、`UNETLoader`、`RandomNoise`、`CLIPLoader`、`SamplerCustomAdvanced`、`AddLabel`、`SaveImage`、`LoadImage`、`VAELoader`、`Int`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
