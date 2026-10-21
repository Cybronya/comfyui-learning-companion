---
key: 图片生成/文生图/Qwen Image 2.1 文生图 25步官流_2101767103564050433.json
name: Qwen Image 2.1 文生图 25步官流_2101767103564050433
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 文生图 25步官流_2101767103564050433.json
hash: 575b686ce5b5c52e
coverage: 1
learned_at: 2026-10-20 01:50:53
nodes: [Text Multiline, VAELoader, TextEncodeQwenImage21, KSampler, VAEDecode, EmptyLatentImage, CLIPLoader, UNETLoader, ResolutionSelector, easy seed, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen Image 2.1 文生图 25步官流_2101767103564050433.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 文生图 25步官流_2101767103564050433.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（11 个）：
- `Text Multiline`
- `VAELoader`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `ResolutionSelector`
- `easy seed`
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

覆盖率 **100%**（11/11）

**有卡**：`Text Multiline`、`VAELoader`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`EmptyLatentImage`、`CLIPLoader`、`UNETLoader`、`ResolutionSelector`、`easy seed`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
