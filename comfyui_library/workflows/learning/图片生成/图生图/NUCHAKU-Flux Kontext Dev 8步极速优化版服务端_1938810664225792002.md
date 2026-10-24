---
key: 图片生成/图生图/NUCHAKU-Flux Kontext Dev 8步极速优化版服务端_1938810664225792002.json
name: NUCHAKU-Flux Kontext Dev 8步极速优化版服务端_1938810664225792002
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/NUCHAKU-Flux Kontext Dev 8步极速优化版服务端_1938810664225792002.json
hash: cab36d9fac98f641
coverage: 0.694444
learned_at: 2026-10-23 11:09:46
nodes: [ConditioningZeroOut, FluxGuidance, ReferenceLatent, UNETLoader, VAELoader, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, CLIPTextEncode, VAEEncode, VAEDecode, MarkdownNote, MarkdownNote, Image Rembg (Remove Background), Image Rembg (Remove Background), MarkdownNote, LoadImage, EmptySD3LatentImage, DeepTranslatorTextNode, PreviewImage, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, FluxKontextImageScale, ImageStitch, easy seed, LoadImage, DualCLIPLoader, Int, JjkText, JjkText, NunchakuFluxDiTLoader, KSampler, NunchakuFluxLoraLoader, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 518679982266954, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/NUCHAKU-Flux Kontext Dev 8步极速优化版服务端_1938810664225792002.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/NUCHAKU-Flux Kontext Dev 8步极速优化版服务端_1938810664225792002.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `ConditioningZeroOut`
- `FluxGuidance`
- `ReferenceLatent`
- `UNETLoader` ★核心
- `VAELoader`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `Image Rembg (Remove Background)`
- `Image Rembg (Remove Background)`
- `MarkdownNote`
- `LoadImage`
- `EmptySD3LatentImage`
- `DeepTranslatorTextNode`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FluxKontextImageScale`
- `ImageStitch`
- `easy seed`
- `LoadImage`
- `DualCLIPLoader`
- `Int`
- `JjkText`
- `JjkText`
- `NunchakuFluxDiTLoader`
- `KSampler` ★核心
- `NunchakuFluxLoraLoader` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `518679982266954`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **69%**（25/36）

**有卡**：`ConditioningZeroOut`、`FluxGuidance`、`ReferenceLatent`、`UNETLoader`、`VAELoader`、`CLIPTextEncode`、`VAEEncode`、`VAEDecode`、`Image Rembg (Remove Background)`、`LoadImage`、`EmptySD3LatentImage`、`DeepTranslatorTextNode`、`LayerUtility: ImageScaleByAspectRatio V2`、`FluxKontextImageScale`、`ImageStitch`、`easy seed`、`DualCLIPLoader`、`Int`、`NunchakuFluxDiTLoader`、`KSampler`、`NunchakuFluxLoraLoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
