---
key: Qwen Image 2.1文生图_2101560854905970690.json
name: Qwen Image 2.1文生图_2101560854905970690
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图_2101560854905970690.json
hash: 7dec0c38da499cb3
coverage: 0.733333
learned_at: 2026-10-10 20:58:53
nodes: [MarkdownNote, CLIPLoader, VAELoader, EmptyLatentImage, KSampler, UNETLoader, ModelAttentionBackend, TextEncodeQwenImage21, Note, MarkdownNote, PrimitiveStringMultiline, ResolutionSelector, SaveImageAdvanced, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 40, "width": 1024}
---

# Qwen Image 2.1文生图_2101560854905970690.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图_2101560854905970690.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `MarkdownNote`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `ModelAttentionBackend`
- `TextEncodeQwenImage21`
- `Note`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImageAdvanced`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `0`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **73%**（11/15）

**有卡**：`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`UNETLoader`、`ModelAttentionBackend`、`TextEncodeQwenImage21`、`ResolutionSelector`、`SaveImageAdvanced`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
