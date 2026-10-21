---
key: 图片生成/文生图/Qwen Image 2.1文生图_2101902260690313218.json
name: Qwen Image 2.1文生图_2101902260690313218
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图_2101902260690313218.json
hash: 9b4b25de0313ba5e
coverage: 0.818182
learned_at: 2026-10-20 01:50:58
nodes: [ResolutionSelector, MarkdownNote, Note, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, KSampler, TextEncodeQwenImage21, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Qwen Image 2.1文生图_2101902260690313218.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图_2101902260690313218.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（11 个）：
- `ResolutionSelector`
- `MarkdownNote`
- `Note`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `TextEncodeQwenImage21`
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

覆盖率 **82%**（9/11）

**有卡**：`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`TextEncodeQwenImage21`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
