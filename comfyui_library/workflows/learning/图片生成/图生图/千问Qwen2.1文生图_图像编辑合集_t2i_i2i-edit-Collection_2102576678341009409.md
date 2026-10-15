---
key: 图片生成/图生图/千问Qwen2.1文生图_图像编辑合集_t2i_i2i-edit-Collection_2102576678341009409.json
name: 千问Qwen2.1文生图_图像编辑合集_t2i_i2i-edit-Collection_2102576678341009409
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/千问Qwen2.1文生图_图像编辑合集_t2i_i2i-edit-Collection_2102576678341009409.json
hash: fbb06529e3c9fdd7
coverage: 0.705882
learned_at: 2026-10-15 22:25:47
nodes: [CLIPLoader, VAELoader, Note, QwenImage21Cache, EmptyLatentImage, MarkdownNote, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, easy imageSize, SeedVR2VideoUpscaler, ImageScaleBy, ImageResize+, ImageResize+, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SaveImage, easy imageSize, GetNode, Any Switch (rgthree), Image Comparer (rgthree), ComfySwitchNode, GetNode, ImageScaleBy, KSampler, UNETLoader, SetNode, ResolutionSelector, SetNode, VAEDecode, SaveImage, MarkdownNote, Image Comparer (rgthree), TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), VAELoader, TextEncodeQwenImage21, CLIPLoader, EmptyLatentImage, MarkdownNote, KSampler, SaveImage, VAEDecode, Int, UNETLoader, PrimitiveStringMultiline, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 381805575527499, "steps": 50, "width": 1024}
---

# 图片生成/图生图/千问Qwen2.1文生图_图像编辑合集_t2i_i2i-edit-Collection_2102576678341009409.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/千问Qwen2.1文生图_图像编辑合集_t2i_i2i-edit-Collection_2102576678341009409.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `CLIPLoader`
- `VAELoader`
- `Note`
- `QwenImage21Cache`
- `EmptyLatentImage` ★核心
- `MarkdownNote`
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
- `ComfySwitchNode`
- `GetNode`
- `ImageScaleBy`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `ResolutionSelector`
- `SetNode`
- `VAEDecode` ★核心
- `SaveImage`
- `MarkdownNote`
- `Image Comparer (rgthree)`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `Fast Groups Bypasser (rgthree)`
- `VAELoader`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `MarkdownNote`
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `Int`
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `ResolutionSelector`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `381805575527499`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **71%**（36/51）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`EmptyLatentImage`、`TTP_Image_Assy`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`easy imageSize`、`SeedVR2VideoUpscaler`、`ImageScaleBy`、`ImageResize+`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SaveImage`、`KSampler`、`UNETLoader`、`ResolutionSelector`、`VAEDecode`、`TextEncodeQwenImage21`、`LoadImage`、`Int`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
