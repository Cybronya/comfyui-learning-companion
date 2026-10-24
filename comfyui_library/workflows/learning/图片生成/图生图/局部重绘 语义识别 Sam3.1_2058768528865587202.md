---
key: 图片生成/图生图/局部重绘 语义识别 Sam3.1_2058768528865587202.json
name: 局部重绘 语义识别 Sam3.1_2058768528865587202
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/局部重绘 语义识别 Sam3.1_2058768528865587202.json
hash: 0b8137bbf2c3290e
coverage: 0.862069
learned_at: 2026-10-23 12:49:48
nodes: [VAEDecode, VAELoader, UNETLoader, CLIPLoader, KSampler, LayerUtility: PurgeVRAM V2, PreviewImage, CLIPTextEncode, PreviewAny, PreviewAny, LoadImage, Text, Text, VAEEncode, RH_Translator, CLIPTextEncode, ReferenceLatent, ConditioningZeroOut, ReferenceLatent, CheckpointLoaderSimple, RH_Translator, SAM3_Detect, INPAINT_ExpandMask, ImageAndMaskPreview, ImageCompositeMasked, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, SaveImage, InpaintModelConditioning]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "sam3.1_multiplex_fp16.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 426629463107977, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/局部重绘 语义识别 Sam3.1_2058768528865587202.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/局部重绘 语义识别 Sam3.1_2058768528865587202.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `VAEDecode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `PreviewAny`
- `LoadImage`
- `Text`
- `Text`
- `VAEEncode` ★核心
- `RH_Translator`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `CheckpointLoaderSimple` ★核心
- `RH_Translator`
- `SAM3_Detect`
- `INPAINT_ExpandMask`
- `ImageAndMaskPreview`
- `ImageCompositeMasked`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `InpaintModelConditioning`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `426629463107977`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **86%**（25/29）

**有卡**：`VAEDecode`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`KSampler`、`LayerUtility: PurgeVRAM V2`、`CLIPTextEncode`、`LoadImage`、`Text`、`VAEEncode`、`RH_Translator`、`ReferenceLatent`、`ConditioningZeroOut`、`CheckpointLoaderSimple`、`SAM3_Detect`、`INPAINT_ExpandMask`、`ImageAndMaskPreview`、`ImageCompositeMasked`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`InpaintModelConditioning`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
