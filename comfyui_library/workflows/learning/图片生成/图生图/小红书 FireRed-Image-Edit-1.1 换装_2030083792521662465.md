---
key: 图片生成/图生图/小红书 FireRed-Image-Edit-1.1 换装_2030083792521662465.json
name: 小红书 FireRed-Image-Edit-1.1 换装_2030083792521662465
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/小红书 FireRed-Image-Edit-1.1 换装_2030083792521662465.json
hash: 202ae2894e89b3be
coverage: 0.809524
learned_at: 2026-10-23 12:49:00
nodes: [CLIPLoader, VAELoader, KSampler, FluxKontextImageScale, TextEncodeQwenImageEditPlus, EmptyLatentImage, Reroute, Reroute, Reroute, GetImageSize, VAEDecode, FluxKontextImageScale, SaveImage, Image Comparer (rgthree), UNETLoader, LoraLoaderModelOnly, LoadImage, LoadImage, LoadImage, FluxKontextImageScale, TextEncodeQwenImageEditPlus]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 263168454641244, "steps": 8, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/小红书 FireRed-Image-Edit-1.1 换装_2030083792521662465.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/小红书 FireRed-Image-Edit-1.1 换装_2030083792521662465.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `FluxKontextImageScale`
- `TextEncodeQwenImageEditPlus`
- `EmptyLatentImage` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `GetImageSize`
- `VAEDecode` ★核心
- `FluxKontextImageScale`
- `SaveImage`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `FluxKontextImageScale`
- `TextEncodeQwenImageEditPlus`

## 关键参数

- `seed` = `263168454641244`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（17/21）

**有卡**：`CLIPLoader`、`VAELoader`、`KSampler`、`FluxKontextImageScale`、`TextEncodeQwenImageEditPlus`、`EmptyLatentImage`、`GetImageSize`、`VAEDecode`、`SaveImage`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
