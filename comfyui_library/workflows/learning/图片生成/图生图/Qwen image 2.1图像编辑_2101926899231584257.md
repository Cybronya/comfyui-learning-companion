---
key: 图片生成/图生图/Qwen image 2.1图像编辑_2101926899231584257.json
name: Qwen image 2.1图像编辑_2101926899231584257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1图像编辑_2101926899231584257.json
hash: 1d607c007b9f4a7b
coverage: 0.823529
learned_at: 2026-10-21 00:42:57
nodes: [UNETLoader, CLIPLoader, VAELoader, KSampler, ComfySwitchNode, MarkdownNote, MarkdownNote, LoadImage, EmptyLatentImage, ResolutionSelector, QwenImage21Cache, TextEncodeQwenImage21, LoadImage, LoadImage, SaveImageAdvanced, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 679038905107644, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen image 2.1图像编辑_2101926899231584257.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1图像编辑_2101926899231584257.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `ComfySwitchNode`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `SaveImageAdvanced`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `679038905107644`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`LoadImage`、`EmptyLatentImage`、`ResolutionSelector`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`SaveImageAdvanced`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
