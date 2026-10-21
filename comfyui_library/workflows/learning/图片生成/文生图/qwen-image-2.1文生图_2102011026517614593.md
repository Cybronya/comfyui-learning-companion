---
key: 图片生成/文生图/qwen-image-2.1文生图_2102011026517614593.json
name: qwen-image-2.1文生图_2102011026517614593
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-image-2.1文生图_2102011026517614593.json
hash: 06892eba60e1f5fa
coverage: 1
learned_at: 2026-10-20 01:51:57
nodes: [CLIPLoader, UNETLoader, KSampler, VAEDecode, VAELoader, TextEncodeQwenImage21, SaveImage, SaveImageAdvanced, EmptyLatentImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2048, "sampler_name": "euler", "scheduler": "simple", "seed": 1075335174517950, "steps": 25, "width": 2048}
---

# 图片生成/文生图/qwen-image-2.1文生图_2102011026517614593.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen-image-2.1文生图_2102011026517614593.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output

**节点**（9 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `TextEncodeQwenImage21`
- `SaveImage`
- `SaveImageAdvanced`
- `EmptyLatentImage` ★核心

## 关键参数

- `seed` = `1075335174517950`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `2048`
- `height` = `2048`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`CLIPLoader`、`UNETLoader`、`KSampler`、`VAEDecode`、`VAELoader`、`TextEncodeQwenImage21`、`SaveImage`、`SaveImageAdvanced`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、UNETLoader、SaveImage
