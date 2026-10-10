---
key: 自用qwen_image_2.1_image_edit接超分放大工作流_2102129332872372226.json
name: 自用qwen_image_2.1_image_edit接超分放大工作流_2102129332872372226
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/自用qwen_image_2.1_image_edit接超分放大工作流_2102129332872372226.json
hash: 5ce30c647ea0a579
coverage: 0.833333
learned_at: 2026-10-10 21:22:47
nodes: [ComfySwitchNode, CM_IntToFloat, ImageScaleToTotalPixels, CLIPLoader, VAELoader, VAEDecode, LoadImage, LoadImage, ResolutionSelector, EmptyLatentImage, QwenImage21Cache, LoadImage, SaveImage, TextEncodeQwenImage21, PrimitiveInt, PrimitiveInt, UNETLoader, KSampler]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 479772469722800, "steps": 25, "width": 1024}
---

# 自用qwen_image_2.1_image_edit接超分放大工作流_2102129332872372226.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/自用qwen_image_2.1_image_edit接超分放大工作流_2102129332872372226.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `ComfySwitchNode`
- `CM_IntToFloat`
- `ImageScaleToTotalPixels`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `PrimitiveInt`
- `PrimitiveInt`
- `UNETLoader` ★核心
- `KSampler` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `479772469722800`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`CM_IntToFloat`、`ImageScaleToTotalPixels`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`LoadImage`、`ResolutionSelector`、`EmptyLatentImage`、`QwenImage21Cache`、`SaveImage`、`TextEncodeQwenImage21`、`UNETLoader`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
