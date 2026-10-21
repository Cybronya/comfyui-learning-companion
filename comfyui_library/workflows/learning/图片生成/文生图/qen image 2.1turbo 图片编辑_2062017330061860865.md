---
key: 图片生成/文生图/qen image 2.1turbo 图片编辑_2062017330061860865.json
name: qen image 2.1turbo 图片编辑_2062017330061860865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qen image 2.1turbo 图片编辑_2062017330061860865.json
hash: 5a35d1c3b46e55d0
coverage: 0.888889
learned_at: 2026-10-21 02:57:26
nodes: [CLIPLoader, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VAELoader, CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, TextEncodeQwenImage21, LoadImage, PrimitiveStringMultiline, ResolutionSelector, EmptyLatentImage, BatchImagesNode, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, TextGenerateLTX2Prompt, SamplerCustom, VAEDecode, SaveImage, KSamplerSelect, ManualSigmas, ComfySwitchNode, UNETLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/文生图/qen image 2.1turbo 图片编辑_2062017330061860865.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qen image 2.1turbo 图片编辑_2062017330061860865.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VAELoader`
- `CLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextEncodeQwenImage21`
- `LoadImage`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `BatchImagesNode`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `TextGenerateLTX2Prompt`
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `ComfySwitchNode`
- `UNETLoader` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（32/36）

**有卡**：`CLIPLoader`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`TextEncodeQwenImage21`、`ResolutionSelector`、`EmptyLatentImage`、`BatchImagesNode`、`TextGenerateLTX2Prompt`、`SamplerCustom`、`VAEDecode`、`SaveImage`、`KSamplerSelect`、`ManualSigmas`、`UNETLoader`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage、UNETLoader
