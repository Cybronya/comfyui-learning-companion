---
key: 图片生成/图生图/flux 2 klein edit single image 单图编辑_2044446355933896705.json
name: flux 2 klein edit single image 单图编辑_2044446355933896705
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/flux 2 klein edit single image 单图编辑_2044446355933896705.json
hash: 4af38a5e34430796
coverage: 0.955556
learned_at: 2026-10-23 11:34:58
nodes: [KSamplerSelect, Flux2Scheduler, CFGGuider, RandomNoise, CLIPTextEncode, SamplerCustomAdvanced, VAEDecode, CFGGuider, ConditioningZeroOut, ReferenceLatent, RandomNoise, Flux2Scheduler, MarkdownNote, KSamplerSelect, CheckpointLoaderSimple, Note, UNETLoader, CLIPTextEncode, ImageScaleToTotalPixels, VAEEncode, ReferenceLatent, ConditioningZeroOut, GetImageSize, VAEEncode, ImageScaleToTotalPixels, VAEEncode, SamplerCustomAdvanced, VAEDecode, SaveImage, GetImageSize, CLIPLoader, VAELoader, UNETLoader, CLIPLoader, VAELoader, ImageScaleToTotalPixels, EmptyFlux2LatentImage, ReferenceLatent, ReferenceLatent, ReferenceLatent, ReferenceLatent, LoadImage, LoadImage, EmptyFlux2LatentImage, SaveImage]
patterns: []
missing: []
parameters: {"checkpoint": "darkBeastFeb0826Latest_dbkBlitzV15.safetensors"}
---

# 图片生成/图生图/flux 2 klein edit single image 单图编辑_2044446355933896705.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/flux 2 klein edit single image 单图编辑_2044446355933896705.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `CFGGuider`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `CFGGuider`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `RandomNoise`
- `Flux2Scheduler`
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `CheckpointLoaderSimple` ★核心
- `Note`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ConditioningZeroOut`
- `GetImageSize`
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `GetImageSize`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ImageScaleToTotalPixels`
- `EmptyFlux2LatentImage`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `LoadImage`
- `LoadImage`
- `EmptyFlux2LatentImage`
- `SaveImage`

## 关键参数

- `checkpoint` = `darkBeastFeb0826Latest_dbkBlitzV15.safetensors`

## 知识

覆盖率 **96%**（43/45）

**有卡**：`KSamplerSelect`、`Flux2Scheduler`、`CFGGuider`、`RandomNoise`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`VAEDecode`、`ConditioningZeroOut`、`ReferenceLatent`、`CheckpointLoaderSimple`、`UNETLoader`、`ImageScaleToTotalPixels`、`VAEEncode`、`GetImageSize`、`SaveImage`、`CLIPLoader`、`VAELoader`、`EmptyFlux2LatentImage`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
