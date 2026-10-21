---
key: 图片生成/图生图/Qwen image 2.1 图生图提示词增强_2101913388136886273.json
name: Qwen image 2.1 图生图提示词增强_2101913388136886273
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 图生图提示词增强_2101913388136886273.json
hash: 01377f7adba6095a
coverage: 0.833333
learned_at: 2026-10-21 00:42:55
nodes: [VAEDecode, UNETLoader, KSampler, ResolutionSelector, BatchImagesNode, CLIPLoader, LoadImage, EmptyLatentImage, ComfySwitchNode, PrimitiveStringMultiline, CLIPLoader, TextEncodeQwenImage21, easy showAnything, VAELoader, LoadImage, SaveImage, PrimitiveBoolean, TextGenerateLTX2Prompt]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 942754696221181, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen image 2.1 图生图提示词增强_2101913388136886273.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 图生图提示词增强_2101913388136886273.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `ResolutionSelector`
- `BatchImagesNode`
- `CLIPLoader`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `easy showAnything`
- `VAELoader`
- `LoadImage`
- `SaveImage`
- `PrimitiveBoolean`
- `TextGenerateLTX2Prompt`

## 关键参数

- `seed` = `942754696221181`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`VAEDecode`、`UNETLoader`、`KSampler`、`ResolutionSelector`、`BatchImagesNode`、`CLIPLoader`、`LoadImage`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`VAELoader`、`SaveImage`、`PrimitiveBoolean`、`TextGenerateLTX2Prompt`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
