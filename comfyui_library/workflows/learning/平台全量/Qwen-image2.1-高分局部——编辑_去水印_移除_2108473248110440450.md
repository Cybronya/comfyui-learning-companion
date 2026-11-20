---
key: 平台全量/Qwen-image2.1-高分局部——编辑_去水印_移除_2108473248110440450.json
name: Qwen-image2.1-高分局部——编辑_去水印_移除_2108473248110440450
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-image2.1-高分局部——编辑_去水印_移除_2108473248110440450.json
hash: d2dd87ecbf19d585
coverage: 0.75
learned_at: 2026-11-14 00:52:12
nodes: [ImageScaleToTotalPixels, SetLatentNoiseMask, TextEncodeQwenImage21, KSampler, VAEDecode, PrimitiveStringMultiline, ComfySwitchNode, CLIPLoader, VAEEncode, PreviewImage, DrawMaskOnImage, PreviewImage, InpaintCropImproved, VAELoader, SimpleMath+, INTConstant, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, InpaintStitchImproved, QwenImage21Cache, LoadImage, LoadImage, LoraLoaderModelOnly, SaveImage, Image Comparer (rgthree), Image Comparer (rgthree)]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 499528052401800, "steps": 25}
---

# 平台全量/Qwen-image2.1-高分局部——编辑_去水印_移除_2108473248110440450.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-image2.1-高分局部——编辑_去水印_移除_2108473248110440450.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `ImageScaleToTotalPixels`
- `SetLatentNoiseMask`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `CLIPLoader`
- `VAEEncode` ★核心
- `PreviewImage`
- `DrawMaskOnImage`
- `PreviewImage`
- `InpaintCropImproved`
- `VAELoader`
- `SimpleMath+`
- `INTConstant`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `InpaintStitchImproved`
- `QwenImage21Cache`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `499528052401800`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **75%**（21/28）

**有卡**：`ImageScaleToTotalPixels`、`SetLatentNoiseMask`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`CLIPLoader`、`VAEEncode`、`DrawMaskOnImage`、`InpaintCropImproved`、`VAELoader`、`SimpleMath+`、`INTConstant`、`LoraLoaderModelOnly`、`UNETLoader`、`InpaintStitchImproved`、`QwenImage21Cache`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache
