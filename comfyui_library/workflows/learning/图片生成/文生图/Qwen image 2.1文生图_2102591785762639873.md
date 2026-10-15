---
key: 图片生成/文生图/Qwen image 2.1文生图_2102591785762639873.json
name: Qwen image 2.1文生图_2102591785762639873
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1文生图_2102591785762639873.json
hash: 38f145b9f2c08c70
coverage: 0.785714
learned_at: 2026-10-10 20:58:57
nodes: [CLIPLoader, KSampler, VAEDecode, UNETLoader, CLIPLoader, VAELoader, TextGenerateLTX2Prompt, PrimitiveStringMultiline, ResolutionSelector, MarkdownNote, easy showAnything, EmptyLatentImage, SaveImage, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 592733723427816, "steps": 50, "width": 1024}
---

# 图片生成/文生图/Qwen image 2.1文生图_2102591785762639873.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1文生图_2102591785762639873.json`

## 结构

**节点**（14 个）：
- `CLIPLoader`
- `KSampler`
- `VAEDecode`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `TextGenerateLTX2Prompt`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `MarkdownNote`
- `easy showAnything`
- `EmptyLatentImage`
- `SaveImage`
- `TextEncodeQwenImage21`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `592733723427816`
- `steps` = `50`
- `width` = `1024`

## 知识

覆盖率 **79%**（11/14）

**有卡**：`CLIPLoader`、`KSampler`、`VAEDecode`、`UNETLoader`、`VAELoader`、`TextGenerateLTX2Prompt`、`PrimitiveStringMultiline`、`ResolutionSelector`、`MarkdownNote`、`easy showAnything`
