---
key: 图片生成/图生图/Z-Image ControlNet 2.1 2601 八步最新洗图_2015610869585027073.json
name: Z-Image ControlNet 2.1 2601 八步最新洗图_2015610869585027073
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-Image ControlNet 2.1 2601 八步最新洗图_2015610869585027073.json
hash: be87b84e0529f4d3
coverage: 0.772727
learned_at: 2026-10-23 11:29:18
nodes: [AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, PreviewImage, UNETLoader, Note, Get Image Size, ImageCASharpening+, SeedVR2, LayerUtility: PurgeVRAM, TTP_Image_Assy, ImageCASharpening+, LayerUtility: PurgeVRAM, QwenImageDiffsynthControlnet, VAELoader, ImageResize+, ImpactMinMax, TTP_Image_Tile_Batch, ImageResize+, KSampler, ModelPatchLoader, easy showAnything, ConditioningZeroOut, PreviewImage, easy cleanGpuUsed, CLIPLoader, easy ifElse, ImageScaleToTotalPixels, EmptyLatentImage, Note, VAEDecode, RH_Captioner, ImpactSwitch, GetImageSizeAndCount, LoraLoaderModelOnly, CLIPTextEncode, ttN concat, Note, MaraScottIsEmptyOrNone_v1, LoadImage, Text Multiline, Fast Groups Bypasser (rgthree), SaveImage, Image Comparer (rgthree)]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 2, "steps": 10, "width": 1024}
---

# 图片生成/图生图/Z-Image ControlNet 2.1 2601 八步最新洗图_2015610869585027073.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-Image ControlNet 2.1 2601 八步最新洗图_2015610869585027073.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `PreviewImage`
- `UNETLoader` ★核心
- `Note`
- `Get Image Size`
- `ImageCASharpening+`
- `SeedVR2`
- `LayerUtility: PurgeVRAM`
- `TTP_Image_Assy`
- `ImageCASharpening+`
- `LayerUtility: PurgeVRAM`
- `QwenImageDiffsynthControlnet`
- `VAELoader`
- `ImageResize+`
- `ImpactMinMax`
- `TTP_Image_Tile_Batch`
- `ImageResize+`
- `KSampler` ★核心
- `ModelPatchLoader`
- `easy showAnything`
- `ConditioningZeroOut`
- `PreviewImage`
- `easy cleanGpuUsed`
- `CLIPLoader`
- `easy ifElse`
- `ImageScaleToTotalPixels`
- `EmptyLatentImage` ★核心
- `Note`
- `VAEDecode` ★核心
- `RH_Captioner`
- `ImpactSwitch`
- `GetImageSizeAndCount`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ttN concat`
- `Note`
- `MaraScottIsEmptyOrNone_v1`
- `LoadImage`
- `Text Multiline`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `Image Comparer (rgthree)`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `2`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **77%**（34/44）

**有卡**：`AIO_Preprocessor`、`UNETLoader`、`Get Image Size`、`ImageCASharpening+`、`SeedVR2`、`LayerUtility: PurgeVRAM`、`TTP_Image_Assy`、`QwenImageDiffsynthControlnet`、`VAELoader`、`ImageResize+`、`ImpactMinMax`、`TTP_Image_Tile_Batch`、`KSampler`、`ModelPatchLoader`、`ConditioningZeroOut`、`easy cleanGpuUsed`、`CLIPLoader`、`ImageScaleToTotalPixels`、`EmptyLatentImage`、`VAEDecode`、`RH_Captioner`、`GetImageSizeAndCount`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`ttN concat`、`MaraScottIsEmptyOrNone_v1`、`LoadImage`、`Text Multiline`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
