---
key: 图片生成/文生图/Qwen_image_2.1_文生图提示词增强_2105104996953059329.json
name: Qwen_image_2.1_文生图提示词增强_2105104996953059329
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen_image_2.1_文生图提示词增强_2105104996953059329.json
hash: 1eef3a3765cf5546
coverage: 0.857143
learned_at: 2026-10-10 20:59:09
nodes: [TextEncodeQwenImage21, EmptyLatentImage, VAEDecode, UNETLoader, CLIPLoader, VAELoader, easy showAnything, SaveImageAdvanced, KSampler, ResolutionSelector, CLIPLoader, PrimitiveStringMultiline, TextGenerateLTX2Prompt, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 30037907342035, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen_image_2.1_文生图提示词增强_2105104996953059329.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen_image_2.1_文生图提示词增强_2105104996953059329.json`

## 结构

**节点**（14 个）：
- `TextEncodeQwenImage21`
- `EmptyLatentImage`
- `VAEDecode`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `easy showAnything`
- `SaveImageAdvanced`
- `KSampler`
- `ResolutionSelector`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `TextGenerateLTX2Prompt`
- `SaveImage`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `30037907342035`
- `steps` = `25`
- `width` = `1024`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`easy showAnything`、`SaveImageAdvanced`、`KSampler`、`ResolutionSelector`、`PrimitiveStringMultiline`
