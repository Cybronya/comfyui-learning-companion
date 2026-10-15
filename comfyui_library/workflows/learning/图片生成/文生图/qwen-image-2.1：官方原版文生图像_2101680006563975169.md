---
key: 图片生成/文生图/qwen-image-2.1：官方原版文生图像_2101680006563975169.json
name: qwen-image-2.1：官方原版文生图像_2101680006563975169
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-image-2.1：官方原版文生图像_2101680006563975169.json
hash: 0867454789caa5f1
coverage: 0.818182
learned_at: 2026-10-10 20:59:25
nodes: [UNETLoader, CLIPLoader, VAELoader, KSampler, ResolutionSelector, EmptyLatentImage, TextEncodeQwenImage21, MarkdownNote, MarkdownNote, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
---

# 图片生成/文生图/qwen-image-2.1：官方原版文生图像_2101680006563975169.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen-image-2.1：官方原版文生图像_2101680006563975169.json`

## 结构

**节点**（11 个）：
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `KSampler`
- `ResolutionSelector`
- `EmptyLatentImage`
- `TextEncodeQwenImage21`
- `MarkdownNote`
- `MarkdownNote`
- `VAEDecode`
- `SaveImage`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `0`
- `steps` = `25`
- `width` = `1024`

## 知识

覆盖率 **82%**（9/11）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`ResolutionSelector`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`MarkdownNote`
