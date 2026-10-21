---
key: 图片生成/图生图/Qwen Image 2.1 元素移除_2101986892471431170.json
name: Qwen Image 2.1 元素移除_2101986892471431170
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 元素移除_2101986892471431170.json
hash: 90de9d42eda345cd
coverage: 0.666667
learned_at: 2026-10-21 00:42:10
nodes: [ResolutionSelector, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, QwenImage21Cache, TextEncodeQwenImage21, ResizeImageMaskNode, ResizeMask, GrowMaskWithBlur, DrawMaskOnImage, PreviewImage, EmptyLatentImage, SaveImageAdvanced, UNETLoader, CLIPLoader, VAELoader, KSampler, LoadImage, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1039593251902720, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1 元素移除_2101986892471431170.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 元素移除_2101986892471431170.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（24 个）：
- `ResolutionSelector`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `ResizeImageMaskNode`
- `ResizeMask`
- `GrowMaskWithBlur`
- `DrawMaskOnImage`
- `PreviewImage`
- `EmptyLatentImage` ★核心
- `SaveImageAdvanced`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1039593251902720`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **67%**（16/24）

**有卡**：`ResolutionSelector`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`ResizeImageMaskNode`、`ResizeMask`、`GrowMaskWithBlur`、`DrawMaskOnImage`、`EmptyLatentImage`、`SaveImageAdvanced`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`LoadImage`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
