---
key: 图片生成/图生图/QwenImage2.1-图像编辑换头_2101872643862523905.json
name: QwenImage2.1-图像编辑换头_2101872643862523905
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QwenImage2.1-图像编辑换头_2101872643862523905.json
hash: c036bbbdd2dbd5e4
coverage: 0.952381
learned_at: 2026-10-21 00:43:52
nodes: [UNETLoader, VAELoader, EmptyLatentImage, VAEDecode, ComfySwitchNode, QwenImage21Cache, CLIPLoader, KSampler, SaveImageAdvanced, SaveImage, TextEncodeQwenImage21, ResolutionSelector, Text, TextGenerateLTX2Prompt, LoadImage, BatchImagesNode, SaveImageAdvanced, CLIPLoader, ImageConcatMulti, LoadImage, ImageConcatMulti]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 50, "width": 1024}
---

# 图片生成/图生图/QwenImage2.1-图像编辑换头_2101872643862523905.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/QwenImage2.1-图像编辑换头_2101872643862523905.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `CLIPLoader`
- `KSampler` ★核心
- `SaveImageAdvanced`
- `SaveImage`
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `Text`
- `TextGenerateLTX2Prompt`
- `LoadImage`
- `BatchImagesNode`
- `SaveImageAdvanced`
- `CLIPLoader`
- `ImageConcatMulti`
- `LoadImage`
- `ImageConcatMulti`

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

覆盖率 **95%**（20/21）

**有卡**：`UNETLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`QwenImage21Cache`、`CLIPLoader`、`KSampler`、`SaveImageAdvanced`、`SaveImage`、`TextEncodeQwenImage21`、`ResolutionSelector`、`Text`、`TextGenerateLTX2Prompt`、`LoadImage`、`BatchImagesNode`、`ImageConcatMulti`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
