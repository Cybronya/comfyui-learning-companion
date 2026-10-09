---
key: 图片生成/图生图/(V2)-qwen-image2.1-编辑_2102577867103236097.json
name: (V2)-qwen-image2.1-编辑_2102577867103236097.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/(V2)-qwen-image2.1-编辑_2102577867103236097.json
hash: 5ae7320c428ca74c
coverage: 0.705882
learned_at: 2026-10-09 22:19:29
nodes: [MarkdownNote, Note, UNETLoader, VAELoader, QwenImage21Cache, TextEncodeQwenImage21, LoadImage, LoadImage, PrimitiveStringMultiline, StringConcatenate, BatchImagesNode, ImageScaleToTotalPixels, SaveImage, SaveImageAdvanced, KSampler, VAEDecode, RegexExtract, CLIPLoader, TextGenerate, LoadImage, ComfySwitchNode, PreviewAny, Image Comparer (rgthree), PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), PrimitiveBoolean, ComfySwitchNode, EmptyLatentImage, LoadImage, LoadImage, ResolutionSelector, LoadImage, PrimitiveBoolean, PrimitiveInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 66651296590055, "steps": 25, "width": 1024}
---

# 图片生成/图生图/(V2)-qwen-image2.1-编辑_2102577867103236097.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102577867103236097.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `MarkdownNote`
- `Note`
- `UNETLoader` ★核心
- `VAELoader`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `StringConcatenate`
- `BatchImagesNode`
- `ImageScaleToTotalPixels`
- `SaveImage`
- `SaveImageAdvanced`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `RegexExtract`
- `CLIPLoader`
- `TextGenerate`
- `LoadImage`
- `ComfySwitchNode`
- `PreviewAny`
- `Image Comparer (rgthree)`
- `PrimitiveStringMultiline`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`
- `LoadImage`
- `PrimitiveBoolean`
- `PrimitiveInt`

## 关键参数

- `seed` = `66651296590055`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **71%**（24/34）

**有卡**：`UNETLoader`、`VAELoader`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`LoadImage`、`StringConcatenate`、`BatchImagesNode`、`ImageScaleToTotalPixels`、`SaveImage`、`SaveImageAdvanced`、`KSampler`、`VAEDecode`、`RegexExtract`、`CLIPLoader`、`TextGenerate`、`PrimitiveBoolean`、`EmptyLatentImage`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
