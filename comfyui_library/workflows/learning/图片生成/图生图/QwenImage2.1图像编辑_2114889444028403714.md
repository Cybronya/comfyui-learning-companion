---
key: 图片生成/图生图/QwenImage2.1图像编辑_2114889444028403714.json
name: QwenImage2.1图像编辑_2114889444028403714
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QwenImage2.1图像编辑_2114889444028403714.json
hash: e7f572086ef04dd7
coverage: 0.772727
learned_at: 2026-10-30 17:51:09
nodes: [Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), VAELoader, ResolutionSelector, CLIPLoader, UNETLoader, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, VAEDecode, SaveImage, ComfySwitchNode, TextEncodeQwenImage21, Seed (rgthree), PrimitiveStringMultiline, EmptyLatentImage, KSampler, easy loraStackApply, QwenImage21Cache, easy loraStack, ComfySwitchNode, EmptyLatentImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 565735262538672, "steps": 25, "width": 1024}
---

# 图片生成/图生图/QwenImage2.1图像编辑_2114889444028403714.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/QwenImage2.1图像编辑_2114889444028403714.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `VAELoader`
- `ResolutionSelector`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `SaveImage`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `Seed (rgthree)`
- `PrimitiveStringMultiline`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `easy loraStackApply`
- `QwenImage21Cache`
- `easy loraStack`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `565735262538672`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（34/44）

**有卡**：`VAELoader`、`ResolutionSelector`、`CLIPLoader`、`UNETLoader`、`LoadImage`、`ImageScaleToTotalPixels`、`VAEDecode`、`SaveImage`、`TextEncodeQwenImage21`、`Seed (rgthree)`、`EmptyLatentImage`、`KSampler`、`easy loraStackApply`、`QwenImage21Cache`、`easy loraStack`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
