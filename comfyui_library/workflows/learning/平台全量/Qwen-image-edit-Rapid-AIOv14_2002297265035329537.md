---
key: 平台全量/Qwen-image-edit-Rapid-AIOv14_2002297265035329537.json
name: Qwen-image-edit-Rapid-AIOv14_2002297265035329537
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-image-edit-Rapid-AIOv14_2002297265035329537.json
hash: 5e3a70609132f768
coverage: 1
learned_at: 2026-11-14 00:52:09
nodes: [VAEDecode, EmptyLatentImage, CLIPTextEncode, KSampler, TextEncodeQwenImageEditPlus, CheckpointLoaderSimple, GetImage, ImageScaleToTotalPixels, ImageScaleToTotalPixels, LoadImage, SaveImage, LoadImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v14.1.safetensors", "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 205344663222365, "steps": 4, "width": 768}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Qwen-image-edit-Rapid-AIOv14_2002297265035329537.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-image-edit-Rapid-AIOv14_2002297265035329537.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlus`
- `CheckpointLoaderSimple` ★核心
- `GetImage`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `SaveImage`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `768`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `205344663222365`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v14.1.safetensors`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`VAEDecode`、`EmptyLatentImage`、`CLIPTextEncode`、`KSampler`、`TextEncodeQwenImageEditPlus`、`CheckpointLoaderSimple`、`GetImage`、`ImageScaleToTotalPixels`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、TextEncodeQwenImageEditPlus、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
