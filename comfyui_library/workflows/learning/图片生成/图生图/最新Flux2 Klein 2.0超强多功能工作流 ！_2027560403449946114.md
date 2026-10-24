---
key: 图片生成/图生图/最新Flux2 Klein 2.0超强多功能工作流 ！_2027560403449946114.json
name: 最新Flux2 Klein 2.0超强多功能工作流 ！_2027560403449946114
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/最新Flux2 Klein 2.0超强多功能工作流 ！_2027560403449946114.json
hash: 73a3fd96e474af39
coverage: 0.85
learned_at: 2026-10-23 13:06:52
nodes: [KSamplerSelect, ReferenceLatent, ReferenceLatent, PreviewImage, PreviewImage, DepthAnythingPreprocessor, CannyEdgePreprocessor, MaskPreview+, CLIPLoader, Mask Fill Holes, VAELoader, InpaintModelConditioning, ImpactGaussianBlurMask, Flux2Scheduler, CFGGuider, ReferenceLatent, ReferenceLatent, ConditioningZeroOut, ReferenceLatent, CR Latent Input Switch, EmptyFlux2LatentImage, CR Latent Input Switch, OpenposePreprocessor, ImageScaleToTotalPixels, easy imageSize, PreviewImage, CR Latent Input Switch, VAEEncode, ImageScaleToTotalPixels, easy imageSize, ImageScaleToTotalPixels, VAEEncode, ReferenceLatent, RandomNoise, SamplerCustomAdvanced, LoadImage, PrimitiveInt, PrimitiveInt, VAEEncode, EmptyFlux2LatentImage, LoadImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, ImageScaleBy, SeedVR2VideoUpscaler, Image Comparer (rgthree), SaveImage, VAEDecode, SaveImage, Image Comparer (rgthree), ImagePadForOutpaint, MaskPreview+, PreviewImage, UNETLoader, PreviewImage, easy imageSize, LoadImage, CLIPTextEncode, GetImageSize, ImageScaleToTotalPixels]
patterns: []
missing: []
---

# 图片生成/图生图/最新Flux2 Klein 2.0超强多功能工作流 ！_2027560403449946114.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/最新Flux2 Klein 2.0超强多功能工作流 ！_2027560403449946114.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
- `KSamplerSelect` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `PreviewImage`
- `PreviewImage`
- `DepthAnythingPreprocessor`
- `CannyEdgePreprocessor`
- `MaskPreview+`
- `CLIPLoader`
- `Mask Fill Holes`
- `VAELoader`
- `InpaintModelConditioning`
- `ImpactGaussianBlurMask`
- `Flux2Scheduler`
- `CFGGuider`
- `ReferenceLatent`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `CR Latent Input Switch`
- `EmptyFlux2LatentImage`
- `CR Latent Input Switch`
- `OpenposePreprocessor`
- `ImageScaleToTotalPixels`
- `easy imageSize`
- `PreviewImage`
- `CR Latent Input Switch`
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `easy imageSize`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `VAEEncode` ★核心
- `EmptyFlux2LatentImage`
- `LoadImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `ImageScaleBy`
- `SeedVR2VideoUpscaler`
- `Image Comparer (rgthree)`
- `SaveImage`
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `ImagePadForOutpaint`
- `MaskPreview+`
- `PreviewImage`
- `UNETLoader` ★核心
- `PreviewImage`
- `easy imageSize`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `GetImageSize`
- `ImageScaleToTotalPixels`

## 知识

覆盖率 **85%**（51/60）

**有卡**：`KSamplerSelect`、`ReferenceLatent`、`DepthAnythingPreprocessor`、`CannyEdgePreprocessor`、`MaskPreview+`、`CLIPLoader`、`Mask Fill Holes`、`VAELoader`、`InpaintModelConditioning`、`ImpactGaussianBlurMask`、`Flux2Scheduler`、`CFGGuider`、`ConditioningZeroOut`、`CR Latent Input Switch`、`EmptyFlux2LatentImage`、`OpenposePreprocessor`、`ImageScaleToTotalPixels`、`easy imageSize`、`VAEEncode`、`RandomNoise`、`SamplerCustomAdvanced`、`LoadImage`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`ImageScaleBy`、`SeedVR2VideoUpscaler`、`SaveImage`、`VAEDecode`、`ImagePadForOutpaint`、`UNETLoader`、`CLIPTextEncode`、`GetImageSize`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、OpenposePreprocessor
