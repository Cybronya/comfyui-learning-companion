---
key: 平台全量/Z-Image 图片去除Ai感  提升图片质量 增加细节 SeedVR放大Z Image Turbo_2008812389692612609.json
name: Z-Image 图片去除Ai感  提升图片质量 增加细节 SeedVR放大Z Image Turbo_2008812389692612609
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Z-Image 图片去除Ai感  提升图片质量 增加细节 SeedVR放大Z Image Turbo_2008812389692612609.json
hash: ae5ff1d6e9a1b596
coverage: 0.764706
learned_at: 2026-11-14 01:08:08
nodes: [JoinStrings, UNETLoader, CLIPLoader, VAELoader, KSampler, MarkdownNote, VAEEncode, ConditioningZeroOut, SaveImage, SeedVR2LoadVAEModel, ImageScaleBy, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, VAEDecode, SaveImage, SeedVR2VideoUpscaler, LayerUtility: ImageReelComposit, PreviewImage, PrimitiveNode, ShowText|pysssss, Fast Groups Bypasser (rgthree), LayerUtility: ImageReel, easy imageConcat, Image Comparer (rgthree), PreviewImage, CLIPTextEncode, LayerUtility: PurgeVRAM, Qwen3_VQA, SeedVR2LoadDiTModel, ImpactInt, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, easy showAnything, TextInput_]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.7000000000000002, "sampler_name": "euler", "scheduler": "simple", "seed": 739252514763307, "steps": 10}
---

# 平台全量/Z-Image 图片去除Ai感  提升图片质量 增加细节 SeedVR放大Z Image Turbo_2008812389692612609.json

> 来源文件 `comfyui_library/workflows/平台全量/Z-Image 图片去除Ai感  提升图片质量 增加细节 SeedVR放大Z Image Turbo_2008812389692612609.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `JoinStrings`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `MarkdownNote`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `SaveImage`
- `SeedVR2LoadVAEModel`
- `ImageScaleBy`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `LayerUtility: ImageReelComposit`
- `PreviewImage`
- `PrimitiveNode`
- `ShowText|pysssss`
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: ImageReel`
- `easy imageConcat`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `Qwen3_VQA`
- `SeedVR2LoadDiTModel`
- `ImpactInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `easy showAnything`
- `TextInput_`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `739252514763307`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.7000000000000002`

## 知识

覆盖率 **76%**（26/34）

**有卡**：`JoinStrings`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`VAEEncode`、`ConditioningZeroOut`、`SaveImage`、`SeedVR2LoadVAEModel`、`ImageScaleBy`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`SeedVR2VideoUpscaler`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`easy imageConcat`、`CLIPTextEncode`、`Qwen3_VQA`、`SeedVR2LoadDiTModel`、`ImpactInt`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`TextInput_`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader
