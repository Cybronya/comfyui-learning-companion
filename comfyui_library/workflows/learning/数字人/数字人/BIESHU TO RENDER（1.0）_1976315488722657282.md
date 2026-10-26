---
key: 数字人/数字人/BIESHU TO RENDER（1.0）_1976315488722657282.json
name: BIESHU TO RENDER（1.0）_1976315488722657282
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/BIESHU TO RENDER（1.0）_1976315488722657282.json
hash: 420bd99ddb82919f
coverage: 0.945455
learned_at: 2026-10-26 01:53:59
nodes: [ConditioningZeroOut, VAEDecode, FluxGuidance, TTP_Tile_image_size, easy imageListToImageBatch, easy imageBatchToImageList, VAELoader, VAEEncode, TTP_Image_Tile_Batch, ImageSharpen, Image Levels Adjustment, ConditioningZeroOut, LoadImage, VAELoader, CLIPLoader, ImageUpscaleWithModel, CLIPTextEncode, UNETLoader, TextEncodeQwenImageEdit_lrzjason, ImageScaleToTotalPixels, KSampler, DualCLIPLoader, TTP_Image_Assy, LoraLoaderModelOnly, ImageScaleToTotalPixels, KSamplerSelect, VAEDecodeTiled, TTP_Tile_image_size, TTP_Image_Tile_Batch, Reroute, easy imageBatchToImageList, VAELoader, RandomNoise, CLIPTextEncode, VAEEncode, ImageListToImageBatch, FluxGuidance, UNETLoader, LoraLoader, KSampler, UpscaleModelLoader, VAEDecode, Image Comparer (rgthree), TTP_Image_Assy, JjkText, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, BasicGuider, UNETLoader, DualCLIPLoader, LoraLoader, SamplerCustomAdvanced, UpscaleModelLoader, ImageUpscaleWithModel, BasicScheduler]
patterns: [image_to_image, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "Flux Turbo Lora.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 98645896615241, "steps": 8, "strength_clip": 1, "strength_model": 1}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/BIESHU TO RENDER（1.0）_1976315488722657282.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/BIESHU TO RENDER（1.0）_1976315488722657282.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（55 个）：
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `FluxGuidance`
- `TTP_Tile_image_size`
- `easy imageListToImageBatch`
- `easy imageBatchToImageList`
- `VAELoader`
- `VAEEncode` ★核心
- `TTP_Image_Tile_Batch`
- `ImageSharpen`
- `Image Levels Adjustment`
- `ConditioningZeroOut`
- `LoadImage`
- `VAELoader`
- `CLIPLoader`
- `ImageUpscaleWithModel`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `TextEncodeQwenImageEdit_lrzjason`
- `ImageScaleToTotalPixels`
- `KSampler` ★核心
- `DualCLIPLoader`
- `TTP_Image_Assy`
- `LoraLoaderModelOnly` ★核心
- `ImageScaleToTotalPixels`
- `KSamplerSelect` ★核心
- `VAEDecodeTiled` ★核心
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `Reroute`
- `easy imageBatchToImageList`
- `VAELoader`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `ImageListToImageBatch`
- `FluxGuidance`
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `KSampler` ★核心
- `UpscaleModelLoader`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `TTP_Image_Assy`
- `JjkText`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `BasicGuider`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoraLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `BasicScheduler`

**识别到的模式**：image_to_image、lora

## 关键参数

- `seed` = `98645896615241`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `Flux Turbo Lora.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **95%**（52/55）

**有卡**：`ConditioningZeroOut`、`VAEDecode`、`FluxGuidance`、`TTP_Tile_image_size`、`easy imageListToImageBatch`、`easy imageBatchToImageList`、`VAELoader`、`VAEEncode`、`TTP_Image_Tile_Batch`、`ImageSharpen`、`Image Levels Adjustment`、`LoadImage`、`CLIPLoader`、`ImageUpscaleWithModel`、`CLIPTextEncode`、`UNETLoader`、`TextEncodeQwenImageEdit_lrzjason`、`ImageScaleToTotalPixels`、`KSampler`、`DualCLIPLoader`、`TTP_Image_Assy`、`LoraLoaderModelOnly`、`KSamplerSelect`、`VAEDecodeTiled`、`RandomNoise`、`ImageListToImageBatch`、`LoraLoader`、`UpscaleModelLoader`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`BasicGuider`、`SamplerCustomAdvanced`、`BasicScheduler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
