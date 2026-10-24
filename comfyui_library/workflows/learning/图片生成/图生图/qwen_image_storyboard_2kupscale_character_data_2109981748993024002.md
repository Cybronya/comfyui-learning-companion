---
key: 图片生成/图生图/qwen_image_storyboard_2kupscale_character_data_2109981748993024002.json
name: qwen_image_storyboard_2kupscale_character_data_2109981748993024002
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen_image_storyboard_2kupscale_character_data_2109981748993024002.json
hash: a70f19b0b7aed7e9
coverage: 0.738095
learned_at: 2026-10-23 11:44:13
nodes: [MarkdownNote, MarkdownNote, KSampler, GetNode, VAEDecode, CenterCropImages, GetNode, Note, ImageFromBatch, KSampler, VAEDecode, GetNode, easy forLoopStart, ImageScaleBy, GetImageSize, BatchImagesNode, SaveImage, ResolutionSelector, easy forLoopEnd, EmptyLatentImage, CLIPLoader, UNETLoader, KSampler, VAEDecode, PreviewImage, GetImageSize, SetNode, SetNode, PreviewImage, BatchImagesNode, VAELoader, TextEncodeQwenImage21, TextEncodeQwenImage21, SaveImage, easy imageSplitGrid, easy imageSplitGrid, PreviewImage, EmptyImage, ImageFromBatch, SaveImage, TextEncodeQwenImage21, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 379815079493169, "steps": 25, "width": 1024}
---

# 图片生成/图生图/qwen_image_storyboard_2kupscale_character_data_2109981748993024002.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen_image_storyboard_2kupscale_character_data_2109981748993024002.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `MarkdownNote`
- `MarkdownNote`
- `KSampler` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `CenterCropImages`
- `GetNode`
- `Note`
- `ImageFromBatch`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `easy forLoopStart`
- `ImageScaleBy`
- `GetImageSize`
- `BatchImagesNode`
- `SaveImage`
- `ResolutionSelector`
- `easy forLoopEnd`
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `GetImageSize`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `BatchImagesNode`
- `VAELoader`
- `TextEncodeQwenImage21`
- `TextEncodeQwenImage21`
- `SaveImage`
- `easy imageSplitGrid`
- `easy imageSplitGrid`
- `PreviewImage`
- `EmptyImage`
- `ImageFromBatch`
- `SaveImage`
- `TextEncodeQwenImage21`
- `LoadImage`

## 关键参数

- `seed` = `379815079493169`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **74%**（31/42）

**有卡**：`KSampler`、`VAEDecode`、`CenterCropImages`、`ImageFromBatch`、`easy forLoopStart`、`ImageScaleBy`、`GetImageSize`、`BatchImagesNode`、`SaveImage`、`ResolutionSelector`、`easy forLoopEnd`、`EmptyLatentImage`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`TextEncodeQwenImage21`、`easy imageSplitGrid`、`EmptyImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
