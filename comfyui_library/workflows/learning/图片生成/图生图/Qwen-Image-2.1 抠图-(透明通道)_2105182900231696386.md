---
key: 图片生成/图生图/Qwen-Image-2.1 抠图-(透明通道)_2105182900231696386.json
name: Qwen-Image-2.1 抠图-(透明通道)_2105182900231696386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 抠图-(透明通道)_2105182900231696386.json
hash: 0ae7e315b8c14423
coverage: 0.928571
learned_at: 2026-10-21 00:43:13
nodes: [UNETLoader, CLIPLoader, VAELoader, KSampler, QwenImage21Cache, TextEncodeQwenImage21, StringConcatenate, VAEDecode, PreviewImage, ResolutionSelector, FastGroupsBypassSwitch, EmptyLatentImage, SaveImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 45, "width": 1024}
---

# 图片生成/图生图/Qwen-Image-2.1 抠图-(透明通道)_2105182900231696386.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 抠图-(透明通道)_2105182900231696386.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `StringConcatenate`
- `VAEDecode` ★核心
- `PreviewImage`
- `ResolutionSelector`
- `FastGroupsBypassSwitch`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `LoadImage`

## 关键参数

- `seed` = `999`
- `steps` = `45`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`StringConcatenate`、`VAEDecode`、`ResolutionSelector`、`FastGroupsBypassSwitch`、`EmptyLatentImage`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
