---
key: 图片生成/文生图/Z-image文生图+高清放大修复FlashVSR+SeedVR2.5_1996233743738224641.json
name: Z-image文生图+高清放大修复FlashVSR+SeedVR2.5_1996233743738224641
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image文生图+高清放大修复FlashVSR+SeedVR2.5_1996233743738224641.json
hash: eae4fa3d8f645930
coverage: 0.825
learned_at: 2026-10-19 21:33:02
nodes: [TTP_Image_Tile_Batch, LayerUtility: PurgeVRAM, TTP_Image_Assy, ImageCASharpening+, ImageResize+, ImageCASharpening+, SeedVR2, Get Image Size, Image Comparer (rgthree), SaveImage, SaveImage, ImageResize+, LoadImage, GetImageRangeFromBatch, LayerUtility: PurgeVRAM, FlashVSR_SM_KSampler, FlashVSR_SM_Model, JWInteger, SaveImage, Image Comparer (rgthree), SaveImage, ImageConcanate, UNETLoader, LoraLoaderModelOnly, VAELoader, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, CLIPTextEncode, VAEDecode, LayerUtility: PurgeVRAM, MarkdownNote, ImpactMinMax, PreviewImage, PreviewImage, easy showAnything, CLIPLoader, EmptyLatentImage, CLIPTextEncode, KSampler]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 47384877881186, "steps": 8, "width": 1920}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-image文生图+高清放大修复FlashVSR+SeedVR2.5_1996233743738224641.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image文生图+高清放大修复FlashVSR+SeedVR2.5_1996233743738224641.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `TTP_Image_Tile_Batch`
- `LayerUtility: PurgeVRAM`
- `TTP_Image_Assy`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageCASharpening+`
- `SeedVR2`
- `Get Image Size`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SaveImage`
- `ImageResize+`
- `LoadImage`
- `GetImageRangeFromBatch`
- `LayerUtility: PurgeVRAM`
- `FlashVSR_SM_KSampler` ★核心
- `FlashVSR_SM_Model`
- `JWInteger`
- `SaveImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `ImageConcanate`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `MarkdownNote`
- `ImpactMinMax`
- `PreviewImage`
- `PreviewImage`
- `easy showAnything`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `47384877881186`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（33/40）

**有卡**：`TTP_Image_Tile_Batch`、`LayerUtility: PurgeVRAM`、`TTP_Image_Assy`、`ImageCASharpening+`、`ImageResize+`、`SeedVR2`、`Get Image Size`、`SaveImage`、`LoadImage`、`GetImageRangeFromBatch`、`FlashVSR_SM_KSampler`、`FlashVSR_SM_Model`、`JWInteger`、`ImageConcanate`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`VAEDecode`、`ImpactMinMax`、`CLIPLoader`、`EmptyLatentImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
