---
key: 平台全量/极致人体洗图CN版Z+Image+Extreme+Asthetics+ControlNet_2030482347077931009.json
name: 极致人体洗图CN版Z+Image+Extreme+Asthetics+ControlNet_2030482347077931009
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/极致人体洗图CN版Z+Image+Extreme+Asthetics+ControlNet_2030482347077931009.json
hash: 84efb33585138d75
coverage: 0.714286
learned_at: 2026-11-14 02:17:27
nodes: [SamplerCustomAdvanced, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, ModelSamplingAuraFlow, CLIPTextEncode, CLIPLoader, ModelSamplingAuraFlow, ConditioningZeroOut, KSamplerSelect, CFGGuider, SaveImage, PreviewImage, VAEDecode, ColorMatch, SeedVR2LoadDiTModel, RandomNoise, Reroute, Image Comparer (rgthree), Reroute, CLIPLoader, VAELoader, SeedVR2LoadVAEModel, CLIPTextEncode, PrimitiveInt, PrimitiveInt, KSamplerAdvanced, KSamplerAdvanced, Fast Groups Bypasser (rgthree), PrimitiveInt, Reroute, SaveImage, Reroute, VAELoader, Reroute, Reroute, SaveImage, ModelSamplingAuraFlow, LayerUtility: ImageScaleByAspectRatio V2, EmptyLatentImage, Note, ImageSharpen, AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, VAEDecode, LayerUtility: PurgeVRAM V2, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, ModelPatchLoader, Note, ZImageFunControlnet, Note, PrimitiveStringMultiline, SeedVR2VideoUpscaler, PrimitiveStringMultiline, PreviewImage, ImageScaleToTotalPixels, GetImageSize, VAEEncode, ReferenceLatent, ReferenceLatent, Image Comparer (rgthree), LoadImage, AILab_QwenVL, ShowText|pysssss]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 3, "denoise": "simple", "height": 1536, "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed", "width": 1024}
---

# 平台全量/极致人体洗图CN版Z+Image+Extreme+Asthetics+ControlNet_2030482347077931009.json

> 来源文件 `comfyui_library/workflows/平台全量/极致人体洗图CN版Z+Image+Extreme+Asthetics+ControlNet_2030482347077931009.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（70 个）：
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
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
- `Note`
- `ZImageFunControlnet`
- `Note`
- `PrimitiveStringMultiline`
- `SeedVR2VideoUpscaler`
- `PrimitiveStringMultiline`
- `PreviewImage`
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `Image Comparer (rgthree)`
- `LoadImage`
- `AILab_QwenVL`
- `ShowText|pysssss`

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

覆盖率 **71%**（50/70）

**有卡**：`SamplerCustomAdvanced`、`CLIPTextEncode`、`ConditioningZeroOut`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`ModelSamplingAuraFlow`、`CLIPLoader`、`KSamplerSelect`、`CFGGuider`、`SaveImage`、`VAEDecode`、`ColorMatch`、`SeedVR2LoadDiTModel`、`RandomNoise`、`VAELoader`、`SeedVR2LoadVAEModel`、`KSamplerAdvanced`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyLatentImage`、`ImageSharpen`、`AIO_Preprocessor`、`LayerUtility: PurgeVRAM V2`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelPatchLoader`、`ZImageFunControlnet`、`SeedVR2VideoUpscaler`、`ImageScaleToTotalPixels`、`GetImageSize`、`VAEEncode`、`ReferenceLatent`、`LoadImage`、`AILab_QwenVL`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage
