---
key: 图片生成/图生图/Qwen Image 2.1 编辑 _ 纯净官流40步无PE_2102038528808013825.json
name: Qwen Image 2.1 编辑 _ 纯净官流40步无PE_2102038528808013825
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 编辑 _ 纯净官流40步无PE_2102038528808013825.json
hash: 28e2b93fa1631fdc
coverage: 0.8
learned_at: 2026-10-15 22:25:12
nodes: [MarkdownNote, PixaromaRunTimer, MarkdownNote, ComfySwitchNode, UNETLoader, CLIPLoader, VAELoader, QwenImage21Cache, Fast Bypasser (rgthree), Image Comparer (rgthree), KSampler, LoadImage, LoadImage, LoadImage, LoadImage, PixaromaSeed, EmptyLatentImage, TextEncodeQwenImage21, PrimitiveBoolean, VAEDecode, SaveImage, LoadImage, ResolutionSelector, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1008717317457582, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1 编辑 _ 纯净官流40步无PE_2102038528808013825.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 编辑 _ 纯净官流40步无PE_2102038528808013825.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（25 个）：
- `MarkdownNote`
- `PixaromaRunTimer`
- `MarkdownNote`
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `Fast Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PixaromaSeed`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `PrimitiveBoolean`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `ResolutionSelector`
- `LoadImage`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `1008717317457582`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（20/25）

**有卡**：`PixaromaRunTimer`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`Fast Bypasser (rgthree)`、`KSampler`、`LoadImage`、`PixaromaSeed`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`PrimitiveBoolean`、`VAEDecode`、`SaveImage`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
