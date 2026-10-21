---
key: 图片生成/图生图/Qwen Image 2.1：图像编辑_2101818506256932866.json
name: Qwen Image 2.1：图像编辑_2101818506256932866
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1：图像编辑_2101818506256932866.json
hash: 9bf1e8fbc359c997
coverage: 0.821429
learned_at: 2026-10-21 00:42:49
nodes: [ResolutionSelector, MarkdownNote, Note, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, QwenImage21Cache, SaveImage, SaveImageAdvanced, PrimitiveStringMultiline, PrimitiveStringMultiline, ComfySwitchNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 586447620346472, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1：图像编辑_2101818506256932866.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1：图像编辑_2101818506256932866.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（28 个）：
- `ResolutionSelector`
- `MarkdownNote`
- `Note`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `QwenImage21Cache`
- `SaveImage`
- `SaveImageAdvanced`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `586447620346472`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（23/28）

**有卡**：`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`SaveImage`、`SaveImageAdvanced`、`LoadImage`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
