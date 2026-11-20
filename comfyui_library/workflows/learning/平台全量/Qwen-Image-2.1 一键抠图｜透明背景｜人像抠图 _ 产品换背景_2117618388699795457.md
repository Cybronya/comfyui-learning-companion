---
key: 平台全量/Qwen-Image-2.1 一键抠图｜透明背景｜人像抠图 _ 产品换背景_2117618388699795457.json
name: Qwen-Image-2.1 一键抠图｜透明背景｜人像抠图 _ 产品换背景_2117618388699795457
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-Image-2.1 一键抠图｜透明背景｜人像抠图 _ 产品换背景_2117618388699795457.json
hash: 3ea3a43b06e73d01
coverage: 0.846154
learned_at: 2026-11-14 00:51:33
nodes: [UNETLoader, CLIPLoader, VAELoader, KSampler, LoadImage, VAEDecode, SaveImage, Image Comparer (rgthree), MarkdownNote, RHHiddenNodes, TextEncodeQwenImage21, RHHiddenNodes, QwenImage21Cache]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 712912552881720, "steps": 25}
---

# 平台全量/Qwen-Image-2.1 一键抠图｜透明背景｜人像抠图 _ 产品换背景_2117618388699795457.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-Image-2.1 一键抠图｜透明背景｜人像抠图 _ 产品换背景_2117618388699795457.json`

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

- `seed` = `712912552881720`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`LoadImage`、`VAEDecode`、`SaveImage`、`RHHiddenNodes`、`TextEncodeQwenImage21`、`QwenImage21Cache`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
