---
key: 图片生成/图生图/image2.5噪点色斑处理放大 图片修复增强方案_2110356753979371521.json
name: image2.5噪点色斑处理放大 图片修复增强方案_2110356753979371521
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/image2.5噪点色斑处理放大 图片修复增强方案_2110356753979371521.json
hash: 2cc662fe9933059c
coverage: 0.815385
learned_at: 2026-10-23 11:37:45
nodes: [ImageScaleToMaxDimension, VAEEncode, RepeatLatentBatch, Florence2Run, easy ifElse, TextConcatenator, CLIPTextEncode, ConditioningZeroOut, VAEDecode, UNETLoader, VAELoader, SeedVR2Preprocess, VAEEncodeTiled, SeedVR2Conditioning, VAEDecodeTiled, SeedVR2PostProcessing, SaveImage, TextConcatenator, PreviewTextNode, VAELoader, UNETLoader, ModelSamplingAuraFlow, ImageScaleToMaxDimension, LoadImage, Florence2ModelLoader, KSampler, PrimitiveNode, CLIPLoader, PrimitiveNode, PrimitiveNode, Image Comparer (rgthree), KSampler, PrimitiveNode, PrimitiveNode, SaveImage, PrimitiveNode, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/image2.5噪点色斑处理放大 图片修复增强方案_2110356753979371521.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/image2.5噪点色斑处理放大 图片修复增强方案_2110356753979371521.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（65 个）：
- `ImageScaleToMaxDimension`
- `VAEEncode` ★核心
- `RepeatLatentBatch`
- `Florence2Run`
- `easy ifElse`
- `TextConcatenator`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `SeedVR2Preprocess`
- `VAEEncodeTiled` ★核心
- `SeedVR2Conditioning`
- `VAEDecodeTiled` ★核心
- `SeedVR2PostProcessing`
- `SaveImage`
- `TextConcatenator`
- `PreviewTextNode`
- `VAELoader`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `ImageScaleToMaxDimension`
- `LoadImage`
- `Florence2ModelLoader`
- `KSampler` ★核心
- `PrimitiveNode`
- `CLIPLoader`
- `PrimitiveNode`
- `PrimitiveNode`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `PrimitiveNode`
- `PrimitiveNode`
- `SaveImage`
- `PrimitiveNode`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
- `Note`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（53/65）

**有卡**：`ImageScaleToMaxDimension`、`VAEEncode`、`RepeatLatentBatch`、`Florence2Run`、`TextConcatenator`、`CLIPTextEncode`、`ConditioningZeroOut`、`VAEDecode`、`UNETLoader`、`VAELoader`、`SeedVR2Preprocess`、`VAEEncodeTiled`、`SeedVR2Conditioning`、`VAEDecodeTiled`、`SeedVR2PostProcessing`、`SaveImage`、`PreviewTextNode`、`ModelSamplingAuraFlow`、`LoadImage`、`Florence2ModelLoader`、`KSampler`、`CLIPLoader`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
