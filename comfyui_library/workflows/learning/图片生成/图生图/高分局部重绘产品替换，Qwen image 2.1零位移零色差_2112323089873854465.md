---
key: 图片生成/图生图/高分局部重绘产品替换，Qwen image 2.1零位移零色差_2112323089873854465.json
name: 高分局部重绘产品替换，Qwen image 2.1零位移零色差_2112323089873854465
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/高分局部重绘产品替换，Qwen image 2.1零位移零色差_2112323089873854465.json
hash: 83aa325c52bcc1eb
coverage: 0.79661
learned_at: 2026-10-23 13:33:36
nodes: [ImageScaleToTotalPixels, MaskFillHoles, SimpleMath+, InpaintCropImproved, DrawMaskOnImage, GetNode, VAEEncode, Seed (rgthree), SetLatentNoiseMask, TextEncodeQwenImage21, KSampler, VAEDecode, InpaintStitchImproved, SaveImage, INTConstant, Image Comparer (rgthree), CLIPLoader, Anything Everywhere, Anything Everywhere, UNETLoader, VAELoader, Anything Everywhere, ComfySwitchNode, LoadImage, LoadImage, QwenImage21Cache, PrimitiveStringMultiline, SetNode, LayerUtility: ImageScaleByAspectRatio V2, ImpactInt, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/高分局部重绘产品替换，Qwen image 2.1零位移零色差_2112323089873854465.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/高分局部重绘产品替换，Qwen image 2.1零位移零色差_2112323089873854465.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `ImageScaleToTotalPixels`
- `MaskFillHoles`
- `SimpleMath+`
- `InpaintCropImproved`
- `DrawMaskOnImage`
- `GetNode`
- `VAEEncode` ★核心
- `Seed (rgthree)`
- `SetLatentNoiseMask`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `InpaintStitchImproved`
- `SaveImage`
- `INTConstant`
- `Image Comparer (rgthree)`
- `CLIPLoader`
- `Anything Everywhere`
- `Anything Everywhere`
- `UNETLoader` ★核心
- `VAELoader`
- `Anything Everywhere`
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `QwenImage21Cache`
- `PrimitiveStringMultiline`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImpactInt`
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

覆盖率 **80%**（47/59）

**有卡**：`ImageScaleToTotalPixels`、`MaskFillHoles`、`SimpleMath+`、`InpaintCropImproved`、`DrawMaskOnImage`、`VAEEncode`、`Seed (rgthree)`、`SetLatentNoiseMask`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`InpaintStitchImproved`、`SaveImage`、`INTConstant`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`LoadImage`、`QwenImage21Cache`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImpactInt`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
