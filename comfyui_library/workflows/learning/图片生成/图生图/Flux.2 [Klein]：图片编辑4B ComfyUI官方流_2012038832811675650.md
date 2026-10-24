---
key: 图片生成/图生图/Flux.2 [Klein]：图片编辑4B ComfyUI官方流_2012038832811675650.json
name: Flux.2 [Klein]：图片编辑4B ComfyUI官方流_2012038832811675650
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.2 [Klein]：图片编辑4B ComfyUI官方流_2012038832811675650.json
hash: 7271ca0e5fea3f6f
coverage: 0.95
learned_at: 2026-10-23 10:58:47
nodes: [MarkdownNote, KSamplerSelect, SamplerCustomAdvanced, VAEDecode, RandomNoise, CLIPLoader, CLIPTextEncode, VAELoader, ImageScaleToTotalPixels, SaveImage, VAEEncode, ReferenceLatent, EmptyFlux2LatentImage, GetImageSize, ReferenceLatent, UNETLoader, LoadImage, CLIPTextEncode, CFGGuider, Flux2Scheduler]
patterns: []
missing: []
---

# 图片生成/图生图/Flux.2 [Klein]：图片编辑4B ComfyUI官方流_2012038832811675650.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.2 [Klein]：图片编辑4B ComfyUI官方流_2012038832811675650.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `RandomNoise`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ImageScaleToTotalPixels`
- `SaveImage`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `ReferenceLatent`
- `UNETLoader` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `Flux2Scheduler`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`KSamplerSelect`、`SamplerCustomAdvanced`、`VAEDecode`、`RandomNoise`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`ImageScaleToTotalPixels`、`SaveImage`、`VAEEncode`、`ReferenceLatent`、`EmptyFlux2LatentImage`、`GetImageSize`、`UNETLoader`、`LoadImage`、`CFGGuider`、`Flux2Scheduler`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、CFGGuider、KSamplerSelect
