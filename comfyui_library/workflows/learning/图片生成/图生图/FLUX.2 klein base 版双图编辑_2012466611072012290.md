---
key: 图片生成/图生图/FLUX.2 klein base 版双图编辑_2012466611072012290.json
name: FLUX.2 klein base 版双图编辑_2012466611072012290
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2 klein base 版双图编辑_2012466611072012290.json
hash: d7d482ef0227f9a9
coverage: 0.96
learned_at: 2026-10-23 10:54:07
nodes: [VAELoader, ReferenceLatent, CLIPTextEncode, ReferenceLatent, ImageScaleToTotalPixels, ImageScaleToTotalPixels, VAEEncode, ReferenceLatent, ReferenceLatent, RandomNoise, CLIPTextEncode, VAEEncode, GetImageSize, EmptyFlux2LatentImage, CFGGuider, Flux2Scheduler, KSamplerSelect, VAEDecode, SamplerCustomAdvanced, CLIPLoader, SaveImage, LoadImage, LoadImage, PrimitiveStringMultiline, UNETLoader]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.2 klein base 版双图编辑_2012466611072012290.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2 klein base 版双图编辑_2012466611072012290.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `VAELoader`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `GetImageSize`
- `EmptyFlux2LatentImage`
- `CFGGuider`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `CLIPLoader`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心

## 知识

覆盖率 **96%**（24/25）

**有卡**：`VAELoader`、`ReferenceLatent`、`CLIPTextEncode`、`ImageScaleToTotalPixels`、`VAEEncode`、`RandomNoise`、`GetImageSize`、`EmptyFlux2LatentImage`、`CFGGuider`、`Flux2Scheduler`、`KSamplerSelect`、`VAEDecode`、`SamplerCustomAdvanced`、`CLIPLoader`、`SaveImage`、`LoadImage`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、CFGGuider、KSamplerSelect
