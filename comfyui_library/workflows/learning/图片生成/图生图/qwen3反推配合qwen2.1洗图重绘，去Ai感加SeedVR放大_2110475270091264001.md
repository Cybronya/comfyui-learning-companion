---
key: 图片生成/图生图/qwen3反推配合qwen2.1洗图重绘，去Ai感加SeedVR放大_2110475270091264001.json
name: qwen3反推配合qwen2.1洗图重绘，去Ai感加SeedVR放大_2110475270091264001
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen3反推配合qwen2.1洗图重绘，去Ai感加SeedVR放大_2110475270091264001.json
hash: 2d68dcc8441e3383
coverage: 0.825397
learned_at: 2026-10-23 11:43:43
nodes: [JoinStrings, easy showAnything, ConditioningZeroOut, SaveImage, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, ImageScaleBy, LayerUtility: PurgeVRAM, SeedVR2VideoUpscaler, LayerUtility: ImageReelComposit, PrimitiveNode, ShowText|pysssss, Fast Groups Bypasser (rgthree), LayerUtility: ImageReel, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), VAEEncode, VAEDecode, easy imageConcat, LayerUtility: PurgeVRAM, SaveImage, PreviewImage, PreviewImage, LoraLoaderModelOnly, KSampler, VAELoader, UNETLoader, CLIPTextEncode, LayerUtility: PurgeVRAM, ImpactInt, CLIPLoader, LoadImage, TextInput_, Qwen3_VQA, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen3反推配合qwen2.1洗图重绘，去Ai感加SeedVR放大_2110475270091264001.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen3反推配合qwen2.1洗图重绘，去Ai感加SeedVR放大_2110475270091264001.json`

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
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
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
