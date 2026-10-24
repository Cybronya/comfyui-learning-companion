---
key: 图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2083752313956687874.json
name: FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2083752313956687874
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2083752313956687874.json
hash: ca91e557d15fbaf7
coverage: 0.809524
learned_at: 2026-10-23 10:55:33
nodes: [PrimitiveNode, CLIPTextEncode, LoraLoaderModelOnly, CLIPLoader, LoadImage, ImageScaleToTotalPixels, RunningHub Deepcleaner, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, TextEncodeQwenImageEditPlus, UNETLoader, VAELoader, JjkText, KSampler, EmptyLatentImage, SeedVR2VideoUpscaler, Image Comparer (rgthree), 孤海注释, VAEDecode, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 385609630761034, "steps": 8, "width": 1920}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2083752313956687874.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2083752313956687874.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `PrimitiveNode`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `RunningHub Deepcleaner`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader` ★核心
- `VAELoader`
- `JjkText`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `SeedVR2VideoUpscaler`
- `Image Comparer (rgthree)`
- `孤海注释`
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `385609630761034`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（17/21）

**有卡**：`CLIPTextEncode`、`LoraLoaderModelOnly`、`CLIPLoader`、`LoadImage`、`ImageScaleToTotalPixels`、`RunningHub Deepcleaner`、`SaveImage`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`TextEncodeQwenImageEditPlus`、`UNETLoader`、`VAELoader`、`KSampler`、`EmptyLatentImage`、`SeedVR2VideoUpscaler`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
