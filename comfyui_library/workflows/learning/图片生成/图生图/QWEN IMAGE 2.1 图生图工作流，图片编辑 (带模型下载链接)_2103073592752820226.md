---
key: 图片生成/图生图/QWEN IMAGE 2.1 图生图工作流，图片编辑 (带模型下载链接)_2103073592752820226.json
name: QWEN IMAGE 2.1 图生图工作流，图片编辑 (带模型下载链接)_2103073592752820226
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QWEN IMAGE 2.1 图生图工作流，图片编辑 (带模型下载链接)_2103073592752820226.json
hash: abcd725a67046722
coverage: 0.764706
learned_at: 2026-10-21 00:41:55
nodes: [QwenImage21Cache, ComfySwitchNode, TextEncodeQwenImage21, EmptyLatentImage, VAEDecode, PrimitiveStringMultiline, PrimitiveStringMultiline, MarkdownNote, SaveImageAdvanced, SaveImage, LoadImage, LoadImage, VAELoader, CLIPLoader, UNETLoader, ResolutionSelector, KSampler]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 135868637753623, "steps": 25, "width": 1024}
---

# 图片生成/图生图/QWEN IMAGE 2.1 图生图工作流，图片编辑 (带模型下载链接)_2103073592752820226.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/QWEN IMAGE 2.1 图生图工作流，图片编辑 (带模型下载链接)_2103073592752820226.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `QwenImage21Cache`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `SaveImageAdvanced`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `ResolutionSelector`
- `KSampler` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `135868637753623`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（13/17）

**有卡**：`QwenImage21Cache`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAEDecode`、`SaveImageAdvanced`、`SaveImage`、`LoadImage`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`ResolutionSelector`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
