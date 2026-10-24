---
key: 图片生成/图生图/qwen3反推qwen2.1洗图重绘去除Ai感+SeedVR放大_2110918495683833858.json
name: qwen3反推qwen2.1洗图重绘去除Ai感+SeedVR放大_2110918495683833858
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen3反推qwen2.1洗图重绘去除Ai感+SeedVR放大_2110918495683833858.json
hash: c7ffa8cf5f2801b4
coverage: 0.75
learned_at: 2026-10-23 11:43:39
nodes: [JoinStrings, easy showAnything, MarkdownNote, ConditioningZeroOut, SaveImage, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, ImageScaleBy, LayerUtility: PurgeVRAM, SeedVR2VideoUpscaler, LayerUtility: ImageReelComposit, PrimitiveNode, ShowText|pysssss, Fast Groups Bypasser (rgthree), LayerUtility: ImageReel, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), VAEEncode, VAEDecode, easy imageConcat, LayerUtility: PurgeVRAM, SaveImage, MarkdownNote, PreviewImage, PreviewImage, LoraLoaderModelOnly, KSampler, VAELoader, UNETLoader, CLIPTextEncode, LayerUtility: PurgeVRAM, ImpactInt, CLIPLoader, TextInput_, Qwen3_VQA, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.7000000000000002, "sampler_name": "euler", "scheduler": "simple", "seed": 820154197628298, "steps": 40}
---

# 图片生成/图生图/qwen3反推qwen2.1洗图重绘去除Ai感+SeedVR放大_2110918495683833858.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen3反推qwen2.1洗图重绘去除Ai感+SeedVR放大_2110918495683833858.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `JoinStrings`
- `easy showAnything`
- `MarkdownNote`
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
- `MarkdownNote`
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
- `TextInput_`
- `Qwen3_VQA`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `820154197628298`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.7000000000000002`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`JoinStrings`、`ConditioningZeroOut`、`SaveImage`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`ImageScaleBy`、`LayerUtility: PurgeVRAM`、`SeedVR2VideoUpscaler`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEEncode`、`VAEDecode`、`easy imageConcat`、`LoraLoaderModelOnly`、`KSampler`、`VAELoader`、`UNETLoader`、`CLIPTextEncode`、`ImpactInt`、`CLIPLoader`、`TextInput_`、`Qwen3_VQA`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
