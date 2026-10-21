---
key: 图片生成/图生图/Qwen Image 2.1零偏移单多图局部遮罩编辑重绘工作流，局部重绘图生图方案_2107943545071030273.json
name: Qwen Image 2.1零偏移单多图局部遮罩编辑重绘工作流，局部重绘图生图方案_2107943545071030273
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1零偏移单多图局部遮罩编辑重绘工作流，局部重绘图生图方案_2107943545071030273.json
hash: 4bda7705dd02c9ff
coverage: 0.877551
learned_at: 2026-10-21 00:42:48
nodes: [CLIPLoader, VAELoader, VAEDecode, GetImageSize, VAEEncode, SetLatentNoiseMask, ResizeImageMaskNode, LoadImage, QwenImage21Cache, Image Comparer (rgthree), SaveImage, UNETLoader, KSampler, PrimitiveStringMultiline, LoadImage, RHHiddenNodes, TextEncodeQwenImage21, VAEDecode, WujiUpscaler2, WujiCleaner, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1零偏移单多图局部遮罩编辑重绘工作流，局部重绘图生图方案_2107943545071030273.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1零偏移单多图局部遮罩编辑重绘工作流，局部重绘图生图方案_2107943545071030273.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `GetImageSize`
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `ResizeImageMaskNode`
- `LoadImage`
- `QwenImage21Cache`
- `Image Comparer (rgthree)`
- `SaveImage`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `PrimitiveStringMultiline`
- `LoadImage`
- `RHHiddenNodes`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `WujiUpscaler2`
- `WujiCleaner`
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

覆盖率 **88%**（43/49）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`GetImageSize`、`VAEEncode`、`SetLatentNoiseMask`、`ResizeImageMaskNode`、`LoadImage`、`QwenImage21Cache`、`SaveImage`、`UNETLoader`、`KSampler`、`RHHiddenNodes`、`TextEncodeQwenImage21`、`WujiUpscaler2`、`WujiCleaner`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
