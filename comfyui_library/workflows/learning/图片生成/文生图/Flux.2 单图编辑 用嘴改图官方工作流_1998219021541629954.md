---
key: 图片生成/文生图/Flux.2 单图编辑 用嘴改图官方工作流_1998219021541629954.json
name: Flux.2 单图编辑 用嘴改图官方工作流_1998219021541629954
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.2 单图编辑 用嘴改图官方工作流_1998219021541629954.json
hash: 934c8b604d2183a2
coverage: 0.84
learned_at: 2026-10-19 21:46:37
nodes: [Flux2Scheduler, BasicGuider, VAEEncode, LoadImage, VAEEncode, ReferenceLatent, FluxGuidance, KSamplerSelect, ReferenceLatent, EmptyFlux2LatentImage, SamplerCustomAdvanced, ImageScaleToTotalPixels, VAEDecode, ImageScaleToTotalPixels, Note, RandomNoise, SaveImage, MarkdownNote, CLIPTextEncode, LoadImage, CLIPLoader, VAELoader, UNETLoader, PrimitiveNode, PrimitiveNode]
patterns: []
missing: []
---

# 图片生成/文生图/Flux.2 单图编辑 用嘴改图官方工作流_1998219021541629954.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.2 单图编辑 用嘴改图官方工作流_1998219021541629954.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `Flux2Scheduler`
- `BasicGuider`
- `VAEEncode` ★核心
- `LoadImage`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `FluxGuidance`
- `KSamplerSelect` ★核心
- `ReferenceLatent`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `Note`
- `RandomNoise`
- `SaveImage`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `PrimitiveNode`
- `PrimitiveNode`

## 知识

覆盖率 **84%**（21/25）

**有卡**：`Flux2Scheduler`、`BasicGuider`、`VAEEncode`、`LoadImage`、`ReferenceLatent`、`FluxGuidance`、`KSamplerSelect`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`ImageScaleToTotalPixels`、`VAEDecode`、`RandomNoise`、`SaveImage`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
