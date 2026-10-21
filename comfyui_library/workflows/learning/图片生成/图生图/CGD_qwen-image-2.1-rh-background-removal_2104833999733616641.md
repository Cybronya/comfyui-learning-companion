---
key: 图片生成/图生图/CGD_qwen-image-2.1-rh-background-removal_2104833999733616641.json
name: CGD_qwen-image-2.1-rh-background-removal_2104833999733616641
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/CGD_qwen-image-2.1-rh-background-removal_2104833999733616641.json
hash: 41f23da185c0760e
coverage: 0.8
learned_at: 2026-10-21 00:38:50
nodes: [MarkdownNote, MarkdownNote, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, ComfySwitchNode, QwenImage21Cache, TextEncodeQwenImage21, LoadImage, ImageCompare, SaveImageAdvanced, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 71705568929043, "steps": 25, "width": 1024}
---

# 图片生成/图生图/CGD_qwen-image-2.1-rh-background-removal_2104833999733616641.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/CGD_qwen-image-2.1-rh-background-removal_2104833999733616641.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `LoadImage`
- `ImageCompare`
- `SaveImageAdvanced`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `71705568929043`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（12/15）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`LoadImage`、`ImageCompare`、`SaveImageAdvanced`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
