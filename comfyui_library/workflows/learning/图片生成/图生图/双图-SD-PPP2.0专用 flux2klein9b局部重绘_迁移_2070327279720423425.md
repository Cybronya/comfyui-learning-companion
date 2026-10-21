---
key: 图片生成/图生图/双图-SD-PPP2.0专用 flux2klein9b局部重绘_迁移_2070327279720423425.json
name: 双图-SD-PPP2.0专用 flux2klein9b局部重绘_迁移_2070327279720423425
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/双图-SD-PPP2.0专用 flux2klein9b局部重绘_迁移_2070327279720423425.json
hash: 52e2d59baea676df
coverage: 0.925
learned_at: 2026-10-21 00:50:56
nodes: [CLIPLoader, VAEEncode, VAELoader, CLIPTextEncode, ReferenceLatent, ReferenceLatent, LoadImage, Int, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, ConditioningZeroOut, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, KSampler, Image Comparer (rgthree), Kontext Inpainting Conditioning, Text Multiline, SaveImage, VAEDecode, PreviewImage, LoadImage, RMBG, GrowMaskWithBlur, MaskFillHoles, VAEEncode, CLIPLoader, VAELoader, UNETLoader, CLIPTextEncode, Text Multiline, KSampler, SaveImage, ConditioningZeroOut, ReferenceLatent, Kontext Inpainting Conditioning, VAEDecode, LoadImage, Int, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 822089962346403, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/双图-SD-PPP2.0专用 flux2klein9b局部重绘_迁移_2070327279720423425.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/双图-SD-PPP2.0专用 flux2klein9b局部重绘_迁移_2070327279720423425.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `CLIPLoader`
- `VAEEncode` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `LoadImage`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `Kontext Inpainting Conditioning`
- `Text Multiline`
- `SaveImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `LoadImage`
- `RMBG`
- `GrowMaskWithBlur`
- `MaskFillHoles`
- `VAEEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `Text Multiline`
- `KSampler` ★核心
- `SaveImage`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `Kontext Inpainting Conditioning`
- `VAEDecode` ★核心
- `LoadImage`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `822089962346403`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（37/40）

**有卡**：`CLIPLoader`、`VAEEncode`、`VAELoader`、`CLIPTextEncode`、`ReferenceLatent`、`LoadImage`、`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`ConditioningZeroOut`、`UNETLoader`、`KSampler`、`Kontext Inpainting Conditioning`、`Text Multiline`、`SaveImage`、`VAEDecode`、`RMBG`、`GrowMaskWithBlur`、`MaskFillHoles`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
