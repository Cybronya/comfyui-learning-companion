---
key: 图片生成/图生图/Qwen2.1自定义修改工作流，千问驱动图生图自定义编辑工具_2103912464470597634.json
name: Qwen2.1自定义修改工作流，千问驱动图生图自定义编辑工具_2103912464470597634
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1自定义修改工作流，千问驱动图生图自定义编辑工具_2103912464470597634.json
hash: 2479508dd0daca7c
coverage: 0.844444
learned_at: 2026-10-21 00:43:40
nodes: [Anything Everywhere3, TextEncodeQwenImage21, VAEDecode, PixaromaUncrop, PixaromaInpaintCrop, ImageToMask, PreviewImage, PreviewImage, Text, LoadImage, LoadImage, SaveImage, UNETLoader, CLIPLoader, VAELoader, KSampler, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen2.1自定义修改工作流，千问驱动图生图自定义编辑工具_2103912464470597634.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1自定义修改工作流，千问驱动图生图自定义编辑工具_2103912464470597634.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（45 个）：
- `Anything Everywhere3`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `PixaromaUncrop`
- `PixaromaInpaintCrop`
- `ImageToMask`
- `PreviewImage`
- `PreviewImage`
- `Text`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
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

覆盖率 **84%**（38/45）

**有卡**：`TextEncodeQwenImage21`、`VAEDecode`、`PixaromaUncrop`、`PixaromaInpaintCrop`、`ImageToMask`、`Text`、`LoadImage`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
