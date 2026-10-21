---
key: 图片生成/图生图/qwen-image-2.1图生图_2101823764827828226.json
name: qwen-image-2.1图生图_2101823764827828226
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image-2.1图生图_2101823764827828226.json
hash: 96171fc3fbd2f4c6
coverage: 1
learned_at: 2026-10-21 00:46:07
nodes: [UNETLoader, CLIPLoader, QwenImage21Cache, LoadImage, LoadImage, CR Text, VAELoader, VAEDecode, SaveImage, TextEncodeQwenImage21, CR Text, KSampler]
patterns: []
missing: []
parameters: {"cfg": 3, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 543572772630121, "steps": 20}
---

# 图片生成/图生图/qwen-image-2.1图生图_2101823764827828226.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-image-2.1图生图_2101823764827828226.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `QwenImage21Cache`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `TextEncodeQwenImage21`
- `CR Text`
- `KSampler` ★核心

## 关键参数

- `seed` = `543572772630121`
- `steps` = `20`
- `cfg` = `3`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`UNETLoader`、`CLIPLoader`、`QwenImage21Cache`、`LoadImage`、`CR Text`、`VAELoader`、`VAEDecode`、`SaveImage`、`TextEncodeQwenImage21`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
