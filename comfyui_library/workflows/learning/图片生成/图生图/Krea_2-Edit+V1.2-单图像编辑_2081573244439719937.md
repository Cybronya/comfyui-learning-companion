---
key: 图片生成/图生图/Krea_2-Edit+V1.2-单图像编辑_2081573244439719937.json
name: Krea_2-Edit+V1.2-单图像编辑_2081573244439719937
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Krea_2-Edit+V1.2-单图像编辑_2081573244439719937.json
hash: 298dc340f082ed62
coverage: 0.851852
learned_at: 2026-10-23 11:08:31
nodes: [UNETLoader, CLIPLoader, VAELoader, KSampler, Krea2EditGroundedEncode, Krea2EditGroundedEncode, LoraLoaderModelOnly, Krea2EditModelPatch, TextInput_, Fast Groups Bypasser (rgthree), ImageBlur, MaskPreview+, ImageToMask, VAEEncode, EmptySD3LatentImage, MaskToImage, GrowMask, SaveImage, SaveImage, ImageCompositeMasked, Image Comparer (rgthree), Image Comparer (rgthree), VAEDecode, PreviewImage, LoadImageMask, LayerUtility: ImageScaleByAspectRatio V2, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 866963243136008, "steps": 10}
---

# 图片生成/图生图/Krea_2-Edit+V1.2-单图像编辑_2081573244439719937.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Krea_2-Edit+V1.2-单图像编辑_2081573244439719937.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `Krea2EditGroundedEncode`
- `Krea2EditGroundedEncode`
- `LoraLoaderModelOnly` ★核心
- `Krea2EditModelPatch`
- `TextInput_`
- `Fast Groups Bypasser (rgthree)`
- `ImageBlur`
- `MaskPreview+`
- `ImageToMask`
- `VAEEncode` ★核心
- `EmptySD3LatentImage`
- `MaskToImage`
- `GrowMask`
- `SaveImage`
- `SaveImage`
- `ImageCompositeMasked`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `PreviewImage`
- `LoadImageMask`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `866963243136008`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（23/27）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`Krea2EditGroundedEncode`、`LoraLoaderModelOnly`、`Krea2EditModelPatch`、`TextInput_`、`ImageBlur`、`MaskPreview+`、`ImageToMask`、`VAEEncode`、`EmptySD3LatentImage`、`MaskToImage`、`GrowMask`、`SaveImage`、`ImageCompositeMasked`、`VAEDecode`、`LoadImageMask`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、VAEEncode
