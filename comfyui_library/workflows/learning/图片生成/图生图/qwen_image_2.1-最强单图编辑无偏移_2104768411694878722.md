---
key: 图片生成/图生图/qwen_image_2.1-最强单图编辑无偏移_2104768411694878722.json
name: qwen_image_2.1-最强单图编辑无偏移_2104768411694878722
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen_image_2.1-最强单图编辑无偏移_2104768411694878722.json
hash: 8e99c31cb9e080e5
coverage: 0.8
learned_at: 2026-10-21 00:46:21
nodes: [CLIPLoader, UNETLoader, QwenImage21Cache, KSampler, ComfySwitchNode, Image Comparer (rgthree), LoadImage, Text, TextEncodeQwenImage21, VAELoader, ResolutionSelector, EmptyLatentImage, VAEDecode, PreviewImage, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 61159198708878, "steps": 25, "width": 1024}
---

# 图片生成/图生图/qwen_image_2.1-最强单图编辑无偏移_2104768411694878722.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen_image_2.1-最强单图编辑无偏移_2104768411694878722.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `KSampler` ★核心
- `ComfySwitchNode`
- `Image Comparer (rgthree)`
- `LoadImage`
- `Text`
- `TextEncodeQwenImage21`
- `VAELoader`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`

## 关键参数

- `seed` = `61159198708878`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（12/15）

**有卡**：`CLIPLoader`、`UNETLoader`、`QwenImage21Cache`、`KSampler`、`LoadImage`、`Text`、`TextEncodeQwenImage21`、`VAELoader`、`ResolutionSelector`、`EmptyLatentImage`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
