---
key: 图片生成/图生图/Qwen2.1图像编辑_（无PE）_2103535325745336321.json
name: Qwen2.1图像编辑_（无PE）_2103535325745336321
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1图像编辑_（无PE）_2103535325745336321.json
hash: a69de176fcf8df6d
coverage: 0.846154
learned_at: 2026-10-21 00:43:38
nodes: [Note, CLIPLoader, VAELoader, QwenImage21Cache, KSampler, UNETLoader, VAEDecode, SaveImage, LoadImage, MarkdownNote, easy seed, LoadImage, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 372980352069668, "steps": 40}
---

# 图片生成/图生图/Qwen2.1图像编辑_（无PE）_2103535325745336321.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1图像编辑_（无PE）_2103535325745336321.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `Note`
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `MarkdownNote`
- `easy seed`
- `LoadImage`
- `TextEncodeQwenImage21`

## 关键参数

- `seed` = `372980352069668`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`KSampler`、`UNETLoader`、`VAEDecode`、`SaveImage`、`LoadImage`、`easy seed`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
