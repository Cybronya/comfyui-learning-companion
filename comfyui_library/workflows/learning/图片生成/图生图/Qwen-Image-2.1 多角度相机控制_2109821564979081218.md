---
key: 图片生成/图生图/Qwen-Image-2.1 多角度相机控制_2109821564979081218.json
name: Qwen-Image-2.1 多角度相机控制_2109821564979081218
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 多角度相机控制_2109821564979081218.json
hash: 428410159f446b4e
coverage: 0.897436
learned_at: 2026-10-23 11:16:26
nodes: [CLIPLoader, VAELoader, EmptyLatentImage, GetImageSize, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, KSampler, UNETLoader, QwenImage21Cache, LoraLoaderModelOnly, VAEDecode, SaveImage, TextEncodeQwenImage21, QwenMultiangleCameraNode, CLIPLoader, VAELoader, EmptyLatentImage, GetImageSize, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, KSampler, QwenImage21Cache, LoraLoaderModelOnly, VAEDecode, UNETLoader, LoadImage, SaveImage, Image Comparer (rgthree), easy promptList, easy showAnything, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, LoadImage, ImageResizeKJv2, TextEncodeQwenImage21]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 788226333990963, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Image-2.1 多角度相机控制_2109821564979081218.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 多角度相机控制_2109821564979081218.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `GetImageSize`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `TextEncodeQwenImage21`
- `QwenMultiangleCameraNode`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `GetImageSize`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `KSampler` ★核心
- `QwenImage21Cache`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `easy promptList`
- `easy showAnything`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `LoadImage`
- `ImageResizeKJv2`
- `TextEncodeQwenImage21`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `788226333990963`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（35/39）

**有卡**：`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`GetImageSize`、`ResolutionSelector`、`KSampler`、`UNETLoader`、`QwenImage21Cache`、`LoraLoaderModelOnly`、`VAEDecode`、`SaveImage`、`TextEncodeQwenImage21`、`QwenMultiangleCameraNode`、`LoadImage`、`easy promptList`、`ImageResizeKJv2`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
