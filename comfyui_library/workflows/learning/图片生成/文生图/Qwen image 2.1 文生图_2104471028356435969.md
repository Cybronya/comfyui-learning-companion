---
key: 图片生成/文生图/Qwen image 2.1 文生图_2104471028356435969.json
name: Qwen image 2.1 文生图_2104471028356435969
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图_2104471028356435969.json
hash: c5d9b09dec068c99
coverage: 0.923077
learned_at: 2026-10-10 20:58:57
nodes: [ResolutionSelector, TextEncodeQwenImage21, EmptyLatentImage, VAEDecode, KSampler, UNETLoader, CLIPLoader, VAELoader, easy showAnything, CLIPLoader, SaveImage, SaveImageAdvanced, TextGenerateLTX2Prompt]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 666, "steps": 50, "width": 1024}
---

# 图片生成/文生图/Qwen image 2.1 文生图_2104471028356435969.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图_2104471028356435969.json`

## 结构

**节点**（13 个）：
- `ResolutionSelector`
- `TextEncodeQwenImage21`
- `EmptyLatentImage`
- `VAEDecode`
- `KSampler`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `easy showAnything`
- `CLIPLoader`
- `SaveImage`
- `SaveImageAdvanced`
- `TextGenerateLTX2Prompt`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `666`
- `steps` = `50`
- `width` = `1024`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`ResolutionSelector`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`easy showAnything`、`SaveImage`、`SaveImageAdvanced`
