---
key: 图片生成/图生图/千问image2.1单图编辑_2101910795029409794.json
name: 千问image2.1单图编辑_2101910795029409794
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/千问image2.1单图编辑_2101910795029409794.json
hash: 696593eb0aa90bd9
coverage: 0.857143
learned_at: 2026-10-21 00:50:39
nodes: [UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, LoadImage, SaveImage, KSampler, QwenImage21Cache, VAEDecode, ComfySwitchNode, MarkdownNote, TextEncodeQwenImage21, CR Text, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 874029283759514, "steps": 25, "width": 1024}
---

# 图片生成/图生图/千问image2.1单图编辑_2101910795029409794.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/千问image2.1单图编辑_2101910795029409794.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `SaveImage`
- `KSampler` ★核心
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `MarkdownNote`
- `TextEncodeQwenImage21`
- `CR Text`
- `ResolutionSelector`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `874029283759514`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`LoadImage`、`SaveImage`、`KSampler`、`QwenImage21Cache`、`VAEDecode`、`TextEncodeQwenImage21`、`CR Text`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
