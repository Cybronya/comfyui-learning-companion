---
key: 图片生成/图生图/Qwen Image 2.1局部编辑无偏移图生图处理生成工具_2102092856801447937.json
name: Qwen Image 2.1局部编辑无偏移图生图处理生成工具_2102092856801447937
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1局部编辑无偏移图生图处理生成工具_2102092856801447937.json
hash: 9eecf99b34030e2b
coverage: 0.851852
learned_at: 2026-10-10 20:48:07
nodes: [ResizeMask, GetImageSize, VAEEncode, ImageScale, SetLatentNoiseMask, ImageScaleToMaxDimension, Image Comparer (rgthree), GetNode, VAEDecode, VAEEncode, UNETLoader, VAELoader, CLIPLoader, SetNode, GrowMaskWithBlur, Fast Groups Bypasser (rgthree), KSamplerAdvanced, ImpactInt, TextEncodeQwenImage21, LoadImage, Text, LoadImage, LoadImage, VAEDecode, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1局部编辑无偏移图生图处理生成工具_2102092856801447937.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1局部编辑无偏移图生图处理生成工具_2102092856801447937.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `ResizeMask`
- `GetImageSize`
- `VAEEncode` ★核心
- `ImageScale`
- `SetLatentNoiseMask`
- `ImageScaleToMaxDimension`
- `Image Comparer (rgthree)`
- `GetNode`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `SetNode`
- `GrowMaskWithBlur`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerAdvanced` ★核心
- `ImpactInt`
- `TextEncodeQwenImage21`
- `LoadImage`
- `Text`
- `LoadImage`
- `LoadImage`
- `VAEDecode` ★核心
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

覆盖率 **85%**（46/54）

**有卡**：`ResizeMask`、`GetImageSize`、`VAEEncode`、`ImageScale`、`SetLatentNoiseMask`、`ImageScaleToMaxDimension`、`VAEDecode`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`GrowMaskWithBlur`、`KSamplerAdvanced`、`ImpactInt`、`TextEncodeQwenImage21`、`LoadImage`、`Text`、`SaveImage`、`LoraLoaderModelOnly`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
