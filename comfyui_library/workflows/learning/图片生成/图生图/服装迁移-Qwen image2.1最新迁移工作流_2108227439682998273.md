---
key: 图片生成/图生图/服装迁移-Qwen image2.1最新迁移工作流_2108227439682998273.json
name: 服装迁移-Qwen image2.1最新迁移工作流_2108227439682998273
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/服装迁移-Qwen image2.1最新迁移工作流_2108227439682998273.json
hash: 430bf93cfdbdaf6e
coverage: 0.65
learned_at: 2026-10-21 00:54:30
nodes: [GetNode, Note, GetNode, SetNode, RemoveBackground, LoadBackgroundRemovalModel, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, Image Comparer (rgthree), ImageResizeKJv2, ImageConcatMulti, SaveImageAdvanced, AddLabel, LoraLoaderModelOnly, LoadImage, ImageResizeKJv2, ResolutionSelector, SetNode, SetNode, JoinImageWithAlpha, InvertMask, UNETLoader, GetNode, CR Text, QwenImage21Cache, TextEncodeQwenImage21, GetNode, GetNode, EmptyLatentImage, KSampler, GetNode, GetNode, ImageConcatMulti, VAEDecode, SaveImage, LoadImage, MarkdownNote, SetNode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 456478698018723, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/服装迁移-Qwen image2.1最新迁移工作流_2108227439682998273.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/服装迁移-Qwen image2.1最新迁移工作流_2108227439682998273.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `GetNode`
- `Note`
- `GetNode`
- `SetNode`
- `RemoveBackground`
- `LoadBackgroundRemovalModel`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `ImageResizeKJv2`
- `ImageConcatMulti`
- `SaveImageAdvanced`
- `AddLabel`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `ImageResizeKJv2`
- `ResolutionSelector`
- `SetNode`
- `SetNode`
- `JoinImageWithAlpha`
- `InvertMask`
- `UNETLoader` ★核心
- `GetNode`
- `CR Text`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `GetNode`
- `GetNode`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `MarkdownNote`
- `SetNode`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `456478698018723`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **65%**（26/40）

**有卡**：`RemoveBackground`、`LoadBackgroundRemovalModel`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`ImageConcatMulti`、`SaveImageAdvanced`、`AddLabel`、`LoadImage`、`ResolutionSelector`、`JoinImageWithAlpha`、`InvertMask`、`UNETLoader`、`CR Text`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
