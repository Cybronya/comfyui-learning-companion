---
key: 图片生成/图生图/Flux.2 [Klein]图像扩图+4K放大_2012429239328444417.json
name: Flux.2 [Klein]图像扩图+4K放大_2012429239328444417
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.2 [Klein]图像扩图+4K放大_2012429239328444417.json
hash: 6d57faa221fb69f6
coverage: 0.909091
learned_at: 2026-10-23 10:58:47
nodes: [LoadImage, UNETLoader, SamplerCustomAdvanced, Flux2Scheduler, KSamplerSelect, RandomNoise, VAELoader, CFGGuider, EmptyFlux2LatentImage, ConditioningZeroOut, CLIPLoader, SeedVR2LoadVAEModel, ReferenceLatent, ReferenceLatent, VAEEncode, ImageScaleToTotalPixels, CLIPTextEncode, ImageScaleToTotalPixels, GetImageSize, ImagePadForOutpaint, ColorMatch, SaveImage, SaveImage, SeedVR2VideoUpscaler, SaveImage, Image Comparer (rgthree), PreviewImage, LoadImage, Image Comparer (rgthree), LoadImage, VAEDecode, LayerUtility: PurgeVRAM V2, SeedVR2LoadDiTModel]
patterns: []
missing: []
---

# 图片生成/图生图/Flux.2 [Klein]图像扩图+4K放大_2012429239328444417.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.2 [Klein]图像扩图+4K放大_2012429239328444417.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `LoadImage`
- `UNETLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `VAELoader`
- `CFGGuider`
- `EmptyFlux2LatentImage`
- `ConditioningZeroOut`
- `CLIPLoader`
- `SeedVR2LoadVAEModel`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `CLIPTextEncode` ★核心
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `ImagePadForOutpaint`
- `ColorMatch`
- `SaveImage`
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `SeedVR2LoadDiTModel`

## 知识

覆盖率 **91%**（30/33）

**有卡**：`LoadImage`、`UNETLoader`、`SamplerCustomAdvanced`、`Flux2Scheduler`、`KSamplerSelect`、`RandomNoise`、`VAELoader`、`CFGGuider`、`EmptyFlux2LatentImage`、`ConditioningZeroOut`、`CLIPLoader`、`SeedVR2LoadVAEModel`、`ReferenceLatent`、`VAEEncode`、`ImageScaleToTotalPixels`、`CLIPTextEncode`、`GetImageSize`、`ImagePadForOutpaint`、`ColorMatch`、`SaveImage`、`SeedVR2VideoUpscaler`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`SeedVR2LoadDiTModel`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
