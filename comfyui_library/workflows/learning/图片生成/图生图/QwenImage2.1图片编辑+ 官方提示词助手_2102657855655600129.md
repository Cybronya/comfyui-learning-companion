---
key: 图片生成/图生图/QwenImage2.1图片编辑+ 官方提示词助手_2102657855655600129.json
name: QwenImage2.1图片编辑+ 官方提示词助手_2102657855655600129
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QwenImage2.1图片编辑+ 官方提示词助手_2102657855655600129.json
hash: 996ff9bda90afbbd
coverage: 0.492754
learned_at: 2026-10-21 00:43:53
nodes: [ImageScaleToTotalPixels, ImageScaleToTotalPixels, TextGenerate, JsonExtractString, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, KSampler, ComfySwitchNode, QwenImage21Cache, Fast Groups Bypasser (rgthree), LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, SetNode, SetNode, SetNode, SetNode, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, SetNode, LoadImage, LoadImage, SetNode, ImageScaleToTotalPixels, ImageScaleToTotalPixels, SetNode, SetNode, LoadImage, ImageScaleToTotalPixels, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPLoader, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, TextConcatenator, easy showAnything, easy showAnything, LoadImage, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Any Switch (rgthree), TextEncodeQwenImage21, LoadImage, ResolutionSelector, SaveImageAdvanced, SaveImage, GetNode, ImageBatchMulti, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 797597453131280, "steps": 25, "width": 1024}
---

# 图片生成/图生图/QwenImage2.1图片编辑+ 官方提示词助手_2102657855655600129.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/QwenImage2.1图片编辑+ 官方提示词助手_2102657855655600129.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `TextGenerate`
- `JsonExtractString`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `SetNode`
- `SetNode`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `TextConcatenator`
- `easy showAnything`
- `easy showAnything`
- `LoadImage`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `TextEncodeQwenImage21`
- `LoadImage`
- `ResolutionSelector`
- `SaveImageAdvanced`
- `SaveImage`
- `GetNode`
- `ImageBatchMulti`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `797597453131280`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **49%**（34/69）

**有卡**：`ImageScaleToTotalPixels`、`TextGenerate`、`JsonExtractString`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`QwenImage21Cache`、`LoadImage`、`TextConcatenator`、`VAEDecode`、`TextEncodeQwenImage21`、`ResolutionSelector`、`SaveImageAdvanced`、`SaveImage`、`ImageBatchMulti`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
