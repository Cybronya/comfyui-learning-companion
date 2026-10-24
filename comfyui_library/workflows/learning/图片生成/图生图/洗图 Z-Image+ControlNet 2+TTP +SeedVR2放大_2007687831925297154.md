---
key: 图片生成/图生图/洗图 Z-Image+ControlNet 2+TTP +SeedVR2放大_2007687831925297154.json
name: 洗图 Z-Image+ControlNet 2+TTP +SeedVR2放大_2007687831925297154
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/洗图 Z-Image+ControlNet 2+TTP +SeedVR2放大_2007687831925297154.json
hash: 281adccdb73156cc
coverage: 0.788462
learned_at: 2026-10-23 13:11:31
nodes: [AIO_Preprocessor, AIO_Preprocessor, ImageScaleToTotalPixels, AIO_Preprocessor, CLIPLoader, easy ifElse, easy showAnything, ttN concat, PreviewImage, UNETLoader, Note, ConditioningZeroOut, QwenImageDiffsynthControlnet, ModelPatchLoader, EmptyLatentImage, GetImageSizeAndCount, ImageResize+, TTP_Image_Tile_Batch, Get Image Size, ImpactMinMax, ImageResize+, ImageCASharpening+, SeedVR2, LayerUtility: PurgeVRAM, TTP_Image_Assy, LayerUtility: PurgeVRAM, SaveImage, Note, RH_Captioner, LoraLoaderModelOnly, QwenImageDiffsynthControlnet, VAELoader, KSampler, ModelPatchLoader, KSampler, CLIPTextEncode, easy showAnything, SaveImage, SaveImage, Image Comparer (rgthree), MaraScottIsEmptyOrNone_v1, ImpactSwitch, VAEDecode, VAEDecode, PreviewImage, LayerUtility: ImageReelComposit, LayerUtility: ImageReel, ImageCASharpening+, Note, Fast Groups Bypasser (rgthree), Text Multiline, LoadImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 2, "steps": 10, "width": 1024}
---

# 图片生成/图生图/洗图 Z-Image+ControlNet 2+TTP +SeedVR2放大_2007687831925297154.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/洗图 Z-Image+ControlNet 2+TTP +SeedVR2放大_2007687831925297154.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `ImageScaleToTotalPixels`
- `AIO_Preprocessor`
- `CLIPLoader`
- `easy ifElse`
- `easy showAnything`
- `ttN concat`
- `PreviewImage`
- `UNETLoader` ★核心
- `Note`
- `ConditioningZeroOut`
- `QwenImageDiffsynthControlnet`
- `ModelPatchLoader`
- `EmptyLatentImage` ★核心
- `GetImageSizeAndCount`
- `ImageResize+`
- `TTP_Image_Tile_Batch`
- `Get Image Size`
- `ImpactMinMax`
- `ImageResize+`
- `ImageCASharpening+`
- `SeedVR2`
- `LayerUtility: PurgeVRAM`
- `TTP_Image_Assy`
- `LayerUtility: PurgeVRAM`
- `SaveImage`
- `Note`
- `RH_Captioner`
- `LoraLoaderModelOnly` ★核心
- `QwenImageDiffsynthControlnet`
- `VAELoader`
- `KSampler` ★核心
- `ModelPatchLoader`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `SaveImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `MaraScottIsEmptyOrNone_v1`
- `ImpactSwitch`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageReel`
- `ImageCASharpening+`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `Text Multiline`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `2`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（41/52）

**有卡**：`AIO_Preprocessor`、`ImageScaleToTotalPixels`、`CLIPLoader`、`ttN concat`、`UNETLoader`、`ConditioningZeroOut`、`QwenImageDiffsynthControlnet`、`ModelPatchLoader`、`EmptyLatentImage`、`GetImageSizeAndCount`、`ImageResize+`、`TTP_Image_Tile_Batch`、`Get Image Size`、`ImpactMinMax`、`ImageCASharpening+`、`SeedVR2`、`LayerUtility: PurgeVRAM`、`TTP_Image_Assy`、`SaveImage`、`RH_Captioner`、`LoraLoaderModelOnly`、`VAELoader`、`KSampler`、`CLIPTextEncode`、`MaraScottIsEmptyOrNone_v1`、`VAEDecode`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`Text Multiline`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
