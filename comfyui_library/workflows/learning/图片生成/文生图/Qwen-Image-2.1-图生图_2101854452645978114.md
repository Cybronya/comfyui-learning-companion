---
key: 图片生成/文生图/Qwen-Image-2.1-图生图_2101854452645978114.json
name: Qwen-Image-2.1-图生图_2101854452645978114
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1-图生图_2101854452645978114.json
hash: 68305183e2aa037b
coverage: 0.8125
learned_at: 2026-10-20 01:51:16
nodes: [MarkdownNote, MarkdownNote, VAELoader, CLIPLoader, UNETLoader, EmptyLatentImage, ComfySwitchNode, KSampler, QwenImage21Cache, LoadImage, ResolutionSelector, VAEDecode, TextEncodeQwenImage21, SaveImageAdvanced, SaveImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 433669288047281, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen-Image-2.1-图生图_2101854452645978114.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1-图生图_2101854452645978114.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `MarkdownNote`
- `MarkdownNote`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `KSampler` ★核心
- `QwenImage21Cache`
- `LoadImage`
- `ResolutionSelector`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `SaveImageAdvanced`
- `SaveImage`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `433669288047281`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`EmptyLatentImage`、`KSampler`、`QwenImage21Cache`、`LoadImage`、`ResolutionSelector`、`VAEDecode`、`TextEncodeQwenImage21`、`SaveImageAdvanced`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
