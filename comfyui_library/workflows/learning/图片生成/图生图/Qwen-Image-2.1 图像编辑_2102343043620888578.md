---
key: 图片生成/图生图/Qwen-Image-2.1 图像编辑_2102343043620888578.json
name: Qwen-Image-2.1 图像编辑_2102343043620888578
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 图像编辑_2102343043620888578.json
hash: a11e3efad9a55af8
coverage: 0.75
learned_at: 2026-10-10 20:48:09
nodes: [QwenImage21Cache, ComfySwitchNode, KSampler, VAELoader, ResolutionSelector, EmptyLatentImage, LoadImage, LoadImage, MarkdownNote, MarkdownNote, MarkdownNote, TextEncodeQwenImage21, UNETLoader, CLIPLoader, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1110267963329213, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen-Image-2.1 图像编辑_2102343043620888578.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 图像编辑_2102343043620888578.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `QwenImage21Cache`
- `ComfySwitchNode`
- `KSampler` ★核心
- `VAELoader`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `1110267963329213`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **75%**（12/16）

**有卡**：`QwenImage21Cache`、`KSampler`、`VAELoader`、`ResolutionSelector`、`EmptyLatentImage`、`LoadImage`、`TextEncodeQwenImage21`、`UNETLoader`、`CLIPLoader`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
