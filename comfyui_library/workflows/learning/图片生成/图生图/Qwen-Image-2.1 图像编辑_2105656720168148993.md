---
key: 图片生成/图生图/Qwen-Image-2.1 图像编辑_2105656720168148993.json
name: Qwen-Image-2.1 图像编辑_2105656720168148993
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 图像编辑_2105656720168148993.json
hash: 6bdde87633c43904
coverage: 0.8
learned_at: 2026-10-10 20:48:09
nodes: [QwenImage21Cache, ComfySwitchNode, KSampler, VAELoader, ResolutionSelector, EmptyLatentImage, MarkdownNote, MarkdownNote, MarkdownNote, UNETLoader, CLIPLoader, VAEDecode, SaveImage, LoadImage, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 557400715096322, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen-Image-2.1 图像编辑_2105656720168148993.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 图像编辑_2105656720168148993.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（20 个）：
- `QwenImage21Cache`
- `ComfySwitchNode`
- `KSampler` ★核心
- `VAELoader`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `557400715096322`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（16/20）

**有卡**：`QwenImage21Cache`、`KSampler`、`VAELoader`、`ResolutionSelector`、`EmptyLatentImage`、`UNETLoader`、`CLIPLoader`、`VAEDecode`、`SaveImage`、`LoadImage`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
