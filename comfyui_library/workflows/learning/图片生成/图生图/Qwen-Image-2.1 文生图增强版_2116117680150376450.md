---
key: 图片生成/图生图/Qwen-Image-2.1 文生图增强版_2116117680150376450.json
name: Qwen-Image-2.1 文生图增强版_2116117680150376450
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 文生图增强版_2116117680150376450.json
hash: 7675fa74bd85789a
coverage: 0.857143
learned_at: 2026-10-30 23:24:27
nodes: [SaveImage, MarkdownNote, ResolutionSelector, PrimitiveStringMultiline, KSampler, UNETLoader, CLIPLoader, VAELoader, CLIPLoader, TextGenerateLTX2Prompt, TextEncodeQwenImage21, EmptyLatentImage, VAEDecode, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1113738823114082, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen-Image-2.1 文生图增强版_2116117680150376450.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 文生图增强版_2116117680150376450.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `SaveImage`
- `MarkdownNote`
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `LoadImage`

## 关键参数

- `seed` = `1113738823114082`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`SaveImage`、`ResolutionSelector`、`KSampler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextGenerateLTX2Prompt`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAEDecode`、`LoadImage`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
