---
key: 图片生成/图生图/Flux2 Klein Multi-Image Edit_2018198139378864129.json
name: Flux2 Klein Multi-Image Edit_2018198139378864129
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux2 Klein Multi-Image Edit_2018198139378864129.json
hash: c6acaeb4f2c6f218
coverage: 0.881579
learned_at: 2026-10-23 10:59:07
nodes: [KSamplerSelect, SamplerCustomAdvanced, CFGGuider, Flux2Scheduler, CLIPTextEncode, ConditioningZeroOut, GetImageSize, KSamplerSelect, SamplerCustomAdvanced, ReferenceLatent, VAEEncode, EmptyFlux2LatentImage, SaveImage, ImageScaleToTotalPixels, GetImageSize, ConditioningZeroOut, SaveImage, Image Comparer (rgthree), SeedVR2VideoUpscaler, LayerUtility: PurgeVRAM, RandomNoise, LoadImage, ImageScaleToTotalPixels, LoadImage, LoadImage, ImageScaleToTotalPixels, ImageScaleToTotalPixels, VAEEncode, VAEEncode, VAEEncode, ReferenceLatent, ReferenceLatent, Image Padding, EmptyFlux2LatentImage, RandomNoise, ImageScaleToTotalPixels, VAEEncode, VAEEncode, Flux2Scheduler, CFGGuider, AIO_Preprocessor, SeedVR2LoadVAEModel, SaveImage, Image Comparer (rgthree), SeedVR2VideoUpscaler, LayerUtility: PurgeVRAM, LoadImage, ReferenceLatent, ReferenceLatent, ReferenceLatent, LoadImage, Fast Groups Bypasser (rgthree), SaveImage, ImageScaleToTotalPixels, VAEDecode, VAEDecode, ReferenceLatent, SeedVR2LoadDiTModel, LoadImage, CLIPTextEncode, MarkdownNote, VAELoader, CLIPLoader, VAELoader, CLIPLoader, LoaderGGUF, UNETLoader, LoaderGGUF, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), UNETLoader, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 图片生成/图生图/Flux2 Klein Multi-Image Edit_2018198139378864129.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux2 Klein Multi-Image Edit_2018198139378864129.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（76 个）：
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `Flux2Scheduler`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `GetImageSize`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `EmptyFlux2LatentImage`
- `SaveImage`
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `ConditioningZeroOut`
- `SaveImage`
- `Image Comparer (rgthree)`
- `SeedVR2VideoUpscaler`
- `LayerUtility: PurgeVRAM`
- `RandomNoise`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `Image Padding`
- `EmptyFlux2LatentImage`
- `RandomNoise`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `Flux2Scheduler`
- `CFGGuider`
- `AIO_Preprocessor`
- `SeedVR2LoadVAEModel`
- `SaveImage`
- `Image Comparer (rgthree)`
- `SeedVR2VideoUpscaler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ReferenceLatent`
- `SeedVR2LoadDiTModel`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `LoaderGGUF`
- `UNETLoader` ★核心
- `LoaderGGUF`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **88%**（67/76）

**有卡**：`KSamplerSelect`、`SamplerCustomAdvanced`、`CFGGuider`、`Flux2Scheduler`、`CLIPTextEncode`、`ConditioningZeroOut`、`GetImageSize`、`ReferenceLatent`、`VAEEncode`、`EmptyFlux2LatentImage`、`SaveImage`、`ImageScaleToTotalPixels`、`SeedVR2VideoUpscaler`、`LayerUtility: PurgeVRAM`、`RandomNoise`、`LoadImage`、`Image Padding`、`AIO_Preprocessor`、`SeedVR2LoadVAEModel`、`VAEDecode`、`SeedVR2LoadDiTModel`、`VAELoader`、`CLIPLoader`、`LoaderGGUF`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
