---
key: 图片生成/图生图/FireRed-Image-Edit 1.1 +Qwen2511图片编辑工作流-高清直出_2036793276518375425.json
name: FireRed-Image-Edit 1.1 +Qwen2511图片编辑工作流-高清直出_2036793276518375425
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1 +Qwen2511图片编辑工作流-高清直出_2036793276518375425.json
hash: 24d64b2acc115ec1
coverage: 0.933333
learned_at: 2026-10-23 10:55:30
nodes: [SaveImage, SaveImage, easy cleanGpuUsed, SeedVR2, VAEDecode, PrimitiveNode, LoraLoaderModelOnly, CLIPLoader, UNETLoader, ImageScaleToTotalPixels, TextEncodeQwenImageEditPlus, CLIPTextEncode, EmptyLatentImage, GetImageSize, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, SeedVR2, KSampler, VAEDecode, CLIPTextEncode, TextEncodeQwenImageEditPlus, KSampler, SaveImage, SaveImage, LoadImage, JjkText, CustomAddLabel, CustomAddLabel]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 732767065190777, "steps": 8, "width": 720}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-Edit 1.1 +Qwen2511图片编辑工作流-高清直出_2036793276518375425.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1 +Qwen2511图片编辑工作流-高清直出_2036793276518375425.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `SaveImage`
- `SaveImage`
- `easy cleanGpuUsed`
- `SeedVR2`
- `VAEDecode` ★核心
- `PrimitiveNode`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `ImageScaleToTotalPixels`
- `TextEncodeQwenImageEditPlus`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `GetImageSize`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `SeedVR2`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `JjkText`
- `CustomAddLabel`
- `CustomAddLabel`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `732767065190777`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（28/30）

**有卡**：`SaveImage`、`easy cleanGpuUsed`、`SeedVR2`、`VAEDecode`、`LoraLoaderModelOnly`、`CLIPLoader`、`UNETLoader`、`ImageScaleToTotalPixels`、`TextEncodeQwenImageEditPlus`、`CLIPTextEncode`、`EmptyLatentImage`、`GetImageSize`、`VAELoader`、`KSampler`、`LoadImage`、`CustomAddLabel`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
