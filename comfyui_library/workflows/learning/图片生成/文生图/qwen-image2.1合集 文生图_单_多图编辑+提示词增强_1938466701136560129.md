---
key: 图片生成/文生图/qwen-image2.1合集 文生图_单_多图编辑+提示词增强_1938466701136560129.json
name: qwen-image2.1合集 文生图_单_多图编辑+提示词增强_1938466701136560129
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-image2.1合集 文生图_单_多图编辑+提示词增强_1938466701136560129.json
hash: 1c90cc442de85b72
coverage: 0.320755
learned_at: 2026-10-07 03:05:14
nodes: [SetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, LoadImage, LoadImage, SetNode, LoadImage, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, VAELoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetNode, BatchImagesNode, GetNode, LoadImage, GetNode, EmptyLatentImage, PreviewAny, ComfySwitchNode, QwenImage21Cache, PrimitiveInt, UNETLoader, TextEncodeQwenImage21, ResolutionSelector, SetNode, easy seed, GetNode, LoadImage, LoadImage, PrimitiveBoolean, VAEDecode, SetNode, GetNode, SetNode, CLIPLoader, GetNode, GetNode, TextGenerateLTX2Prompt, KSampler, SaveImageAdvanced, SetNode, SetNode, CLIPLoader, CLIPLoader, JjkText, SetNode, SetNode, SetNode, SetNode, ResolutionSelector, PrimitiveBoolean, GetNode, GetNode, EmptyLatentImage, SetNode, easy seed, JjkText, GetNode, GetNode, GetNode, easy showAnything, TextGenerateLTX2Prompt, GetNode, TextEncodeQwenImage21, GetNode, VAEDecode, KSampler, SetNode, SaveImage, MarkdownNote, LoadImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), SaveImage]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, easy seed, easy seed]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 401379519546083, "steps": 25, "width": 1024}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/qwen-image2.1合集 文生图_单_多图编辑+提示词增强_1938466701136560129.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen-image2.1合集 文生图_单_多图编辑+提示词增强_1938466701136560129.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（106 个）：
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VAELoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LoadImage`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `GetNode`
- `BatchImagesNode`
- `GetNode`
- `LoadImage`
- `GetNode`
- `EmptyLatentImage` ★核心
- `PreviewAny`
- `ComfySwitchNode`
- `QwenImage21Cache`
- `PrimitiveInt`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `SetNode`
- `easy seed`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `PrimitiveBoolean`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `CLIPLoader`
- `GetNode`
- `GetNode`
- `TextGenerateLTX2Prompt`
- `KSampler` ★核心
- `SaveImageAdvanced`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `CLIPLoader`
- `JjkText`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ResolutionSelector`
- `PrimitiveBoolean`
- `GetNode`
- `GetNode`
- `EmptyLatentImage` ★核心
- `SetNode`
- `easy seed`
- `JjkText`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `TextGenerateLTX2Prompt`
- `GetNode`
- `TextEncodeQwenImage21`
- `GetNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SetNode`
- `SaveImage`
- `MarkdownNote`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `401379519546083`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **32%**（34/106）

**有卡**：`LoadImage`、`VAELoader`、`BatchImagesNode`、`EmptyLatentImage`、`QwenImage21Cache`、`UNETLoader`、`TextEncodeQwenImage21`、`ResolutionSelector`、`PrimitiveBoolean`、`VAEDecode`、`CLIPLoader`、`TextGenerateLTX2Prompt`、`KSampler`、`SaveImageAdvanced`、`SaveImage`

**缺卡**（11）：`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy seed`、`easy seed`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
