---
key: 图片生成/图生图/脸部加强！NUCHAKU-Flux Kontext Dev 8步极速优化版服务端_1940326991549874177.json
name: 脸部加强！NUCHAKU-Flux Kontext Dev 8步极速优化版服务端_1940326991549874177
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/脸部加强！NUCHAKU-Flux Kontext Dev 8步极速优化版服务端_1940326991549874177.json
hash: 30848f291623e971
coverage: 0.722222
learned_at: 2026-10-23 13:23:43
nodes: [ConditioningZeroOut, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, VAEEncode, MarkdownNote, Image Rembg (Remove Background), Image Rembg (Remove Background), MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, ImageStitch, MarkdownNote, DeepTranslatorTextNode, FluxKontextImageScale, CLIPTextEncode, ReferenceLatent, KSampler, VAEDecode, PreviewImage, LoadImage, Int, LoadImage, JjkText, RepeatLatentBatch, Int, Image Comparer (rgthree), easy seed, FluxGuidance, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, VAELoader, NunchakuFluxLoraLoader, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 92647358383638, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/脸部加强！NUCHAKU-Flux Kontext Dev 8步极速优化版服务端_1940326991549874177.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/脸部加强！NUCHAKU-Flux Kontext Dev 8步极速优化版服务端_1940326991549874177.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `ConditioningZeroOut`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `VAEEncode` ★核心
- `MarkdownNote`
- `Image Rembg (Remove Background)`
- `Image Rembg (Remove Background)`
- `MarkdownNote`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageStitch`
- `MarkdownNote`
- `DeepTranslatorTextNode`
- `FluxKontextImageScale`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `LoadImage`
- `Int`
- `LoadImage`
- `JjkText`
- `RepeatLatentBatch`
- `Int`
- `Image Comparer (rgthree)`
- `easy seed`
- `FluxGuidance`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuTextEncoderLoader`
- `VAELoader`
- `NunchakuFluxLoraLoader` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `92647358383638`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **72%**（26/36）

**有卡**：`ConditioningZeroOut`、`VAEEncode`、`Image Rembg (Remove Background)`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageStitch`、`DeepTranslatorTextNode`、`FluxKontextImageScale`、`CLIPTextEncode`、`ReferenceLatent`、`KSampler`、`VAEDecode`、`LoadImage`、`Int`、`RepeatLatentBatch`、`easy seed`、`FluxGuidance`、`NunchakuFluxDiTLoader`、`NunchakuFluxLoraLoader`、`NunchakuTextEncoderLoader`、`VAELoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、easy seed

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
