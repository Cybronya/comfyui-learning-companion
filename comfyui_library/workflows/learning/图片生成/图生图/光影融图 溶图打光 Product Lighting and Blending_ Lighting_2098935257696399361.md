---
key: 图片生成/图生图/光影融图 溶图打光 Product Lighting and Blending_ Lighting_2098935257696399361.json
name: 光影融图 溶图打光 Product Lighting and Blending_ Lighting_2098935257696399361
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/光影融图 溶图打光 Product Lighting and Blending_ Lighting_2098935257696399361.json
hash: 0f87ce402ad1d7f8
coverage: 0.8
learned_at: 2026-10-21 00:48:10
nodes: [SeedVR2BlockSwap, easy cleanGpuUsed, ConditioningZeroOut, ConditioningZeroOut, KSampler, VAELoader, CLIPLoader, UNETLoader, VAEDecode, SaveImage, easy cleanGpuUsed, ImageResize+, FluxKontextMultiReferenceLatentMethod, Anything Everywhere, SeedVR2, ShowText|pysssss, VAELoader, LoraLoaderModelOnly, UNETLoader, TextEncodeQwenImageEditPlusPro_lrzjason, VAEEncode, CLIPTextEncode, ReferenceLatent, VAEDecode, ColorMatch, ImageResize+, KSampler, Image Comparer (rgthree), Qwen3VL_Chat, CR Text Concatenate, CR Text Concatenate, JjkText, JjkText, CLIPLoader, SaveImage, LoadImage, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, Note, Image Comparer (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 281984656592210, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/光影融图 溶图打光 Product Lighting and Blending_ Lighting_2098935257696399361.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/光影融图 溶图打光 Product Lighting and Blending_ Lighting_2098935257696399361.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `SeedVR2BlockSwap`
- `easy cleanGpuUsed`
- `ConditioningZeroOut`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `easy cleanGpuUsed`
- `ImageResize+`
- `FluxKontextMultiReferenceLatentMethod`
- `Anything Everywhere`
- `SeedVR2`
- `ShowText|pysssss`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `TextEncodeQwenImageEditPlusPro_lrzjason`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `VAEDecode` ★核心
- `ColorMatch`
- `ImageResize+`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `Qwen3VL_Chat`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `JjkText`
- `JjkText`
- `CLIPLoader`
- `SaveImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Image Comparer (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `281984656592210`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（32/40）

**有卡**：`SeedVR2BlockSwap`、`easy cleanGpuUsed`、`ConditioningZeroOut`、`KSampler`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`VAEDecode`、`SaveImage`、`ImageResize+`、`FluxKontextMultiReferenceLatentMethod`、`SeedVR2`、`LoraLoaderModelOnly`、`TextEncodeQwenImageEditPlusPro_lrzjason`、`VAEEncode`、`CLIPTextEncode`、`ReferenceLatent`、`ColorMatch`、`Qwen3VL_Chat`、`CR Text Concatenate`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
