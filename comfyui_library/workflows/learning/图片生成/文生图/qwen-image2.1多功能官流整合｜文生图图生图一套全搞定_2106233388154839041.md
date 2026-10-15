---
key: 图片生成/文生图/qwen-image2.1多功能官流整合｜文生图图生图一套全搞定_2106233388154839041.json
name: qwen-image2.1多功能官流整合｜文生图图生图一套全搞定_2106233388154839041
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-image2.1多功能官流整合｜文生图图生图一套全搞定_2106233388154839041.json
hash: c973afac4aec3849
coverage: 0.8375
learned_at: 2026-10-10 20:59:25
nodes: [ResolutionSelector, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, KSampler, ComfySwitchNode, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveBoolean, PrimitiveInt, PreviewAny, PrimitiveStringMultiline, TextGenerate, BatchImagesNode, ImageScaleToTotalPixels, QwenImage21Cache, ModelAttentionBackend, CLIPLoader, TextGenerate, CLIPLoader, PrimitiveStringMultiline, GetImageSize, Any Switch (rgthree), TextEncodeQwenImage21, ImageResizeKJv2, VAEDecode, Image Comparer (rgthree), LoadImage, LoadImage, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/qwen-image2.1多功能官流整合｜文生图图生图一套全搞定_2106233388154839041.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen-image2.1多功能官流整合｜文生图图生图一套全搞定_2106233388154839041.json`

## 结构

**节点**（80 个）：
- `ResolutionSelector`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage`
- `KSampler`
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `TextGenerate`
- `BatchImagesNode`
- `ImageScaleToTotalPixels`
- `QwenImage21Cache`
- `ModelAttentionBackend`
- `CLIPLoader`
- `TextGenerate`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `GetImageSize`
- `Any Switch (rgthree)`
- `TextEncodeQwenImage21`
- `ImageResizeKJv2`
- `VAEDecode`
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `SaveImage`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `孤海注释`
- `孤海注释`
- `UNETLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `VAELoader`
- `EmptyLatentImage`
- `KSampler`
- `VAEDecode`
- `solarL_SaveImagesToZip`
- `JjkText`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `CLIPTextEncode`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `4.5`
- `denoise` = `1`
- `height` = `80`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `seed` = `598626327129635`
- `steps` = `4`
- `width` = `80`

## 知识

覆盖率 **84%**（67/80）

**有卡**：`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`ComfySwitchNode`、`LoadImage`、`PrimitiveBoolean`、`PrimitiveInt`、`PreviewAny`、`PrimitiveStringMultiline`、`TextGenerate`、`BatchImagesNode`、`ImageScaleToTotalPixels`、`QwenImage21Cache`、`ModelAttentionBackend`、`GetImageSize`、`Any Switch (rgthree)`、`TextEncodeQwenImage21`、`ImageResizeKJv2`、`VAEDecode`、`Image Comparer (rgthree)`、`Fast Groups Bypasser (rgthree)`、`SaveImage`、`LoraLoaderModelOnly`、`孤海注释`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`JjkText`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
