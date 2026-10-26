---
key: 图片生成/图生图/qwen_image2.1AI短剧真人写实类角色卡生成器_2113887691749285890.json
name: qwen_image2.1AI短剧真人写实类角色卡生成器_2113887691749285890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen_image2.1AI短剧真人写实类角色卡生成器_2113887691749285890.json
hash: dc5359bf799f1128
coverage: 0.738095
learned_at: 2026-10-26 22:04:20
nodes: [MarkdownNote, MarkdownNote, GetNode, VAEDecode, CenterCropImages, GetNode, Note, ImageFromBatch, VAEDecode, GetNode, easy forLoopStart, ImageFromBatch, EmptyImage, ImageScaleBy, GetImageSize, BatchImagesNode, SaveImage, ResolutionSelector, TextEncodeQwenImage21, TextEncodeQwenImage21, easy forLoopEnd, EmptyLatentImage, VAELoader, CLIPLoader, VAEDecode, easy imageSplitGrid, easy imageSplitGrid, GetImageSize, SetNode, SetNode, TextEncodeQwenImage21, PreviewImage, BatchImagesNode, PreviewImage, SaveImage, PreviewImage, SaveImage, UNETLoader, KSampler, KSampler, KSampler, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 379815079493169, "steps": 25, "width": 1024}
---

# 图片生成/图生图/qwen_image2.1AI短剧真人写实类角色卡生成器_2113887691749285890.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen_image2.1AI短剧真人写实类角色卡生成器_2113887691749285890.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `MarkdownNote`
- `MarkdownNote`
- `GetNode`
- `VAEDecode` ★核心
- `CenterCropImages`
- `GetNode`
- `Note`
- `ImageFromBatch`
- `VAEDecode` ★核心
- `GetNode`
- `easy forLoopStart`
- `ImageFromBatch`
- `EmptyImage`
- `ImageScaleBy`
- `GetImageSize`
- `BatchImagesNode`
- `SaveImage`
- `ResolutionSelector`
- `TextEncodeQwenImage21`
- `TextEncodeQwenImage21`
- `easy forLoopEnd`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `CLIPLoader`
- `VAEDecode` ★核心
- `easy imageSplitGrid`
- `easy imageSplitGrid`
- `GetImageSize`
- `SetNode`
- `SetNode`
- `TextEncodeQwenImage21`
- `PreviewImage`
- `BatchImagesNode`
- `PreviewImage`
- `SaveImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `LoadImage`

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

覆盖率 **74%**（31/42）

**有卡**：`VAEDecode`、`CenterCropImages`、`ImageFromBatch`、`easy forLoopStart`、`EmptyImage`、`ImageScaleBy`、`GetImageSize`、`BatchImagesNode`、`SaveImage`、`ResolutionSelector`、`TextEncodeQwenImage21`、`easy forLoopEnd`、`EmptyLatentImage`、`VAELoader`、`CLIPLoader`、`easy imageSplitGrid`、`UNETLoader`、`KSampler`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
