---
key: 平台全量/修复图像 高清放大-8K 画质高清修复 Ultimate Upscaler  Flux klein_2061970842417975297.json
name: 修复图像 高清放大-8K 画质高清修复 Ultimate Upscaler  Flux klein_2061970842417975297
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/修复图像 高清放大-8K 画质高清修复 Ultimate Upscaler  Flux klein_2061970842417975297.json
hash: 124263d724b6539e
coverage: 0.765957
learned_at: 2026-11-14 01:39:08
nodes: [EmptyFlux2LatentImage, ConstrainImage|pysssss, Note, GetImageSize, VAEEncode, Note, ImageResize+, ImageResize+, Get Image Size, Note, ImageScaleBy, VAEDecode, ReferenceLatent, ReferenceLatent, ConditioningZeroOut, SeedVR2VideoUpscaler, easy imageSize, SeedVR2LoadVAEModel, TTP_Image_Tile_Batch, TTP_Tile_image_size, Note, ConstrainImage|pysssss, ImageScaleBy, Note, Get Image Size, VAELoader, SeedVR2LoadDiTModel, SeedVR2BlockSwap, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, SeedVR2, Image Comparer (rgthree), ColorMatch, Image Comparer (rgthree), CLIPLoader, LoraLoaderModelOnly, UNETLoader, KSampler, SaveImage, SaveImage, SaveImage, LoadImage, TTP_Image_Assy, Image Comparer (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 783982000436742, "steps": 5}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/修复图像 高清放大-8K 画质高清修复 Ultimate Upscaler  Flux klein_2061970842417975297.json

> 来源文件 `comfyui_library/workflows/平台全量/修复图像 高清放大-8K 画质高清修复 Ultimate Upscaler  Flux klein_2061970842417975297.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `EmptyFlux2LatentImage`
- `ConstrainImage|pysssss`
- `Note`
- `GetImageSize`
- `VAEEncode` ★核心
- `Note`
- `ImageResize+`
- `ImageResize+`
- `Get Image Size`
- `Note`
- `ImageScaleBy`
- `VAEDecode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `SeedVR2VideoUpscaler`
- `easy imageSize`
- `SeedVR2LoadVAEModel`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `Note`
- `ConstrainImage|pysssss`
- `ImageScaleBy`
- `Note`
- `Get Image Size`
- `VAELoader`
- `SeedVR2LoadDiTModel`
- `SeedVR2BlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `SeedVR2`
- `Image Comparer (rgthree)`
- `ColorMatch`
- `Image Comparer (rgthree)`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `TTP_Image_Assy`
- `Image Comparer (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `783982000436742`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（36/47）

**有卡**：`EmptyFlux2LatentImage`、`ConstrainImage|pysssss`、`GetImageSize`、`VAEEncode`、`ImageResize+`、`Get Image Size`、`ImageScaleBy`、`VAEDecode`、`ReferenceLatent`、`ConditioningZeroOut`、`SeedVR2VideoUpscaler`、`easy imageSize`、`SeedVR2LoadVAEModel`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`VAELoader`、`SeedVR2LoadDiTModel`、`SeedVR2BlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`SeedVR2`、`ColorMatch`、`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`KSampler`、`SaveImage`、`LoadImage`、`TTP_Image_Assy`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
