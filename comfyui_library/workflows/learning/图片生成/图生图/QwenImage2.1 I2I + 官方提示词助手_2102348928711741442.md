---
key: 图片生成/图生图/QwenImage2.1 I2I + 官方提示词助手_2102348928711741442.json
name: QwenImage2.1 I2I + 官方提示词助手_2102348928711741442.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QwenImage2.1 I2I + 官方提示词助手_2102348928711741442.json
hash: 6fa58af1f3d29672
coverage: 0.492754
learned_at: 2026-10-09 22:27:11
nodes: [ResolutionSelector, SaveImageAdvanced, ImageScaleToTotalPixels, ImageScaleToTotalPixels, TextGenerate, JsonExtractString, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, KSampler, ComfySwitchNode, QwenImage21Cache, Fast Groups Bypasser (rgthree), LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, SetNode, SetNode, SetNode, SetNode, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, SetNode, LoadImage, LoadImage, SetNode, ImageScaleToTotalPixels, ImageScaleToTotalPixels, SetNode, SetNode, LoadImage, ImageScaleToTotalPixels, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPLoader, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, TextConcatenator, PrimitiveStringMultiline, easy showAnything, easy showAnything, LoadImage, LoadImage, SaveImage, VAEDecode, ImageBatchMulti, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Any Switch (rgthree), TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 384223180024151, "steps": 25, "width": 1024}
---

# 图片生成/图生图/QwenImage2.1 I2I + 官方提示词助手_2102348928711741442.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102348928711741442.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `ResolutionSelector`
- `SaveImageAdvanced`
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
- `GetNode`
- `CLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `TextConcatenator`
- `PrimitiveStringMultiline`
- `easy showAnything`
- `easy showAnything`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `VAEDecode` ★核心
- `ImageBatchMulti`
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

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `384223180024151`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **49%**（34/69）

**有卡**：`ResolutionSelector`、`SaveImageAdvanced`、`ImageScaleToTotalPixels`、`TextGenerate`、`JsonExtractString`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`QwenImage21Cache`、`LoadImage`、`TextConcatenator`、`SaveImage`、`VAEDecode`、`ImageBatchMulti`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
