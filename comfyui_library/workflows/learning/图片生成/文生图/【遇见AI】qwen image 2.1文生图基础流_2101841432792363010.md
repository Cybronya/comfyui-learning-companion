---
key: 图片生成/文生图/【遇见AI】qwen image 2.1文生图基础流_2101841432792363010.json
name: 【遇见AI】qwen image 2.1文生图基础流_2101841432792363010
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【遇见AI】qwen image 2.1文生图基础流_2101841432792363010.json
hash: 8685f1cbd7f3e5d0
coverage: 0.923077
learned_at: 2026-10-20 01:52:07
nodes: [ResolutionSelector, EmptyLatentImage, KSampler, MarkdownNote, LoadImage, LoadImage, TextEncodeQwenImage21, CLIPLoader, VAELoader, UNETLoader, SaveImageAdvanced, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 817643478163194, "steps": 25, "width": 1024}
---

# 图片生成/文生图/【遇见AI】qwen image 2.1文生图基础流_2101841432792363010.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【遇见AI】qwen image 2.1文生图基础流_2101841432792363010.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `SaveImageAdvanced`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `817643478163194`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`ResolutionSelector`、`EmptyLatentImage`、`KSampler`、`LoadImage`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`SaveImageAdvanced`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
