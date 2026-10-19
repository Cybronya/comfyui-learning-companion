---
key: 图片生成/文生图/LHSTW30M-DMT.Z-Image亿级像素文生图_1998758421291749377.json
name: LHSTW30M-DMT.Z-Image亿级像素文生图_1998758421291749377
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/LHSTW30M-DMT.Z-Image亿级像素文生图_1998758421291749377.json
hash: 14993b4a3fd6c578
coverage: 0.756098
learned_at: 2026-10-19 21:46:42
nodes: [RH_LLMAPI_NODE, Note, PreviewAny, KSampler, CLIPTextEncode, EmptySD3LatentImage, UNETLoader, CLIPLoader, VAELoader, ConditioningZeroOut, VAEDecode, PreviewImage, Image Comparer (rgthree), PreviewImage, Image Comparer (rgthree), PreviewImage, LatentPixelScale, VAEDecodeTiled, LayerUtility: ImageReel, KSampler, UpscaleModelLoader, LayerUtility: ImageReelComposit, easy cleanGpuUsed, ImageScaleBy, GetImageSize+, PreviewImage, TTP_Image_Assy, ImageResize+, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, GetImageSize+, ImageScaleBy, SeedVR2LoadDiTModel, TTP_Image_Tile_Batch, TTP_Tile_image_size, ImageResize+, Note, SaveImage, LoraLoaderModelOnly, AILab_QwenVL, JjkText]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.25000000000000006, "sampler_name": "dpmpp_2m_sde", "scheduler": "sgm_uniform", "seed": 6, "steps": 10}
---

# 图片生成/文生图/LHSTW30M-DMT.Z-Image亿级像素文生图_1998758421291749377.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/LHSTW30M-DMT.Z-Image亿级像素文生图_1998758421291749377.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `RH_LLMAPI_NODE`
- `Note`
- `PreviewAny`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `PreviewImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `LatentPixelScale`
- `VAEDecodeTiled` ★核心
- `LayerUtility: ImageReel`
- `KSampler` ★核心
- `UpscaleModelLoader`
- `LayerUtility: ImageReelComposit`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `GetImageSize+`
- `PreviewImage`
- `TTP_Image_Assy`
- `ImageResize+`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `GetImageSize+`
- `ImageScaleBy`
- `SeedVR2LoadDiTModel`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `ImageResize+`
- `Note`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `AILab_QwenVL`
- `JjkText`

## 关键参数

- `seed` = `6`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m_sde`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.25000000000000006`

## 知识

覆盖率 **76%**（31/41）

**有卡**：`RH_LLMAPI_NODE`、`KSampler`、`CLIPTextEncode`、`EmptySD3LatentImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`VAEDecode`、`LatentPixelScale`、`VAEDecodeTiled`、`LayerUtility: ImageReel`、`UpscaleModelLoader`、`LayerUtility: ImageReelComposit`、`easy cleanGpuUsed`、`ImageScaleBy`、`GetImageSize+`、`TTP_Image_Assy`、`ImageResize+`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`SaveImage`、`LoraLoaderModelOnly`、`AILab_QwenVL`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、UNETLoader
