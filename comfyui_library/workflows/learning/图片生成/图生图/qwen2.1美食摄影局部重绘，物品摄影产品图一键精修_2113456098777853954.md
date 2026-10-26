---
key: 图片生成/图生图/qwen2.1美食摄影局部重绘，物品摄影产品图一键精修_2113456098777853954.json
name: qwen2.1美食摄影局部重绘，物品摄影产品图一键精修_2113456098777853954
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen2.1美食摄影局部重绘，物品摄影产品图一键精修_2113456098777853954.json
hash: c32637300459c55f
coverage: 0.891304
learned_at: 2026-10-26 22:04:19
nodes: [VAELoader, CLIPLoader, KSamplerAdvanced, TextEncodeQwenImage21, CR Prompt Text, VAEDecode, Image Comparer (rgthree), LoadImage, INTConstant, SimpleMath+, PreviewImage, InpaintCropImproved, VAEEncode, SetLatentNoiseMask, UNETLoader, InpaintStitchImproved, SaveImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note, EmptyImage, PreviewImage]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen2.1美食摄影局部重绘，物品摄影产品图一键精修_2113456098777853954.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen2.1美食摄影局部重绘，物品摄影产品图一键精修_2113456098777853954.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `VAELoader`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `TextEncodeQwenImage21`
- `CR Prompt Text`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `INTConstant`
- `SimpleMath+`
- `PreviewImage`
- `InpaintCropImproved`
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `UNETLoader` ★核心
- `InpaintStitchImproved`
- `SaveImage`
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
- `EmptyImage`
- `PreviewImage`

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

覆盖率 **89%**（41/46）

**有卡**：`VAELoader`、`CLIPLoader`、`KSamplerAdvanced`、`TextEncodeQwenImage21`、`CR Prompt Text`、`VAEDecode`、`LoadImage`、`INTConstant`、`SimpleMath+`、`InpaintCropImproved`、`VAEEncode`、`SetLatentNoiseMask`、`UNETLoader`、`InpaintStitchImproved`、`SaveImage`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
