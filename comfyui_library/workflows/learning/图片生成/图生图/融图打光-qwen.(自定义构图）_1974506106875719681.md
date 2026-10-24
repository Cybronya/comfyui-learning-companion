---
key: 图片生成/图生图/融图打光-qwen.(自定义构图）_1974506106875719681.json
name: 融图打光-qwen.(自定义构图）_1974506106875719681
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/融图打光-qwen.(自定义构图）_1974506106875719681.json
hash: 3ecfa100282b2b8f
coverage: 0.808511
learned_at: 2026-10-23 13:25:14
nodes: [PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, FastCanvasTool, LayerUtility: ImageScaleByAspectRatio V2, TextEncodeQwenImageEditEnhanced, CLIPLoader, Text Multiline, VAELoader, VAEEncode, TextEncodeQwenImageEditEnhanced, ImageCrop, LayerMask: MaskGrow, VAEDecode, CFGNorm, ModelSamplingAuraFlow, SetLatentNoiseMask, UNETLoader, PreviewImage, SaveImage, LoraLoaderModelOnly, KSampler, LoraLoaderModelOnly, ImageResize+, Image Comparer (rgthree), DetailTransfer, BiRefNetRMBG, EmptyImage, Image Blank, MathExpression|pysssss, easy imageConcat, easy imageConcat, Image To Mask, LoadImage, LoadImage, RMBG, LayerUtility: CropByMask V2, RMBG, LoadImage, RMBG, LayerUtility: CropByMask V2, RMBG, FastCanvas, MarkdownNote]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 508308925227756, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/融图打光-qwen.(自定义构图）_1974506106875719681.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/融图打光-qwen.(自定义构图）_1974506106875719681.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `FastCanvasTool`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextEncodeQwenImageEditEnhanced`
- `CLIPLoader`
- `Text Multiline`
- `VAELoader`
- `VAEEncode` ★核心
- `TextEncodeQwenImageEditEnhanced`
- `ImageCrop`
- `LayerMask: MaskGrow`
- `VAEDecode` ★核心
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `SetLatentNoiseMask`
- `UNETLoader` ★核心
- `PreviewImage`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageResize+`
- `Image Comparer (rgthree)`
- `DetailTransfer`
- `BiRefNetRMBG`
- `EmptyImage`
- `Image Blank`
- `MathExpression|pysssss`
- `easy imageConcat`
- `easy imageConcat`
- `Image To Mask`
- `LoadImage`
- `LoadImage`
- `RMBG`
- `LayerUtility: CropByMask V2`
- `RMBG`
- `LoadImage`
- `RMBG`
- `LayerUtility: CropByMask V2`
- `RMBG`
- `FastCanvas`
- `MarkdownNote`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `508308925227756`
- `steps` = `8`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **81%**（38/47）

**有卡**：`FastCanvasTool`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImageEditEnhanced`、`CLIPLoader`、`Text Multiline`、`VAELoader`、`VAEEncode`、`ImageCrop`、`LayerMask: MaskGrow`、`VAEDecode`、`CFGNorm`、`ModelSamplingAuraFlow`、`SetLatentNoiseMask`、`UNETLoader`、`SaveImage`、`LoraLoaderModelOnly`、`KSampler`、`ImageResize+`、`DetailTransfer`、`BiRefNetRMBG`、`EmptyImage`、`Image Blank`、`MathExpression|pysssss`、`easy imageConcat`、`Image To Mask`、`LoadImage`、`RMBG`、`LayerUtility: CropByMask V2`、`FastCanvas`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
