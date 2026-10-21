---
key: 图片生成/文生图/文字生成图片（Qwen-Image 2.1）_2107738529978732546.json
name: 文字生成图片（Qwen-Image 2.1）_2107738529978732546
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文字生成图片（Qwen-Image 2.1）_2107738529978732546.json
hash: 838dfa4a905d9cd7
coverage: 0.9
learned_at: 2026-10-21 03:00:12
nodes: [MarkdownNote, UNETLoader, CLIPLoader, VAELoader, QwenImage21Cache, TextEncodeQwenImage21, EmptyLatentImage, KSampler, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
---

# 图片生成/文生图/文字生成图片（Qwen-Image 2.1）_2107738529978732546.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文字生成图片（Qwen-Image 2.1）_2107738529978732546.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（10 个）：
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `0`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、QwenImage21Cache、UNETLoader
