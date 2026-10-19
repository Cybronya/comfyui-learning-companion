---
key: 图片生成/文生图/qwen3VL反推+Z-Image生图+SeedVR2.5高清修复，电影场景_写实肖像_动漫角色_1995712593509617666.json
name: qwen3VL反推+Z-Image生图+SeedVR2.5高清修复，电影场景_写实肖像_动漫角色_1995712593509617666
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen3VL反推+Z-Image生图+SeedVR2.5高清修复，电影场景_写实肖像_动漫角色_1995712593509617666.json
hash: 84110020330b9142
coverage: 0.675676
learned_at: 2026-10-19 21:33:14
nodes: [CLIPLoader, easy showAnything, easy showAnything, LayerUtility: PurgeVRAM V2, ImageScaleToTotalPixels, easy ifElse, CLIPTextEncode, ConditioningZeroOut, LayerUtility: PurgeVRAM V2, ImageScaleToTotalPixels, Image Comparer (rgthree), SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, Text Multiline, KSampler, UNETLoader, MaraScottIsEmptyOrNone_v1, Anything Everywhere, Fast Groups Bypasser (rgthree), Int, Note, VAEDecode, easy ifElse, EmptyLatentImage, PreviewAny, Int, Int, Note, easy ifElse, PreviewAny, VAELoader, PrimitiveBoolean, SeedVR2VideoUpscaler, SaveImage, LayerUtility: PurgeVRAM V2, AILab_QwenVL, ImageLoader]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1060167827728077, "steps": 10, "width": 544}
---

# 图片生成/文生图/qwen3VL反推+Z-Image生图+SeedVR2.5高清修复，电影场景_写实肖像_动漫角色_1995712593509617666.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen3VL反推+Z-Image生图+SeedVR2.5高清修复，电影场景_写实肖像_动漫角色_1995712593509617666.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `CLIPLoader`
- `easy showAnything`
- `easy showAnything`
- `LayerUtility: PurgeVRAM V2`
- `ImageScaleToTotalPixels`
- `easy ifElse`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `LayerUtility: PurgeVRAM V2`
- `ImageScaleToTotalPixels`
- `Image Comparer (rgthree)`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `Text Multiline`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `MaraScottIsEmptyOrNone_v1`
- `Anything Everywhere`
- `Fast Groups Bypasser (rgthree)`
- `Int`
- `Note`
- `VAEDecode` ★核心
- `easy ifElse`
- `EmptyLatentImage` ★核心
- `PreviewAny`
- `Int`
- `Int`
- `Note`
- `easy ifElse`
- `PreviewAny`
- `VAELoader`
- `PrimitiveBoolean`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `LayerUtility: PurgeVRAM V2`
- `AILab_QwenVL`
- `ImageLoader`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `1060167827728077`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `544`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **68%**（25/37）

**有卡**：`CLIPLoader`、`LayerUtility: PurgeVRAM V2`、`ImageScaleToTotalPixels`、`CLIPTextEncode`、`ConditioningZeroOut`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`Text Multiline`、`KSampler`、`UNETLoader`、`MaraScottIsEmptyOrNone_v1`、`Int`、`VAEDecode`、`EmptyLatentImage`、`VAELoader`、`PrimitiveBoolean`、`SeedVR2VideoUpscaler`、`SaveImage`、`AILab_QwenVL`、`ImageLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader
