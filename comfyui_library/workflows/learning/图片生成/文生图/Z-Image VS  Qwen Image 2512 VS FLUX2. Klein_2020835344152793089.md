---
key: 图片生成/文生图/Z-Image VS  Qwen Image 2512 VS FLUX2. Klein_2020835344152793089.json
name: Z-Image VS  Qwen Image 2512 VS FLUX2. Klein_2020835344152793089
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image VS  Qwen Image 2512 VS FLUX2. Klein_2020835344152793089.json
hash: b30f1682f49447b8
coverage: 0.830508
learned_at: 2026-10-19 22:29:57
nodes: [ConditioningZeroOut, KSamplerSelect, CFGGuider, Flux2Scheduler, CLIPLoader, VAELoader, UNETLoader, LoraLoaderModelOnly, ConditioningZeroOut, KSamplerAdvanced, VAEDecode, UNETLoader, VAELoader, UNETLoader, SamplerCustomAdvanced, KSamplerAdvanced, VAEEncode, VAEEncode, VAELoader, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPLoader, ConditioningZeroOut, CLIPTextEncode, ConditioningZeroOut, CLIPTextEncode, CLIPLoader, LayerUtility: ImageReelComposit, SaveImage, ConditioningZeroOut, CLIPTextEncode, RandomNoise, PreviewImage, LayerUtility: ImageReel, VAEDecode, VAEDecode, Image Comparer (rgthree), VAEDecode, VAEDecode, VAEDecode, UNETLoader, CLIPLoader, VAELoader, PreviewImage, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, KSamplerAdvanced, EmptyLatentImage, easy promptList, easy promptList, PreviewImage, PreviewImage, PreviewImage, PreviewImage, Image Comparer (rgthree), Image Comparer (rgthree), Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": "FlowMatchEulerDiscreteScheduler", "height": 1536, "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed", "width": 1024}
---

# 图片生成/文生图/Z-Image VS  Qwen Image 2512 VS FLUX2. Klein_2020835344152793089.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image VS  Qwen Image 2512 VS FLUX2. Klein_2020835344152793089.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `ConditioningZeroOut`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `Flux2Scheduler`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `PreviewImage`
- `LayerUtility: ImageReel`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `PreviewImage`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `EmptyLatentImage` ★核心
- `easy promptList`
- `easy promptList`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `FlowMatchEulerDiscreteScheduler`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（49/59）

**有卡**：`ConditioningZeroOut`、`KSamplerSelect`、`CFGGuider`、`Flux2Scheduler`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`VAEDecode`、`SamplerCustomAdvanced`、`VAEEncode`、`CLIPTextEncode`、`LayerUtility: ImageReelComposit`、`SaveImage`、`RandomNoise`、`LayerUtility: ImageReel`、`EmptyLatentImage`、`easy promptList`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
