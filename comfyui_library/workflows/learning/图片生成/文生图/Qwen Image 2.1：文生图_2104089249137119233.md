---
key: 图片生成/文生图/Qwen Image 2.1：文生图_2104089249137119233.json
name: Qwen Image 2.1：文生图_2104089249137119233
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1：文生图_2104089249137119233.json
hash: 870a04411bc05848
coverage: 0.833333
learned_at: 2026-10-07 02:22:27
nodes: [ResolutionSelector, MarkdownNote, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, MarkdownNote, KSampler, SaveImageAdvanced, SaveImage, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 694882236846726, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen Image 2.1：文生图_2104089249137119233.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1：文生图_2104089249137119233.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（12 个）：
- `ResolutionSelector`
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `MarkdownNote`
- `KSampler` ★核心
- `SaveImageAdvanced`
- `SaveImage`
- `TextEncodeQwenImage21`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `694882236846726`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`SaveImageAdvanced`、`SaveImage`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
