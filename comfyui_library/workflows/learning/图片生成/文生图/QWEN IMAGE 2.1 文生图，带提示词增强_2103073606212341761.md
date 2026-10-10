---
key: QWEN IMAGE 2.1 文生图，带提示词增强_2103073606212341761.json
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

# QWEN IMAGE 2.1 文生图，带提示词增强_2103073606212341761.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/QWEN IMAGE 2.1 文生图，带提示词增强_2103073606212341761.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `PreviewAny`
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `PrimitiveStringMultiline`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `TextGenerateLTX2Prompt`
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `812256206208017`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **67%**（10/15）

**有卡**：`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`TextGenerateLTX2Prompt`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
