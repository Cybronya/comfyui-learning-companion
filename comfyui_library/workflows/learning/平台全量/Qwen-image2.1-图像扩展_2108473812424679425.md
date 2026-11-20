---
key: 平台全量/Qwen-image2.1-图像扩展_2108473812424679425.json
name: Qwen-image2.1-图像扩展_2108473812424679425
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-image2.1-图像扩展_2108473812424679425.json
hash: da219c87fd75c87d
coverage: 0.770833
learned_at: 2026-11-14 00:52:11
nodes: [LoraLoaderModelOnly, QwenImage21Cache, UNETLoader, DrawMaskOnImage, KSampler, VAEDecode, LoraLoaderModelOnly, LoadImage, ImageScaleToTotalPixels, ImagePadForOutpaint, SaveImage, TextEncodeQwenImage21, CLIPLoader, InpaintCropImproved, PreviewImage, InpaintStitchImproved, Image Comparer (rgthree), CLIPLoader, VAELoader, KSampler, Seed (rgthree), Fast Groups Bypasser (rgthree), VAEEncode, SetLatentNoiseMask, Image Comparer (rgthree), DrawMaskOnImage, PreviewImage, ComfySwitchNode, INTConstant, SimpleMath+, UNETLoader, QwenImage21Cache, VAEDecode, LoadImage, LoraLoaderModelOnly, SaveImage, LoadImage, TextEncodeQwenImage21, Fast Groups Bypasser (rgthree), PreviewImage, VAELoader, PrimitiveStringMultiline, ImageScaleToTotalPixels, PreviewImage, PrimitiveStringMultiline, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageScaleToTotalPixels]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 240843227721620, "steps": 25}
---

# 平台全量/Qwen-image2.1-图像扩展_2108473812424679425.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-image2.1-图像扩展_2108473812424679425.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `LoraLoaderModelOnly` ★核心
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `DrawMaskOnImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `ImageScaleToTotalPixels`
- `ImagePadForOutpaint`
- `SaveImage`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `InpaintCropImproved`
- `PreviewImage`
- `InpaintStitchImproved`
- `Image Comparer (rgthree)`
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `Seed (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `Image Comparer (rgthree)`
- `DrawMaskOnImage`
- `PreviewImage`
- `ComfySwitchNode`
- `INTConstant`
- `SimpleMath+`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `Fast Groups Bypasser (rgthree)`
- `PreviewImage`
- `VAELoader`
- `PrimitiveStringMultiline`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageScaleToTotalPixels`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `240843227721620`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（37/48）

**有卡**：`LoraLoaderModelOnly`、`QwenImage21Cache`、`UNETLoader`、`DrawMaskOnImage`、`KSampler`、`VAEDecode`、`LoadImage`、`ImageScaleToTotalPixels`、`ImagePadForOutpaint`、`SaveImage`、`TextEncodeQwenImage21`、`CLIPLoader`、`InpaintCropImproved`、`InpaintStitchImproved`、`VAELoader`、`Seed (rgthree)`、`VAEEncode`、`SetLatentNoiseMask`、`INTConstant`、`SimpleMath+`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache
