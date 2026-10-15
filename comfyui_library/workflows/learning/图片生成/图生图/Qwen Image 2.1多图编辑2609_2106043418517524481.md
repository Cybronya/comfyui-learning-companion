---
key: 图片生成/图生图/Qwen Image 2.1多图编辑2609_2106043418517524481.json
name: Qwen Image 2.1多图编辑2609_2106043418517524481
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1多图编辑2609_2106043418517524481.json
hash: 3b5c0a323da06a9f
coverage: 0.463768
learned_at: 2026-10-15 22:25:14
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, UNETLoader, CLIPLoader, VAELoader, SetNode, EmptyLatentImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, TextEncodeQwenImage21, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ResolutionSelector, GetNode, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, Text Multiline, MarkdownNote, GetNode, GetNode, GetNode, GetNode, GetImageSize, EmptyLatentImage, KSampler, VAEDecode, GetNode, SaveImage, SetNode, SetNode, SetNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 255948325634901, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1多图编辑2609_2106043418517524481.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1多图编辑2609_2106043418517524481.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
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
- `EmptyLatentImage` ★核心
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
- `SetNode`
- `TextEncodeQwenImage21`
- `SetNode`
- `SetNode`
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
- `ResolutionSelector`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `Text Multiline`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSize`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `SaveImage`
- `SetNode`
- `SetNode`
- `SetNode`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `255948325634901`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **46%**（32/69）

**有卡**：`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImage21`、`ResolutionSelector`、`Text Multiline`、`GetImageSize`、`KSampler`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
