---
key: 图片生成/图生图/智能修图丨Qwen Image 2.1丨指令增强·多图编辑_2113116700873940993.json
name: 智能修图丨Qwen Image 2.1丨指令增强·多图编辑_2113116700873940993
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/智能修图丨Qwen Image 2.1丨指令增强·多图编辑_2113116700873940993.json
hash: b988d5c862e2cdb5
coverage: 0.928571
learned_at: 2026-10-26 22:06:22
nodes: [easy positive, ResolutionSelector, LoadImage, easy positive, CLIPLoader, PrimitiveBoolean, VAELoader, CLIPLoader, UNETLoader, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, EmptyLatentImage, ImageScaleToTotalPixels, QwenImage21Cache, StringConcatenate, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, BatchImagesNode, TextGenerate, JsonExtractString, RegexMatch, ComfySwitchNode, ShowText|pysssss, TextEncodeQwenImage21, ComfySwitchNode, KSampler, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1184, "sampler_name": "euler", "scheduler": "simple", "seed": 633386983712418, "steps": 25, "width": 896}
---

# 图片生成/图生图/智能修图丨Qwen Image 2.1丨指令增强·多图编辑_2113116700873940993.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/智能修图丨Qwen Image 2.1丨指令增强·多图编辑_2113116700873940993.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `easy positive`
- `ResolutionSelector`
- `LoadImage`
- `easy positive`
- `CLIPLoader`
- `PrimitiveBoolean`
- `VAELoader`
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
- `EmptyLatentImage` ★核心
- `ImageScaleToTotalPixels`
- `QwenImage21Cache`
- `StringConcatenate`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `BatchImagesNode`
- `TextGenerate`
- `JsonExtractString`
- `RegexMatch`
- `ComfySwitchNode`
- `ShowText|pysssss`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `width` = `896`
- `height` = `1184`
- `batch_size` = `1`
- `seed` = `633386983712418`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（39/42）

**有卡**：`easy positive`、`ResolutionSelector`、`LoadImage`、`CLIPLoader`、`PrimitiveBoolean`、`VAELoader`、`UNETLoader`、`EmptyLatentImage`、`ImageScaleToTotalPixels`、`QwenImage21Cache`、`StringConcatenate`、`BatchImagesNode`、`TextGenerate`、`JsonExtractString`、`RegexMatch`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
