---
key: 图片生成/图生图/Qwen image 2.1图片编辑【自动提示词版】_2101837155051073537.json
name: Qwen image 2.1图片编辑【自动提示词版】_2101837155051073537
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1图片编辑【自动提示词版】_2101837155051073537.json
hash: 8245ee0f66c17485
coverage: 0.931034
learned_at: 2026-10-21 00:42:58
nodes: [UNETLoader, VAELoader, VAEDecode, QwenImage21Cache, LoadImage, CLIPLoader, KSampler, SaveImage, BatchImagesNode, CLIPLoader, easy showAnything, EmptyLatentImage, TextEncodeQwenImage21, ComfySwitchNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ImageConcatMulti, SaveImageAdvanced, ImageConcatMulti, SaveImageAdvanced, LoadImage, TextGenerateLTX2Prompt, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen image 2.1图片编辑【自动提示词版】_2101837155051073537.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1图片编辑【自动提示词版】_2101837155051073537.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `QwenImage21Cache`
- `LoadImage`
- `CLIPLoader`
- `KSampler` ★核心
- `SaveImage`
- `BatchImagesNode`
- `CLIPLoader`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageConcatMulti`
- `SaveImageAdvanced`
- `ImageConcatMulti`
- `SaveImageAdvanced`
- `LoadImage`
- `TextGenerateLTX2Prompt`
- `ResolutionSelector`

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

覆盖率 **93%**（27/29）

**有卡**：`UNETLoader`、`VAELoader`、`VAEDecode`、`QwenImage21Cache`、`LoadImage`、`CLIPLoader`、`KSampler`、`SaveImage`、`BatchImagesNode`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`ImageConcatMulti`、`SaveImageAdvanced`、`TextGenerateLTX2Prompt`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
