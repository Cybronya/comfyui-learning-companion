---
key: 图片生成/图生图/Qwen-image2.1-图像人像+角度操控（AnyAngl-lora）_2105204359549243394.json
name: Qwen-image2.1-图像人像+角度操控（AnyAngl-lora）_2105204359549243394
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-图像人像+角度操控（AnyAngl-lora）_2105204359549243394.json
hash: dc46a09c5e5fc659
coverage: 0.888889
learned_at: 2026-10-21 00:43:26
nodes: [CLIPLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, easy promptList, easy showAnything, VAEDecode, SaveImage, VAELoader, UNETLoader, LoraLoaderModelOnly, TextEncodeQwenImage21, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, PreviewImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 316628973553948, "steps": 25}
---

# 图片生成/图生图/Qwen-image2.1-图像人像+角度操控（AnyAngl-lora）_2105204359549243394.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-图像人像+角度操控（AnyAngl-lora）_2105204359549243394.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `CLIPLoader`
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `easy promptList`
- `easy showAnything`
- `VAEDecode` ★核心
- `SaveImage`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImage21`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `PreviewImage`

## 关键参数

- `seed` = `316628973553948`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`CLIPLoader`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`easy promptList`、`VAEDecode`、`SaveImage`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`QwenMultiangleCameraNode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader
