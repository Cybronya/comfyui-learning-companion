---
key: 图片生成/文生图/Qwen Image 2.1：文生图_2101751274873122818.json
name: Qwen Image 2.1：文生图_2101751274873122818
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1：文生图_2101751274873122818.json
hash: df9bf98f18100c80
coverage: 0.65
learned_at: 2026-10-07 02:22:24
nodes: [ResolutionSelector, MarkdownNote, MarkdownNote, MarkdownNote, UNETLoader, TextEncodeQwenImage21, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, PreviewAny, CLIPLoader, PrimitiveStringMultiline, QwenImage21Cache, SaveImage, SaveImageAdvanced, ComfySwitchNode, KSampler, TextGenerate, JjkText]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 560836252052479, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen Image 2.1：文生图_2101751274873122818.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1：文生图_2101751274873122818.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（20 个）：
- `ResolutionSelector`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `PreviewAny`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `SaveImage`
- `SaveImageAdvanced`
- `ComfySwitchNode`
- `KSampler` ★核心
- `TextGenerate`
- `JjkText`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `560836252052479`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **65%**（13/20）

**有卡**：`ResolutionSelector`、`UNETLoader`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`QwenImage21Cache`、`SaveImage`、`SaveImageAdvanced`、`KSampler`、`TextGenerate`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache
