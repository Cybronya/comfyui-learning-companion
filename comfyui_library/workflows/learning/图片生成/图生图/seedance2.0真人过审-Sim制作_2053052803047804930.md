---
key: 图片生成/图生图/seedance2.0真人过审-Sim制作_2053052803047804930.json
name: seedance2.0真人过审-Sim制作_2053052803047804930
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/seedance2.0真人过审-Sim制作_2053052803047804930.json
hash: 98db82bf593b5eae
coverage: 0.882353
learned_at: 2026-10-23 11:45:12
nodes: [VAELoader, CLIPLoader, UNETLoader, LoraLoaderModelOnly, ImageScaleToTotalPixels, GetImageSize, EmptyLatentImage, PrimitiveNode, TextEncodeQwenImageEditPlus, KSampler, VAEDecode, easy cleanGpuUsed, CLIPTextEncode, JjkText, SeedVR2, LoadImage, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 400856844246881, "steps": 8, "width": 720}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/seedance2.0真人过审-Sim制作_2053052803047804930.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/seedance2.0真人过审-Sim制作_2053052803047804930.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `EmptyLatentImage` ★核心
- `PrimitiveNode`
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `JjkText`
- `SeedVR2`
- `LoadImage`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `400856844246881`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`ImageScaleToTotalPixels`、`GetImageSize`、`EmptyLatentImage`、`TextEncodeQwenImageEditPlus`、`KSampler`、`VAEDecode`、`easy cleanGpuUsed`、`CLIPTextEncode`、`SeedVR2`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
