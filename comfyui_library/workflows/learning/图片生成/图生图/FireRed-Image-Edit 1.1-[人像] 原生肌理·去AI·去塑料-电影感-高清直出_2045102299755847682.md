---
key: 图片生成/图生图/FireRed-Image-Edit 1.1-[人像] 原生肌理·去AI·去塑料-电影感-高清直出_2045102299755847682.json
name: FireRed-Image-Edit 1.1-[人像] 原生肌理·去AI·去塑料-电影感-高清直出_2045102299755847682
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1-[人像] 原生肌理·去AI·去塑料-电影感-高清直出_2045102299755847682.json
hash: 724079b462304e72
coverage: 0.894737
learned_at: 2026-10-23 10:55:31
nodes: [PrimitiveNode, TextEncodeQwenImageEditPlus, CLIPTextEncode, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, KSampler, EmptyLatentImage, LoadImage, SaveImage, SaveImage, VAEDecode, CustomAddLabel, RunningHub Deepcleaner, SeedVR2, GetImageSize, ImageScaleToTotalPixels, JjkText]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 529402642099083, "steps": 8, "width": 1920}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-Edit 1.1-[人像] 原生肌理·去AI·去塑料-电影感-高清直出_2045102299755847682.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1-[人像] 原生肌理·去AI·去塑料-电影感-高清直出_2045102299755847682.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `PrimitiveNode`
- `TextEncodeQwenImageEditPlus`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `CustomAddLabel`
- `RunningHub Deepcleaner`
- `SeedVR2`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `JjkText`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `529402642099083`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`TextEncodeQwenImageEditPlus`、`CLIPTextEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`KSampler`、`EmptyLatentImage`、`LoadImage`、`SaveImage`、`VAEDecode`、`CustomAddLabel`、`RunningHub Deepcleaner`、`SeedVR2`、`GetImageSize`、`ImageScaleToTotalPixels`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
