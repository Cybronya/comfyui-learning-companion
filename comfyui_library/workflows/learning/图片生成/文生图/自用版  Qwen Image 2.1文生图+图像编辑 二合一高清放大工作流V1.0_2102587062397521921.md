---
key: 自用版  Qwen Image 2.1文生图+图像编辑 二合一高清放大工作流V1.0_2102587062397521921.json
name: 自用版  Qwen Image 2.1文生图+图像编辑 二合一高清放大工作流V1.0_2102587062397521921
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/自用版  Qwen Image 2.1文生图+图像编辑 二合一高清放大工作流V1.0_2102587062397521921.json
hash: 42bf3ebbc3070bec
coverage: 0.490196
learned_at: 2026-10-10 20:59:56
nodes: [TextGenerateLTX2Prompt, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, LoadImage, LoadImage, 忽略多组孤海, ResolutionSelector, EmptyLatentImage, KSampler, VAEDecode, TTP_Tile_image_size, TTP_Image_Tile_Batch, ImageScaleBy, GetImageSize+, ImageResize+, TTP_Image_Assy, TextEncodeQwenImage21, 孤海注释, 孤海注释, 孤海注释, 孤海注释, SeedVR2VideoUpscaler, PreviewImage, Image Comparer (rgthree), ImageScaleBy, UNETLoader, CLIPLoader, VAELoader, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, 忽略多组孤海, CLIPLoader, LoadImage, SaveImageAdvanced, PrimitiveStringMultiline, VRAM_Debug, ImageCASharpening+, SaveImage, LoadImage]
patterns: []
missing: [ImageCASharpening+, 忽略多组孤海, 忽略多组孤海, GetImageSize+, ImageResize+]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1019724879078939, "steps": 40, "width": 1024}
discoveries: [次要节点 `ImageCASharpening+` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 自用版  Qwen Image 2.1文生图+图像编辑 二合一高清放大工作流V1.0_2102587062397521921.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/自用版  Qwen Image 2.1文生图+图像编辑 二合一高清放大工作流V1.0_2102587062397521921.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `TextGenerateLTX2Prompt`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `忽略多组孤海`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `ImageScaleBy`
- `GetImageSize+`
- `ImageResize+`
- `TTP_Image_Assy`
- `TextEncodeQwenImage21`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `SeedVR2VideoUpscaler`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `忽略多组孤海`
- `CLIPLoader`
- `LoadImage`
- `SaveImageAdvanced`
- `PrimitiveStringMultiline`
- `VRAM_Debug`
- `ImageCASharpening+`
- `SaveImage`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1019724879078939`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **49%**（25/51）

**有卡**：`TextGenerateLTX2Prompt`、`LoadImage`、`ResolutionSelector`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`ImageScaleBy`、`TTP_Image_Assy`、`TextEncodeQwenImage21`、`SeedVR2VideoUpscaler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SaveImageAdvanced`、`VRAM_Debug`、`SaveImage`

**缺卡**（5）：`ImageCASharpening+`、`忽略多组孤海`、`忽略多组孤海`、`GetImageSize+`、`ImageResize+`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `ImageCASharpening+` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
