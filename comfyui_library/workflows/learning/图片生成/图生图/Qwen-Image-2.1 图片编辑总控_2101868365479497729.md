---
key: 图片生成/图生图/Qwen-Image-2.1 图片编辑总控_2101868365479497729.json
name: Qwen-Image-2.1 图片编辑总控_2101868365479497729
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 图片编辑总控_2101868365479497729.json
hash: 5dee106588c1b9db
coverage: 0.785714
learned_at: 2026-10-21 00:43:13
nodes: [MarkdownNote, Image Comparer (rgthree), LoadImage, MarkdownNote, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, MarkdownNote, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, QwenImage21Cache, Label (rgthree), Label (rgthree), Fast Groups Bypasser (rgthree), LoadImage, KSampler, ComfySwitchNode, ResolutionSelector, VAEDecode, SaveImage, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 885102754078274, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen-Image-2.1 图片编辑总控_2101868365479497729.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 图片编辑总控_2101868365479497729.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（28 个）：
- `MarkdownNote`
- `Image Comparer (rgthree)`
- `LoadImage`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `Label (rgthree)`
- `Label (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `KSampler` ★核心
- `ComfySwitchNode`
- `ResolutionSelector`
- `VAEDecode` ★核心
- `SaveImage`
- `TextEncodeQwenImage21`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `885102754078274`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（22/28）

**有卡**：`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`QwenImage21Cache`、`Label (rgthree)`、`KSampler`、`ResolutionSelector`、`VAEDecode`、`SaveImage`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
