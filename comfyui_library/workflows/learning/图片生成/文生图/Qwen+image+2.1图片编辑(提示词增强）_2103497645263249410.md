---
key: 图片生成/文生图/Qwen+image+2.1图片编辑(提示词增强）_2103497645263249410.json
name: Qwen+image+2.1图片编辑(提示词增强）_2103497645263249410
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen+image+2.1图片编辑(提示词增强）_2103497645263249410.json
hash: c631dbaf6d63c6ee
coverage: 0.677419
learned_at: 2026-10-06 21:49:54
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CLIPLoader, VAELoader, UNETLoader, QwenImage21Cache, LoadImage, BatchImagesNode, ComfySwitchNode, KSampler, ImageConcatMulti, ImageConcatMulti, SaveImageAdvanced, VAEDecode, SaveImage, ResolutionSelector, ImageResizeKJv2, LoadImage, LoadImage, CLIPLoader, EmptyLatentImage, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, TextEncodeQwenImage21, TextGenerateLTX2Prompt, easy showAnything]
patterns: []
missing: [BatchImagesNode, ImageConcatMulti, ImageConcatMulti, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, SaveImageAdvanced, TextGenerateLTX2Prompt]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 50, "width": 1024}
discoveries: [次要节点 `BatchImagesNode` 知识库中没有该节点类型的任何知识, 次要节点 `ImageConcatMulti` 知识库中没有该节点类型的任何知识, 次要节点 `ImageConcatMulti` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `TextGenerateLTX2Prompt` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Qwen+image+2.1图片编辑(提示词增强）_2103497645263249410.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen+image+2.1图片编辑(提示词增强）_2103497645263249410.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `LoadImage`
- `BatchImagesNode`
- `ComfySwitchNode`
- `KSampler` ★核心
- `ImageConcatMulti`
- `ImageConcatMulti`
- `SaveImageAdvanced`
- `VAEDecode` ★核心
- `SaveImage`
- `ResolutionSelector`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `easy showAnything`

## 关键参数

- `seed` = `999`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **68%**（21/31）

**有卡**：`LoadImage`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`SaveImage`、`ResolutionSelector`、`EmptyLatentImage`、`TextEncodeQwenImage21`

**缺卡**（7）：`BatchImagesNode`、`ImageConcatMulti`、`ImageConcatMulti`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`SaveImageAdvanced`、`TextGenerateLTX2Prompt`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `BatchImagesNode` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageConcatMulti` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageConcatMulti` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `TextGenerateLTX2Prompt` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
