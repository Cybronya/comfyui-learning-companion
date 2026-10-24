---
key: 图片生成/图生图/FLUX.2-klein_官方基础工作流（图像编辑）_2048613383078944770.json
name: FLUX.2-klein_官方基础工作流（图像编辑）_2048613383078944770
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2-klein_官方基础工作流（图像编辑）_2048613383078944770.json
hash: a8015c952eecfda8
coverage: 0.977778
learned_at: 2026-10-23 10:54:14
nodes: [VAELoader, SamplerCustomAdvanced, GetImageSize, CFGGuider, KSamplerSelect, Flux2Scheduler, VAEDecode, RandomNoise, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, ReferenceLatent, ReferenceLatent, ReferenceLatent, ReferenceLatent, VAEDecode, Flux2Scheduler, RandomNoise, EmptyFlux2LatentImage, ImageScaleToTotalPixels, ImageScaleToTotalPixels, SaveImage, ImageScaleToTotalPixels, ConditioningZeroOut, VAEEncode, ReferenceLatent, ReferenceLatent, CLIPTextEncode, ConditioningZeroOut, GetImageSize, VAEEncode, VAEEncode, EmptyFlux2LatentImage, VAELoader, SamplerCustomAdvanced, CFGGuider, KSamplerSelect, VAEDecode, RandomNoise, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, ReferenceLatent, ReferenceLatent, ReferenceLatent, ReferenceLatent, VAEDecode, Flux2Scheduler, RandomNoise, ImageScaleToTotalPixels, ImageScaleToTotalPixels, SaveImage, SaveImage, ConditioningZeroOut, VAEEncode, ReferenceLatent, ReferenceLatent, CLIPTextEncode, ConditioningZeroOut, VAEEncode, VAEEncode, ImageScaleToTotalPixels, ImpactInt, ImpactInt, EmptyFlux2LatentImage, Flux2Scheduler, EmptyFlux2LatentImage, ImpactInt, ImpactInt, Note, CLIPLoader, VAELoader, UNETLoader, UNETLoader, VAELoader, CLIPLoader, CLIPLoader, CLIPLoader, CLIPTextEncode, UNETLoader, UNETLoader, SaveImage, LoadImage, LoadImage, LoadImage, CLIPTextEncode, LoadImage, LoadImage, LoadImage, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.2-klein_官方基础工作流（图像编辑）_2048613383078944770.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2-klein_官方基础工作流（图像编辑）_2048613383078944770.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（90 个）：
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `GetImageSize`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `VAEDecode` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEDecode` ★核心
- `Flux2Scheduler`
- `RandomNoise`
- `EmptyFlux2LatentImage`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `SaveImage`
- `ImageScaleToTotalPixels`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `GetImageSize`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `EmptyFlux2LatentImage`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEDecode` ★核心
- `Flux2Scheduler`
- `RandomNoise`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `SaveImage`
- `SaveImage`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `ImpactInt`
- `ImpactInt`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `ImpactInt`
- `ImpactInt`
- `Note`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `CLIPLoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **98%**（88/90）

**有卡**：`VAELoader`、`SamplerCustomAdvanced`、`GetImageSize`、`CFGGuider`、`KSamplerSelect`、`Flux2Scheduler`、`VAEDecode`、`RandomNoise`、`ReferenceLatent`、`EmptyFlux2LatentImage`、`ImageScaleToTotalPixels`、`SaveImage`、`ConditioningZeroOut`、`VAEEncode`、`CLIPTextEncode`、`ImpactInt`、`CLIPLoader`、`UNETLoader`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
