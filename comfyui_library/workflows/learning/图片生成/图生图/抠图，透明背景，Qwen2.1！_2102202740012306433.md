---
key: 图片生成/图生图/抠图，透明背景，Qwen2.1！_2102202740012306433.json
name: 抠图，透明背景，Qwen2.1！_2102202740012306433
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/抠图，透明背景，Qwen2.1！_2102202740012306433.json
hash: 7f434972d975b79a
coverage: 0.7
learned_at: 2026-10-10 20:48:17
nodes: [CLIPLoader, VAELoader, QwenImage21Cache, SetNode, CLIPLoader, UNETLoader, PreviewImage, FastGroupsBypassSwitch, ResolutionSelector, JjkText, SaveImage, GetNode, easy showAnything, LoadImage, EmptyLatentImage, TextEncodeQwenImage21, TextCombinerTwo, KSampler, VAEDecode, JjkText]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 45, "width": 1024}
---

# 图片生成/图生图/抠图，透明背景，Qwen2.1！_2102202740012306433.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/抠图，透明背景，Qwen2.1！_2102202740012306433.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（20 个）：
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `SetNode`
- `CLIPLoader`
- `UNETLoader` ★核心
- `PreviewImage`
- `FastGroupsBypassSwitch`
- `ResolutionSelector`
- `JjkText`
- `SaveImage`
- `GetNode`
- `easy showAnything`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `TextCombinerTwo`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`

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

覆盖率 **70%**（14/20）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`UNETLoader`、`FastGroupsBypassSwitch`、`ResolutionSelector`、`SaveImage`、`LoadImage`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`TextCombinerTwo`、`KSampler`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
