---
key: 图片生成/图生图/一键抠图背景移除-qwen image 2.1_2112444591415848961.json
name: 一键抠图背景移除-qwen image 2.1_2112444591415848961
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/一键抠图背景移除-qwen image 2.1_2112444591415848961.json
hash: c263f0fad4b43ad2
coverage: 0.857143
learned_at: 2026-10-23 11:55:58
nodes: [VAELoader, CLIPLoader, QwenImage21Cache, ComfySwitchNode, VAEDecode, UNETLoader, KSampler, MarkdownNote, ResolutionSelector, EmptyLatentImage, SaveImageAdvanced, LoadImage, TextEncodeQwenImage21, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 481282152054107, "steps": 25, "width": 1024}
---

# 图片生成/图生图/一键抠图背景移除-qwen image 2.1_2112444591415848961.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/一键抠图背景移除-qwen image 2.1_2112444591415848961.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `VAELoader`
- `CLIPLoader`
- `QwenImage21Cache`
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `MarkdownNote`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `SaveImageAdvanced`
- `LoadImage`
- `TextEncodeQwenImage21`
- `SaveImage`

## 关键参数

- `seed` = `481282152054107`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`VAELoader`、`CLIPLoader`、`QwenImage21Cache`、`VAEDecode`、`UNETLoader`、`KSampler`、`ResolutionSelector`、`EmptyLatentImage`、`SaveImageAdvanced`、`LoadImage`、`TextEncodeQwenImage21`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
