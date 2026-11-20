---
key: 平台全量/Qwen2511+wan2.2皮肤质感完美修复_2007377921459097602.json
name: Qwen2511+wan2.2皮肤质感完美修复_2007377921459097602
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen2511+wan2.2皮肤质感完美修复_2007377921459097602.json
hash: 26c47bee64110fe0
coverage: 0.891892
learned_at: 2026-11-14 00:52:31
nodes: [ModelSamplingSD3, VAEEncode, ImageFromBatch, TTP_Image_Tile_Batch, VAEDecode, FluxGuidance, easy imageBatchToImageList, ImageListToImageBatch, ImageScaleToTotalPixels, TTP_Image_Assy, CLIPTextEncode, PathchSageAttentionKJ, easy cleanGpuUsed, TTP_Tile_image_size, ImageUpscaleWithModel, CLIPTextEncode, Image Comparer (rgthree), LoadImage, ImageScaleToTotalPixels, VAEEncode, QwenImageIntegratedKSampler, PreviewImage, VAEDecode, PreviewImage, SaveImage, KSampler, easy cleanGpuUsed, PrimitiveFloat, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, UpscaleModelLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CheckpointLoaderSimple]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen--AIO-NSFW-v18.safetensors", "denoise": 0.02, "sampler_name": "euler", "scheduler": "simple", "seed": 933993308877410, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Qwen2511+wan2.2皮肤质感完美修复_2007377921459097602.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen2511+wan2.2皮肤质感完美修复_2007377921459097602.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `ModelSamplingSD3`
- `VAEEncode` ★核心
- `ImageFromBatch`
- `TTP_Image_Tile_Batch`
- `VAEDecode` ★核心
- `FluxGuidance`
- `easy imageBatchToImageList`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `TTP_Image_Assy`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `easy cleanGpuUsed`
- `TTP_Tile_image_size`
- `ImageUpscaleWithModel`
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `QwenImageIntegratedKSampler` ★核心
- `PreviewImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `PrimitiveFloat`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `UpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `933993308877410`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.02`
- `checkpoint` = `Qwen--AIO-NSFW-v18.safetensors`

## 知识

覆盖率 **89%**（33/37）

**有卡**：`ModelSamplingSD3`、`VAEEncode`、`ImageFromBatch`、`TTP_Image_Tile_Batch`、`VAEDecode`、`FluxGuidance`、`easy imageBatchToImageList`、`ImageListToImageBatch`、`ImageScaleToTotalPixels`、`TTP_Image_Assy`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`easy cleanGpuUsed`、`TTP_Tile_image_size`、`ImageUpscaleWithModel`、`LoadImage`、`QwenImageIntegratedKSampler`、`SaveImage`、`KSampler`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`UpscaleModelLoader`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、CLIPTextEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
