---
key: 图片生成/图生图/qwen-image-2.1多图编辑_2102013603833532417.json
name: qwen-image-2.1多图编辑_2102013603833532417
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image-2.1多图编辑_2102013603833532417.json
hash: c12c45055732627f
coverage: 0.923077
learned_at: 2026-10-21 00:46:07
nodes: [CLIPLoader, VAELoader, LoadImage, LoadImage, UNETLoader, TextEncodeQwenImage21, QwenImage21Cache, KSampler, VAEDecode, SaveImage, MarkdownNote, SaveImageAdvanced, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 758857520347577, "steps": 25}
---

# 图片生成/图生图/qwen-image-2.1多图编辑_2102013603833532417.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-image-2.1多图编辑_2102013603833532417.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `MarkdownNote`
- `SaveImageAdvanced`
- `LoadImage`

## 关键参数

- `seed` = `758857520347577`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`CLIPLoader`、`VAELoader`、`LoadImage`、`UNETLoader`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`SaveImage`、`SaveImageAdvanced`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
