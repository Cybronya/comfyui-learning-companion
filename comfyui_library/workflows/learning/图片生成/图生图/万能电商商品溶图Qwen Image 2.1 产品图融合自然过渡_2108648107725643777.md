---
key: 图片生成/图生图/万能电商商品溶图Qwen Image 2.1 产品图融合自然过渡_2108648107725643777.json
name: 万能电商商品溶图Qwen Image 2.1 产品图融合自然过渡_2108648107725643777
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/万能电商商品溶图Qwen Image 2.1 产品图融合自然过渡_2108648107725643777.json
hash: 7db24ae22727d8fb
coverage: 0.901961
learned_at: 2026-10-23 12:01:36
nodes: [KSamplerAdvanced, TextEncodeQwenImage21, CLIPLoader, VAELoader, ImageUpscaleWithModel, LoraLoaderModelOnly, ImageScaleToTotalPixels, CR Prompt Text, CR Text Concatenate, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, VAEDecode, UpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, FastCanvasTool, InspyrenetRembg, SaveImage, Image Comparer (rgthree), CR Prompt Text, FastCanvas, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/万能电商商品溶图Qwen Image 2.1 产品图融合自然过渡_2108648107725643777.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/万能电商商品溶图Qwen Image 2.1 产品图融合自然过渡_2108648107725643777.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `KSamplerAdvanced` ★核心
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `ImageUpscaleWithModel`
- `LoraLoaderModelOnly` ★核心
- `ImageScaleToTotalPixels`
- `CR Prompt Text`
- `CR Text Concatenate`
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `VAEDecode` ★核心
- `UpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FastCanvasTool`
- `InspyrenetRembg`
- `SaveImage`
- `Image Comparer (rgthree)`
- `CR Prompt Text`
- `FastCanvas`
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
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
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

覆盖率 **90%**（46/51）

**有卡**：`KSamplerAdvanced`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`ImageUpscaleWithModel`、`LoraLoaderModelOnly`、`ImageScaleToTotalPixels`、`CR Prompt Text`、`CR Text Concatenate`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`VAEDecode`、`UpscaleModelLoader`、`FastCanvasTool`、`InspyrenetRembg`、`SaveImage`、`FastCanvas`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
