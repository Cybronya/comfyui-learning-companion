---
key: 图片生成/图生图/Qwen-Image-2.1遮罩局部重绘V1，指哪改哪精准编辑_2110480100507602946.json
name: Qwen-Image-2.1遮罩局部重绘V1，指哪改哪精准编辑_2110480100507602946
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1遮罩局部重绘V1，指哪改哪精准编辑_2110480100507602946.json
hash: afde8146e13f4b91
coverage: 0.810345
learned_at: 2026-10-23 11:16:32
nodes: [CLIPLoader, VAELoader, KSampler, QwenImage21Cache, Seed (rgthree), VAEEncode, SetLatentNoiseMask, TextEncodeQwenImage21, UNETLoader, ComfySwitchNode, PreviewImage, DrawMaskOnImage, ComfySwitchNode, Int, Int, SimpleMath+, Image Comparer (rgthree), VAEDecode, PrimitiveStringMultiline, LoadImage, PreviewImage, InpaintStitchImproved, SimpleMath+, InpaintCropImproved, LoadImage, easy isNone, ImageScaleToTotalPixels, Image Comparer (rgthree), SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Image-2.1遮罩局部重绘V1，指哪改哪精准编辑_2110480100507602946.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1遮罩局部重绘V1，指哪改哪精准编辑_2110480100507602946.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `QwenImage21Cache`
- `Seed (rgthree)`
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `ComfySwitchNode`
- `PreviewImage`
- `DrawMaskOnImage`
- `ComfySwitchNode`
- `Int`
- `Int`
- `SimpleMath+`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `PrimitiveStringMultiline`
- `LoadImage`
- `PreviewImage`
- `InpaintStitchImproved`
- `SimpleMath+`
- `InpaintCropImproved`
- `LoadImage`
- `easy isNone`
- `ImageScaleToTotalPixels`
- `Image Comparer (rgthree)`
- `SaveImage`
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

覆盖率 **81%**（47/58）

**有卡**：`CLIPLoader`、`VAELoader`、`KSampler`、`QwenImage21Cache`、`Seed (rgthree)`、`VAEEncode`、`SetLatentNoiseMask`、`TextEncodeQwenImage21`、`UNETLoader`、`DrawMaskOnImage`、`Int`、`SimpleMath+`、`VAEDecode`、`LoadImage`、`InpaintStitchImproved`、`InpaintCropImproved`、`easy isNone`、`ImageScaleToTotalPixels`、`SaveImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
