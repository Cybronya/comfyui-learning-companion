---
key: 图片生成/图生图/flux.2-klein-9b老照片修复，照片去AI，质感提升_2028040297262882817.json
name: flux.2-klein-9b老照片修复，照片去AI，质感提升_2028040297262882817
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/flux.2-klein-9b老照片修复，照片去AI，质感提升_2028040297262882817.json
hash: 5cf6e1e0caf7747b
coverage: 0.837838
learned_at: 2026-10-23 11:35:52
nodes: [CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, KSamplerAdvanced, VAEDecode, VAEEncode, ConditioningZeroOut, ReferenceLatent, LoadImage, INTConstant, INTConstant, VAELoader, KSamplerAdvanced, UNETLoader, ImageResizeKJv2, ImageScaleBy, PrimitiveFloat, ImageResize+, GetImageSize+, TTP_Image_Tile_Batch, ImageScaleBy, GetImageSize+, TTP_Tile_image_size, easy showAnything, easy showAnything, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, ImageResize+, SaveImage, Image Comparer (rgthree), SaveImage, Fast Groups Bypasser (rgthree), Note, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 图片生成/图生图/flux.2-klein-9b老照片修复，照片去AI，质感提升_2028040297262882817.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/flux.2-klein-9b老照片修复，照片去AI，质感提升_2028040297262882817.json`

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
- `LoadImage`
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
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **84%**（31/37）

**有卡**：`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSamplerAdvanced`、`VAEDecode`、`VAEEncode`、`ConditioningZeroOut`、`ReferenceLatent`、`LoadImage`、`INTConstant`、`VAELoader`、`UNETLoader`、`ImageResizeKJv2`、`ImageScaleBy`、`ImageResize+`、`GetImageSize+`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`TTP_Image_Assy`、`SaveImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
