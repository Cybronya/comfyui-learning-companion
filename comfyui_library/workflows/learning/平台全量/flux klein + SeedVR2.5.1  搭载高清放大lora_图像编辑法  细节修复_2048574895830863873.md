---
key: 平台全量/flux klein + SeedVR2.5.1  搭载高清放大lora_图像编辑法  细节修复_2048574895830863873.json
name: flux klein + SeedVR2.5.1  搭载高清放大lora_图像编辑法  细节修复_2048574895830863873
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/flux klein + SeedVR2.5.1  搭载高清放大lora_图像编辑法  细节修复_2048574895830863873.json
hash: 67c8a3b36a880a02
coverage: 0.80198
learned_at: 2026-11-14 01:10:33
nodes: [easy mathInt, easy mathInt, ReferenceLatent, CLIPTextEncode, CLIPTextEncode, easy mathInt, VAELoader, ConditioningZeroOut, ConditioningZeroOut, SeedVR2LoadDiTModel, easy mathInt, BatchCount+, easy mathInt, easy mathInt, easy mathInt, easy mathInt, SeedVR2VideoUpscaler, easy imageBatchToImageList, LoraLoader, Qwen3_VQA, CLIPLoader, TTP_Tile_image_size, easy mathInt, CLIPTextEncode, Reroute, SaveImage, Reroute, Image Comparer (rgthree), TTP_Image_Tile_Batch, VAEEncode, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, easy mathInt, easy mathInt, TTP_Tile_image_size, TTP_Tile_image_size, easy mathInt, easy mathInt, TTP_Image_Tile_Batch, easy imageSizeBySide, ImageFromBatch, SeedVR2LoadVAEModel, LoraLoader, UNETLoader, UNETLoader, LayerUtility: ImageScaleByAspectRatio, Image Comparer (rgthree), VAEEncode, VAEDecode, TTP_Image_Assy, Image Comparer (rgthree), VAEDecode, easy imageListToImageBatch, easy imageBatchToImageList, easy imageBatchToImageList, Reroute, LayerUtility: ImageScaleByAspectRatio V2, TTP_Image_Tile_Batch, Reroute, ShowText|pysssss, Image Comparer (rgthree), Fast Groups Muter (rgthree), easy imageListToImageBatch, easy imageColorMatch, PrimitiveInt, easy imageBatchToImageList, PreviewImage, easy rangeInt, TTP_Image_Assy, ImageFromBatch, KSampler, SaveImage, TTP_Image_Assy, SaveImage, HAIGC_LoadImagesFromZip, easy imageListToImageBatch, easy showAnything, PreviewImage, PreviewImage, Reroute, KSampler, TTP_Image_Assy, easy imageBatchToImageList, easy mathInt, easy mathInt, ImageFromBatch, BatchCount+, easy mathInt, easy imageListToImageBatch, easy rangeInt, ImageFromBatch, Int, Int, easy mathInt, easy rangeInt, LoadImage, Reroute, ImageTile+, Reroute, Reroute, easy mathInt]
patterns: [image_to_image, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "lora_name": "ultra_real_v2.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 66796681569714, "steps": 4, "strength_clip": 1, "strength_model": 1}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/flux klein + SeedVR2.5.1  搭载高清放大lora_图像编辑法  细节修复_2048574895830863873.json

> 来源文件 `comfyui_library/workflows/平台全量/flux klein + SeedVR2.5.1  搭载高清放大lora_图像编辑法  细节修复_2048574895830863873.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（101 个）：
- `easy mathInt`
- `easy mathInt`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy mathInt`
- `VAELoader`
- `ConditioningZeroOut`
- `ConditioningZeroOut`
- `SeedVR2LoadDiTModel`
- `easy mathInt`
- `BatchCount+`
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `SeedVR2VideoUpscaler`
- `easy imageBatchToImageList`
- `LoraLoader` ★核心
- `Qwen3_VQA`
- `CLIPLoader`
- `TTP_Tile_image_size`
- `easy mathInt`
- `CLIPTextEncode` ★核心
- `Reroute`
- `SaveImage`
- `Reroute`
- `Image Comparer (rgthree)`
- `TTP_Image_Tile_Batch`
- `VAEEncode` ★核心
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy mathInt`
- `easy mathInt`
- `TTP_Tile_image_size`
- `TTP_Tile_image_size`
- `easy mathInt`
- `easy mathInt`
- `TTP_Image_Tile_Batch`
- `easy imageSizeBySide`
- `ImageFromBatch`
- `SeedVR2LoadVAEModel`
- `LoraLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio`
- `Image Comparer (rgthree)`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `TTP_Image_Assy`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `easy imageListToImageBatch`
- `easy imageBatchToImageList`
- `easy imageBatchToImageList`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TTP_Image_Tile_Batch`
- `Reroute`
- `ShowText|pysssss`
- `Image Comparer (rgthree)`
- `Fast Groups Muter (rgthree)`
- `easy imageListToImageBatch`
- `easy imageColorMatch`
- `PrimitiveInt`
- `easy imageBatchToImageList`
- `PreviewImage`
- `easy rangeInt`
- `TTP_Image_Assy`
- `ImageFromBatch`
- `KSampler` ★核心
- `SaveImage`
- `TTP_Image_Assy`
- `SaveImage`
- `HAIGC_LoadImagesFromZip`
- `easy imageListToImageBatch`
- `easy showAnything`
- `PreviewImage`
- `PreviewImage`
- `Reroute`
- `KSampler` ★核心
- `TTP_Image_Assy`
- `easy imageBatchToImageList`
- `easy mathInt`
- `easy mathInt`
- `ImageFromBatch`
- `BatchCount+`
- `easy mathInt`
- `easy imageListToImageBatch`
- `easy rangeInt`
- `ImageFromBatch`
- `Int`
- `Int`
- `easy mathInt`
- `easy rangeInt`
- `LoadImage`
- `Reroute`
- `ImageTile+`
- `Reroute`
- `Reroute`
- `easy mathInt`

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `ultra_real_v2.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `seed` = `66796681569714`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **80%**（81/101）

**有卡**：`easy mathInt`、`ReferenceLatent`、`CLIPTextEncode`、`VAELoader`、`ConditioningZeroOut`、`SeedVR2LoadDiTModel`、`BatchCount+`、`SeedVR2VideoUpscaler`、`easy imageBatchToImageList`、`LoraLoader`、`Qwen3_VQA`、`CLIPLoader`、`TTP_Tile_image_size`、`SaveImage`、`TTP_Image_Tile_Batch`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy imageSizeBySide`、`ImageFromBatch`、`SeedVR2LoadVAEModel`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio`、`VAEDecode`、`TTP_Image_Assy`、`easy imageListToImageBatch`、`easy imageColorMatch`、`easy rangeInt`、`KSampler`、`HAIGC_LoadImagesFromZip`、`Int`、`LoadImage`、`ImageTile+`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
