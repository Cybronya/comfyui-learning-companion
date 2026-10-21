---
key: 图片生成/文生图/Qwen-Image-2.1 文生图_2102343034200477698.json
name: Qwen-Image-2.1 文生图_2102343034200477698
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1 文生图_2102343034200477698.json
hash: 2e8424b91b6f3ac5
coverage: 0.75
learned_at: 2026-10-20 01:51:15
nodes: [KSampler, VAELoader, EmptyLatentImage, ResolutionSelector, MarkdownNote, MarkdownNote, MarkdownNote, TextEncodeQwenImage21, UNETLoader, CLIPLoader, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen-Image-2.1 文生图_2102343034200477698.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1 文生图_2102343034200477698.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（12 个）：
- `KSampler` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `0`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **75%**（9/12）

**有卡**：`KSampler`、`VAELoader`、`EmptyLatentImage`、`ResolutionSelector`、`TextEncodeQwenImage21`、`UNETLoader`、`CLIPLoader`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
