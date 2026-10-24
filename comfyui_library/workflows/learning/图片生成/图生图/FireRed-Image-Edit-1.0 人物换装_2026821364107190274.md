---
key: 图片生成/图生图/FireRed-Image-Edit-1.0 人物换装_2026821364107190274.json
name: FireRed-Image-Edit-1.0 人物换装_2026821364107190274
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit-1.0 人物换装_2026821364107190274.json
hash: 3bdae8589aa661f1
coverage: 0.809524
learned_at: 2026-10-23 10:55:41
nodes: [CLIPLoader, VAELoader, KSampler, LoadImage, UNETLoader, LoadImage, FluxKontextImageScale, TextEncodeQwenImageEditPlus, EmptyLatentImage, Reroute, Reroute, Reroute, FluxKontextImageScale, GetImageSize, LoraLoaderModelOnly, LoadImage, VAEDecode, FluxKontextImageScale, SaveImage, Image Comparer (rgthree), TextEncodeQwenImageEditPlus]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 390180897168833, "steps": 8, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-Edit-1.0 人物换装_2026821364107190274.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit-1.0 人物换装_2026821364107190274.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `LoadImage`
- `UNETLoader` ★核心
- `LoadImage`
- `FluxKontextImageScale`
- `TextEncodeQwenImageEditPlus`
- `EmptyLatentImage` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `FluxKontextImageScale`
- `GetImageSize`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `VAEDecode` ★核心
- `FluxKontextImageScale`
- `SaveImage`
- `Image Comparer (rgthree)`
- `TextEncodeQwenImageEditPlus`

## 关键参数

- `seed` = `390180897168833`
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

**有卡**：`CLIPLoader`、`VAELoader`、`KSampler`、`LoadImage`、`UNETLoader`、`FluxKontextImageScale`、`TextEncodeQwenImageEditPlus`、`EmptyLatentImage`、`GetImageSize`、`LoraLoaderModelOnly`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
