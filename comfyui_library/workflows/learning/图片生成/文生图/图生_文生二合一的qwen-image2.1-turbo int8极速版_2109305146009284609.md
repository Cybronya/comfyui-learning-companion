---
key: 图片生成/文生图/图生_文生二合一的qwen-image2.1-turbo int8极速版_2109305146009284609.json
name: 图生_文生二合一的qwen-image2.1-turbo int8极速版_2109305146009284609
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/图生_文生二合一的qwen-image2.1-turbo int8极速版_2109305146009284609.json
hash: b0630eac7259783b
coverage: 0.717949
learned_at: 2026-10-21 02:59:37
nodes: [PrimitiveStringMultiline, TextGenerate, BatchImagesNode, ImageScaleToTotalPixels, CLIPLoader, PrimitiveStringMultiline, KSamplerSelect, MarkdownNote, ResolutionSelector, MarkdownNote, UNETLoader, LoraLoaderModelOnly, QwenImage21Cache, ModelAttentionBackend, TextGenerate, LoraLoaderModelOnly, VAELoader, CLIPLoader, TextEncodeQwenImage21, ComfySwitchNode, SamplerCustom, ManualSigmas, EmptyLatentImage, PrimitiveBoolean, VAEDecode, PreviewAny, Any Switch (rgthree), CLIPLoader, PrimitiveInt, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, SaveImage, 孤海注释, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/文生图/图生_文生二合一的qwen-image2.1-turbo int8极速版_2109305146009284609.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/图生_文生二合一的qwen-image2.1-turbo int8极速版_2109305146009284609.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `PrimitiveStringMultiline`
- `TextGenerate`
- `BatchImagesNode`
- `ImageScaleToTotalPixels`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `KSamplerSelect` ★核心
- `MarkdownNote`
- `ResolutionSelector`
- `MarkdownNote`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `QwenImage21Cache`
- `ModelAttentionBackend`
- `TextGenerate`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `SamplerCustom` ★核心
- `ManualSigmas`
- `EmptyLatentImage` ★核心
- `PrimitiveBoolean`
- `VAEDecode` ★核心
- `PreviewAny`
- `Any Switch (rgthree)`
- `CLIPLoader`
- `PrimitiveInt`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `孤海注释`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **72%**（28/39）

**有卡**：`TextGenerate`、`BatchImagesNode`、`ImageScaleToTotalPixels`、`CLIPLoader`、`KSamplerSelect`、`ResolutionSelector`、`UNETLoader`、`LoraLoaderModelOnly`、`QwenImage21Cache`、`ModelAttentionBackend`、`VAELoader`、`TextEncodeQwenImage21`、`SamplerCustom`、`ManualSigmas`、`EmptyLatentImage`、`PrimitiveBoolean`、`VAEDecode`、`LoadImage`、`SaveImage`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
