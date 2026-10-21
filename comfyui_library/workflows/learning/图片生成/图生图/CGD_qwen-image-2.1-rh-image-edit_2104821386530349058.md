---
key: 图片生成/图生图/CGD_qwen-image-2.1-rh-image-edit_2104821386530349058.json
name: CGD_qwen-image-2.1-rh-image-edit_2104821386530349058
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/CGD_qwen-image-2.1-rh-image-edit_2104821386530349058.json
hash: 2b3c80d9af88d4e6
coverage: 0.806452
learned_at: 2026-10-21 00:38:50
nodes: [MarkdownNote, MarkdownNote, EmptyLatentImage, VAEDecode, KSampler, ComfySwitchNode, QwenImage21Cache, ComfySwitchNode, TextGenerate, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline, PreviewAny, ImageCompare, CLIPLoader, CLIPLoader, VAELoader, UNETLoader, BatchImagesNode, LoadImage, LoadImage, TextEncodeQwenImage21, SaveImageAdvanced, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 819783454393719, "steps": 25, "width": 1024}
---

# 图片生成/图生图/CGD_qwen-image-2.1-rh-image-edit_2104821386530349058.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/CGD_qwen-image-2.1-rh-image-edit_2104821386530349058.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `MarkdownNote`
- `MarkdownNote`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `ComfySwitchNode`
- `TextGenerate`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `PreviewAny`
- `ImageCompare`
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `BatchImagesNode`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `SaveImageAdvanced`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `819783454393719`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（25/31）

**有卡**：`EmptyLatentImage`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`TextGenerate`、`TextEncodeQwenImage21`、`LoadImage`、`ImageCompare`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`BatchImagesNode`、`SaveImageAdvanced`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
