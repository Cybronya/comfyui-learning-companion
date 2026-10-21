---
key: 图片生成/图生图/Qwen-Image-2.1 一键抠图｜透明背景｜自动识别主体 _ 电商产品照_2103702044094853121.json
name: Qwen-Image-2.1 一键抠图｜透明背景｜自动识别主体 _ 电商产品照_2103702044094853121
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 一键抠图｜透明背景｜自动识别主体 _ 电商产品照_2103702044094853121.json
hash: d6f411aa35ce3b31
coverage: 0.846154
learned_at: 2026-10-21 00:43:12
nodes: [UNETLoader, CLIPLoader, VAELoader, KSampler, LoadImage, VAEDecode, SaveImage, Image Comparer (rgthree), MarkdownNote, RHHiddenNodes, TextEncodeQwenImage21, RHHiddenNodes, QwenImage21Cache]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 268896275271165, "steps": 25}
---

# 图片生成/图生图/Qwen-Image-2.1 一键抠图｜透明背景｜自动识别主体 _ 电商产品照_2103702044094853121.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 一键抠图｜透明背景｜自动识别主体 _ 电商产品照_2103702044094853121.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `MarkdownNote`
- `RHHiddenNodes`
- `TextEncodeQwenImage21`
- `RHHiddenNodes`
- `QwenImage21Cache`

## 关键参数

- `seed` = `268896275271165`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`LoadImage`、`VAEDecode`、`SaveImage`、`RHHiddenNodes`、`TextEncodeQwenImage21`、`QwenImage21Cache`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
