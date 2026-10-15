---
key: 图片生成/文生图/qwen-image2.1(多功能官流）_2105926870020747266.json
name: qwen-image2.1(多功能官流）_2105926870020747266
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-image2.1(多功能官流）_2105926870020747266.json
hash: bf969085097b939e
coverage: 0.736842
learned_at: 2026-10-10 20:59:25
nodes: [ResolutionSelector, MarkdownNote, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, KSampler, ComfySwitchNode, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveBoolean, PrimitiveInt, PreviewAny, PrimitiveStringMultiline, TextGenerate, BatchImagesNode, ImageScaleToTotalPixels, QwenImage21Cache, ModelAttentionBackend, CLIPLoader, TextGenerate, CLIPLoader, PrimitiveStringMultiline, GetImageSize, Any Switch (rgthree), TextEncodeQwenImage21, ImageResizeKJv2, VAEDecode, Image Comparer (rgthree), LoadImage, LoadImage, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 755988244719898, "steps": 30, "width": 1024}
---

# 图片生成/文生图/qwen-image2.1(多功能官流）_2105926870020747266.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen-image2.1(多功能官流）_2105926870020747266.json`

## 结构

**节点**（38 个）：
- `ResolutionSelector`
- `MarkdownNote`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage`
- `KSampler`
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `TextGenerate`
- `BatchImagesNode`
- `ImageScaleToTotalPixels`
- `QwenImage21Cache`
- `ModelAttentionBackend`
- `CLIPLoader`
- `TextGenerate`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `GetImageSize`
- `Any Switch (rgthree)`
- `TextEncodeQwenImage21`
- `ImageResizeKJv2`
- `VAEDecode`
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `SaveImage`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `755988244719898`
- `steps` = `30`
- `width` = `1024`

## 知识

覆盖率 **74%**（28/38）

**有卡**：`ResolutionSelector`、`MarkdownNote`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`ComfySwitchNode`、`LoadImage`、`PrimitiveBoolean`、`PrimitiveInt`、`PreviewAny`、`PrimitiveStringMultiline`、`TextGenerate`、`BatchImagesNode`、`ImageScaleToTotalPixels`、`QwenImage21Cache`、`ModelAttentionBackend`、`GetImageSize`、`Any Switch (rgthree)`、`TextEncodeQwenImage21`
