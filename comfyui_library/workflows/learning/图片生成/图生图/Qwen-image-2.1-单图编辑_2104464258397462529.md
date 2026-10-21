---
key: 图片生成/图生图/Qwen-image-2.1-单图编辑_2104464258397462529.json
name: Qwen-image-2.1-单图编辑_2104464258397462529
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image-2.1-单图编辑_2104464258397462529.json
hash: ad95b4432cb44155
coverage: 0.823529
learned_at: 2026-10-21 00:43:22
nodes: [MarkdownNote, MarkdownNote, VAELoader, QwenImage21Cache, UNETLoader, CLIPLoader, TextEncodeQwenImage21, EmptyLatentImage, LoraLoaderModelOnly, VAEDecode, LoraLoaderModelOnly, SaveImageAdvanced, LoraLoaderModelOnly, ComfySwitchNode, KSampler, SaveImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2048, "sampler_name": "euler", "scheduler": "simple", "seed": 370402199118978, "steps": 40, "width": 2048}
---

# 图片生成/图生图/Qwen-image-2.1-单图编辑_2104464258397462529.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image-2.1-单图编辑_2104464258397462529.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `MarkdownNote`
- `MarkdownNote`
- `VAELoader`
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImageAdvanced`
- `LoraLoaderModelOnly` ★核心
- `ComfySwitchNode`
- `KSampler` ★核心
- `SaveImage`
- `LoadImage`

## 关键参数

- `width` = `2048`
- `height` = `2048`
- `batch_size` = `1`
- `seed` = `370402199118978`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`VAELoader`、`QwenImage21Cache`、`UNETLoader`、`CLIPLoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`VAEDecode`、`SaveImageAdvanced`、`KSampler`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage
