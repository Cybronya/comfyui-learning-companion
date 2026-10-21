---
key: 图片生成/图生图/Qwen image 2.1单图编辑_2101881268609830914.json
name: Qwen image 2.1单图编辑_2101881268609830914
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1单图编辑_2101881268609830914.json
hash: 97d6c8288110289e
coverage: 0.903226
learned_at: 2026-10-21 00:42:56
nodes: [TextEncodeQwenImage21, KSampler, UNETLoader, CLIPLoader, VAELoader, CLIPLoader, EmptyLatentImage, ComfySwitchNode, QwenImage21Cache, VAEDecode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, easy cleanGpuUsed, easy showAnything, LoadImage, ResolutionSelector, ImageConcatMulti, SaveImageAdvanced, ImageConcatMulti, SaveImageAdvanced, SaveImage, BatchImagesNode, TextGenerateLTX2Prompt, JjkText, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen image 2.1单图编辑_2101881268609830914.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1单图编辑_2101881268609830914.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `easy cleanGpuUsed`
- `easy showAnything`
- `LoadImage`
- `ResolutionSelector`
- `ImageConcatMulti`
- `SaveImageAdvanced`
- `ImageConcatMulti`
- `SaveImageAdvanced`
- `SaveImage`
- `BatchImagesNode`
- `TextGenerateLTX2Prompt`
- `JjkText`
- `LoadImage`

## 关键参数

- `seed` = `999`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **90%**（28/31）

**有卡**：`TextEncodeQwenImage21`、`KSampler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`QwenImage21Cache`、`VAEDecode`、`LoadImage`、`easy cleanGpuUsed`、`ResolutionSelector`、`ImageConcatMulti`、`SaveImageAdvanced`、`SaveImage`、`BatchImagesNode`、`TextGenerateLTX2Prompt`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
