---
key: 图片生成/图生图/qwen-image-2.1一键抠图 PNG通道_2102236996667265025.json
name: qwen-image-2.1一键抠图 PNG通道_2102236996667265025
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image-2.1一键抠图 PNG通道_2102236996667265025.json
hash: 386713589d08dd91
coverage: 1
learned_at: 2026-10-10 20:48:12
nodes: [CLIPLoader, VAELoader, QwenImage21Cache, SaveImageAdvanced, KSampler, UNETLoader, TextEncodeQwenImage21, LoadImage, SaveImage, VAEDecode]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1013261198599981, "steps": 25}
---

# 图片生成/图生图/qwen-image-2.1一键抠图 PNG通道_2102236996667265025.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-image-2.1一键抠图 PNG通道_2102236996667265025.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（10 个）：
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `SaveImageAdvanced`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `LoadImage`
- `SaveImage`
- `VAEDecode` ★核心

## 关键参数

- `seed` = `1013261198599981`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`SaveImageAdvanced`、`KSampler`、`UNETLoader`、`TextEncodeQwenImage21`、`LoadImage`、`SaveImage`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
