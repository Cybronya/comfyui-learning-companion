---
key: 图片生成/图生图/Qwen-Image-2.1 任意风格转写实_2110205939604344834.json
name: Qwen-Image-2.1 任意风格转写实_2110205939604344834
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 任意风格转写实_2110205939604344834.json
hash: 9eb790192a788ad5
coverage: 0.785714
learned_at: 2026-10-23 11:16:24
nodes: [CLIPLoader, VAELoader, EmptyLatentImage, GetImageSize, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, UNETLoader, KSampler, LoraLoaderModelOnly, LoraLoaderModelOnly, QwenImage21Cache, LoadImage, TextEncodeQwenImage21, ImageResizeKJv2, Fast Groups Bypasser (rgthree), easy imageSize, TTP_Image_Tile_Batch, SeedVR2LoadVAEModel, LayerUtility: PurgeVRAM, SeedVR2VideoUpscaler, PreviewImage, ImageResize+, ImageScaleBy, SeedVR2LoadDiTModel, ImageResize+, PreviewImage, easy imageSize, easy imageSize, ImageScaleBy, MarkdownNote, GetNode, TTP_Tile_image_size, VAEDecode, SetNode, SaveImage, TTP_Image_Assy, SaveImage, Image Comparer (rgthree), ImageConcanate, SaveImage, Image Comparer (rgthree)]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 926576823871430, "steps": 7, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Image-2.1 任意风格转写实_2110205939604344834.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 任意风格转写实_2110205939604344834.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `GetImageSize`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `QwenImage21Cache`
- `LoadImage`
- `TextEncodeQwenImage21`
- `ImageResizeKJv2`
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
- `GetNode`
- `TTP_Tile_image_size`
- `VAEDecode` ★核心
- `SetNode`
- `SaveImage`
- `TTP_Image_Assy`
- `SaveImage`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `SaveImage`
- `Image Comparer (rgthree)`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `926576823871430`
- `steps` = `7`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（33/42）

**有卡**：`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`GetImageSize`、`ResolutionSelector`、`UNETLoader`、`KSampler`、`LoraLoaderModelOnly`、`QwenImage21Cache`、`LoadImage`、`TextEncodeQwenImage21`、`ImageResizeKJv2`、`easy imageSize`、`TTP_Image_Tile_Batch`、`SeedVR2LoadVAEModel`、`LayerUtility: PurgeVRAM`、`SeedVR2VideoUpscaler`、`ImageResize+`、`ImageScaleBy`、`SeedVR2LoadDiTModel`、`TTP_Tile_image_size`、`VAEDecode`、`SaveImage`、`TTP_Image_Assy`、`ImageConcanate`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
