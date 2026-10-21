---
key: 图片生成/图生图/Qwen image 2.1图片编辑（双图）_2101862560432746498.json
name: Qwen image 2.1图片编辑（双图）_2101862560432746498
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1图片编辑（双图）_2101862560432746498.json
hash: 3966851b1d541f69
coverage: 0.933333
learned_at: 2026-10-21 00:42:59
nodes: [UNETLoader, VAELoader, QwenImage21Cache, ImageConcatMulti, LoadImage, LoadImage, LoadImage, CLIPLoader, KSampler, SaveImageAdvanced, SaveImage, VAEDecode, ImageConcatMulti, LoadImage, ResolutionSelector, ComfySwitchNode, EmptyLatentImage, LoadImage, LoadImage, LoadImage, Int, Int, CLIPLoader, easy showAnything, TextEncodeQwenImage21, LoadImage, BatchImagesNode, LoadImage, LoadImage, TextGenerateLTX2Prompt]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen image 2.1图片编辑（双图）_2101862560432746498.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1图片编辑（双图）_2101862560432746498.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `QwenImage21Cache`
- `ImageConcatMulti`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `KSampler` ★核心
- `SaveImageAdvanced`
- `SaveImage`
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `LoadImage`
- `ResolutionSelector`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Int`
- `Int`
- `CLIPLoader`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `LoadImage`
- `BatchImagesNode`
- `LoadImage`
- `LoadImage`
- `TextGenerateLTX2Prompt`

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

覆盖率 **93%**（28/30）

**有卡**：`UNETLoader`、`VAELoader`、`QwenImage21Cache`、`ImageConcatMulti`、`LoadImage`、`CLIPLoader`、`KSampler`、`SaveImageAdvanced`、`SaveImage`、`VAEDecode`、`ResolutionSelector`、`EmptyLatentImage`、`Int`、`TextEncodeQwenImage21`、`BatchImagesNode`、`TextGenerateLTX2Prompt`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
