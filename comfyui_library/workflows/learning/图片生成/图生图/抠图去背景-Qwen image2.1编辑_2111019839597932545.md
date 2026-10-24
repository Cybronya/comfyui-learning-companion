---
key: 图片生成/图生图/抠图去背景-Qwen image2.1编辑_2111019839597932545.json
name: 抠图去背景-Qwen image2.1编辑_2111019839597932545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/抠图去背景-Qwen image2.1编辑_2111019839597932545.json
hash: 7c192b1ba641f203
coverage: 0.866667
learned_at: 2026-10-23 12:55:12
nodes: [SaveImage, Image Comparer (rgthree), VAELoader, VAEDecode, UNETLoader, PrimitiveStringMultiline, CLIPLoader, TextEncodeQwenImage21, EmptyLatentImage, QwenImage21Cache, KSampler, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, GetImageSize]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 508493878500646, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/抠图去背景-Qwen image2.1编辑_2111019839597932545.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/抠图去背景-Qwen image2.1编辑_2111019839597932545.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `SaveImage`
- `Image Comparer (rgthree)`
- `VAELoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `GetImageSize`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `508493878500646`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`SaveImage`、`VAELoader`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`QwenImage21Cache`、`KSampler`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`GetImageSize`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
