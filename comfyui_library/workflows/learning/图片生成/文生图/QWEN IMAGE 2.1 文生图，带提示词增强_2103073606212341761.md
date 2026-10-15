---
key: 图片生成/文生图/QWEN IMAGE 2.1 文生图，带提示词增强_2103073606212341761.json
name: QWEN IMAGE 2.1 文生图，带提示词增强_2103073606212341761
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/QWEN IMAGE 2.1 文生图，带提示词增强_2103073606212341761.json
hash: f8eee639785637ea
coverage: 0.666667
learned_at: 2026-10-10 20:58:49
nodes: [PreviewAny, ResolutionSelector, PrimitiveStringMultiline, MarkdownNote, UNETLoader, CLIPLoader, VAELoader, PrimitiveStringMultiline, TextEncodeQwenImage21, EmptyLatentImage, KSampler, TextGenerateLTX2Prompt, ComfySwitchNode, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 812256206208017, "steps": 25, "width": 1024}
---

# 图片生成/文生图/QWEN IMAGE 2.1 文生图，带提示词增强_2103073606212341761.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/QWEN IMAGE 2.1 文生图，带提示词增强_2103073606212341761.json`

## 结构

**节点**（15 个）：
- `PreviewAny`
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `PrimitiveStringMultiline`
- `TextEncodeQwenImage21`
- `EmptyLatentImage`
- `KSampler`
- `TextGenerateLTX2Prompt`
- `ComfySwitchNode`
- `VAEDecode`
- `SaveImage`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `812256206208017`
- `steps` = `25`
- `width` = `1024`

## 知识

覆盖率 **67%**（10/15）

**有卡**：`PreviewAny`、`ResolutionSelector`、`PrimitiveStringMultiline`、`MarkdownNote`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`
