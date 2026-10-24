---
key: 图片生成/图生图/qwen3反推qwen2.1洗图重绘去除Ai感+SeedVR放大_2110389747871993858.json
name: qwen3反推qwen2.1洗图重绘去除Ai感+SeedVR放大_2110389747871993858
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen3反推qwen2.1洗图重绘去除Ai感+SeedVR放大_2110389747871993858.json
hash: 8d51b90dc482b0a9
coverage: 0.72973
learned_at: 2026-10-23 11:43:39
nodes: [JoinStrings, easy showAnything, MarkdownNote, ConditioningZeroOut, SaveImage, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, ImageScaleBy, LayerUtility: PurgeVRAM, SeedVR2VideoUpscaler, LayerUtility: ImageReelComposit, PrimitiveNode, ShowText|pysssss, Fast Groups Bypasser (rgthree), LayerUtility: ImageReel, Image Comparer (rgthree), VAEEncode, VAEDecode, easy imageConcat, LayerUtility: PurgeVRAM, SaveImage, MarkdownNote, PreviewImage, PreviewImage, LoraLoaderModelOnly, KSampler, VAELoader, UNETLoader, CLIPTextEncode, LayerUtility: PurgeVRAM, ImpactInt, CLIPLoader, LoadImage, MarkdownNote, TextInput_, LayerUtility: ImageScaleByAspectRatio V2, Qwen3_VQA]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.7000000000000002, "sampler_name": "euler", "scheduler": "simple", "seed": 652802153079609, "steps": 40}
---

# 图片生成/图生图/qwen3反推qwen2.1洗图重绘去除Ai感+SeedVR放大_2110389747871993858.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen3反推qwen2.1洗图重绘去除Ai感+SeedVR放大_2110389747871993858.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
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
- `LoadImage`
- `MarkdownNote`
- `TextInput_`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Qwen3_VQA`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `652802153079609`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.7000000000000002`

## 知识

覆盖率 **73%**（27/37）

**有卡**：`JoinStrings`、`ConditioningZeroOut`、`SaveImage`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`ImageScaleBy`、`LayerUtility: PurgeVRAM`、`SeedVR2VideoUpscaler`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`VAEEncode`、`VAEDecode`、`easy imageConcat`、`LoraLoaderModelOnly`、`KSampler`、`VAELoader`、`UNETLoader`、`CLIPTextEncode`、`ImpactInt`、`CLIPLoader`、`LoadImage`、`TextInput_`、`LayerUtility: ImageScaleByAspectRatio V2`、`Qwen3_VQA`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
