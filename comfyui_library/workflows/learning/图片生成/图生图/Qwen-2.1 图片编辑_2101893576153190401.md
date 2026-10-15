---
key: 图片生成/图生图/Qwen-2.1 图片编辑_2101893576153190401.json
name: Qwen-2.1 图片编辑_2101893576153190401
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-2.1 图片编辑_2101893576153190401.json
hash: b9483ef1027b2019
coverage: 0.736842
learned_at: 2026-10-15 22:25:21
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, Label (rgthree), LoadImage, LoadImage, ResolutionSelector, UNETLoader, VAELoader, TextEncodeQwenImage21, QwenImage21Cache, KSampler, EmptyLatentImage, MultiTextConcatenate, JjkText, JjkText, VAEDecode, SaveImage, CLIPLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 249413519482856, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen-2.1 图片编辑_2101893576153190401.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-2.1 图片编辑_2101893576153190401.json`

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

覆盖率 **74%**（14/19）

**有卡**：`Label (rgthree)`、`LoadImage`、`ResolutionSelector`、`UNETLoader`、`VAELoader`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`KSampler`、`EmptyLatentImage`、`MultiTextConcatenate`、`VAEDecode`、`SaveImage`、`CLIPLoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
