---
key: 图片生成/文生图/qwen image 2.1 文生图提示词扩写_2102006301646745601.json
name: qwen image 2.1 文生图提示词扩写_2102006301646745601
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen image 2.1 文生图提示词扩写_2102006301646745601.json
hash: 9ee9c7adf8a172ba
coverage: 0.458333
learned_at: 2026-10-20 01:51:53
nodes: [SaveImage, CLIPLoader, EmptyLatentImage, Reroute, UNETLoader, CLIPLoader, Reroute, easy showAnything, Reroute, Reroute, VAELoader, Reroute, Reroute, TextGenerate, Reroute, VAEDecode, Reroute, Reroute, Reroute, Reroute, TextEncodeQwenImage21, ResolutionSelector, KSampler, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 962902238094829, "steps": 50, "width": 1024}
---

# 图片生成/文生图/qwen image 2.1 文生图提示词扩写_2102006301646745601.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen image 2.1 文生图提示词扩写_2102006301646745601.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（24 个）：
- `SaveImage`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `Reroute`
- `UNETLoader` ★核心
- `CLIPLoader`
- `Reroute`
- `easy showAnything`
- `Reroute`
- `Reroute`
- `VAELoader`
- `Reroute`
- `Reroute`
- `TextGenerate`
- `Reroute`
- `VAEDecode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `KSampler` ★核心
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `962902238094829`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **46%**（11/24）

**有卡**：`SaveImage`、`CLIPLoader`、`EmptyLatentImage`、`UNETLoader`、`VAELoader`、`TextGenerate`、`VAEDecode`、`TextEncodeQwenImage21`、`ResolutionSelector`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
