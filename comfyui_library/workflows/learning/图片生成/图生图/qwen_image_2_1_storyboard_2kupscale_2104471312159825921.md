---
key: 图片生成/图生图/qwen_image_2_1_storyboard_2kupscale_2104471312159825921.json
name: qwen_image_2_1_storyboard_2kupscale_2104471312159825921
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen_image_2_1_storyboard_2kupscale_2104471312159825921.json
hash: 5d840a7fb6e19b75
coverage: 0.735294
learned_at: 2026-10-21 00:46:22
nodes: [MarkdownNote, MarkdownNote, UNETLoader, CLIPLoader, VAELoader, LoadImage, VAEDecode, SaveImage, PreviewImage, easy imageSplitGrid, SetNode, GetImageSize, SetNode, EmptyLatentImage, TextEncodeQwenImage21, KSampler, ResolutionSelector, EmptyImage, easy forLoopStart, ImageFromBatch, GetNode, GetNode, VAEDecode, ImageScaleBy, GetImageSize, CenterCropImages, BatchImagesNode, easy forLoopEnd, GetNode, Note, ImageFromBatch, SaveImage, TextEncodeQwenImage21, KSampler]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 144777429357800, "steps": 25, "width": 1024}
---

# 图片生成/图生图/qwen_image_2_1_storyboard_2kupscale_2104471312159825921.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen_image_2_1_storyboard_2kupscale_2104471312159825921.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `easy imageSplitGrid`
- `SetNode`
- `GetImageSize`
- `SetNode`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `ResolutionSelector`
- `EmptyImage`
- `easy forLoopStart`
- `ImageFromBatch`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `ImageScaleBy`
- `GetImageSize`
- `CenterCropImages`
- `BatchImagesNode`
- `easy forLoopEnd`
- `GetNode`
- `Note`
- `ImageFromBatch`
- `SaveImage`
- `TextEncodeQwenImage21`
- `KSampler` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `144777429357800`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **74%**（25/34）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`VAEDecode`、`SaveImage`、`easy imageSplitGrid`、`GetImageSize`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`KSampler`、`ResolutionSelector`、`EmptyImage`、`easy forLoopStart`、`ImageFromBatch`、`ImageScaleBy`、`CenterCropImages`、`BatchImagesNode`、`easy forLoopEnd`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
