---
key: 图片生成/文生图/万亿级像素文生图 - 文生图Z-image+SeedVR2.5.1 定义超高清影像新标准高_2034249664538611713.json
name: 万亿级像素文生图 - 文生图Z-image+SeedVR2.5.1 定义超高清影像新标准高_2034249664538611713
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/万亿级像素文生图 - 文生图Z-image+SeedVR2.5.1 定义超高清影像新标准高_2034249664538611713.json
hash: d94c8151f331c07c
coverage: 0.789474
learned_at: 2026-10-21 02:58:17
nodes: [ConditioningZeroOut, LatentPixelScale, KSampler, UpscaleModelLoader, GetImageSize+, ImageResize+, ImageScaleBy, GetImageSize+, ImageScaleBy, TTP_Image_Tile_Batch, easy cleanGpuUsed, ImageResize+, SeedVR2LoadVAEModel, VAEDecodeTiled, KSampler, CLIPLoader, VAELoader, VAEDecode, CLIPTextEncode, UNETLoader, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, LoraLoaderModelOnly, TTP_Tile_image_size, EmptySD3LatentImage, PreviewImage, TTP_Image_Assy, PreviewImage, Image Comparer (rgthree), SaveImage, RH_LLMAPI_NODE, PreviewAny, PreviewImage, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, Image Comparer (rgthree), PreviewImage, JjkText]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "gradient_estimation", "scheduler": "sgm_uniform", "seed": 123456789, "steps": 10}
---

# 图片生成/文生图/万亿级像素文生图 - 文生图Z-image+SeedVR2.5.1 定义超高清影像新标准高_2034249664538611713.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/万亿级像素文生图 - 文生图Z-image+SeedVR2.5.1 定义超高清影像新标准高_2034249664538611713.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `ConditioningZeroOut`
- `LatentPixelScale`
- `KSampler` ★核心
- `UpscaleModelLoader`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `GetImageSize+`
- `ImageScaleBy`
- `TTP_Image_Tile_Batch`
- `easy cleanGpuUsed`
- `ImageResize+`
- `SeedVR2LoadVAEModel`
- `VAEDecodeTiled` ★核心
- `KSampler` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `LoraLoaderModelOnly` ★核心
- `TTP_Tile_image_size`
- `EmptySD3LatentImage`
- `PreviewImage`
- `TTP_Image_Assy`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `RH_LLMAPI_NODE`
- `PreviewAny`
- `PreviewImage`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `JjkText`

## 关键参数

- `seed` = `123456789`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `gradient_estimation`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **79%**（30/38）

**有卡**：`ConditioningZeroOut`、`LatentPixelScale`、`KSampler`、`UpscaleModelLoader`、`GetImageSize+`、`ImageResize+`、`ImageScaleBy`、`TTP_Image_Tile_Batch`、`easy cleanGpuUsed`、`SeedVR2LoadVAEModel`、`VAEDecodeTiled`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`CLIPTextEncode`、`UNETLoader`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`LoraLoaderModelOnly`、`TTP_Tile_image_size`、`EmptySD3LatentImage`、`TTP_Image_Assy`、`SaveImage`、`RH_LLMAPI_NODE`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、UNETLoader
