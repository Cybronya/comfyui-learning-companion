---
key: 图片生成/图生图/光影重塑-图片重新打光-V2-FireRed-Image-Edit 1.1-图生图_2061104265892024321.json
name: 光影重塑-图片重新打光-V2-FireRed-Image-Edit 1.1-图生图_2061104265892024321
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/光影重塑-图片重新打光-V2-FireRed-Image-Edit 1.1-图生图_2061104265892024321.json
hash: ace6712e662b8c52
coverage: 0.814815
learned_at: 2026-10-23 12:13:00
nodes: [TextEncodeQwenImageEditPlus, CLIPTextEncode, EmptyLatentImage, UNETLoader, LoraLoaderModelOnly, CLIPLoader, llama_cpp_parameters, easy showAnything, llama_cpp_model_loader, easy cleanGpuUsed, PreviewImage, SaveImage, VAELoader, VAEDecode, easy cleanGpuUsed, KSampler, PrimitiveNode, GetImageSize, ImageScaleToTotalPixels, MarkdownNote, SeedVR2, LayerUtility: ImageScaleByAspectRatio V2, Int, Text, llama_cpp_instruct_adv, LoadImage, JjkText]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 663076679212843, "steps": 8, "width": 720}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/光影重塑-图片重新打光-V2-FireRed-Image-Edit 1.1-图生图_2061104265892024321.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/光影重塑-图片重新打光-V2-FireRed-Image-Edit 1.1-图生图_2061104265892024321.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `TextEncodeQwenImageEditPlus`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `llama_cpp_parameters`
- `easy showAnything`
- `llama_cpp_model_loader`
- `easy cleanGpuUsed`
- `PreviewImage`
- `SaveImage`
- `VAELoader`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `PrimitiveNode`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `MarkdownNote`
- `SeedVR2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `Text`
- `llama_cpp_instruct_adv`
- `LoadImage`
- `JjkText`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `663076679212843`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（22/27）

**有卡**：`TextEncodeQwenImageEditPlus`、`CLIPTextEncode`、`EmptyLatentImage`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`easy cleanGpuUsed`、`SaveImage`、`VAELoader`、`VAEDecode`、`KSampler`、`GetImageSize`、`ImageScaleToTotalPixels`、`SeedVR2`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`Text`、`llama_cpp_instruct_adv`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
