---
key: 图片生成/文生图/image_qwen_image_2_1_background_removal_2109217853978271745.json
name: image_qwen_image_2_1_background_removal_2109217853978271745
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/image_qwen_image_2_1_background_removal_2109217853978271745.json
hash: d3f1ed7409b8aac9
coverage: 0.785714
learned_at: 2026-10-21 02:57:11
nodes: [MarkdownNote, MarkdownNote, UNETLoader, QwenImage21Cache, KSampler, VAEDecode, SaveImage, CLIPLoader, VAELoader, LoadImage, LoadImage, ComfySwitchNode, EmptyLatentImage, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1672, "sampler_name": "euler", "scheduler": "simple", "seed": 11202792221562, "steps": 25, "width": 944}
---

# 图片生成/文生图/image_qwen_image_2_1_background_removal_2109217853978271745.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/image_qwen_image_2_1_background_removal_2109217853978271745.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`

## 关键参数

- `seed` = `11202792221562`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `944`
- `height` = `1672`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（11/14）

**有卡**：`UNETLoader`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`SaveImage`、`CLIPLoader`、`VAELoader`、`LoadImage`、`EmptyLatentImage`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
