---
key: 图片生成/文生图/Qwen Image2.1文生图2609_2106041124522643458.json
name: Qwen Image2.1文生图2609_2106041124522643458
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image2.1文生图2609_2106041124522643458.json
hash: eba2e077a12a6aa2
coverage: 0.75
learned_at: 2026-10-07 02:23:33
nodes: [MarkdownNote, MarkdownNote, TextEncodeQwenImage21, SaveImage, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, KSampler, VAEDecode, Text Multiline, ResolutionSelector]
patterns: []
missing: [Text Multiline]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 831376256341051, "steps": 25, "width": 1024}
discoveries: [次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Qwen Image2.1文生图2609_2106041124522643458.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image2.1文生图2609_2106041124522643458.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（12 个）：
- `MarkdownNote`
- `MarkdownNote`
- `TextEncodeQwenImage21`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Text Multiline`
- `ResolutionSelector`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `831376256341051`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **75%**（9/12）

**有卡**：`TextEncodeQwenImage21`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`ResolutionSelector`

**缺卡**（1）：`Text Multiline`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader

## 学习发现

- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
