---
key: 图片生成/图生图/Flux.2-支持中文-图片一致性-单图编辑_1993529953790738433.json
name: Flux.2-支持中文-图片一致性-单图编辑_1993529953790738433
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.2-支持中文-图片一致性-单图编辑_1993529953790738433.json
hash: 4f4ccae361b9660d
coverage: 0.8
learned_at: 2026-10-23 10:58:51
nodes: [Flux2Scheduler, BasicGuider, VAEEncode, FluxGuidance, KSamplerSelect, ReferenceLatent, VAELoader, EmptyFlux2LatentImage, VAEDecode, ImageScaleToTotalPixels, Note, UNETLoader, RandomNoise, CLIPLoader, MarkdownNote, SamplerCustomAdvanced, AddLabel, ImageScaleToTotalPixels, VAEEncode, LoadImage, GetNode, GetNode, SetNode, SetNode, SaveImage, Int, Int, LoadImage, ReferenceLatent, CLIPTextEncode]
patterns: []
missing: []
---

# 图片生成/图生图/Flux.2-支持中文-图片一致性-单图编辑_1993529953790738433.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.2-支持中文-图片一致性-单图编辑_1993529953790738433.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `Flux2Scheduler`
- `BasicGuider`
- `VAEEncode` ★核心
- `FluxGuidance`
- `KSamplerSelect` ★核心
- `ReferenceLatent`
- `VAELoader`
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
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `LoadImage`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SaveImage`
- `Int`
- `Int`
- `LoadImage`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **80%**（24/30）

**有卡**：`Flux2Scheduler`、`BasicGuider`、`VAEEncode`、`FluxGuidance`、`KSamplerSelect`、`ReferenceLatent`、`VAELoader`、`EmptyFlux2LatentImage`、`VAEDecode`、`ImageScaleToTotalPixels`、`UNETLoader`、`RandomNoise`、`CLIPLoader`、`SamplerCustomAdvanced`、`AddLabel`、`LoadImage`、`SaveImage`、`Int`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
