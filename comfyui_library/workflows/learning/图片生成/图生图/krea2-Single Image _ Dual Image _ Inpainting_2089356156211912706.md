---
key: 图片生成/图生图/krea2-Single Image _ Dual Image _ Inpainting_2089356156211912706.json
name: krea2-Single Image _ Dual Image _ Inpainting_2089356156211912706
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/krea2-Single Image _ Dual Image _ Inpainting_2089356156211912706.json
hash: 9994e8a8b1fe9418
coverage: 0.84127
learned_at: 2026-10-15 22:25:34
nodes: [Krea2EditGroundedEncode, EmptySD3LatentImage, Krea2EditModelPatch, Krea2EditGroundedEncode, CLIPLoader, VAELoader, VAEEncode, VAEEncode, CLIPLoader, VAELoader, KSampler, VAEDecode, SaveImage, Seed (rgthree), VAEDecode, VAEEncode, Krea2EditGroundedEncode, EmptySD3LatentImage, VAELoader, Krea2EditModelPatch, Krea2EditGroundedEncode, GetImageSize+, CLIPLoader, Seed (rgthree), DrawMaskOnImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, ImageScaleToTotalPixels, LoadImage, ResolutionSelector, PrimitiveStringMultiline, Seed (rgthree), VAEEncode, Krea2EditGroundedEncode, Krea2EditGroundedEncode, LoadImage, ImageScaleToTotalPixels, GetImageSize+, EmptySD3LatentImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PrimitiveStringMultiline, UNETLoader, Note, UNETLoader, UNETLoader, UNETLoader, LoadImage, PreviewImage, KSampler, SaveImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Note, Note, KSampler, VAEDecode, Krea2EditModelPatch, SaveImage, PrimitiveStringMultiline]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 478172831101520, "steps": 10}
---

# 图片生成/图生图/krea2-Single Image _ Dual Image _ Inpainting_2089356156211912706.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/krea2-Single Image _ Dual Image _ Inpainting_2089356156211912706.json`

## 结构

**生成流程**：Model → Encode → Latent → Sampling → Decode → Process → Output → Other

**节点**（63 个）：
- `Krea2EditGroundedEncode`
- `EmptySD3LatentImage`
- `Krea2EditModelPatch`
- `Krea2EditGroundedEncode`
- `CLIPLoader`
- `VAELoader`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Seed (rgthree)`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `Krea2EditGroundedEncode`
- `EmptySD3LatentImage`
- `VAELoader`
- `Krea2EditModelPatch`
- `Krea2EditGroundedEncode`
- `GetImageSize+`
- `CLIPLoader`
- `Seed (rgthree)`
- `DrawMaskOnImage`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `Seed (rgthree)`
- `VAEEncode` ★核心
- `Krea2EditGroundedEncode`
- `Krea2EditGroundedEncode`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `GetImageSize+`
- `EmptySD3LatentImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `Note`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `PreviewImage`
- `KSampler` ★核心
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `Note`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Krea2EditModelPatch`
- `SaveImage`
- `PrimitiveStringMultiline`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `478172831101520`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **84%**（53/63）

**有卡**：`Krea2EditGroundedEncode`、`EmptySD3LatentImage`、`Krea2EditModelPatch`、`CLIPLoader`、`VAELoader`、`VAEEncode`、`KSampler`、`VAEDecode`、`SaveImage`、`Seed (rgthree)`、`GetImageSize+`、`DrawMaskOnImage`、`ImageScaleToTotalPixels`、`LoadImage`、`ResolutionSelector`、`LoraLoaderModelOnly`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader
