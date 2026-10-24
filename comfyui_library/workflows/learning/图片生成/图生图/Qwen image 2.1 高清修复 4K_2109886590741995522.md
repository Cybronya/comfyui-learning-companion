---
key: 图片生成/图生图/Qwen image 2.1 高清修复 4K_2109886590741995522.json
name: Qwen image 2.1 高清修复 4K_2109886590741995522
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 高清修复 4K_2109886590741995522.json
hash: 7b9591fec02eb0eb
coverage: 0.780488
learned_at: 2026-10-23 11:13:59
nodes: [CLIPLoader, VAELoader, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, QwenImage21Cache, Latent Switch (JPS), UNETLoader, TextEncodeQwenImage21, EmptyLatentImage, SaveImage, KSampler, LoraLoaderModelOnly, Image Comparer (rgthree), CR Text, Fast Groups Bypasser (rgthree), easy imageSize, TTP_Image_Tile_Batch, SeedVR2LoadVAEModel, LayerUtility: PurgeVRAM, SeedVR2VideoUpscaler, PreviewImage, ImageResize+, ImageScaleBy, SeedVR2LoadDiTModel, ImageResize+, PreviewImage, easy imageSize, easy imageSize, ImageScaleBy, MarkdownNote, TTP_Image_Assy, GetNode, TTP_Tile_image_size, VAEDecode, SetNode, LoraLoaderModelOnly, ImageResizeKJv2, LoadImage, Image Comparer (rgthree), SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 10, "width": 1024}
---

# 图片生成/图生图/Qwen image 2.1 高清修复 4K_2109886590741995522.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 高清修复 4K_2109886590741995522.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `CLIPLoader`
- `VAELoader`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `Latent Switch (JPS)`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `easy imageSize`
- `TTP_Image_Tile_Batch`
- `SeedVR2LoadVAEModel`
- `LayerUtility: PurgeVRAM`
- `SeedVR2VideoUpscaler`
- `PreviewImage`
- `ImageResize+`
- `ImageScaleBy`
- `SeedVR2LoadDiTModel`
- `ImageResize+`
- `PreviewImage`
- `easy imageSize`
- `easy imageSize`
- `ImageScaleBy`
- `MarkdownNote`
- `TTP_Image_Assy`
- `GetNode`
- `TTP_Tile_image_size`
- `VAEDecode` ★核心
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `LoadImage`
- `Image Comparer (rgthree)`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `999`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（32/41）

**有卡**：`CLIPLoader`、`VAELoader`、`ResolutionSelector`、`EmptyLatentImage`、`QwenImage21Cache`、`Latent Switch (JPS)`、`UNETLoader`、`TextEncodeQwenImage21`、`SaveImage`、`KSampler`、`LoraLoaderModelOnly`、`CR Text`、`easy imageSize`、`TTP_Image_Tile_Batch`、`SeedVR2LoadVAEModel`、`LayerUtility: PurgeVRAM`、`SeedVR2VideoUpscaler`、`ImageResize+`、`ImageScaleBy`、`SeedVR2LoadDiTModel`、`TTP_Image_Assy`、`TTP_Tile_image_size`、`VAEDecode`、`ImageResizeKJv2`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
