---
key: 平台全量/flux klein + SeedVR2.5.1 + 4宫格自动分块_2048989705114488834.json
name: flux klein + SeedVR2.5.1 + 4宫格自动分块_2048989705114488834
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/flux klein + SeedVR2.5.1 + 4宫格自动分块_2048989705114488834.json
hash: fd417df8ad4ebdb1
coverage: 0.829787
learned_at: 2026-11-14 01:10:35
nodes: [easy mathInt, easy mathInt, ReferenceLatent, CLIPTextEncode, CLIPTextEncode, easy mathInt, VAELoader, ConditioningZeroOut, ConditioningZeroOut, SeedVR2LoadDiTModel, easy mathInt, BatchCount+, easy mathInt, easy mathInt, easy mathInt, easy mathInt, SeedVR2VideoUpscaler, PrimitiveInt, easy imageBatchToImageList, easy imageListToImageBatch, LoraLoader, Qwen3_VQA, CLIPLoader, ImageFromBatch, TTP_Tile_image_size, easy rangeInt, easy mathInt, CLIPTextEncode, easy mathInt, Reroute, SaveImage, Reroute, easy imageBatchToImageList, PreviewImage, Image Comparer (rgthree), TTP_Image_Tile_Batch, VAEEncode, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, Reroute, easy mathInt, easy mathInt, TTP_Tile_image_size, TTP_Tile_image_size, easy mathInt, easy mathInt, TTP_Image_Tile_Batch, easy imageSizeBySide, ImageFromBatch, KSampler, PreviewImage, SeedVR2LoadVAEModel, LoraLoader, UNETLoader, Fast Groups Muter (rgthree), UNETLoader, LayerUtility: ImageScaleByAspectRatio, Image Comparer (rgthree), VAEEncode, Int, Int, ImageTile+, VAEDecode, easy imageListToImageBatch, TTP_Image_Assy, Image Comparer (rgthree), VAEDecode, easy rangeInt, TTP_Image_Assy, ImageFromBatch, easy imageListToImageBatch, easy rangeInt, ImageFromBatch, easy imageColorMatch, easy imageBatchToImageList, easy imageBatchToImageList, TTP_Image_Assy, Reroute, easy imageBatchToImageList, LayerUtility: ImageScaleByAspectRatio V2, TTP_Image_Tile_Batch, PreviewImage, easy mathInt, easy mathInt, easy mathInt, TTP_Image_Assy, Reroute, SaveImage, KSampler, LoadImage, SaveImage, ShowText|pysssss, Image Comparer (rgthree), BatchCount+]
patterns: [image_to_image, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "ultra_real_v2.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 822853769729490, "steps": 4, "strength_clip": 1, "strength_model": 1}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/flux klein + SeedVR2.5.1 + 4宫格自动分块_2048989705114488834.json

> 来源文件 `comfyui_library/workflows/平台全量/flux klein + SeedVR2.5.1 + 4宫格自动分块_2048989705114488834.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（94 个）：
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
- `PrimitiveInt`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `LoraLoader` ★核心
- `Qwen3_VQA`
- `CLIPLoader`
- `ImageFromBatch`
- `TTP_Tile_image_size`
- `easy rangeInt`
- `easy mathInt`
- `CLIPTextEncode` ★核心
- `easy mathInt`
- `Reroute`
- `SaveImage`
- `Reroute`
- `easy imageBatchToImageList`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `TTP_Image_Tile_Batch`
- `VAEEncode` ★核心
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `easy mathInt`
- `easy mathInt`
- `TTP_Tile_image_size`
- `TTP_Tile_image_size`
- `easy mathInt`
- `easy mathInt`
- `TTP_Image_Tile_Batch`
- `easy imageSizeBySide`
- `ImageFromBatch`
- `KSampler` ★核心
- `PreviewImage`
- `SeedVR2LoadVAEModel`
- `LoraLoader` ★核心
- `UNETLoader` ★核心
- `Fast Groups Muter (rgthree)`
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio`
- `Image Comparer (rgthree)`
- `VAEEncode` ★核心
- `Int`
- `Int`
- `ImageTile+`
- `VAEDecode` ★核心
- `easy imageListToImageBatch`
- `TTP_Image_Assy`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `easy rangeInt`
- `TTP_Image_Assy`
- `ImageFromBatch`
- `easy imageListToImageBatch`
- `easy rangeInt`
- `ImageFromBatch`
- `easy imageColorMatch`
- `easy imageBatchToImageList`
- `easy imageBatchToImageList`
- `TTP_Image_Assy`
- `Reroute`
- `easy imageBatchToImageList`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TTP_Image_Tile_Batch`
- `PreviewImage`
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `TTP_Image_Assy`
- `Reroute`
- `SaveImage`
- `KSampler` ★核心
- `LoadImage`
- `SaveImage`
- `ShowText|pysssss`
- `Image Comparer (rgthree)`
- `BatchCount+`

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `ultra_real_v2.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `seed` = `822853769729490`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（78/94）

**有卡**：`easy mathInt`、`ReferenceLatent`、`CLIPTextEncode`、`VAELoader`、`ConditioningZeroOut`、`SeedVR2LoadDiTModel`、`BatchCount+`、`SeedVR2VideoUpscaler`、`easy imageBatchToImageList`、`easy imageListToImageBatch`、`LoraLoader`、`Qwen3_VQA`、`CLIPLoader`、`ImageFromBatch`、`TTP_Tile_image_size`、`easy rangeInt`、`SaveImage`、`TTP_Image_Tile_Batch`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy imageSizeBySide`、`KSampler`、`SeedVR2LoadVAEModel`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio`、`Int`、`ImageTile+`、`VAEDecode`、`TTP_Image_Assy`、`easy imageColorMatch`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
