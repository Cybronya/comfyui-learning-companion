---
key: 图片生成/图生图/Qwen image 2.1 高分图像局部重绘｜局部重绘｜换头换脸｜产品替换｜零色差｜零位移｜零色差_2108344197836263425.json
name: Qwen image 2.1 高分图像局部重绘｜局部重绘｜换头换脸｜产品替换｜零色差｜零位移｜零色差_2108344197836263425
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 高分图像局部重绘｜局部重绘｜换头换脸｜产品替换｜零色差｜零位移｜零色差_2108344197836263425.json
hash: 87fec68b500dab67
coverage: 0.631579
learned_at: 2026-10-23 11:13:58
nodes: [ImageScaleToTotalPixels, LayerUtility: ImageScaleByAspectRatio V2, MaskFillHoles, SimpleMath+, InpaintCropImproved, DrawMaskOnImage, GetNode, VAEEncode, Seed (rgthree), SetLatentNoiseMask, TextEncodeQwenImage21, KSampler, VAEDecode, InpaintStitchImproved, SaveImage, INTConstant, Image Comparer (rgthree), PrimitiveStringMultiline, Any Switch (rgthree), SetNode, CLIPLoader, Anything Everywhere, QwenImage21Cache, Anything Everywhere, UNETLoader, VAELoader, Anything Everywhere, LoraLoaderModelOnly, PrimitiveStringMultiline, 孤海注释, Fast Groups Bypasser (rgthree), 孤海注释, ComfySwitchNode, LoadImage, ImpactInt, PrimitiveStringMultiline, LoadImage, 忽略多组孤海]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 746646509892973, "steps": 25}
---

# 图片生成/图生图/Qwen image 2.1 高分图像局部重绘｜局部重绘｜换头换脸｜产品替换｜零色差｜零位移｜零色差_2108344197836263425.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 高分图像局部重绘｜局部重绘｜换头换脸｜产品替换｜零色差｜零位移｜零色差_2108344197836263425.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
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
- `孤海注释`
- `Fast Groups Bypasser (rgthree)`
- `孤海注释`
- `ComfySwitchNode`
- `LoadImage`
- `ImpactInt`
- `PrimitiveStringMultiline`
- `LoadImage`
- `忽略多组孤海`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `746646509892973`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **63%**（24/38）

**有卡**：`ImageScaleToTotalPixels`、`LayerUtility: ImageScaleByAspectRatio V2`、`MaskFillHoles`、`SimpleMath+`、`InpaintCropImproved`、`DrawMaskOnImage`、`VAEEncode`、`Seed (rgthree)`、`SetLatentNoiseMask`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`InpaintStitchImproved`、`SaveImage`、`INTConstant`、`CLIPLoader`、`QwenImage21Cache`、`UNETLoader`、`VAELoader`、`LoraLoaderModelOnly`、`LoadImage`、`ImpactInt`、`忽略多组孤海`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache
