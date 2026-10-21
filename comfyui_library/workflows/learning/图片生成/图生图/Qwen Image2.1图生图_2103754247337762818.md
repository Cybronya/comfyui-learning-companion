---
key: 图片生成/图生图/Qwen Image2.1图生图_2103754247337762818.json
name: Qwen Image2.1图生图_2103754247337762818
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image2.1图生图_2103754247337762818.json
hash: dcb2d8449e74b45e
coverage: 0.777778
learned_at: 2026-10-21 00:42:51
nodes: [UNETLoader, CLIPLoader, VAELoader, KSampler, ComfySwitchNode, QwenImage21Cache, Note, MarkdownNote, SaveImageAdvanced, LoadImage, Text, VAEDecode, SaveImage, EmptyLatentImage, TextEncodeQwenImage21, ResolutionSelector, Image Comparer (rgthree), LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 507799650192607, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen Image2.1图生图_2103754247337762818.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image2.1图生图_2103754247337762818.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（18 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `Note`
- `MarkdownNote`
- `SaveImageAdvanced`
- `LoadImage`
- `Text`
- `VAEDecode` ★核心
- `SaveImage`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `Image Comparer (rgthree)`
- `LoadImage`

## 关键参数

- `seed` = `507799650192607`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（14/18）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`QwenImage21Cache`、`SaveImageAdvanced`、`LoadImage`、`Text`、`VAEDecode`、`SaveImage`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
