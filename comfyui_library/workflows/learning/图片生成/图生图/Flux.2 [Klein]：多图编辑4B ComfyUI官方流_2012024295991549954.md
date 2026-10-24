---
key: 图片生成/图生图/Flux.2 [Klein]：多图编辑4B ComfyUI官方流_2012024295991549954.json
name: Flux.2 [Klein]：多图编辑4B ComfyUI官方流_2012024295991549954
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.2 [Klein]：多图编辑4B ComfyUI官方流_2012024295991549954.json
hash: 616c1213626578b3
coverage: 0.884615
learned_at: 2026-10-23 10:58:48
nodes: [MarkdownNote, KSamplerSelect, CFGGuider, SamplerCustomAdvanced, VAEDecode, RandomNoise, UNETLoader, CLIPLoader, VAELoader, ImageScaleToTotalPixels, ConditioningZeroOut, SaveImage, ReferenceLatent, ReferenceLatent, VAEEncode, ImageScaleToTotalPixels, VAEEncode, ReferenceLatent, ReferenceLatent, LoadImage, EmptyFlux2LatentImage, Flux2Scheduler, LoadImage, PrimitiveInt, PrimitiveInt, CLIPTextEncode]
patterns: []
missing: []
---

# 图片生成/图生图/Flux.2 [Klein]：多图编辑4B ComfyUI官方流_2012024295991549954.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.2 [Klein]：多图编辑4B ComfyUI官方流_2012024295991549954.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `RandomNoise`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ImageScaleToTotalPixels`
- `ConditioningZeroOut`
- `SaveImage`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `LoadImage`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **88%**（23/26）

**有卡**：`KSamplerSelect`、`CFGGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`RandomNoise`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ImageScaleToTotalPixels`、`ConditioningZeroOut`、`SaveImage`、`ReferenceLatent`、`VAEEncode`、`LoadImage`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
