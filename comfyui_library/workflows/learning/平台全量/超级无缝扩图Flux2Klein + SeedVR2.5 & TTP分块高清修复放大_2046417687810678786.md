---
key: 平台全量/超级无缝扩图Flux2Klein + SeedVR2.5 & TTP分块高清修复放大_2046417687810678786.json
name: 超级无缝扩图Flux2Klein + SeedVR2.5 & TTP分块高清修复放大_2046417687810678786
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/超级无缝扩图Flux2Klein + SeedVR2.5 & TTP分块高清修复放大_2046417687810678786.json
hash: 58edda4e5a0e04f7
coverage: 0.909091
learned_at: 2026-11-14 02:46:44
nodes: [RandomNoise, Flux2Scheduler, KSamplerSelect, ConditioningZeroOut, SamplerCustomAdvanced, ReferenceLatent, GetImageSize+, ConditioningZeroOut, DualCLIPLoader, LoraLoaderModelOnly, VAELoader, ImpactImageBatchToImageList, ImageListToImageBatch, FluxGuidance, VAEEncode, TTP_Tile_image_size, TTP_Image_Tile_Batch, CLIPTextEncode, TTP_Image_Assy, Image Comparer (rgthree), LoadImage, Image Comparer (rgthree), ReferenceLatent, ImpactInt, ConstrainImage|pysssss, LayerUtility: ExtendCanvasV2, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, CFGGuider, ImageUpscaleWithModel, KSampler, VAEDecodeTiled, ImageScaleToTotalPixels, UpscaleModelLoader, UNETLoader, PreviewImage, VAEEncode, VAEDecode, LoadImage, CLIPTextEncode, SaveImage, Fast Groups Bypasser (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.4, "sampler_name": "euler", "scheduler": "kl_optimal", "seed": 346344373822338, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/超级无缝扩图Flux2Klein + SeedVR2.5 & TTP分块高清修复放大_2046417687810678786.json

> 来源文件 `comfyui_library/workflows/平台全量/超级无缝扩图Flux2Klein + SeedVR2.5 & TTP分块高清修复放大_2046417687810678786.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `RandomNoise`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `ConditioningZeroOut`
- `SamplerCustomAdvanced` ★核心
- `ReferenceLatent`
- `GetImageSize+`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `ImpactImageBatchToImageList`
- `ImageListToImageBatch`
- `FluxGuidance`
- `VAEEncode` ★核心
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `CLIPTextEncode` ★核心
- `TTP_Image_Assy`
- `Image Comparer (rgthree)`
- `LoadImage`
- `Image Comparer (rgthree)`
- `ReferenceLatent`
- `ImpactInt`
- `ConstrainImage|pysssss`
- `LayerUtility: ExtendCanvasV2`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CFGGuider`
- `ImageUpscaleWithModel`
- `KSampler` ★核心
- `VAEDecodeTiled` ★核心
- `ImageScaleToTotalPixels`
- `UpscaleModelLoader`
- `UNETLoader` ★核心
- `PreviewImage`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `346344373822338`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `kl_optimal`
- `denoise` = `0.4`

## 知识

覆盖率 **91%**（40/44）

**有卡**：`RandomNoise`、`Flux2Scheduler`、`KSamplerSelect`、`ConditioningZeroOut`、`SamplerCustomAdvanced`、`ReferenceLatent`、`GetImageSize+`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`VAELoader`、`ImpactImageBatchToImageList`、`ImageListToImageBatch`、`FluxGuidance`、`VAEEncode`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`CLIPTextEncode`、`TTP_Image_Assy`、`LoadImage`、`ImpactInt`、`ConstrainImage|pysssss`、`LayerUtility: ExtendCanvasV2`、`UNETLoader`、`CLIPLoader`、`CFGGuider`、`ImageUpscaleWithModel`、`KSampler`、`VAEDecodeTiled`、`ImageScaleToTotalPixels`、`UpscaleModelLoader`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
