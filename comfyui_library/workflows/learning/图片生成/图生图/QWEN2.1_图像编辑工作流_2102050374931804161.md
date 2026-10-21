---
key: 图片生成/图生图/QWEN2.1_图像编辑工作流_2102050374931804161.json
name: QWEN2.1_图像编辑工作流_2102050374931804161
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QWEN2.1_图像编辑工作流_2102050374931804161.json
hash: a4f605c90a1744b8
coverage: 0.8
learned_at: 2026-10-21 00:41:56
nodes: [EmptyLatentImage, ComfySwitchNode, MarkdownNote, QwenImage21Cache, UNETLoader, Note, VAELoader, CLIPLoader, KSampler, ResolutionSelector, LoadImage, TextEncodeQwenImage21, VAEDecode, LoadImage, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 102735107321090, "steps": 25, "width": 1024}
---

# 图片生成/图生图/QWEN2.1_图像编辑工作流_2102050374931804161.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/QWEN2.1_图像编辑工作流_2102050374931804161.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `MarkdownNote`
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `Note`
- `VAELoader`
- `CLIPLoader`
- `KSampler` ★核心
- `ResolutionSelector`
- `LoadImage`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `LoadImage`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `102735107321090`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（12/15）

**有卡**：`EmptyLatentImage`、`QwenImage21Cache`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`KSampler`、`ResolutionSelector`、`LoadImage`、`TextEncodeQwenImage21`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
