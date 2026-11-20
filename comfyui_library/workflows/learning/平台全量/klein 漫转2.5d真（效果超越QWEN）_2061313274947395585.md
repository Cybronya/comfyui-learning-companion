---
key: 平台全量/klein 漫转2.5d真（效果超越QWEN）_2061313274947395585.json
name: klein 漫转2.5d真（效果超越QWEN）_2061313274947395585
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/klein 漫转2.5d真（效果超越QWEN）_2061313274947395585.json
hash: a6ada4e81d5af85a
coverage: 0.831325
learned_at: 2026-11-14 01:13:03
nodes: [CFGGuider, RandomNoise, VAELoader, CLIPTextEncode, CLIPTextEncode, VAEDecode, VAEEncode, MathExpression|pysssss, MathExpression|pysssss, PrimitiveFloat, GetImageSize+, Seed (rgthree), CLIPTextEncode, ConditioningZeroOut, VAELoader, PrimitiveFloat, ReferenceLatent, ReferenceLatent, ConditioningZeroOut, VAEEncode, Textbox, EmptyFlux2LatentImage, KSamplerSelect, SamplerCustomAdvanced, GetImageSize, Flux2Scheduler, ImageScaleToTotalPixels, Text Concatenate, Textbox, ImageResizeKJv2, CLIPTextEncode, Textbox, KSampler, easy imageColorMatch, Reroute, Reroute, VAEDecode, Reroute, SaveImage, Image Comparer (rgthree), CLIPLoader, VAELoader, ImageUpscaleWithModel, ImageScale, UpscaleModelLoader, Seed (rgthree), CLIPLoaderGGUF, UpscaleModelLoader, MathExpression|pysssss, MathExpression|pysssss, SaveImage, UltimateSDUpscale, Image Comparer (rgthree), MarkdownNote, GetImageSize, Note, LayerUtility: ImageReelComposit, easy imageColorMatch, LayerUtility: ImageReel, Reroute, ColorMatchV2, SaveImage, PrimitiveStringMultiline, Image Comparer (rgthree), PreviewImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, MarkdownNote, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, CLIPLoader, WD14Tagger|pysssss, UNETLoader, UNETLoader, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.15, "sampler_name": "euler", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 258952074027197, "steps": 5}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/klein 漫转2.5d真（效果超越QWEN）_2061313274947395585.json

> 来源文件 `comfyui_library/workflows/平台全量/klein 漫转2.5d真（效果超越QWEN）_2061313274947395585.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（83 个）：
- `CFGGuider`
- `RandomNoise`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `PrimitiveFloat`
- `GetImageSize+`
- `Seed (rgthree)`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAELoader`
- `PrimitiveFloat`
- `ReferenceLatent`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `Textbox`
- `EmptyFlux2LatentImage`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `GetImageSize`
- `Flux2Scheduler`
- `ImageScaleToTotalPixels`
- `Text Concatenate`
- `Textbox`
- `ImageResizeKJv2`
- `CLIPTextEncode` ★核心
- `Textbox`
- `KSampler` ★核心
- `easy imageColorMatch`
- `Reroute`
- `Reroute`
- `VAEDecode` ★核心
- `Reroute`
- `SaveImage`
- `Image Comparer (rgthree)`
- `CLIPLoader`
- `VAELoader`
- `ImageUpscaleWithModel`
- `ImageScale`
- `UpscaleModelLoader`
- `Seed (rgthree)`
- `CLIPLoaderGGUF`
- `UpscaleModelLoader`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `SaveImage`
- `UltimateSDUpscale`
- `Image Comparer (rgthree)`
- `MarkdownNote`
- `GetImageSize`
- `Note`
- `LayerUtility: ImageReelComposit`
- `easy imageColorMatch`
- `LayerUtility: ImageReel`
- `Reroute`
- `ColorMatchV2`
- `SaveImage`
- `PrimitiveStringMultiline`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `WD14Tagger|pysssss`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `258952074027197`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `0.15`

## 知识

覆盖率 **83%**（69/83）

**有卡**：`CFGGuider`、`RandomNoise`、`VAELoader`、`CLIPTextEncode`、`VAEDecode`、`VAEEncode`、`MathExpression|pysssss`、`GetImageSize+`、`Seed (rgthree)`、`ConditioningZeroOut`、`ReferenceLatent`、`Textbox`、`EmptyFlux2LatentImage`、`KSamplerSelect`、`SamplerCustomAdvanced`、`GetImageSize`、`Flux2Scheduler`、`ImageScaleToTotalPixels`、`Text Concatenate`、`ImageResizeKJv2`、`KSampler`、`easy imageColorMatch`、`SaveImage`、`CLIPLoader`、`ImageUpscaleWithModel`、`ImageScale`、`UpscaleModelLoader`、`CLIPLoaderGGUF`、`UltimateSDUpscale`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`ColorMatchV2`、`LoraLoaderModelOnly`、`UNETLoader`、`WD14Tagger|pysssss`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
