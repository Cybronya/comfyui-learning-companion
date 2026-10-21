---
key: 图片生成/图生图/Qwen-2.1 五视图-透明背景_2103379501370658818.json
name: Qwen-2.1 五视图-透明背景_2103379501370658818
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-2.1 五视图-透明背景_2103379501370658818.json
hash: 184fe812b07b55d2
coverage: 0.823529
learned_at: 2026-10-21 00:43:05
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, Label (rgthree), UNETLoader, LoadImage, VAELoader, CLIPLoader, TextEncodeQwenImage21, QwenImage21Cache, EmptyLatentImage, KSampler, CR Prompt List, HAIGC_SaveImagesToZip, VAEDecode, SaveImage, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 866485946042008, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen-2.1 五视图-透明背景_2103379501370658818.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-2.1 五视图-透明背景_2103379501370658818.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `Label (rgthree)`
- `UNETLoader` ★核心
- `LoadImage`
- `VAELoader`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `CR Prompt List`
- `HAIGC_SaveImagesToZip`
- `VAEDecode` ★核心
- `SaveImage`
- `ResolutionSelector`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `866485946042008`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`Label (rgthree)`、`UNETLoader`、`LoadImage`、`VAELoader`、`CLIPLoader`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`EmptyLatentImage`、`KSampler`、`CR Prompt List`、`HAIGC_SaveImagesToZip`、`VAEDecode`、`SaveImage`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
