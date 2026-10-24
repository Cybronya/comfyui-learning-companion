---
key: 图片生成/图生图/Z-image-base+高清放大 文生图_图生图  高清放大Z-image+Flux2-klein_2020661220746993665.json
name: Z-image-base+高清放大 文生图_图生图  高清放大Z-image+Flux2-klein_2020661220746993665
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-image-base+高清放大 文生图_图生图  高清放大Z-image+Flux2-klein_2020661220746993665.json
hash: 39d551abe76f2c99
coverage: 0.877551
learned_at: 2026-10-23 11:30:52
nodes: [KSamplerSelect, RandomNoise, CFGGuider, CLIPTextEncode, ReferenceLatent, VAEEncode, ImageScaleToTotalPixels, UNETLoader, CLIPLoader, VAELoader, VAELoader, CLIPLoader, CLIPTextEncode, UNETLoader, ModelSamplingAuraFlow, CLIPTextEncode, Qwen3_VQA, SomethingToString, LayerUtility: PurgeVRAM V2, SamplerCustomAdvanced, Flux2Scheduler, EmptyFlux2LatentImage, ColorMatch, VAEDecode, SaveImage, ImageSharpen, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, PreviewImage, KSampler, VAEDecode, ReferenceLatent, ConditioningZeroOut, GetImageSize, Image Comparer (rgthree), LoraLoaderModelOnly, EmptySD3LatentImage, INTConstant, INTConstant, CR Text, ShowText|pysssss, ImageScaleBy, LoadImage, Any Switch (rgthree), SaveImage, Fast Groups Bypasser (rgthree), MemoryCleaner, SeedVR2VideoUpscaler, Image Comparer (rgthree)]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 3, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 66967720136191, "steps": 40}
---

# 图片生成/图生图/Z-image-base+高清放大 文生图_图生图  高清放大Z-image+Flux2-klein_2020661220746993665.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-image-base+高清放大 文生图_图生图  高清放大Z-image+Flux2-klein_2020661220746993665.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `Qwen3_VQA`
- `SomethingToString`
- `LayerUtility: PurgeVRAM V2`
- `SamplerCustomAdvanced` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `ColorMatch`
- `VAEDecode` ★核心
- `SaveImage`
- `ImageSharpen`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `PreviewImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ReferenceLatent`
- `ConditioningZeroOut`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `EmptySD3LatentImage`
- `INTConstant`
- `INTConstant`
- `CR Text`
- `ShowText|pysssss`
- `ImageScaleBy`
- `LoadImage`
- `Any Switch (rgthree)`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `MemoryCleaner`
- `SeedVR2VideoUpscaler`
- `Image Comparer (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `66967720136191`
- `steps` = `40`
- `cfg` = `3`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（43/49）

**有卡**：`KSamplerSelect`、`RandomNoise`、`CFGGuider`、`CLIPTextEncode`、`ReferenceLatent`、`VAEEncode`、`ImageScaleToTotalPixels`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`Qwen3_VQA`、`SomethingToString`、`LayerUtility: PurgeVRAM V2`、`SamplerCustomAdvanced`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`ColorMatch`、`VAEDecode`、`SaveImage`、`ImageSharpen`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`KSampler`、`ConditioningZeroOut`、`GetImageSize`、`LoraLoaderModelOnly`、`EmptySD3LatentImage`、`INTConstant`、`CR Text`、`ImageScaleBy`、`LoadImage`、`MemoryCleaner`、`SeedVR2VideoUpscaler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut
