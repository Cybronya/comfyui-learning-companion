---
key: 平台全量/Wan2.1+TTP超高清放大_1950792152269914113.json
name: Wan2.1+TTP超高清放大_1950792152269914113
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1+TTP超高清放大_1950792152269914113.json
hash: 3eb1209bf7459c28
coverage: 0.894737
learned_at: 2026-11-14 01:04:34
nodes: [LoadImage, LoadImage, easy cleanGpuUsed, GetImageSize, easy imageListToImageBatch, ImageScale, easy cleanGpuUsed, Florence2ModelLoader, easy cleanGpuUsed, SeedVR2BlockSwap, SeedVR2, Image Comparer (rgthree), VAEEncode, ImageScale, easy cleanGpuUsed, easy cleanGpuUsed, CLIPTextEncode, Number Multiple Of, Number Multiple Of, easy cleanGpuUsed, CLIPTextEncode, CLIPTextEncode, CM_IntToNumber, GetImageSize, Number to Int, CLIPTextEncode, Number to Int, LayerUtility: ImageRemoveAlpha, easy cleanGpuUsed, SimpleMath+, easy cleanGpuUsed, ImageBatchToList, TTP_Image_Assy, TTP_Image_Tile_Batch, Florence2Run, CM_IntToNumber, VAEEncode, SimpleMath+, VAEDecode, ImageUpscaleWithModel, TTP_Tile_image_size, KSampler, KSampler, LayerUtility: ImageScaleByAspectRatio V2, VAEDecodeTiled, LoadImage, PrimitiveNode, PrimitiveInt, Note, Note, UpscaleModelLoader, CLIPLoader, UNETLoader, VAELoader, LoraLoader, SaveImage, PreviewImage]
patterns: [image_to_image, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "lora_name": "Wan2.1_I2V_14B_FusionX_LoRA.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 1772787130599, "steps": 8, "strength_clip": 0.4000000000000001, "strength_model": 0.4000000000000001}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Wan2.1+TTP超高清放大_1950792152269914113.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1+TTP超高清放大_1950792152269914113.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
- `LoadImage`
- `LoadImage`
- `easy cleanGpuUsed`
- `GetImageSize`
- `easy imageListToImageBatch`
- `ImageScale`
- `easy cleanGpuUsed`
- `Florence2ModelLoader`
- `easy cleanGpuUsed`
- `SeedVR2BlockSwap`
- `SeedVR2`
- `Image Comparer (rgthree)`
- `VAEEncode` ★核心
- `ImageScale`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `Number Multiple Of`
- `Number Multiple Of`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CM_IntToNumber`
- `GetImageSize`
- `Number to Int`
- `CLIPTextEncode` ★核心
- `Number to Int`
- `LayerUtility: ImageRemoveAlpha`
- `easy cleanGpuUsed`
- `SimpleMath+`
- `easy cleanGpuUsed`
- `ImageBatchToList`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `Florence2Run`
- `CM_IntToNumber`
- `VAEEncode` ★核心
- `SimpleMath+`
- `VAEDecode` ★核心
- `ImageUpscaleWithModel`
- `TTP_Tile_image_size`
- `KSampler` ★核心
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecodeTiled` ★核心
- `LoadImage`
- `PrimitiveNode`
- `PrimitiveInt`
- `Note`
- `Note`
- `UpscaleModelLoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `LoraLoader` ★核心
- `SaveImage`
- `PreviewImage`

**识别到的模式**：image_to_image、lora

## 关键参数

- `seed` = `1772787130599`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.10000000000000002`
- `lora_name` = `Wan2.1_I2V_14B_FusionX_LoRA.safetensors`
- `strength_model` = `0.4000000000000001`
- `strength_clip` = `0.4000000000000001`

## 知识

覆盖率 **89%**（51/57）

**有卡**：`LoadImage`、`easy cleanGpuUsed`、`GetImageSize`、`easy imageListToImageBatch`、`ImageScale`、`Florence2ModelLoader`、`SeedVR2BlockSwap`、`SeedVR2`、`VAEEncode`、`CLIPTextEncode`、`Number Multiple Of`、`CM_IntToNumber`、`Number to Int`、`LayerUtility: ImageRemoveAlpha`、`SimpleMath+`、`ImageBatchToList`、`TTP_Image_Assy`、`TTP_Image_Tile_Batch`、`Florence2Run`、`VAEDecode`、`ImageUpscaleWithModel`、`TTP_Tile_image_size`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecodeTiled`、`UpscaleModelLoader`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`LoraLoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、SeedVR2

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
