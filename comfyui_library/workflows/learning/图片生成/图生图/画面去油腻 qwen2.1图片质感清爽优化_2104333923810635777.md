---
key: 图片生成/图生图/画面去油腻 qwen2.1图片质感清爽优化_2104333923810635777.json
name: 画面去油腻 qwen2.1图片质感清爽优化_2104333923810635777
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/画面去油腻 qwen2.1图片质感清爽优化_2104333923810635777.json
hash: b1570c6657e35af3
coverage: 0.854167
learned_at: 2026-10-21 00:55:25
nodes: [Anything Everywhere3, VAEDecode, PixaromaInpaintCrop, PreviewImage, VAELoader, KSampler, TextEncodeQwenImage21, UNETLoader, CLIPLoader, LoraLoaderModelOnly, ImageToMask, PreviewImage, SaveImage, Text, PixaromaUncrop, LoadImage, LoadImage, Image Remove Alpha JK, ImageColorMatch+, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/画面去油腻 qwen2.1图片质感清爽优化_2104333923810635777.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/画面去油腻 qwen2.1图片质感清爽优化_2104333923810635777.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `Anything Everywhere3`
- `VAEDecode` ★核心
- `PixaromaInpaintCrop`
- `PreviewImage`
- `VAELoader`
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `ImageToMask`
- `PreviewImage`
- `SaveImage`
- `Text`
- `PixaromaUncrop`
- `LoadImage`
- `LoadImage`
- `Image Remove Alpha JK`
- `ImageColorMatch+`
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

覆盖率 **85%**（41/48）

**有卡**：`VAEDecode`、`PixaromaInpaintCrop`、`VAELoader`、`KSampler`、`TextEncodeQwenImage21`、`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`ImageToMask`、`SaveImage`、`Text`、`PixaromaUncrop`、`LoadImage`、`Image Remove Alpha JK`、`ImageColorMatch+`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
