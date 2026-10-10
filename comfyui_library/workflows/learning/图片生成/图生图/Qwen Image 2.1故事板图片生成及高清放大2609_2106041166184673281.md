---
key: 图片生成/图生图/Qwen Image 2.1故事板图片生成及高清放大2609_2106041166184673281.json
name: Qwen Image 2.1故事板图片生成及高清放大2609_2106041166184673281
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1故事板图片生成及高清放大2609_2106041166184673281.json
hash: 614e6023fef7cc8f
coverage: 0.647059
learned_at: 2026-10-10 20:48:07
nodes: [MarkdownNote, MarkdownNote, UNETLoader, CLIPLoader, VAELoader, VAEDecode, easy imageSplitGrid, GetImageSize, EmptyLatentImage, ResolutionSelector, EmptyImage, easy forLoopStart, ImageFromBatch, GetNode, GetNode, Note, KSampler, KSampler, VAEDecode, ImageScaleBy, GetImageSize, CenterCropImages, BatchImagesNode, easy forLoopEnd, GetNode, ImageFromBatch, LoadImage, SaveImage, TextEncodeQwenImage21, TextEncodeQwenImage21, SaveImage, SetNode, SetNode, PreviewImage]
patterns: []
missing: [easy forLoopEnd, easy forLoopStart, easy imageSplitGrid]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 379815079493169, "steps": 25, "width": 1024}
discoveries: [次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageSplitGrid` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/Qwen Image 2.1故事板图片生成及高清放大2609_2106041166184673281.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1故事板图片生成及高清放大2609_2106041166184673281.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `easy imageSplitGrid`
- `GetImageSize`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `EmptyImage`
- `easy forLoopStart`
- `ImageFromBatch`
- `GetNode`
- `GetNode`
- `Note`
- `KSampler` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImageScaleBy`
- `GetImageSize`
- `CenterCropImages`
- `BatchImagesNode`
- `easy forLoopEnd`
- `GetNode`
- `ImageFromBatch`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextEncodeQwenImage21`
- `SaveImage`
- `SetNode`
- `SetNode`
- `PreviewImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `379815079493169`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **65%**（22/34）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`GetImageSize`、`EmptyLatentImage`、`ResolutionSelector`、`EmptyImage`、`ImageFromBatch`、`KSampler`、`ImageScaleBy`、`CenterCropImages`、`BatchImagesNode`、`LoadImage`、`SaveImage`、`TextEncodeQwenImage21`

**缺卡**（3）：`easy forLoopEnd`、`easy forLoopStart`、`easy imageSplitGrid`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageSplitGrid` 知识库中没有该节点类型的任何知识
