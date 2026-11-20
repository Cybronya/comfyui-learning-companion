---
key: 视频生成/图生视频/qwen3反推qwen2.1洗图重绘去除Ai感+SeedVR放大_2114897270448680961.json
name: qwen3反推qwen2.1洗图重绘去除Ai感+SeedVR放大_2114897270448680961
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/qwen3反推qwen2.1洗图重绘去除Ai感+SeedVR放大_2114897270448680961.json
hash: 6432eb09f9b3f3aa
coverage: 0.72973
learned_at: 2026-10-30 17:59:45
nodes: [JoinStrings, easy showAnything, MarkdownNote, ConditioningZeroOut, SaveImage, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, ImageScaleBy, LayerUtility: PurgeVRAM, SeedVR2VideoUpscaler, LayerUtility: ImageReelComposit, PrimitiveNode, ShowText|pysssss, Fast Groups Bypasser (rgthree), LayerUtility: ImageReel, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), VAEEncode, VAEDecode, easy imageConcat, LayerUtility: PurgeVRAM, SaveImage, MarkdownNote, PreviewImage, PreviewImage, LoraLoaderModelOnly, KSampler, VAELoader, UNETLoader, CLIPTextEncode, LayerUtility: PurgeVRAM, ImpactInt, CLIPLoader, LoadImage, MarkdownNote, TextInput_, Qwen3_VQA]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.7, "sampler_name": "euler", "scheduler": "simple", "seed": 954625365900745, "steps": 40}
---

# 视频生成/图生视频/qwen3反推qwen2.1洗图重绘去除Ai感+SeedVR放大_2114897270448680961.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/qwen3反推qwen2.1洗图重绘去除Ai感+SeedVR放大_2114897270448680961.json`

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
- `LoadImage`
- `MarkdownNote`
- `TextInput_`
- `Qwen3_VQA`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `954625365900745`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.7`

## 知识

覆盖率 **73%**（27/37）

**有卡**：`JoinStrings`、`ConditioningZeroOut`、`SaveImage`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`ImageScaleBy`、`LayerUtility: PurgeVRAM`、`SeedVR2VideoUpscaler`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEEncode`、`VAEDecode`、`easy imageConcat`、`LoraLoaderModelOnly`、`KSampler`、`VAELoader`、`UNETLoader`、`CLIPTextEncode`、`ImpactInt`、`CLIPLoader`、`LoadImage`、`TextInput_`、`Qwen3_VQA`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
