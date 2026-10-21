---
key: 图片生成/图生图/Qwen-image-2.1-单图编辑_2101839855062966274.json
name: Qwen-image-2.1-单图编辑_2101839855062966274
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image-2.1-单图编辑_2101839855062966274.json
hash: 03e2e0f7fdb9a925
coverage: 0.909091
learned_at: 2026-10-21 00:43:22
nodes: [UNETLoader, CLIPLoader, VAELoader, PreviewImage, SaveImage, QwenImage21Cache, VAEDecode, KSampler, LoadImage, TextEncodeQwenImage21, CR Prompt Text]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 873496162677716, "steps": 40}
---

# 图片生成/图生图/Qwen-image-2.1-单图编辑_2101839855062966274.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image-2.1-单图编辑_2101839855062966274.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（11 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `PreviewImage`
- `SaveImage`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `LoadImage`
- `TextEncodeQwenImage21`
- `CR Prompt Text`

## 关键参数

- `seed` = `873496162677716`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`SaveImage`、`QwenImage21Cache`、`VAEDecode`、`KSampler`、`LoadImage`、`TextEncodeQwenImage21`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
