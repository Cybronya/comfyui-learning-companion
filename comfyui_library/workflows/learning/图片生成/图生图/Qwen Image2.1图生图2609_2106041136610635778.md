---
key: 图片生成/图生图/Qwen Image2.1图生图2609_2106041136610635778.json
name: Qwen Image2.1图生图2609_2106041136610635778
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image2.1图生图2609_2106041136610635778.json
hash: 8357131478c2f430
coverage: 0.833333
learned_at: 2026-10-10 20:48:08
nodes: [UNETLoader, CLIPLoader, MarkdownNote, MarkdownNote, EmptyLatentImage, VAELoader, ResolutionSelector, TextEncodeQwenImage21, KSampler, VAEDecode, SaveImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 577555063525252, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen Image2.1图生图2609_2106041136610635778.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image2.1图生图2609_2106041136610635778.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（12 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `MarkdownNote`
- `MarkdownNote`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `ResolutionSelector`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `577555063525252`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`UNETLoader`、`CLIPLoader`、`EmptyLatentImage`、`VAELoader`、`ResolutionSelector`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
