---
key: 图片生成/图生图/Qwen Image 2.1文生图和多图编辑（官流）2609_2106051868412694529.json
name: Qwen Image 2.1文生图和多图编辑（官流）2609_2106051868412694529.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1文生图和多图编辑（官流）2609_2106051868412694529.json
hash: 9ea71e7aabf45bcd
coverage: 0.736842
learned_at: 2026-10-09 22:09:18
nodes: [ResolutionSelector, MarkdownNote, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, KSampler, ComfySwitchNode, LoadImage, LoadImage, LoadImage, PrimitiveBoolean, PrimitiveInt, TextGenerate, BatchImagesNode, QwenImage21Cache, ModelAttentionBackend, CLIPLoader, TextGenerate, CLIPLoader, GetImageSize, Any Switch (rgthree), TextEncodeQwenImage21, ImageResizeKJv2, VAEDecode, Image Comparer (rgthree), SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageScaleToTotalPixels, LoadImage, LoadImage, PreviewAny, PrimitiveStringMultiline, LoadImage, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 844359539850640, "steps": 30, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1文生图和多图编辑（官流）2609_2106051868412694529.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2106051868412694529.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `ResolutionSelector`
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `TextGenerate`
- `BatchImagesNode`
- `QwenImage21Cache`
- `ModelAttentionBackend`
- `CLIPLoader`
- `TextGenerate`
- `CLIPLoader`
- `GetImageSize`
- `Any Switch (rgthree)`
- `TextEncodeQwenImage21`
- `ImageResizeKJv2`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageScaleToTotalPixels`
- `LoadImage`
- `LoadImage`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `844359539850640`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **74%**（28/38）

**有卡**：`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`LoadImage`、`PrimitiveBoolean`、`TextGenerate`、`BatchImagesNode`、`QwenImage21Cache`、`ModelAttentionBackend`、`GetImageSize`、`TextEncodeQwenImage21`、`ImageResizeKJv2`、`VAEDecode`、`SaveImage`、`LoraLoaderModelOnly`、`ImageScaleToTotalPixels`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
