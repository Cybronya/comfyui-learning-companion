---
key: 图片生成/文生图/文生图Z-image+SeedVR2.5.1 万亿级像素文生图，细节纤毫毕现，定义超高清影像新标准高_2033734929732870146.json
name: 文生图Z-image+SeedVR2.5.1 万亿级像素文生图，细节纤毫毕现，定义超高清影像新标准高_2033734929732870146
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图Z-image+SeedVR2.5.1 万亿级像素文生图，细节纤毫毕现，定义超高清影像新标准高_2033734929732870146.json
hash: b6f572aac387326e
coverage: 0.789474
learned_at: 2026-10-21 03:00:45
nodes: [ConditioningZeroOut, LatentPixelScale, KSampler, UpscaleModelLoader, GetImageSize+, ImageResize+, ImageScaleBy, GetImageSize+, ImageScaleBy, TTP_Image_Tile_Batch, easy cleanGpuUsed, ImageResize+, SeedVR2LoadVAEModel, VAEDecodeTiled, LayerUtility: ImageReelComposit, KSampler, CLIPLoader, LayerUtility: ImageReel, VAELoader, VAEDecode, PreviewImage, CLIPTextEncode, UNETLoader, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, LoraLoaderModelOnly, Image Comparer (rgthree), TTP_Tile_image_size, EmptySD3LatentImage, JjkText, RH_LLMAPI_NODE, PreviewAny, PreviewImage, PreviewImage, TTP_Image_Assy, PreviewImage, Image Comparer (rgthree), SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "gradient_estimation", "scheduler": "sgm_uniform", "seed": 123456789, "steps": 10}
---

# 图片生成/文生图/文生图Z-image+SeedVR2.5.1 万亿级像素文生图，细节纤毫毕现，定义超高清影像新标准高_2033734929732870146.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图Z-image+SeedVR2.5.1 万亿级像素文生图，细节纤毫毕现，定义超高清影像新标准高_2033734929732870146.json`

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
- `LayerUtility: ImageReelComposit`
- `KSampler` ★核心
- `CLIPLoader`
- `LayerUtility: ImageReel`
- `VAELoader`
- `VAEDecode` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `TTP_Tile_image_size`
- `EmptySD3LatentImage`
- `JjkText`
- `RH_LLMAPI_NODE`
- `PreviewAny`
- `PreviewImage`
- `PreviewImage`
- `TTP_Image_Assy`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `SaveImage`

## 关键参数

- `seed` = `123456789`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `gradient_estimation`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **79%**（30/38）

**有卡**：`ConditioningZeroOut`、`LatentPixelScale`、`KSampler`、`UpscaleModelLoader`、`GetImageSize+`、`ImageResize+`、`ImageScaleBy`、`TTP_Image_Tile_Batch`、`easy cleanGpuUsed`、`SeedVR2LoadVAEModel`、`VAEDecodeTiled`、`LayerUtility: ImageReelComposit`、`CLIPLoader`、`LayerUtility: ImageReel`、`VAELoader`、`VAEDecode`、`CLIPTextEncode`、`UNETLoader`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`LoraLoaderModelOnly`、`TTP_Tile_image_size`、`EmptySD3LatentImage`、`RH_LLMAPI_NODE`、`TTP_Image_Assy`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、UNETLoader
