---
key: 图片生成/文生图/Z-image turbo文生图+高清放大(FlashVSR+SeedVR2.5)_1999312098377203714.json
name: Z-image turbo文生图+高清放大(FlashVSR+SeedVR2.5)_1999312098377203714
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image turbo文生图+高清放大(FlashVSR+SeedVR2.5)_1999312098377203714.json
hash: c99f680e838aa478
coverage: 0.842105
learned_at: 2026-10-19 21:47:05
nodes: [TTP_Image_Tile_Batch, LayerUtility: PurgeVRAM, TTP_Image_Assy, ImageCASharpening+, ImageResize+, ImageCASharpening+, SeedVR2, Get Image Size, Image Comparer (rgthree), SaveImage, SaveImage, ImageResize+, GetImageRangeFromBatch, LayerUtility: PurgeVRAM, FlashVSR_SM_KSampler, FlashVSR_SM_Model, JWInteger, SaveImage, Image Comparer (rgthree), SaveImage, ImageConcanate, UNETLoader, VAELoader, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, VAEDecode, LayerUtility: PurgeVRAM, ImpactMinMax, PreviewImage, PreviewImage, easy showAnything, CLIPLoader, CLIPTextEncode, KSampler, LoraLoaderModelOnly, EmptyLatentImage, CLIPTextEncode]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1464, "sampler_name": "euler", "scheduler": "simple", "seed": 966740776245231, "steps": 8, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-image turbo文生图+高清放大(FlashVSR+SeedVR2.5)_1999312098377203714.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image turbo文生图+高清放大(FlashVSR+SeedVR2.5)_1999312098377203714.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
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
- `VAELoader`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `ImpactMinMax`
- `PreviewImage`
- `PreviewImage`
- `easy showAnything`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `966740776245231`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1464`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（32/38）

**有卡**：`TTP_Image_Tile_Batch`、`LayerUtility: PurgeVRAM`、`TTP_Image_Assy`、`ImageCASharpening+`、`ImageResize+`、`SeedVR2`、`Get Image Size`、`SaveImage`、`GetImageRangeFromBatch`、`FlashVSR_SM_KSampler`、`FlashVSR_SM_Model`、`JWInteger`、`ImageConcanate`、`UNETLoader`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`ImpactMinMax`、`CLIPLoader`、`CLIPTextEncode`、`KSampler`、`LoraLoaderModelOnly`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
