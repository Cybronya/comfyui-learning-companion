---
key: 图片生成/文生图/文生图-qwen image2.1_2101922635541213185.json
name: 文生图-qwen image2.1_2101922635541213185
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图-qwen image2.1_2101922635541213185.json
hash: 67bb60ce50ab79c9
coverage: 0.909091
learned_at: 2026-10-20 01:52:46
nodes: [VAEDecode, VAELoader, UNETLoader, CLIPLoader, KSampler, MarkdownNote, TextEncodeQwenImage21, EmptyLatentImage, ResolutionSelector, SaveImage, SaveImageAdvanced]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
---

# 图片生成/文生图/文生图-qwen image2.1_2101922635541213185.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图-qwen image2.1_2101922635541213185.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（11 个）：
- `VAEDecode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `MarkdownNote`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `SaveImage`
- `SaveImageAdvanced`

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

**有卡**：`VAEDecode`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`KSampler`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`ResolutionSelector`、`SaveImage`、`SaveImageAdvanced`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
