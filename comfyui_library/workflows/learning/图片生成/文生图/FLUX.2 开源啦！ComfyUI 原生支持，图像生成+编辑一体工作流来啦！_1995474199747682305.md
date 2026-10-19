---
key: 图片生成/文生图/FLUX.2 开源啦！ComfyUI 原生支持，图像生成+编辑一体工作流来啦！_1995474199747682305.json
name: FLUX.2 开源啦！ComfyUI 原生支持，图像生成+编辑一体工作流来啦！_1995474199747682305
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX.2 开源啦！ComfyUI 原生支持，图像生成+编辑一体工作流来啦！_1995474199747682305.json
hash: 26001792d2b5aae7
coverage: 0.882353
learned_at: 2026-10-19 21:32:28
nodes: [Flux2Scheduler, BasicGuider, VAEEncode, KSamplerSelect, ReferenceLatent, EmptyFlux2LatentImage, SamplerCustomAdvanced, ImageScaleToTotalPixels, VAEDecode, ImageScaleToTotalPixels, UNETLoader, SaveImage, CLIPLoader, Note, ImageScaleToTotalPixels, ImageScaleToTotalPixels, VAEEncode, FluxGuidance, VAEEncode, VAELoader, VAEEncode, ReferenceLatent, ReferenceLatent, ReferenceLatent, LoadImage, LoadImage, PrimitiveNode, PrimitiveNode, LoadImage, LoadImage, MarkdownNote, CLIPTextEncode, RandomNoise, Label (rgthree)]
patterns: []
missing: []
---

# 图片生成/文生图/FLUX.2 开源啦！ComfyUI 原生支持，图像生成+编辑一体工作流来啦！_1995474199747682305.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX.2 开源啦！ComfyUI 原生支持，图像生成+编辑一体工作流来啦！_1995474199747682305.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `Flux2Scheduler`
- `BasicGuider`
- `VAEEncode` ★核心
- `KSamplerSelect` ★核心
- `ReferenceLatent`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `UNETLoader` ★核心
- `SaveImage`
- `CLIPLoader`
- `Note`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `FluxGuidance`
- `VAEEncode` ★核心
- `VAELoader`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `LoadImage`
- `LoadImage`
- `PrimitiveNode`
- `PrimitiveNode`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `Label (rgthree)`

## 知识

覆盖率 **88%**（30/34）

**有卡**：`Flux2Scheduler`、`BasicGuider`、`VAEEncode`、`KSamplerSelect`、`ReferenceLatent`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`ImageScaleToTotalPixels`、`VAEDecode`、`UNETLoader`、`SaveImage`、`CLIPLoader`、`FluxGuidance`、`VAELoader`、`LoadImage`、`CLIPTextEncode`、`RandomNoise`、`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
