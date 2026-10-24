---
key: 图片生成/图生图/Qwen-image2.1-人像多角度生成_2110187888993456130.json
name: Qwen-image2.1-人像多角度生成_2110187888993456130
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-人像多角度生成_2110187888993456130.json
hash: 442c3440b22035a5
coverage: 0.882353
learned_at: 2026-10-23 11:18:25
nodes: [CLIPLoader, VAELoader, UNETLoader, KSampler, TextEncodeQwenImage21, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, LoadImage, easy promptList, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, easy showAnything, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 907622579038562, "steps": 25}
---

# 图片生成/图生图/Qwen-image2.1-人像多角度生成_2110187888993456130.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-人像多角度生成_2110187888993456130.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `LoadImage`
- `easy promptList`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `easy showAnything`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `907622579038562`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`KSampler`、`TextEncodeQwenImage21`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`easy promptList`、`QwenMultiangleCameraNode`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、easy promptList
