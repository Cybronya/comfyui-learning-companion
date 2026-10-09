---
key: 图片生成/图生图/Qwen image 2.1图片编辑_2101946565576454146.json
name: Qwen image 2.1图片编辑_2101946565576454146.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1图片编辑_2101946565576454146.json
hash: 518beb89eb46237e
coverage: 0.923077
learned_at: 2026-10-09 22:19:27
nodes: [UNETLoader, VAELoader, EmptyLatentImage, VAEDecode, QwenImage21Cache, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CLIPLoader, ResolutionSelector, easy showAnything, SaveImage, TextGenerateLTX2Prompt, CLIPLoader, BatchImagesNode, TextEncodeQwenImage21, KSampler, SaveImageAdvanced, ComfySwitchNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen image 2.1图片编辑_2101946565576454146.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2101946565576454146.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `QwenImage21Cache`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `ResolutionSelector`
- `easy showAnything`
- `SaveImage`
- `TextGenerateLTX2Prompt`
- `CLIPLoader`
- `BatchImagesNode`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `SaveImageAdvanced`
- `ComfySwitchNode`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `999`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（24/26）

**有卡**：`UNETLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`QwenImage21Cache`、`LoadImage`、`CLIPLoader`、`ResolutionSelector`、`SaveImage`、`TextGenerateLTX2Prompt`、`BatchImagesNode`、`TextEncodeQwenImage21`、`KSampler`、`SaveImageAdvanced`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
