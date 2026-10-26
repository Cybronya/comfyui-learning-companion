---
key: 图片生成/文生图/Qwen Image2.1文生图（LTX2提示词扩写）2609_2106051218907942913.json
name: Qwen Image2.1文生图（LTX2提示词扩写）2609_2106051218907942913
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image2.1文生图（LTX2提示词扩写）2609_2106051218907942913.json
hash: ad511d0e53abacf3
coverage: 0.733333
learned_at: 2026-10-26 22:08:41
nodes: [UNETLoader, CLIPLoader, VAELoader, CLIPLoader, TextGenerateLTX2Prompt, VAEDecode, SaveImage, EmptyLatentImage, MarkdownNote, Note, TextEncodeQwenImage21, KSampler, PreviewAny, ResolutionSelector, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen Image2.1文生图（LTX2提示词扩写）2609_2106051218907942913.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image2.1文生图（LTX2提示词扩写）2609_2106051218907942913.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `VAEDecode` ★核心
- `SaveImage`
- `EmptyLatentImage` ★核心
- `MarkdownNote`
- `Note`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `PreviewAny`
- `ResolutionSelector`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `0`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **73%**（11/15）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextGenerateLTX2Prompt`、`VAEDecode`、`SaveImage`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`KSampler`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
