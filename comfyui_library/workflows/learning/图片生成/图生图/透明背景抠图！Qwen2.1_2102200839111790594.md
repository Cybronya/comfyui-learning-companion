---
key: 图片生成/图生图/透明背景抠图！Qwen2.1_2102200839111790594.json
name: 透明背景抠图！Qwen2.1_2102200839111790594.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/透明背景抠图！Qwen2.1_2102200839111790594.json
hash: b7d8f3b98ec04c26
coverage: 0.522727
learned_at: 2026-10-09 22:27:09
nodes: [CLIPLoader, VAELoader, EmptyLatentImage, QwenImage21Cache, SetNode, SetNode, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, LoadImage, SetNode, LoadImage, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPLoader, FastGroupsBypassSwitch, ResolutionSelector, Fast Groups Bypasser (rgthree), UNETLoader, easy showAnything, KSampler, TextEncodeQwenImage21, BatchImagesNode, TextCombinerTwo, JjkText, SaveImage, LoadImage, LoadImage, JjkText, GH_ImageVideoComparer, VAEDecode, PreviewImage, GetNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 45, "width": 1024}
---

# 图片生成/图生图/透明背景抠图！Qwen2.1_2102200839111790594.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102200839111790594.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPLoader`
- `FastGroupsBypassSwitch`
- `ResolutionSelector`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `easy showAnything`
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `BatchImagesNode`
- `TextCombinerTwo`
- `JjkText`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `JjkText`
- `GH_ImageVideoComparer`
- `VAEDecode` ★核心
- `PreviewImage`
- `GetNode`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `999`
- `steps` = `45`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **52%**（23/44）

**有卡**：`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`QwenImage21Cache`、`LoadImage`、`FastGroupsBypassSwitch`、`ResolutionSelector`、`UNETLoader`、`KSampler`、`TextEncodeQwenImage21`、`BatchImagesNode`、`TextCombinerTwo`、`SaveImage`、`GH_ImageVideoComparer`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
