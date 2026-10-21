---
key: 图片生成/图生图/Qwen Image 2.1单图编辑（角色四视图）2609_2106315774649528321.json
name: Qwen Image 2.1单图编辑（角色四视图）2609_2106315774649528321
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1单图编辑（角色四视图）2609_2106315774649528321.json
hash: 6c2e447624a831f6
coverage: 0.909091
learned_at: 2026-10-21 00:42:23
nodes: [ResolutionSelector, EmptyLatentImage, KSampler, TextEncodeQwenImage21, VAEDecode, SaveImage, LoadImage, VAELoader, CLIPLoader, UNETLoader, Anything Everywhere3]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 9527, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1单图编辑（角色四视图）2609_2106315774649528321.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1单图编辑（角色四视图）2609_2106315774649528321.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（11 个）：
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `Anything Everywhere3`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `9527`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`ResolutionSelector`、`EmptyLatentImage`、`KSampler`、`TextEncodeQwenImage21`、`VAEDecode`、`SaveImage`、`LoadImage`、`VAELoader`、`CLIPLoader`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
