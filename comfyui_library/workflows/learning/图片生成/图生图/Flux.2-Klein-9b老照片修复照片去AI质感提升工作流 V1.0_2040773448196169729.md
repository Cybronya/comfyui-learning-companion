---
key: 图片生成/图生图/Flux.2-Klein-9b老照片修复照片去AI质感提升工作流 V1.0_2040773448196169729.json
name: Flux.2-Klein-9b老照片修复照片去AI质感提升工作流 V1.0_2040773448196169729
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.2-Klein-9b老照片修复照片去AI质感提升工作流 V1.0_2040773448196169729.json
hash: 7a94ead065c02055
coverage: 0.837838
learned_at: 2026-10-23 10:58:50
nodes: [CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, KSamplerAdvanced, VAEDecode, VAEEncode, ConditioningZeroOut, ReferenceLatent, INTConstant, INTConstant, VAELoader, KSamplerAdvanced, UNETLoader, ImageResizeKJv2, ImageScaleBy, PrimitiveFloat, ImageResize+, GetImageSize+, TTP_Image_Tile_Batch, ImageScaleBy, GetImageSize+, TTP_Tile_image_size, easy showAnything, easy showAnything, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, ImageResize+, SaveImage, Image Comparer (rgthree), SaveImage, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 图片生成/图生图/Flux.2-Klein-9b老照片修复照片去AI质感提升工作流 V1.0_2040773448196169729.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.2-Klein-9b老照片修复照片去AI质感提升工作流 V1.0_2040773448196169729.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `CLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `ReferenceLatent`
- `INTConstant`
- `INTConstant`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `ImageResizeKJv2`
- `ImageScaleBy`
- `PrimitiveFloat`
- `ImageResize+`
- `GetImageSize+`
- `TTP_Image_Tile_Batch`
- `ImageScaleBy`
- `GetImageSize+`
- `TTP_Tile_image_size`
- `easy showAnything`
- `easy showAnything`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `ImageResize+`
- `SaveImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **84%**（31/37）

**有卡**：`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSamplerAdvanced`、`VAEDecode`、`VAEEncode`、`ConditioningZeroOut`、`ReferenceLatent`、`INTConstant`、`VAELoader`、`UNETLoader`、`ImageResizeKJv2`、`ImageScaleBy`、`ImageResize+`、`GetImageSize+`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`TTP_Image_Assy`、`SaveImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
