---
key: 图片生成/文生图/文生图-qwen image2.1_2104155833666990081.json
name: 文生图-qwen image2.1_2104155833666990081
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图-qwen image2.1_2104155833666990081.json
hash: 197cbf4c7340129c
coverage: 0.909091
learned_at: 2026-10-07 02:00:27
nodes: [VAEDecode, VAELoader, UNETLoader, CLIPLoader, KSampler, MarkdownNote, EmptyLatentImage, SaveImageAdvanced, TextEncodeQwenImage21, ResolutionSelector, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
---

# 图片生成/文生图/文生图-qwen image2.1_2104155833666990081.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图-qwen image2.1_2104155833666990081.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（11 个）：
- `VAEDecode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `MarkdownNote`
- `EmptyLatentImage` ★核心
- `SaveImageAdvanced`
- `TextEncodeQwenImage21`
- `ResolutionSelector`
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

覆盖率 **91%**（10/11）

**有卡**：`VAEDecode`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`KSampler`、`EmptyLatentImage`、`SaveImageAdvanced`、`TextEncodeQwenImage21`、`ResolutionSelector`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
