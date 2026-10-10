---
key: 图片生成/文生图/自用版  Qwen Image 2.1文生图+图像编辑 二合一高清放大工作流V2.0_2105125909257871362.json
name: 自用版  Qwen Image 2.1文生图+图像编辑 二合一高清放大工作流V2.0_2105125909257871362
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/自用版  Qwen Image 2.1文生图+图像编辑 二合一高清放大工作流V2.0_2105125909257871362.json
hash: 8be7dc5326901061
coverage: 0.410714
learned_at: 2026-10-10 23:17:03
nodes: [GetNode, SetNode, GetNode, KSampler, VAEDecode, GetNode, GetNode, GetNode, TextEncodeQwenImage21, GetNode, LoadImage, LoadImage, SetNode, SetNode, SetNode, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海, TTP_Image_Tile_Batch, ImageScaleBy, ImageScaleBy, SeedVR2VideoUpscaler, TTP_Image_Assy, GetImageSize+, ImageCASharpening+, ImageResize+, SeedVR2LoadVAEModel, LoadImage, SetNode, 孤海注释, 孤海注释, 孤海注释, EmptyLatentImage, easy ifElse, SetNode, ResolutionSelector, SetNode, TTP_Tile_image_size, SetNode, SetNode, SetNode, easy promptLine, TextToListNode, 忽略多组孤海, 孤海注释, UNETLoader, CLIPLoader, VAELoader, SeedVR2LoadDiTModel, Image Comparer (rgthree), LoraLoaderModelOnly, PreviewImage, SaveImage, PrimitiveStringMultiline, LoadImage]
patterns: []
missing: [ImageCASharpening+, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海, GetImageSize+, ImageResize+, easy promptLine]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 496066043992409, "steps": 40, "width": 1024}
discoveries: [次要节点 `ImageCASharpening+` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/自用版  Qwen Image 2.1文生图+图像编辑 二合一高清放大工作流V2.0_2105125909257871362.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/自用版  Qwen Image 2.1文生图+图像编辑 二合一高清放大工作流V2.0_2105125909257871362.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `GetNode`
- `SetNode`
- `GetNode`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `TextEncodeQwenImage21`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `忽略多组孤海`
- `忽略多组孤海`
- `忽略多组孤海`
- `忽略多组孤海`
- `TTP_Image_Tile_Batch`
- `ImageScaleBy`
- `ImageScaleBy`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `GetImageSize+`
- `ImageCASharpening+`
- `ImageResize+`
- `SeedVR2LoadVAEModel`
- `LoadImage`
- `SetNode`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `EmptyLatentImage` ★核心
- `easy ifElse`
- `SetNode`
- `ResolutionSelector`
- `SetNode`
- `TTP_Tile_image_size`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy promptLine`
- `TextToListNode`
- `忽略多组孤海`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `SeedVR2LoadDiTModel`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `SaveImage`
- `PrimitiveStringMultiline`
- `LoadImage`

## 关键参数

- `seed` = `496066043992409`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **41%**（23/56）

**有卡**：`KSampler`、`VAEDecode`、`TextEncodeQwenImage21`、`LoadImage`、`TTP_Image_Tile_Batch`、`ImageScaleBy`、`SeedVR2VideoUpscaler`、`TTP_Image_Assy`、`SeedVR2LoadVAEModel`、`EmptyLatentImage`、`ResolutionSelector`、`TTP_Tile_image_size`、`TextToListNode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SeedVR2LoadDiTModel`、`LoraLoaderModelOnly`、`SaveImage`

**缺卡**（9）：`ImageCASharpening+`、`忽略多组孤海`、`忽略多组孤海`、`忽略多组孤海`、`忽略多组孤海`、`忽略多组孤海`、`GetImageSize+`、`ImageResize+`、`easy promptLine`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 学习发现

- 次要节点 `ImageCASharpening+` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
