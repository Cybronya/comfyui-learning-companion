---
key: 图片生成/文生图/Qwen Image 2.1文生图和多图编辑（官流）2609_2106051868412694529.json
name: Qwen Image 2.1文生图和多图编辑（官流）2609_2106051868412694529
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图和多图编辑（官流）2609_2106051868412694529.json
hash: affc5a6c48c45a17
coverage: 0.736842
learned_at: 2026-10-10 21:27:46
nodes: [ResolutionSelector, MarkdownNote, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, KSampler, ComfySwitchNode, LoadImage, LoadImage, LoadImage, PrimitiveBoolean, PrimitiveInt, TextGenerate, BatchImagesNode, QwenImage21Cache, ModelAttentionBackend, CLIPLoader, TextGenerate, CLIPLoader, GetImageSize, Any Switch (rgthree), TextEncodeQwenImage21, ImageResizeKJv2, VAEDecode, Image Comparer (rgthree), SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageScaleToTotalPixels, LoadImage, LoadImage, PreviewAny, PrimitiveStringMultiline, LoadImage, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 844359539850640, "steps": 30, "width": 1024}
---

# 图片生成/文生图/Qwen Image 2.1文生图和多图编辑（官流）2609_2106051868412694529.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图和多图编辑（官流）2609_2106051868412694529.json`

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
- `VAEDecode`
- `Image Comparer (rgthree)`
- `SaveImage`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
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

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `844359539850640`
- `steps` = `30`
- `width` = `1024`

## 知识

覆盖率 **74%**（28/38）

**有卡**：`ResolutionSelector`、`MarkdownNote`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`ComfySwitchNode`、`LoadImage`、`PrimitiveBoolean`、`PrimitiveInt`、`TextGenerate`、`BatchImagesNode`、`QwenImage21Cache`、`ModelAttentionBackend`、`GetImageSize`、`Any Switch (rgthree)`、`TextEncodeQwenImage21`、`ImageResizeKJv2`、`VAEDecode`、`Image Comparer (rgthree)`、`SaveImage`、`LoraLoaderModelOnly`
