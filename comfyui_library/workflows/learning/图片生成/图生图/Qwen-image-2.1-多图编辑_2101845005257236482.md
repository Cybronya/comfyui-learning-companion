---
key: 图片生成/图生图/Qwen-image-2.1-多图编辑_2101845005257236482.json
name: Qwen-image-2.1-多图编辑_2101845005257236482
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image-2.1-多图编辑_2101845005257236482.json
hash: d9e2060621d2d191
coverage: 0.928571
learned_at: 2026-10-21 00:43:22
nodes: [UNETLoader, CLIPLoader, VAELoader, QwenImage21Cache, VAEDecode, LoadImage, LoadImage, LoadImage, LoadImage, TextEncodeQwenImage21, CR Prompt Text, KSampler, PreviewImage, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 953430755504843, "steps": 25}
---

# 图片生成/图生图/Qwen-image-2.1-多图编辑_2101845005257236482.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image-2.1-多图编辑_2101845005257236482.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（14 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `CR Prompt Text`
- `KSampler` ★核心
- `PreviewImage`
- `SaveImage`

## 关键参数

- `seed` = `953430755504843`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`VAEDecode`、`LoadImage`、`TextEncodeQwenImage21`、`CR Prompt Text`、`KSampler`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
