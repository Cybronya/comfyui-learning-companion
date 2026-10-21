---
key: 图片生成/图生图/一键换头-qwen image2.1最新迁移_2107910635219668994.json
name: 一键换头-qwen image2.1最新迁移_2107910635219668994
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/一键换头-qwen image2.1最新迁移_2107910635219668994.json
hash: e3f67da7b8d3c100
coverage: 0.628571
learned_at: 2026-10-21 00:46:51
nodes: [GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, VAELoader, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, EmptyLatentImage, GetNode, LoraLoaderModelOnly, KSampler, UNETLoader, TextEncodeQwenImage21, GetNode, SetNode, CR Text, QwenImage21Cache, SaveImage, ImageResizeKJv2, ResolutionSelector, ImageResizeKJv2, GetNode, Image Comparer (rgthree), SaveImageAdvanced, VAEDecode, AddLabel, LoadImage, ImageConcatMulti, ImageConcatMulti, LoadImage, MarkdownNote]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/一键换头-qwen image2.1最新迁移_2107910635219668994.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/一键换头-qwen image2.1最新迁移_2107910635219668994.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
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
- `LoraLoaderModelOnly` ★核心
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
- `GetNode`
- `Image Comparer (rgthree)`
- `SaveImageAdvanced`
- `VAEDecode` ★核心
- `AddLabel`
- `LoadImage`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `LoadImage`
- `MarkdownNote`

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

覆盖率 **63%**（22/35）

**有卡**：`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`KSampler`、`UNETLoader`、`TextEncodeQwenImage21`、`CR Text`、`QwenImage21Cache`、`SaveImage`、`ImageResizeKJv2`、`ResolutionSelector`、`SaveImageAdvanced`、`VAEDecode`、`AddLabel`、`LoadImage`、`ImageConcatMulti`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
