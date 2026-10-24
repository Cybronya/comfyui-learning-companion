---
key: 图片生成/图生图/Qwen image 2.1局部重绘零色差零位移，换头换脸与商品替换高清重绘_2112244498993606658.json
name: Qwen image 2.1局部重绘零色差零位移，换头换脸与商品替换高清重绘_2112244498993606658
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1局部重绘零色差零位移，换头换脸与商品替换高清重绘_2112244498993606658.json
hash: 9f87b9e60e96531b
coverage: 0.75
learned_at: 2026-10-23 11:14:08
nodes: [ImageScaleToTotalPixels, LayerUtility: ImageScaleByAspectRatio V2, MaskFillHoles, SimpleMath+, InpaintCropImproved, DrawMaskOnImage, GetNode, VAEEncode, Seed (rgthree), SetLatentNoiseMask, TextEncodeQwenImage21, KSampler, VAEDecode, InpaintStitchImproved, SaveImage, INTConstant, Image Comparer (rgthree), PrimitiveStringMultiline, Any Switch (rgthree), SetNode, CLIPLoader, Anything Everywhere, QwenImage21Cache, Anything Everywhere, UNETLoader, VAELoader, Anything Everywhere, LoraLoaderModelOnly, PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), ComfySwitchNode, LoadImage, ImpactInt, PrimitiveStringMultiline, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen image 2.1局部重绘零色差零位移，换头换脸与商品替换高清重绘_2112244498993606658.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1局部重绘零色差零位移，换头换脸与商品替换高清重绘_2112244498993606658.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（64 个）：
- `ImageScaleToTotalPixels`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `PrimitiveStringMultiline`
- `Any Switch (rgthree)`
- `SetNode`
- `CLIPLoader`
- `Anything Everywhere`
- `QwenImage21Cache`
- `Anything Everywhere`
- `UNETLoader` ★核心
- `VAELoader`
- `Anything Everywhere`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `Fast Groups Bypasser (rgthree)`
- `ComfySwitchNode`
- `LoadImage`
- `ImpactInt`
- `PrimitiveStringMultiline`
- `LoadImage`
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

覆盖率 **75%**（48/64）

**有卡**：`ImageScaleToTotalPixels`、`LayerUtility: ImageScaleByAspectRatio V2`、`MaskFillHoles`、`SimpleMath+`、`InpaintCropImproved`、`DrawMaskOnImage`、`VAEEncode`、`Seed (rgthree)`、`SetLatentNoiseMask`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`InpaintStitchImproved`、`SaveImage`、`INTConstant`、`CLIPLoader`、`QwenImage21Cache`、`UNETLoader`、`VAELoader`、`LoraLoaderModelOnly`、`LoadImage`、`ImpactInt`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
