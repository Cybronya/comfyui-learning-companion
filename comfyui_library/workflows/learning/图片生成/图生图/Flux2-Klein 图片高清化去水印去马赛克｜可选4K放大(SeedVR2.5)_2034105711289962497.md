---
key: 图片生成/图生图/Flux2-Klein 图片高清化去水印去马赛克｜可选4K放大(SeedVR2.5)_2034105711289962497.json
name: Flux2-Klein 图片高清化去水印去马赛克｜可选4K放大(SeedVR2.5)_2034105711289962497
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux2-Klein 图片高清化去水印去马赛克｜可选4K放大(SeedVR2.5)_2034105711289962497.json
hash: a985c3eed309887f
coverage: 0.738095
learned_at: 2026-10-23 10:59:59
nodes: [RandomNoise, CFGGuider, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, SamplerCustomAdvanced, GetImageSize, ReferenceLatent, ReferenceLatent, VAELoader, VAELoader, UNETLoader, VAEEncode, ConditioningZeroOut, RH_Translator, CLIPTextEncode, CLIPLoader, MuyeTextEditOutput, ImageScaleToTotalPixels, SaveImage, VAEDecode, LoadImage, SetNode, GetNode, Image Comparer (rgthree), ImageScaleBy, PreviewImage, SeedVR2LoadVAEModel, SeedVR2LoadVAEModel, ImageScaleToTotalPixels, SeedVR2VideoUpscaler, Image Comparer (rgthree), SetNode, Fast Groups Bypasser (rgthree), GetNode, SeedVR2LoadDiTModel, LoadImage, SeedVR2VideoUpscaler, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), SeedVR2LoadDiTModel, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 图片生成/图生图/Flux2-Klein 图片高清化去水印去马赛克｜可选4K放大(SeedVR2.5)_2034105711289962497.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux2-Klein 图片高清化去水印去马赛克｜可选4K放大(SeedVR2.5)_2034105711289962497.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `GetImageSize`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `RH_Translator`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `MuyeTextEditOutput`
- `ImageScaleToTotalPixels`
- `SaveImage`
- `VAEDecode` ★核心
- `LoadImage`
- `SetNode`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `PreviewImage`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadVAEModel`
- `ImageScaleToTotalPixels`
- `SeedVR2VideoUpscaler`
- `Image Comparer (rgthree)`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `SeedVR2LoadDiTModel`
- `LoadImage`
- `SeedVR2VideoUpscaler`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `SeedVR2LoadDiTModel`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **74%**（31/42）

**有卡**：`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`GetImageSize`、`ReferenceLatent`、`VAELoader`、`UNETLoader`、`VAEEncode`、`ConditioningZeroOut`、`RH_Translator`、`CLIPTextEncode`、`CLIPLoader`、`MuyeTextEditOutput`、`ImageScaleToTotalPixels`、`SaveImage`、`VAEDecode`、`LoadImage`、`ImageScaleBy`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、SaveImage、LoadImage
