---
key: 图片生成/图生图/Qwen image2.1万能局部重绘低像素重绘 精准控制改图_2109734236285657090.json
name: Qwen image2.1万能局部重绘低像素重绘 精准控制改图_2109734236285657090
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image2.1万能局部重绘低像素重绘 精准控制改图_2109734236285657090.json
hash: 4581cc57786dff52
coverage: 0.87234
learned_at: 2026-10-23 11:14:21
nodes: [UNETLoader, CLIPLoader, VAELoader, Mask Fill Holes, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: CropByMask V2, LayerUtility: ImageScaleRestore V2, ImageScale, PreviewImage, TextEncodeQwenImage21, InpaintModelConditioning, KSampler, VAEDecode, GetImageSize, LayerUtility: RestoreCropBox, SaveImage, Image Comparer (rgthree), 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen image2.1万能局部重绘低像素重绘 精准控制改图_2109734236285657090.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image2.1万能局部重绘低像素重绘 精准控制改图_2109734236285657090.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Mask Fill Holes`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleRestore V2`
- `ImageScale`
- `PreviewImage`
- `TextEncodeQwenImage21`
- `InpaintModelConditioning`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `GetImageSize`
- `LayerUtility: RestoreCropBox`
- `SaveImage`
- `Image Comparer (rgthree)`
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

**识别到的模式**：text_to_image

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

覆盖率 **87%**（41/47）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`Mask Fill Holes`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`LayerUtility: CropByMask V2`、`LayerUtility: ImageScaleRestore V2`、`ImageScale`、`TextEncodeQwenImage21`、`InpaintModelConditioning`、`KSampler`、`VAEDecode`、`GetImageSize`、`LayerUtility: RestoreCropBox`、`SaveImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
