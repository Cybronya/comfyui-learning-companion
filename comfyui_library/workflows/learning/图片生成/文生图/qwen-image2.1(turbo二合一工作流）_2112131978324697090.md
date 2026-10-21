---
key: 图片生成/文生图/qwen-image2.1(turbo二合一工作流）_2112131978324697090.json
name: qwen-image2.1(turbo二合一工作流）_2112131978324697090
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-image2.1(turbo二合一工作流）_2112131978324697090.json
hash: dec2c0e797c5f2ca
coverage: 0.731707
learned_at: 2026-10-21 02:57:31
nodes: [MarkdownNote, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, ComfySwitchNode, Image Comparer (rgthree), LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveBoolean, PreviewAny, PrimitiveStringMultiline, TextGenerate, BatchImagesNode, ImageScaleToTotalPixels, ModelAttentionBackend, CLIPLoader, TextGenerate, CLIPLoader, PrimitiveStringMultiline, ImageResizeKJv2, GetImageSize, SamplerCustom, KSamplerSelect, QwenImage21Cache, LoadImage, LoadImage, Any Switch (rgthree), TextEncodeQwenImage21, ResolutionSelector, MarkdownNote, VAEDecode, SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly, PrimitiveInt, ManualSigmas, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/文生图/qwen-image2.1(turbo二合一工作流）_2112131978324697090.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen-image2.1(turbo二合一工作流）_2112131978324697090.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveBoolean`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `TextGenerate`
- `BatchImagesNode`
- `ImageScaleToTotalPixels`
- `ModelAttentionBackend`
- `CLIPLoader`
- `TextGenerate`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `ImageResizeKJv2`
- `GetImageSize`
- `SamplerCustom` ★核心
- `KSamplerSelect` ★核心
- `QwenImage21Cache`
- `LoadImage`
- `LoadImage`
- `Any Switch (rgthree)`
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `MarkdownNote`
- `VAEDecode` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `ManualSigmas`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **73%**（30/41）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`LoadImage`、`PrimitiveBoolean`、`TextGenerate`、`BatchImagesNode`、`ImageScaleToTotalPixels`、`ModelAttentionBackend`、`ImageResizeKJv2`、`GetImageSize`、`SamplerCustom`、`KSamplerSelect`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`ResolutionSelector`、`VAEDecode`、`SaveImage`、`LoraLoaderModelOnly`、`ManualSigmas`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
