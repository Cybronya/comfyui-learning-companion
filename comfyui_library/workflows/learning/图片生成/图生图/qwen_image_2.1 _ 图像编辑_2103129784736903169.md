---
key: 图片生成/图生图/qwen_image_2.1 _ 图像编辑_2103129784736903169.json
name: qwen_image_2.1 _ 图像编辑_2103129784736903169
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen_image_2.1 _ 图像编辑_2103129784736903169.json
hash: d86ecbe03973f39d
coverage: 0.818182
learned_at: 2026-10-21 00:46:21
nodes: [VAEDecode, CLIPLoader, UNETLoader, QwenImage21Cache, LoadImage, VAELoader, Image Comparer (rgthree), SaveImage, TextEncodeQwenImage21, JjkText, KSampler]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 953703460993983, "steps": 25}
---

# 图片生成/图生图/qwen_image_2.1 _ 图像编辑_2103129784736903169.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen_image_2.1 _ 图像编辑_2103129784736903169.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（11 个）：
- `VAEDecode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `LoadImage`
- `VAELoader`
- `Image Comparer (rgthree)`
- `SaveImage`
- `TextEncodeQwenImage21`
- `JjkText`
- `KSampler` ★核心

## 关键参数

- `seed` = `953703460993983`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（9/11）

**有卡**：`VAEDecode`、`CLIPLoader`、`UNETLoader`、`QwenImage21Cache`、`LoadImage`、`VAELoader`、`SaveImage`、`TextEncodeQwenImage21`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
