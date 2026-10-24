---
key: 图片生成/图生图/Z Image Extreme Asthetics ControlNet (极致人体CN版）_2075071970105970689.json
name: Z Image Extreme Asthetics ControlNet (极致人体CN版）_2075071970105970689
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z Image Extreme Asthetics ControlNet (极致人体CN版）_2075071970105970689.json
hash: 56079cf233120493
coverage: 0.722222
learned_at: 2026-10-23 11:28:56
nodes: [SamplerCustomAdvanced, ImageScaleToTotalPixels, GetImageSize, CLIPTextEncode, ConditioningZeroOut, VAEEncode, ReferenceLatent, ReferenceLatent, EmptyFlux2LatentImage, Flux2Scheduler, ModelSamplingAuraFlow, CLIPTextEncode, CLIPLoader, ModelSamplingAuraFlow, ConditioningZeroOut, KSamplerSelect, CFGGuider, SaveImage, PreviewImage, VAEDecode, ColorMatch, SeedVR2LoadDiTModel, RandomNoise, Reroute, Image Comparer (rgthree), Reroute, CLIPLoader, VAELoader, SeedVR2LoadVAEModel, Image Comparer (rgthree), CLIPTextEncode, PrimitiveInt, PrimitiveInt, KSamplerAdvanced, KSamplerAdvanced, Fast Groups Bypasser (rgthree), PrimitiveInt, Reroute, SaveImage, Reroute, VAELoader, Reroute, Reroute, SaveImage, ModelSamplingAuraFlow, LayerUtility: ImageScaleByAspectRatio V2, EmptyLatentImage, Note, ImageSharpen, AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, VAEDecode, LayerUtility: PurgeVRAM V2, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, ModelPatchLoader, AILab_QwenVL, Note, ZImageFunControlnet, Note, PrimitiveStringMultiline, SeedVR2VideoUpscaler, PreviewImage, ShowText|pysssss, PrimitiveStringMultiline, LoadImage, LoadImage, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 3, "denoise": "simple", "height": 1536, "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed", "width": 1024}
---

# 图片生成/图生图/Z Image Extreme Asthetics ControlNet (极致人体CN版）_2075071970105970689.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z Image Extreme Asthetics ControlNet (极致人体CN版）_2075071970105970689.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（72 个）：
- `SamplerCustomAdvanced` ★核心
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `ConditioningZeroOut`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `SaveImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `ColorMatch`
- `SeedVR2LoadDiTModel`
- `RandomNoise`
- `Reroute`
- `Image Comparer (rgthree)`
- `Reroute`
- `CLIPLoader`
- `VAELoader`
- `SeedVR2LoadVAEModel`
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveInt`
- `Reroute`
- `SaveImage`
- `Reroute`
- `VAELoader`
- `Reroute`
- `Reroute`
- `SaveImage`
- `ModelSamplingAuraFlow`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyLatentImage` ★核心
- `Note`
- `ImageSharpen`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelPatchLoader`
- `AILab_QwenVL`
- `Note`
- `ZImageFunControlnet`
- `Note`
- `PrimitiveStringMultiline`
- `SeedVR2VideoUpscaler`
- `PreviewImage`
- `ShowText|pysssss`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`
- `SaveImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `3`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **72%**（52/72）

**有卡**：`SamplerCustomAdvanced`、`ImageScaleToTotalPixels`、`GetImageSize`、`CLIPTextEncode`、`ConditioningZeroOut`、`VAEEncode`、`ReferenceLatent`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`ModelSamplingAuraFlow`、`CLIPLoader`、`KSamplerSelect`、`CFGGuider`、`SaveImage`、`VAEDecode`、`ColorMatch`、`SeedVR2LoadDiTModel`、`RandomNoise`、`VAELoader`、`SeedVR2LoadVAEModel`、`KSamplerAdvanced`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyLatentImage`、`ImageSharpen`、`AIO_Preprocessor`、`LayerUtility: PurgeVRAM V2`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelPatchLoader`、`AILab_QwenVL`、`ZImageFunControlnet`、`SeedVR2VideoUpscaler`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
