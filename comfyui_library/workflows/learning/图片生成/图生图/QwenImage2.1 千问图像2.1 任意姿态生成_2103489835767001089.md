---
key: 图片生成/图生图/QwenImage2.1 千问图像2.1 任意姿态生成_2103489835767001089.json
name: QwenImage2.1 千问图像2.1 任意姿态生成_2103489835767001089
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QwenImage2.1 千问图像2.1 任意姿态生成_2103489835767001089.json
hash: 637c499ffb1fd035
coverage: 0.733333
learned_at: 2026-10-21 00:43:52
nodes: [CLIPLoader, VAELoader, VAEDecode, SaveImage, Seed (rgthree), ImageScaleToTotalPixels, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, Note, easy loraStackApply, QwenImage21Cache, KSampler, LoadImage, easy loraStack, UNETLoader, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, Fast Groups Bypasser (rgthree), LoadImage, PrimitiveStringMultiline, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 269532970235213, "steps": 25, "width": 1024}
---

# 图片生成/图生图/QwenImage2.1 千问图像2.1 任意姿态生成_2103489835767001089.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/QwenImage2.1 千问图像2.1 任意姿态生成_2103489835767001089.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `Seed (rgthree)`
- `ImageScaleToTotalPixels`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Note`
- `easy loraStackApply`
- `QwenImage21Cache`
- `KSampler` ★核心
- `LoadImage`
- `easy loraStack`
- `UNETLoader` ★核心
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `PrimitiveStringMultiline`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `TextEncodeQwenImage21`

## 关键参数

- `seed` = `269532970235213`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **73%**（33/45）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`SaveImage`、`Seed (rgthree)`、`ImageScaleToTotalPixels`、`LoadImage`、`easy loraStackApply`、`QwenImage21Cache`、`KSampler`、`easy loraStack`、`UNETLoader`、`ResolutionSelector`、`EmptyLatentImage`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
