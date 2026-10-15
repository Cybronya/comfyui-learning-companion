---
key: 图片生成/图生图/Qwen3反推Qwen2.1洗图重绘去除AI感加SeedVR放大，图生图写实化处理_2106072614019096578.json
name: Qwen3反推Qwen2.1洗图重绘去除AI感加SeedVR放大，图生图写实化处理_2106072614019096578
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen3反推Qwen2.1洗图重绘去除AI感加SeedVR放大，图生图写实化处理_2106072614019096578.json
hash: a1e6a348a9142445
coverage: 0.825397
learned_at: 2026-10-15 22:25:27
nodes: [JoinStrings, easy showAnything, ConditioningZeroOut, SaveImage, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, ImageScaleBy, LayerUtility: PurgeVRAM, SeedVR2VideoUpscaler, LayerUtility: ImageReelComposit, PrimitiveNode, ShowText|pysssss, Fast Groups Bypasser (rgthree), LayerUtility: ImageReel, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), VAEEncode, VAEDecode, easy imageConcat, LayerUtility: PurgeVRAM, SaveImage, PreviewImage, PreviewImage, LoraLoaderModelOnly, KSampler, VAELoader, UNETLoader, CLIPTextEncode, LayerUtility: PurgeVRAM, ImpactInt, CLIPLoader, LoadImage, TextInput_, Qwen3_VQA, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen3反推Qwen2.1洗图重绘去除AI感加SeedVR放大，图生图写实化处理_2106072614019096578.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen3反推Qwen2.1洗图重绘去除AI感加SeedVR放大，图生图写实化处理_2106072614019096578.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（63 个）：
- `JoinStrings`
- `easy showAnything`
- `ConditioningZeroOut`
- `SaveImage`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `ImageScaleBy`
- `LayerUtility: PurgeVRAM`
- `SeedVR2VideoUpscaler`
- `LayerUtility: ImageReelComposit`
- `PrimitiveNode`
- `ShowText|pysssss`
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `easy imageConcat`
- `LayerUtility: PurgeVRAM`
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `ImpactInt`
- `CLIPLoader`
- `LoadImage`
- `TextInput_`
- `Qwen3_VQA`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（52/63）

**有卡**：`JoinStrings`、`ConditioningZeroOut`、`SaveImage`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`ImageScaleBy`、`LayerUtility: PurgeVRAM`、`SeedVR2VideoUpscaler`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEEncode`、`VAEDecode`、`easy imageConcat`、`LoraLoaderModelOnly`、`KSampler`、`VAELoader`、`UNETLoader`、`CLIPTextEncode`、`ImpactInt`、`CLIPLoader`、`LoadImage`、`TextInput_`、`Qwen3_VQA`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
