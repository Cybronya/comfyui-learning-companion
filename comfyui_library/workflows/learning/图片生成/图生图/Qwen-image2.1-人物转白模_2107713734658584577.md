---
key: 图片生成/图生图/Qwen-image2.1-人物转白模_2107713734658584577.json
name: Qwen-image2.1-人物转白模_2107713734658584577
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-人物转白模_2107713734658584577.json
hash: 60c6df088ff9f464
coverage: 0.909091
learned_at: 2026-10-21 00:43:25
nodes: [CLIPLoader, UNETLoader, KSampler, VAEDecode, SaveImage, VAELoader, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, TextEncodeQwenImage21, LoadImage, PreviewImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 307098866779704, "steps": 25}
---

# 图片生成/图生图/Qwen-image2.1-人物转白模_2107713734658584577.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-人物转白模_2107713734658584577.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（11 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextEncodeQwenImage21`
- `LoadImage`
- `PreviewImage`

## 关键参数

- `seed` = `307098866779704`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`CLIPLoader`、`UNETLoader`、`KSampler`、`VAEDecode`、`SaveImage`、`VAELoader`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImage21`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader
