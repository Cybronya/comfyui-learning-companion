---
key: 图片生成/图生图/Flux2.klein单图编辑（去水印_换背景_改色）_2013100887060779010.json
name: Flux2.klein单图编辑（去水印_换背景_改色）_2013100887060779010
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux2.klein单图编辑（去水印_换背景_改色）_2013100887060779010.json
hash: 713636ef77c1dc31
coverage: 0.947368
learned_at: 2026-10-23 11:00:53
nodes: [BasicGuider, SamplerCustomAdvanced, VAELoader, SaveImage, CLIPLoader, ReferenceLatent, VAEEncode, Flux2Scheduler, EmptyFlux2LatentImage, CLIPTextEncode, FluxGuidance, Image Comparer (rgthree), VAEDecode, RandomNoise, ImageScaleToTotalPixels, GetImageSize, KSamplerSelect, LoadImage, UNETLoader]
patterns: []
missing: []
---

# 图片生成/图生图/Flux2.klein单图编辑（去水印_换背景_改色）_2013100887060779010.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux2.klein单图编辑（去水印_换背景_改色）_2013100887060779010.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `SaveImage`
- `CLIPLoader`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `RandomNoise`
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `KSamplerSelect` ★核心
- `LoadImage`
- `UNETLoader` ★核心

## 知识

覆盖率 **95%**（18/19）

**有卡**：`BasicGuider`、`SamplerCustomAdvanced`、`VAELoader`、`SaveImage`、`CLIPLoader`、`ReferenceLatent`、`VAEEncode`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`CLIPTextEncode`、`FluxGuidance`、`VAEDecode`、`RandomNoise`、`ImageScaleToTotalPixels`、`GetImageSize`、`KSamplerSelect`、`LoadImage`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
