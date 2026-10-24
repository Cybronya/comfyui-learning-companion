---
key: 图片生成/图生图/模型渲染Flux2_1.0_2088092960683548674.json
name: 模型渲染Flux2_1.0_2088092960683548674
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/模型渲染Flux2_1.0_2088092960683548674.json
hash: fd2667fd6d647640
coverage: 0.891892
learned_at: 2026-10-23 13:10:02
nodes: [KSamplerSelect, SamplerCustomAdvanced, VAEDecode, EmptyFlux2LatentImage, GetImageSize, RandomNoise, ReferenceLatent, ReferenceLatent, VAEEncode, ConditioningZeroOut, VAELoader, InpaintModelConditioning, ImageScaleToTotalPixels, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, ImageScaleBy, SeedVR2VideoUpscaler, Image Comparer (rgthree), SaveImage, FeatherMask, MaskPreview, ImageStitch, PreviewImage, CLIPLoader, Flux2Scheduler, UNETLoader, CFGGuider, CLIPTextEncode, LoraLoaderModelOnly, Image Comparer (rgthree), UpscaleModelLoader, ImageUpscaleWithModel, Image Comparer (rgthree), SaveImage, SaveImage, LoadImage, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 图片生成/图生图/模型渲染Flux2_1.0_2088092960683548674.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/模型渲染Flux2_1.0_2088092960683548674.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `RandomNoise`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `VAELoader`
- `InpaintModelConditioning`
- `ImageScaleToTotalPixels`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `ImageScaleBy`
- `SeedVR2VideoUpscaler`
- `Image Comparer (rgthree)`
- `SaveImage`
- `FeatherMask`
- `MaskPreview`
- `ImageStitch`
- `PreviewImage`
- `CLIPLoader`
- `Flux2Scheduler`
- `UNETLoader` ★核心
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **89%**（33/37）

**有卡**：`KSamplerSelect`、`SamplerCustomAdvanced`、`VAEDecode`、`EmptyFlux2LatentImage`、`GetImageSize`、`RandomNoise`、`ReferenceLatent`、`VAEEncode`、`ConditioningZeroOut`、`VAELoader`、`InpaintModelConditioning`、`ImageScaleToTotalPixels`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`ImageScaleBy`、`SeedVR2VideoUpscaler`、`SaveImage`、`FeatherMask`、`MaskPreview`、`ImageStitch`、`CLIPLoader`、`Flux2Scheduler`、`UNETLoader`、`CFGGuider`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
