---
key: 图片生成/图生图/AI代码侠土豆-Qwen Image 2.1 图生图_2101914903496974338.json
name: AI代码侠土豆-Qwen Image 2.1 图生图_2101914903496974338
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/AI代码侠土豆-Qwen Image 2.1 图生图_2101914903496974338.json
hash: 66b84af7d8568738
coverage: 0.486111
learned_at: 2026-10-21 00:38:36
nodes: [Label (rgthree), Label (rgthree), Label (rgthree), LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, UNETLoader, CLIPLoader, VAELoader, SetNode, SetNode, SetNode, SetNode, EmptyLatentImage, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetNode, SetNode, TextEncodeQwenImage21, GetNode, SetNode, SetNode, GetImageSize, EmptyLatentImage, KSampler, GetNode, GetNode, GetNode, MarkdownNote, SaveImage, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoadImage, Fast Groups Bypasser (rgthree), LoadImage, Text Multiline, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1108788226273640, "steps": 40, "width": 1024}
---

# 图片生成/图生图/AI代码侠土豆-Qwen Image 2.1 图生图_2101914903496974338.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/AI代码侠土豆-Qwen Image 2.1 图生图_2101914903496974338.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（72 个）：
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `GetNode`
- `SetNode`
- `TextEncodeQwenImage21`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetImageSize`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `MarkdownNote`
- `SaveImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `Text Multiline`
- `ResolutionSelector`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1108788226273640`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **49%**（35/72）

**有卡**：`Label (rgthree)`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImage21`、`GetImageSize`、`KSampler`、`SaveImage`、`Text Multiline`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
