---
key: 图片生成/文生图/qwen image2.1 单图_文生图工作流_2101896635692437505.json
name: qwen image2.1 单图_文生图工作流_2101896635692437505
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen image2.1 单图_文生图工作流_2101896635692437505.json
hash: b23d3ef0ec6fdee2
coverage: 0.764706
learned_at: 2026-10-20 01:51:54
nodes: [LoadImage, UNETLoader, CLIPLoader, VAELoader, QwenImage21Cache, KSampler, VAEDecode, SaveImage, ModelAttentionBackend, TextEncodeQwenImage21, EmptyLatentImage, MarkdownNote, PrimitiveInt, GetImageSize, Fast Groups Bypasser (rgthree), ResolutionSelector, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 240452564874383, "steps": 40, "width": 1024}
---

# 图片生成/文生图/qwen image2.1 单图_文生图工作流_2101896635692437505.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen image2.1 单图_文生图工作流_2101896635692437505.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ModelAttentionBackend`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `MarkdownNote`
- `PrimitiveInt`
- `GetImageSize`
- `Fast Groups Bypasser (rgthree)`
- `ResolutionSelector`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `240452564874383`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **76%**（13/17）

**有卡**：`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`SaveImage`、`ModelAttentionBackend`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`GetImageSize`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
