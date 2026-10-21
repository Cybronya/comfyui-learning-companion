---
key: 图片生成/文生图/Qwen2.1文生图_图生视频高清工作流合集_2102020890262331394.json
name: Qwen2.1文生图_图生视频高清工作流合集_2102020890262331394
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图_图生视频高清工作流合集_2102020890262331394.json
hash: 59978e3b6bcde1cb
coverage: 0.811321
learned_at: 2026-10-20 01:51:23
nodes: [CLIPLoader, CLIPLoader, Label (rgthree), Label (rgthree), Label (rgthree), VAELoader, VAELoader, Note, QwenImage21Cache, EmptyLatentImage, UNETLoader, KSampler, SaveImage, SetNode, ResolutionSelector, EmptyLatentImage, SetNode, ImageConcatMulti, VAEDecode, TextEncodeQwenImage21, SaveImage, MarkdownNote, KSampler, VAEDecode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, easy imageSize, SeedVR2VideoUpscaler, ImageScaleBy, ImageResize+, ImageResize+, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SaveImage, easy imageSize, GetNode, Any Switch (rgthree), Image Comparer (rgthree), ResolutionSelector, TextEncodeQwenImage21, SaveImage, UNETLoader, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ComfySwitchNode, GetNode, ImageScaleBy, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 627507740345127, "steps": 50, "width": 1024}
---

# 图片生成/文生图/Qwen2.1文生图_图生视频高清工作流合集_2102020890262331394.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图_图生视频高清工作流合集_2102020890262331394.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `CLIPLoader`
- `CLIPLoader`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `VAELoader`
- `VAELoader`
- `Note`
- `QwenImage21Cache`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `SaveImage`
- `SetNode`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `SetNode`
- `ImageConcatMulti`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `SaveImage`
- `MarkdownNote`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `easy imageSize`
- `SeedVR2VideoUpscaler`
- `ImageScaleBy`
- `ImageResize+`
- `ImageResize+`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `SaveImage`
- `easy imageSize`
- `GetNode`
- `Any Switch (rgthree)`
- `Image Comparer (rgthree)`
- `ResolutionSelector`
- `TextEncodeQwenImage21`
- `SaveImage`
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ComfySwitchNode`
- `GetNode`
- `ImageScaleBy`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `627507740345127`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（43/53）

**有卡**：`CLIPLoader`、`Label (rgthree)`、`VAELoader`、`QwenImage21Cache`、`EmptyLatentImage`、`UNETLoader`、`KSampler`、`SaveImage`、`ResolutionSelector`、`ImageConcatMulti`、`VAEDecode`、`TextEncodeQwenImage21`、`TTP_Image_Assy`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`easy imageSize`、`SeedVR2VideoUpscaler`、`ImageScaleBy`、`ImageResize+`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
