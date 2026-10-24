---
key: 图片生成/图生图/Qwen image 2.1 高分图像局部重绘-产品替换｜零位移｜零色差_2111813686213038081.json
name: Qwen image 2.1 高分图像局部重绘-产品替换｜零位移｜零色差_2111813686213038081
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 高分图像局部重绘-产品替换｜零位移｜零色差_2111813686213038081.json
hash: 06d800bb6367c57a
coverage: 0.71875
learned_at: 2026-10-23 11:13:58
nodes: [ImageScaleToTotalPixels, MaskFillHoles, SimpleMath+, InpaintCropImproved, DrawMaskOnImage, GetNode, VAEEncode, Seed (rgthree), SetLatentNoiseMask, TextEncodeQwenImage21, KSampler, VAEDecode, InpaintStitchImproved, SaveImage, INTConstant, Image Comparer (rgthree), CLIPLoader, Anything Everywhere, Anything Everywhere, UNETLoader, VAELoader, Anything Everywhere, 孤海注释, ComfySwitchNode, LoadImage, LoadImage, 忽略多组孤海, QwenImage21Cache, PrimitiveStringMultiline, SetNode, LayerUtility: ImageScaleByAspectRatio V2, ImpactInt]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 746646509892971, "steps": 25}
---

# 图片生成/图生图/Qwen image 2.1 高分图像局部重绘-产品替换｜零位移｜零色差_2111813686213038081.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 高分图像局部重绘-产品替换｜零位移｜零色差_2111813686213038081.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
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
- `孤海注释`
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `忽略多组孤海`
- `QwenImage21Cache`
- `PrimitiveStringMultiline`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImpactInt`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `746646509892971`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **72%**（23/32）

**有卡**：`ImageScaleToTotalPixels`、`MaskFillHoles`、`SimpleMath+`、`InpaintCropImproved`、`DrawMaskOnImage`、`VAEEncode`、`Seed (rgthree)`、`SetLatentNoiseMask`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`InpaintStitchImproved`、`SaveImage`、`INTConstant`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`LoadImage`、`忽略多组孤海`、`QwenImage21Cache`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImpactInt`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
