---
key: 图片生成/文生图/qwen image  edit 2.1_2101931566393024514.json
name: qwen image  edit 2.1_2101931566393024514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen image  edit 2.1_2101931566393024514.json
hash: 25d71500d9201bd4
coverage: 0.8125
learned_at: 2026-10-20 01:51:52
nodes: [UNETLoader, CLIPLoader, VAELoader, MarkdownNote, KSampler, QwenImage21Cache, VAEDecode, EmptyLatentImage, ResolutionSelector, TextEncodeQwenImage21, LoadImage, LoadImage, ComfySwitchNode, SaveImageAdvanced, MarkdownNote, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 535940685282476, "steps": 25, "width": 1024}
---

# 图片生成/文生图/qwen image  edit 2.1_2101931566393024514.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen image  edit 2.1_2101931566393024514.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `MarkdownNote`
- `KSampler` ★核心
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `ComfySwitchNode`
- `SaveImageAdvanced`
- `MarkdownNote`
- `SaveImage`

## 关键参数

- `seed` = `535940685282476`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`QwenImage21Cache`、`VAEDecode`、`EmptyLatentImage`、`ResolutionSelector`、`TextEncodeQwenImage21`、`LoadImage`、`SaveImageAdvanced`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
