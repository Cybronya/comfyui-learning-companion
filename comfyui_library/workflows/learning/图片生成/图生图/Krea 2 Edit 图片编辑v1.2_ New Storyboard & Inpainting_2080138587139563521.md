---
key: 图片生成/图生图/Krea 2 Edit 图片编辑v1.2_ New Storyboard & Inpainting_2080138587139563521.json
name: Krea 2 Edit 图片编辑v1.2_ New Storyboard & Inpainting_2080138587139563521
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Krea 2 Edit 图片编辑v1.2_ New Storyboard & Inpainting_2080138587139563521.json
hash: 2b672cefbfcbd9ff
coverage: 0.866667
learned_at: 2026-10-23 11:07:34
nodes: [Krea2EditGroundedEncode, KSampler, Note, ImageScaleBy, VAEEncode, GrowMask, ImageToMask, ImageBlur, MaskToImage, MaskPreview+, ResizeImageMaskNode, PreviewImage, Fast Groups Bypasser (rgthree), Krea2EditModelPatch, GetImageSize, ImageCompositeMasked, VAEDecode, ResizeImageMaskNode, VAELoader, VAELoader, Image Comparer (rgthree), SaveImage, EmptySD3LatentImage, CLIPLoader, LoraLoaderModelOnly, UNETLoader, SaveImage, LoadImage, TextInput_, Krea2EditGroundedEncode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 759645231847319, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Krea 2 Edit 图片编辑v1.2_ New Storyboard & Inpainting_2080138587139563521.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Krea 2 Edit 图片编辑v1.2_ New Storyboard & Inpainting_2080138587139563521.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `Krea2EditGroundedEncode`
- `KSampler` ★核心
- `Note`
- `ImageScaleBy`
- `VAEEncode` ★核心
- `GrowMask`
- `ImageToMask`
- `ImageBlur`
- `MaskToImage`
- `MaskPreview+`
- `ResizeImageMaskNode`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `Krea2EditModelPatch`
- `GetImageSize`
- `ImageCompositeMasked`
- `VAEDecode` ★核心
- `ResizeImageMaskNode`
- `VAELoader`
- `VAELoader`
- `Image Comparer (rgthree)`
- `SaveImage`
- `EmptySD3LatentImage`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `LoadImage`
- `TextInput_`
- `Krea2EditGroundedEncode`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `759645231847319`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（26/30）

**有卡**：`Krea2EditGroundedEncode`、`KSampler`、`ImageScaleBy`、`VAEEncode`、`GrowMask`、`ImageToMask`、`ImageBlur`、`MaskToImage`、`MaskPreview+`、`ResizeImageMaskNode`、`Krea2EditModelPatch`、`GetImageSize`、`ImageCompositeMasked`、`VAEDecode`、`VAELoader`、`SaveImage`、`EmptySD3LatentImage`、`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`LoadImage`、`TextInput_`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、VAEEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
