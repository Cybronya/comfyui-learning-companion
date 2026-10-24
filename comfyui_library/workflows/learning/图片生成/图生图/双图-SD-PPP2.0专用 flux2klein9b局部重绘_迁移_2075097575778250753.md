---
key: 图片生成/图生图/双图-SD-PPP2.0专用 flux2klein9b局部重绘_迁移_2075097575778250753.json
name: 双图-SD-PPP2.0专用 flux2klein9b局部重绘_迁移_2075097575778250753
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/双图-SD-PPP2.0专用 flux2klein9b局部重绘_迁移_2075097575778250753.json
hash: 0efb27b03e6e69ce
coverage: 0.916667
learned_at: 2026-10-23 12:34:59
nodes: [Text Multiline, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Int, VAELoader, GrowMaskWithBlur, VAEEncode, ReferenceLatent, UNETLoader, ConditioningZeroOut, KSampler, VAEDecode, SaveImage, Image Comparer (rgthree), ReferenceLatent, CLIPTextEncode, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, MaskFillHoles, Kontext Inpainting Conditioning, RMBG, PreviewImage, CLIPLoader, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 410613308124534, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/双图-SD-PPP2.0专用 flux2klein9b局部重绘_迁移_2075097575778250753.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/双图-SD-PPP2.0专用 flux2klein9b局部重绘_迁移_2075097575778250753.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `Text Multiline`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Int`
- `VAELoader`
- `GrowMaskWithBlur`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MaskFillHoles`
- `Kontext Inpainting Conditioning`
- `RMBG`
- `PreviewImage`
- `CLIPLoader`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `410613308124534`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（22/24）

**有卡**：`Text Multiline`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`Int`、`VAELoader`、`GrowMaskWithBlur`、`VAEEncode`、`ReferenceLatent`、`UNETLoader`、`ConditioningZeroOut`、`KSampler`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`MaskFillHoles`、`Kontext Inpainting Conditioning`、`RMBG`、`CLIPLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
