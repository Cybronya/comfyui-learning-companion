---
key: 图片生成/文生图/Qwen-Image-2.1 文生图增强版_2116095851314630657.json
name: Qwen-Image-2.1 文生图增强版_2116095851314630657
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1 文生图增强版_2116095851314630657.json
hash: 18f70fab9eeb26c5
coverage: 0.846154
learned_at: 2026-10-30 23:26:51
nodes: [SaveImage, MarkdownNote, ResolutionSelector, PrimitiveStringMultiline, KSampler, UNETLoader, CLIPLoader, VAELoader, CLIPLoader, TextGenerateLTX2Prompt, TextEncodeQwenImage21, EmptyLatentImage, VAEDecode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1036382916451902, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen-Image-2.1 文生图增强版_2116095851314630657.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1 文生图增强版_2116095851314630657.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
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

## 关键参数

- `seed` = `1036382916451902`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`SaveImage`、`ResolutionSelector`、`KSampler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextGenerateLTX2Prompt`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAEDecode`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
