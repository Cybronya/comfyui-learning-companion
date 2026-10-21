---
key: 图片生成/文生图/Z-image Base & Turbo+Klein三重采样文生图_2063539477594857474.json
name: Z-image Base & Turbo+Klein三重采样文生图_2063539477594857474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image Base & Turbo+Klein三重采样文生图_2063539477594857474.json
hash: df5e206add4ea91c
coverage: 0.915254
learned_at: 2026-10-19 23:21:56
nodes: [LayerUtility: PurgeVRAM, easy showAnything, llama_cpp_model_loader, llama_cpp_instruct_adv, KSamplerAdvanced, ModelSamplingAuraFlow, VAELoader, UNETLoader, KSamplerAdvanced, LayerUtility: PurgeVRAM, PrimitiveInt, PrimitiveInt, UNETLoader, LoraLoaderModelOnly, EmptyLatentImage, ModelSamplingAuraFlow, CLIPLoader, CR Text, SeedVR2LoadVAEModel, LayerUtility: PurgeVRAM, SaveImage, easy setNode, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, Image Comparer (rgthree), LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, easy setNode, VAEDecode, easy setNode, KSamplerSelect, RandomNoise, EmptyFlux2LatentImage, CLIPTextEncode, CFGGuider, GetImageSize, VAEEncode, ImageScaleToTotalPixels, Flux2Scheduler, SamplerCustomAdvanced, VAEDecode, easy setNode, ColorMatch, LayerUtility: PurgeVRAM, easy getNode, SaveImage, LoraLoaderModelOnly, VAELoader, CLIPLoader, ConditioningZeroOut, ReferenceLatent, UNETLoader, easy getNode, easy getNode, SaveImage, Fast Groups Bypasser (rgthree), CR Text, easy getNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 40, "denoise": "simple", "height": 1536, "sampler_name": 4, "scheduler": "res_multistep", "seed": "enable", "steps": "randomize", "width": 864}
---

# 图片生成/文生图/Z-image Base & Turbo+Klein三重采样文生图_2063539477594857474.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image Base & Turbo+Klein三重采样文生图_2063539477594857474.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `LayerUtility: PurgeVRAM`
- `easy showAnything`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `KSamplerAdvanced` ★核心
- `ModelSamplingAuraFlow`
- `VAELoader`
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM`
- `PrimitiveInt`
- `PrimitiveInt`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyLatentImage` ★核心
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `CR Text`
- `SeedVR2LoadVAEModel`
- `LayerUtility: PurgeVRAM`
- `SaveImage`
- `easy setNode`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy setNode`
- `VAEDecode` ★核心
- `easy setNode`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `EmptyFlux2LatentImage`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `GetImageSize`
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `Flux2Scheduler`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `easy setNode`
- `ColorMatch`
- `LayerUtility: PurgeVRAM`
- `easy getNode`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `UNETLoader` ★核心
- `easy getNode`
- `easy getNode`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `CR Text`
- `easy getNode`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `40`
- `sampler_name` = `4`
- `scheduler` = `res_multistep`
- `denoise` = `simple`
- `width` = `864`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（54/59）

**有卡**：`LayerUtility: PurgeVRAM`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`KSamplerAdvanced`、`ModelSamplingAuraFlow`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`CLIPLoader`、`CR Text`、`SeedVR2LoadVAEModel`、`SaveImage`、`easy setNode`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`CLIPTextEncode`、`VAEDecode`、`KSamplerSelect`、`RandomNoise`、`EmptyFlux2LatentImage`、`CFGGuider`、`GetImageSize`、`VAEEncode`、`ImageScaleToTotalPixels`、`Flux2Scheduler`、`SamplerCustomAdvanced`、`ColorMatch`、`easy getNode`、`ConditioningZeroOut`、`ReferenceLatent`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
