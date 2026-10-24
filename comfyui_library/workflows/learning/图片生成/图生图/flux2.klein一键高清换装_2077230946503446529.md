---
key: 图片生成/图生图/flux2.klein一键高清换装_2077230946503446529.json
name: flux2.klein一键高清换装_2077230946503446529
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/flux2.klein一键高清换装_2077230946503446529.json
hash: f2fcbb6f99599a65
coverage: 0.977778
learned_at: 2026-10-23 11:36:30
nodes: [KSamplerSelect, Flux2Scheduler, CFGGuider, SamplerCustomAdvanced, RandomNoise, UNETLoader, CLIPLoader, ConditioningZeroOut, EmptyFlux2LatentImage, GetImageSize, VAEEncode, ReferenceLatent, ReferenceLatent, VAEEncode, VAELoader, ReferenceLatent, ReferenceLatent, ImageScaleToTotalPixels, ImageScaleToTotalPixels, VAEDecode, SaveImage, ImageSmartSharpen+, CLIPTextEncode, KSamplerSelect, VAEDecode, RandomNoise, UNETLoader, CLIPLoader, CFGGuider, Flux2Scheduler, ReferenceLatent, ReferenceLatent, VAEEncode, VAELoader, ImageResize+, ImageScaleToTotalPixels, CLIPTextEncode, Image Comparer (rgthree), SaveImage, SamplerCustomAdvanced, GetImageSize, EmptyFlux2LatentImage, ConditioningZeroOut, LoadImage, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/flux2.klein一键高清换装_2077230946503446529.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/flux2.klein一键高清换装_2077230946503446529.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `VAELoader`
- `ReferenceLatent`
- `ReferenceLatent`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `SaveImage`
- `ImageSmartSharpen+`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `RandomNoise`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CFGGuider`
- `Flux2Scheduler`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `VAELoader`
- `ImageResize+`
- `ImageScaleToTotalPixels`
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `SamplerCustomAdvanced` ★核心
- `GetImageSize`
- `EmptyFlux2LatentImage`
- `ConditioningZeroOut`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **98%**（44/45）

**有卡**：`KSamplerSelect`、`Flux2Scheduler`、`CFGGuider`、`SamplerCustomAdvanced`、`RandomNoise`、`UNETLoader`、`CLIPLoader`、`ConditioningZeroOut`、`EmptyFlux2LatentImage`、`GetImageSize`、`VAEEncode`、`ReferenceLatent`、`VAELoader`、`ImageScaleToTotalPixels`、`VAEDecode`、`SaveImage`、`ImageSmartSharpen+`、`CLIPTextEncode`、`ImageResize+`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
