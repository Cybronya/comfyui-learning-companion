---
key: 图片生成/图生图/Flux.3-Kelin图像编辑（提示词优化）_2115070389184458753.json
name: Flux.3-Kelin图像编辑（提示词优化）_2115070389184458753
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.3-Kelin图像编辑（提示词优化）_2115070389184458753.json
hash: 251083ea90eeb5de
coverage: 0.681818
learned_at: 2026-10-30 17:49:42
nodes: [UNETLoader, VAELoader, KSampler, VAEDecode, MarkdownNote, MarkdownNote, CreateBoundingBoxes, PreviewAny, MarkdownNote, EmptyFlux2LatentImage, CLIPTextEncode, CLIPLoader, ReferenceMultiLatent, CLIPLoader, SaveImage, Image Comparer (rgthree), CLIPTextEncode, TextGenerate, LoadImage, Text, MarkdownNote, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 3.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1099001873561556, "steps": 25}
---

# 图片生成/图生图/Flux.3-Kelin图像编辑（提示词优化）_2115070389184458753.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.3-Kelin图像编辑（提示词优化）_2115070389184458753.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `CreateBoundingBoxes`
- `PreviewAny`
- `MarkdownNote`
- `EmptyFlux2LatentImage`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `ReferenceMultiLatent`
- `CLIPLoader`
- `SaveImage`
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `TextGenerate`
- `LoadImage`
- `Text`
- `MarkdownNote`
- `MarkdownNote`

## 关键参数

- `seed` = `1099001873561556`
- `steps` = `25`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **68%**（15/22）

**有卡**：`UNETLoader`、`VAELoader`、`KSampler`、`VAEDecode`、`CreateBoundingBoxes`、`EmptyFlux2LatentImage`、`CLIPTextEncode`、`CLIPLoader`、`ReferenceMultiLatent`、`SaveImage`、`TextGenerate`、`LoadImage`、`Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、EmptyFlux2LatentImage
