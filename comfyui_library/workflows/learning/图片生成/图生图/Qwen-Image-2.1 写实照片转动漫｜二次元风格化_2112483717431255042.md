---
key: 图片生成/图生图/Qwen-Image-2.1 写实照片转动漫｜二次元风格化_2112483717431255042.json
name: Qwen-Image-2.1 写实照片转动漫｜二次元风格化_2112483717431255042
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 写实照片转动漫｜二次元风格化_2112483717431255042.json
hash: f6542dbe57e01459
coverage: 0.855422
learned_at: 2026-10-23 11:16:24
nodes: [CLIPLoader, VAELoader, EmptyLatentImage, GetImageSize, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, UNETLoader, ImageResizeKJv2, easy imageSize, TTP_Image_Tile_Batch, SeedVR2LoadVAEModel, LayerUtility: PurgeVRAM, SeedVR2VideoUpscaler, PreviewImage, ImageResize+, ImageScaleBy, SeedVR2LoadDiTModel, ImageResize+, PreviewImage, easy imageSize, easy imageSize, ImageScaleBy, GetNode, TTP_Tile_image_size, TTP_Image_Assy, SaveImage, Image Comparer (rgthree), SaveImage, Image Comparer (rgthree), ImageConcanate, Fast Groups Bypasser (rgthree), SetNode, LoraLoaderModelOnly, SaveImage, KSampler, VAEDecode, LoadImage, TextEncodeQwenImage21, LoraLoaderModelOnly, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Image-2.1 写实照片转动漫｜二次元风格化_2112483717431255042.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 写实照片转动漫｜二次元风格化_2112483717431255042.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（83 个）：
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `GetImageSize`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `ImageResizeKJv2`
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
- `GetNode`
- `TTP_Tile_image_size`
- `TTP_Image_Assy`
- `SaveImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `TextEncodeQwenImage21`
- `LoraLoaderModelOnly` ★核心
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **86%**（71/83）

**有卡**：`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`GetImageSize`、`ResolutionSelector`、`UNETLoader`、`ImageResizeKJv2`、`easy imageSize`、`TTP_Image_Tile_Batch`、`SeedVR2LoadVAEModel`、`LayerUtility: PurgeVRAM`、`SeedVR2VideoUpscaler`、`ImageResize+`、`ImageScaleBy`、`SeedVR2LoadDiTModel`、`TTP_Tile_image_size`、`TTP_Image_Assy`、`SaveImage`、`ImageConcanate`、`LoraLoaderModelOnly`、`KSampler`、`VAEDecode`、`LoadImage`、`TextEncodeQwenImage21`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
