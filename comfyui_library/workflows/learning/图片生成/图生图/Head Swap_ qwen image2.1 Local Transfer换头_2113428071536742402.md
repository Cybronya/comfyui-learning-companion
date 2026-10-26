---
key: 图片生成/图生图/Head Swap_ qwen image2.1 Local Transfer换头_2113428071536742402.json
name: Head Swap_ qwen image2.1 Local Transfer换头_2113428071536742402
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Head Swap_ qwen image2.1 Local Transfer换头_2113428071536742402.json
hash: 20024a28b9d6c22a
coverage: 0.647059
learned_at: 2026-10-26 22:01:59
nodes: [GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, VAELoader, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, EmptyLatentImage, GetNode, KSampler, UNETLoader, TextEncodeQwenImage21, GetNode, SetNode, CR Text, QwenImage21Cache, SaveImage, ImageResizeKJv2, ResolutionSelector, ImageResizeKJv2, SaveImageAdvanced, AddLabel, ImageConcatMulti, ImageConcatMulti, LoadImage, LoadImage, VAEDecode, GetNode, Image Comparer (rgthree), LoraLoaderModelOnly]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Head Swap_ qwen image2.1 Local Transfer换头_2113428071536742402.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Head Swap_ qwen image2.1 Local Transfer换头_2113428071536742402.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyLatentImage` ★核心
- `GetNode`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `GetNode`
- `SetNode`
- `CR Text`
- `QwenImage21Cache`
- `SaveImage`
- `ImageResizeKJv2`
- `ResolutionSelector`
- `ImageResizeKJv2`
- `SaveImageAdvanced`
- `AddLabel`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `LoadImage`
- `LoadImage`
- `VAEDecode` ★核心
- `GetNode`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `42`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **65%**（22/34）

**有卡**：`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`KSampler`、`UNETLoader`、`TextEncodeQwenImage21`、`CR Text`、`QwenImage21Cache`、`SaveImage`、`ImageResizeKJv2`、`ResolutionSelector`、`SaveImageAdvanced`、`AddLabel`、`ImageConcatMulti`、`LoadImage`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
