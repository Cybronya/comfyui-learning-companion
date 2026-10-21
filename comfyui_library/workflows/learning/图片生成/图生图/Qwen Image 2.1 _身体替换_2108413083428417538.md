---
key: 图片生成/图生图/Qwen Image 2.1 _身体替换_2108413083428417538.json
name: Qwen Image 2.1 _身体替换_2108413083428417538
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 _身体替换_2108413083428417538.json
hash: 961c102ddc446f3f
coverage: 0.605263
learned_at: 2026-10-21 00:42:08
nodes: [GetNode, GetNode, VAELoader, CLIPLoader, UNETLoader, MarkdownNote, VAEDecode, ImageConcatMulti, GetNode, GetNode, GetNode, EmptyLatentImage, MarkdownNote, SaveImageAdvanced, Image Comparer (rgthree), SetNode, SetNode, GetNode, SetNode, ImageResizeKJv2, ImageResizeKJv2, RemoveBackground, LoadBackgroundRemovalModel, JoinImageWithAlpha, InvertMask, SetNode, QwenImage21Cache, LoraLoaderModelOnly, KSampler, GetNode, TextEncodeQwenImage21, LoadImage, LoadImage, LoraLoaderModelOnly, AddLabel, SaveImage, Image Comparer (rgthree), ResolutionSelector]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "deis_2m", "scheduler": "simple", "seed": 42, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1 _身体替换_2108413083428417538.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 _身体替换_2108413083428417538.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `GetNode`
- `GetNode`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `MarkdownNote`
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLatentImage` ★核心
- `MarkdownNote`
- `SaveImageAdvanced`
- `Image Comparer (rgthree)`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `RemoveBackground`
- `LoadBackgroundRemovalModel`
- `JoinImageWithAlpha`
- `InvertMask`
- `SetNode`
- `QwenImage21Cache`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `GetNode`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `AddLabel`
- `SaveImage`
- `Image Comparer (rgthree)`
- `ResolutionSelector`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `42`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `deis_2m`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **61%**（23/38）

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`VAEDecode`、`ImageConcatMulti`、`EmptyLatentImage`、`SaveImageAdvanced`、`ImageResizeKJv2`、`RemoveBackground`、`LoadBackgroundRemovalModel`、`JoinImageWithAlpha`、`InvertMask`、`QwenImage21Cache`、`LoraLoaderModelOnly`、`KSampler`、`TextEncodeQwenImage21`、`LoadImage`、`AddLabel`、`SaveImage`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
