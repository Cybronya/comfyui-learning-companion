---
key: qwen_image_2.1 _ 文生图_2103128462868443138.json
name: qwen_image_2.1 _ 文生图_2103128462868443138
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen_image_2.1 _ 文生图_2103128462868443138.json
hash: 27df6fbf0e8b11e5
coverage: 0.9
learned_at: 2026-10-10 20:59:25
nodes: [VAELoader, TextEncodeQwenImage21, VAEDecode, SaveImage, ResolutionSelector, UNETLoader, CLIPLoader, JjkText, EmptyLatentImage, KSampler]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 406067692802873, "steps": 25, "width": 1024}
---

# qwen_image_2.1 _ 文生图_2103128462868443138.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen_image_2.1 _ 文生图_2103128462868443138.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（10 个）：
- `VAELoader`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `SaveImage`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `CLIPLoader`
- `JjkText`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `406067692802873`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`VAELoader`、`TextEncodeQwenImage21`、`VAEDecode`、`SaveImage`、`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`EmptyLatentImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
