---
key: 图片生成/文生图/文生图-qwen image2.1_2104155833666990081.json
name: 文生图-qwen image2.1_2104155833666990081
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图-qwen image2.1_2104155833666990081.json
hash: 197cbf4c7340129c
coverage: 0.909091
learned_at: 2026-10-10 20:59:47
nodes: [VAEDecode, VAELoader, UNETLoader, CLIPLoader, KSampler, MarkdownNote, EmptyLatentImage, SaveImageAdvanced, TextEncodeQwenImage21, ResolutionSelector, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
---

# 图片生成/文生图/文生图-qwen image2.1_2104155833666990081.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图-qwen image2.1_2104155833666990081.json`

## 结构

**节点**（11 个）：
- `VAEDecode`
- `VAELoader`
- `UNETLoader`
- `CLIPLoader`
- `KSampler`
- `MarkdownNote`
- `EmptyLatentImage`
- `SaveImageAdvanced`
- `TextEncodeQwenImage21`
- `ResolutionSelector`
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

覆盖率 **91%**（10/11）

**有卡**：`VAEDecode`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`KSampler`、`MarkdownNote`、`EmptyLatentImage`、`SaveImageAdvanced`、`TextEncodeQwenImage21`、`ResolutionSelector`
