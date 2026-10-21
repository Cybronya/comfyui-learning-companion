---
key: 图片生成/文生图/Z Image 极致人体文生图 Extreme Asthetics Text to Image_2075065299652669442.json
name: Z Image 极致人体文生图 Extreme Asthetics Text to Image_2075065299652669442
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z Image 极致人体文生图 Extreme Asthetics Text to Image_2075065299652669442.json
hash: 0ab73b685a834adc
coverage: 0.692308
learned_at: 2026-10-20 00:20:13
nodes: [VAELoader, CLIPLoader, SamplerCustomAdvanced, UNETLoader, ImageScaleToTotalPixels, GetImageSize, CLIPTextEncode, ConditioningZeroOut, VAEEncode, UNETLoader, ReferenceLatent, ReferenceLatent, PreviewImage, EmptyFlux2LatentImage, Flux2Scheduler, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, SaveImage, PrimitiveInt, StringReplace, CLIPTextEncode, VAELoader, CLIPLoader, ConditioningZeroOut, KSamplerSelect, CFGGuider, VAEDecode, LayerUtility: PurgeVRAM V2, SaveImage, PreviewImage, VAEDecode, ColorMatch, ImageSharpen, Image Comparer (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, RandomNoise, Reroute, Reroute, Reroute, LoraLoaderModelOnly, Image Comparer (rgthree), PrimitiveInt, PrimitiveInt, Reroute, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, Note, AILab_QwenVL, CLIPTextEncode, PrimitiveStringMultiline, ShowText|pysssss, EmptyLatentImage, KSamplerAdvanced, KSamplerAdvanced, ModelSamplingAuraFlow, ModelSamplingAuraFlow, Note, PrimitiveStringMultiline, Note, PrimitiveStringMultiline, LoadImage, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 3, "denoise": "simple", "height": 1920, "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed", "width": 1080}
---

# 图片生成/文生图/Z Image 极致人体文生图 Extreme Asthetics Text to Image_2075065299652669442.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z Image 极致人体文生图 Extreme Asthetics Text to Image_2075065299652669442.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（65 个）：
- `VAELoader`
- `CLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `PreviewImage`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `PrimitiveInt`
- `StringReplace`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `SaveImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `ColorMatch`
- `ImageSharpen`
- `Image Comparer (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `RandomNoise`
- `Reroute`
- `Reroute`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `PrimitiveInt`
- `PrimitiveInt`
- `Reroute`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `Note`
- `AILab_QwenVL`
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `ShowText|pysssss`
- `EmptyLatentImage` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ModelSamplingAuraFlow`
- `ModelSamplingAuraFlow`
- `Note`
- `PrimitiveStringMultiline`
- `Note`
- `PrimitiveStringMultiline`
- `LoadImage`
- `SaveImage`

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `3`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **69%**（45/65）

**有卡**：`VAELoader`、`CLIPLoader`、`SamplerCustomAdvanced`、`UNETLoader`、`ImageScaleToTotalPixels`、`GetImageSize`、`CLIPTextEncode`、`ConditioningZeroOut`、`VAEEncode`、`ReferenceLatent`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`LoraLoaderModelOnly`、`SaveImage`、`StringReplace`、`KSamplerSelect`、`CFGGuider`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`ColorMatch`、`ImageSharpen`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`RandomNoise`、`AILab_QwenVL`、`EmptyLatentImage`、`KSamplerAdvanced`、`ModelSamplingAuraFlow`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
