---
key: 图片生成/图生图/Qwen+image+2.1图片编辑_2104102668070383618.json
name: Qwen+image+2.1图片编辑_2104102668070383618
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen+image+2.1图片编辑_2104102668070383618.json
hash: 4ac094a66ee966c5
coverage: 0.705882
learned_at: 2026-10-21 00:43:04
nodes: [MarkdownNote, Note, UNETLoader, VAELoader, QwenImage21Cache, TextEncodeQwenImage21, LoadImage, LoadImage, PrimitiveStringMultiline, StringConcatenate, BatchImagesNode, ImageScaleToTotalPixels, SaveImage, SaveImageAdvanced, KSampler, VAEDecode, RegexExtract, CLIPLoader, TextGenerate, ComfySwitchNode, PreviewAny, Image Comparer (rgthree), PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), PrimitiveBoolean, ComfySwitchNode, EmptyLatentImage, LoadImage, ResolutionSelector, PrimitiveBoolean, PrimitiveInt, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 66651296590055, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen+image+2.1图片编辑_2104102668070383618.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen+image+2.1图片编辑_2104102668070383618.json`

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
- `ComfySwitchNode`
- `PreviewAny`
- `Image Comparer (rgthree)`
- `PrimitiveStringMultiline`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `ResolutionSelector`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `LoadImage`
- `LoadImage`
- `LoadImage`

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
