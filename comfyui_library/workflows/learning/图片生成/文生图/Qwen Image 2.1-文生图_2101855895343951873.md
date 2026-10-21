---
key: 图片生成/文生图/Qwen Image 2.1-文生图_2101855895343951873.json
name: Qwen Image 2.1-文生图_2101855895343951873
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1-文生图_2101855895343951873.json
hash: e4f320eee952009f
coverage: 0.769231
learned_at: 2026-10-20 01:50:54
nodes: [MarkdownNote, CLIPLoader, UNETLoader, EmptyLatentImage, VAELoader, ResolutionSelector, MarkdownNote, TextEncodeQwenImage21, PrimitiveStringMultiline, VAEDecode, SaveImageAdvanced, SaveImage, KSampler]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen Image 2.1-文生图_2101855895343951873.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1-文生图_2101855895343951873.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `MarkdownNote`
- `CLIPLoader`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `ResolutionSelector`
- `MarkdownNote`
- `TextEncodeQwenImage21`
- `PrimitiveStringMultiline`
- `VAEDecode` ★核心
- `SaveImageAdvanced`
- `SaveImage`
- `KSampler` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `42`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（10/13）

**有卡**：`CLIPLoader`、`UNETLoader`、`EmptyLatentImage`、`VAELoader`、`ResolutionSelector`、`TextEncodeQwenImage21`、`VAEDecode`、`SaveImageAdvanced`、`SaveImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
