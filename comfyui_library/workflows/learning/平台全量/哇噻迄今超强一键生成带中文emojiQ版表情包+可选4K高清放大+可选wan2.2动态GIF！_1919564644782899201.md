---
key: 平台全量/哇噻迄今超强一键生成带中文emojiQ版表情包+可选4K高清放大+可选wan2.2动态GIF！_1919564644782899201.json
name: 哇噻迄今超强一键生成带中文emojiQ版表情包+可选4K高清放大+可选wan2.2动态GIF！_1919564644782899201
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/哇噻迄今超强一键生成带中文emojiQ版表情包+可选4K高清放大+可选wan2.2动态GIF！_1919564644782899201.json
hash: 7748d8922c5a7a4d
coverage: 0.745763
learned_at: 2026-11-14 01:52:01
nodes: [DifferentialDiffusion, easy cleanGpuUsed, LayerUtility: PurgeVRAM, FluxGuidance, RepeatLatentBatch, Mute / Bypass Repeater (rgthree), ConditioningZeroOut, Note, Note, ImageUpscaleWithModel, easy imageScaleDownToSize, VAEDecode, PreviewImage, ImageCrop+, VAEEncode, Reroute, easy clearCacheAll, easy cleanGpuUsed, FluxGuidance, StyleModelApply, CLIPTextEncode, KSampler, CLIPVisionEncode, Reroute, PreviewImage, PreviewImage, easy imageSize, SolidMask, easy makeImageForICLora, PreviewImage, LayerMask: MaskPreview, ConditioningZeroOut, Note, InpaintModelConditioning, Image Comparer (rgthree), Note, easy imageSize, Note, Note, KSampler (Efficient), LoadImage, VAELoader, Anything Everywhere3, LoraLoaderModelOnly, ImageScaleBy, CLIPVisionLoader, StyleModelLoader, UpscaleModelLoader, DualCLIPLoaderGGUF, UNETLoader, DualCLIPLoader, UNETLoader, DualCLIPLoader, LoraLoaderModelOnly, Note, CLIPTextEncode, VAEDecode, SaveImage, LoraLoaderModelOnly]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 59053874728107, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/哇噻迄今超强一键生成带中文emojiQ版表情包+可选4K高清放大+可选wan2.2动态GIF！_1919564644782899201.json

> 来源文件 `comfyui_library/workflows/平台全量/哇噻迄今超强一键生成带中文emojiQ版表情包+可选4K高清放大+可选wan2.2动态GIF！_1919564644782899201.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `DifferentialDiffusion`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM`
- `FluxGuidance`
- `RepeatLatentBatch`
- `Mute / Bypass Repeater (rgthree)`
- `ConditioningZeroOut`
- `Note`
- `Note`
- `ImageUpscaleWithModel`
- `easy imageScaleDownToSize`
- `VAEDecode` ★核心
- `PreviewImage`
- `ImageCrop+`
- `VAEEncode` ★核心
- `Reroute`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `FluxGuidance`
- `StyleModelApply`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CLIPVisionEncode`
- `Reroute`
- `PreviewImage`
- `PreviewImage`
- `easy imageSize`
- `SolidMask`
- `easy makeImageForICLora`
- `PreviewImage`
- `LayerMask: MaskPreview`
- `ConditioningZeroOut`
- `Note`
- `InpaintModelConditioning`
- `Image Comparer (rgthree)`
- `Note`
- `easy imageSize`
- `Note`
- `Note`
- `KSampler (Efficient)` ★核心
- `LoadImage`
- `VAELoader`
- `Anything Everywhere3`
- `LoraLoaderModelOnly` ★核心
- `ImageScaleBy`
- `CLIPVisionLoader`
- `StyleModelLoader`
- `UpscaleModelLoader`
- `DualCLIPLoaderGGUF`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `59053874728107`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **75%**（44/59）

**有卡**：`DifferentialDiffusion`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM`、`FluxGuidance`、`RepeatLatentBatch`、`Mute / Bypass Repeater (rgthree)`、`ConditioningZeroOut`、`ImageUpscaleWithModel`、`easy imageScaleDownToSize`、`VAEDecode`、`ImageCrop+`、`VAEEncode`、`easy clearCacheAll`、`StyleModelApply`、`CLIPTextEncode`、`KSampler`、`CLIPVisionEncode`、`easy imageSize`、`SolidMask`、`easy makeImageForICLora`、`LayerMask: MaskPreview`、`InpaintModelConditioning`、`KSampler (Efficient)`、`LoadImage`、`VAELoader`、`LoraLoaderModelOnly`、`ImageScaleBy`、`CLIPVisionLoader`、`StyleModelLoader`、`UpscaleModelLoader`、`DualCLIPLoaderGGUF`、`UNETLoader`、`DualCLIPLoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
