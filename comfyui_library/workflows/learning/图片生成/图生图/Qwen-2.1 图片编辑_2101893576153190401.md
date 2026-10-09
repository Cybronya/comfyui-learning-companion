---
key: 图片生成/图生图/Qwen-2.1 图片编辑_2101893576153190401.json
name: Qwen-2.1 图片编辑_2101893576153190401.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-2.1 图片编辑_2101893576153190401.json
hash: b9483ef1027b2019
coverage: 0.684211
learned_at: 2026-10-09 22:19:27
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, Label (rgthree), LoadImage, LoadImage, ResolutionSelector, UNETLoader, VAELoader, TextEncodeQwenImage21, QwenImage21Cache, KSampler, EmptyLatentImage, MultiTextConcatenate, JjkText, JjkText, VAEDecode, SaveImage, CLIPLoader]
patterns: []
missing: [Label (rgthree)]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 249413519482856, "steps": 25, "width": 1024}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/Qwen-2.1 图片编辑_2101893576153190401.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2101893576153190401.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（19 个）：
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `Label (rgthree)`
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `VAELoader`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `MultiTextConcatenate`
- `JjkText`
- `JjkText`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPLoader`

## 关键参数

- `seed` = `249413519482856`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **68%**（13/19）

**有卡**：`LoadImage`、`ResolutionSelector`、`UNETLoader`、`VAELoader`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`KSampler`、`EmptyLatentImage`、`MultiTextConcatenate`、`VAEDecode`、`SaveImage`、`CLIPLoader`

**缺卡**（1）：`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
