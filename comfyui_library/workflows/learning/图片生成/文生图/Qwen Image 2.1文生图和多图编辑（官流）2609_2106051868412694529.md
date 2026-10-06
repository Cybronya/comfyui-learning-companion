---
key: 图片生成/文生图/Qwen Image 2.1文生图和多图编辑（官流）2609_2106051868412694529.json
name: Qwen Image 2.1文生图和多图编辑（官流）2609_2106051868412694529
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图和多图编辑（官流）2609_2106051868412694529.json
hash: affc5a6c48c45a17
coverage: 0.526316
learned_at: 2026-10-06 21:48:59
nodes: [ResolutionSelector, MarkdownNote, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, KSampler, ComfySwitchNode, LoadImage, LoadImage, LoadImage, PrimitiveBoolean, PrimitiveInt, TextGenerate, BatchImagesNode, QwenImage21Cache, ModelAttentionBackend, CLIPLoader, TextGenerate, CLIPLoader, GetImageSize, Any Switch (rgthree), TextEncodeQwenImage21, ImageResizeKJv2, VAEDecode, Image Comparer (rgthree), SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageScaleToTotalPixels, LoadImage, LoadImage, PreviewAny, PrimitiveStringMultiline, LoadImage, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, PrimitiveStringMultiline]
patterns: []
missing: [BatchImagesNode, Fast Groups Bypasser (rgthree), ImageScaleToTotalPixels, ModelAttentionBackend, PrimitiveBoolean, TextGenerate, TextGenerate, GetImageSize, ImageResizeKJv2, PreviewAny]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 844359539850640, "steps": 30, "width": 1024}
discoveries: [次要节点 `BatchImagesNode` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识, 次要节点 `ModelAttentionBackend` 知识库中没有该节点类型的任何知识, 次要节点 `PrimitiveBoolean` 知识库中没有该节点类型的任何知识, 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识, 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识, 次要节点 `GetImageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Qwen Image 2.1文生图和多图编辑（官流）2609_2106051868412694529.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图和多图编辑（官流）2609_2106051868412694529.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

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

覆盖率 **53%**（20/38）

**有卡**：`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`LoadImage`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`VAEDecode`、`SaveImage`、`LoraLoaderModelOnly`

**缺卡**（10）：`BatchImagesNode`、`Fast Groups Bypasser (rgthree)`、`ImageScaleToTotalPixels`、`ModelAttentionBackend`、`PrimitiveBoolean`、`TextGenerate`、`TextGenerate`、`GetImageSize`、`ImageResizeKJv2`、`PreviewAny`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 学习发现

- 次要节点 `BatchImagesNode` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识
- 次要节点 `ModelAttentionBackend` 知识库中没有该节点类型的任何知识
- 次要节点 `PrimitiveBoolean` 知识库中没有该节点类型的任何知识
- 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识
- 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识
- 次要节点 `GetImageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明
