---
key: 图片生成/图生图/qwen-image-2.1：官方原版图生图工作流_2101686169661693953.json
name: qwen-image-2.1：官方原版图生图工作流_2101686169661693953.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image-2.1：官方原版图生图工作流_2101686169661693953.json
hash: 6d9628c7be614820
coverage: 0.8
learned_at: 2026-10-09 22:19:27
nodes: [QwenImage21Cache, ComfySwitchNode, KSampler, VAELoader, ResolutionSelector, EmptyLatentImage, UNETLoader, CLIPLoader, SaveImage, LoadImage, LoadImage, TextEncodeQwenImage21, VAEDecode, MarkdownNote, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 335964428442202, "steps": 25, "width": 1024}
---

# 图片生成/图生图/qwen-image-2.1：官方原版图生图工作流_2101686169661693953.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2101686169661693953.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `QwenImage21Cache`
- `ComfySwitchNode`
- `KSampler` ★核心
- `VAELoader`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `MarkdownNote`
- `MarkdownNote`

## 关键参数

- `seed` = `335964428442202`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（12/15）

**有卡**：`QwenImage21Cache`、`KSampler`、`VAELoader`、`ResolutionSelector`、`EmptyLatentImage`、`UNETLoader`、`CLIPLoader`、`SaveImage`、`LoadImage`、`TextEncodeQwenImage21`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
