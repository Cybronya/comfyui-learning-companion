---
key: 图片生成/图生图/模型渲染Flux2_1.1_2088837920449974273.json
name: 模型渲染Flux2_1.1_2088837920449974273
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/模型渲染Flux2_1.1_2088837920449974273.json
hash: 8af489676b0b2a6b
coverage: 0.941176
learned_at: 2026-10-23 13:10:02
nodes: [KSamplerSelect, SamplerCustomAdvanced, EmptyFlux2LatentImage, GetImageSize, RandomNoise, ReferenceLatent, ReferenceLatent, VAEEncode, ConditioningZeroOut, VAELoader, InpaintModelConditioning, ImageScaleToTotalPixels, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, ImageScaleBy, SeedVR2VideoUpscaler, Image Comparer (rgthree), SaveImage, FeatherMask, MaskPreview, ImageStitch, PreviewImage, CLIPLoader, Flux2Scheduler, UNETLoader, CFGGuider, CLIPTextEncode, LoraLoaderModelOnly, LoadImage, LoraLoaderModelOnly, SaveImage, VAEDecode, ImageUpscaleWithModel, UpscaleModelLoader]
patterns: []
missing: []
---

# 图片生成/图生图/模型渲染Flux2_1.1_2088837920449974273.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/模型渲染Flux2_1.1_2088837920449974273.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
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
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`

## 知识

覆盖率 **94%**（32/34）

**有卡**：`KSamplerSelect`、`SamplerCustomAdvanced`、`EmptyFlux2LatentImage`、`GetImageSize`、`RandomNoise`、`ReferenceLatent`、`VAEEncode`、`ConditioningZeroOut`、`VAELoader`、`InpaintModelConditioning`、`ImageScaleToTotalPixels`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`ImageScaleBy`、`SeedVR2VideoUpscaler`、`SaveImage`、`FeatherMask`、`MaskPreview`、`ImageStitch`、`CLIPLoader`、`Flux2Scheduler`、`UNETLoader`、`CFGGuider`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`LoadImage`、`VAEDecode`、`ImageUpscaleWithModel`、`UpscaleModelLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
