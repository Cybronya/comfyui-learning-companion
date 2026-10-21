---
key: 图片生成/图生图/flux_klein_+_SeedVR2.5.1_搭载高清放大lora_图像编辑法_细节修复_2087437139972808706.json
name: flux_klein_+_SeedVR2.5.1_搭载高清放大lora_图像编辑法_细节修复_2087437139972808706
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/flux_klein_+_SeedVR2.5.1_搭载高清放大lora_图像编辑法_细节修复_2087437139972808706.json
hash: ae7f32d15e80a5e6
coverage: 0.803922
learned_at: 2026-10-21 00:45:27
nodes: [easy mathInt, easy mathInt, ReferenceLatent, CLIPTextEncode, CLIPTextEncode, VAELoader, ConditioningZeroOut, CLIPLoader, TTP_Tile_image_size, easy mathInt, easy mathInt, LoraLoader, UNETLoader, UNETLoader, VAEEncode, VAEDecode, easy imageBatchToImageList, easy imageBatchToImageList, Reroute, TTP_Image_Tile_Batch, Reroute, Fast Groups Muter (rgthree), easy imageListToImageBatch, easy imageColorMatch, PreviewImage, easy rangeInt, TTP_Image_Assy, ImageFromBatch, KSampler, SaveImage, TTP_Image_Assy, SaveImage, easy imageListToImageBatch, easy showAnything, easy mathInt, easy mathInt, BatchCount+, easy mathInt, Int, Int, Reroute, Reroute, HAIGC_LoadImagesFromZip, ImageTile+, LoadImage, Image Comparer (rgthree), Reroute, PrimitiveInt, LoraLoader, easy imageBatchToImageList, LayerUtility: ImageScaleByAspectRatio V2]
patterns: [image_to_image, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "Flux2-Klein9B-Anything2Real_v3.0.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 822853769729490, "steps": 4, "strength_clip": 1, "strength_model": 1}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/flux_klein_+_SeedVR2.5.1_搭载高清放大lora_图像编辑法_细节修复_2087437139972808706.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/flux_klein_+_SeedVR2.5.1_搭载高清放大lora_图像编辑法_细节修复_2087437139972808706.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `easy mathInt`
- `easy mathInt`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ConditioningZeroOut`
- `CLIPLoader`
- `TTP_Tile_image_size`
- `easy mathInt`
- `easy mathInt`
- `LoraLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `easy imageBatchToImageList`
- `easy imageBatchToImageList`
- `Reroute`
- `TTP_Image_Tile_Batch`
- `Reroute`
- `Fast Groups Muter (rgthree)`
- `easy imageListToImageBatch`
- `easy imageColorMatch`
- `PreviewImage`
- `easy rangeInt`
- `TTP_Image_Assy`
- `ImageFromBatch`
- `KSampler` ★核心
- `SaveImage`
- `TTP_Image_Assy`
- `SaveImage`
- `easy imageListToImageBatch`
- `easy showAnything`
- `easy mathInt`
- `easy mathInt`
- `BatchCount+`
- `easy mathInt`
- `Int`
- `Int`
- `Reroute`
- `Reroute`
- `HAIGC_LoadImagesFromZip`
- `ImageTile+`
- `LoadImage`
- `Image Comparer (rgthree)`
- `Reroute`
- `PrimitiveInt`
- `LoraLoader` ★核心
- `easy imageBatchToImageList`
- `LayerUtility: ImageScaleByAspectRatio V2`

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `Flux2-Klein9B-Anything2Real_v3.0.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `seed` = `822853769729490`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（41/51）

**有卡**：`easy mathInt`、`ReferenceLatent`、`CLIPTextEncode`、`VAELoader`、`ConditioningZeroOut`、`CLIPLoader`、`TTP_Tile_image_size`、`LoraLoader`、`UNETLoader`、`VAEEncode`、`VAEDecode`、`easy imageBatchToImageList`、`TTP_Image_Tile_Batch`、`easy imageListToImageBatch`、`easy imageColorMatch`、`easy rangeInt`、`TTP_Image_Assy`、`ImageFromBatch`、`KSampler`、`SaveImage`、`BatchCount+`、`Int`、`HAIGC_LoadImagesFromZip`、`ImageTile+`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
