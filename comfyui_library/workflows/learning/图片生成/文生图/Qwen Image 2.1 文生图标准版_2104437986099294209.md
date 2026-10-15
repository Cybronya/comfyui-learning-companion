---
key: 图片生成/文生图/Qwen Image 2.1 文生图标准版_2104437986099294209.json
name: Qwen Image 2.1 文生图标准版_2104437986099294209
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 文生图标准版_2104437986099294209.json
hash: 3de29a32fb1f3db6
coverage: 0.833333
learned_at: 2026-10-10 20:58:51
nodes: [UNETLoader, CLIPLoader, VAELoader, KSampler, VAEDecode, MarkdownNote, MarkdownNote, ResolutionSelector, EmptyLatentImage, SaveImage, SaveImageAdvanced, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen Image 2.1 文生图标准版_2104437986099294209.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 文生图标准版_2104437986099294209.json`

## 结构

**节点**（12 个）：
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `KSampler`
- `VAEDecode`
- `MarkdownNote`
- `MarkdownNote`
- `ResolutionSelector`
- `EmptyLatentImage`
- `SaveImage`
- `SaveImageAdvanced`
- `TextEncodeQwenImage21`

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

覆盖率 **83%**（10/12）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`VAEDecode`、`MarkdownNote`、`ResolutionSelector`、`EmptyLatentImage`、`SaveImage`
