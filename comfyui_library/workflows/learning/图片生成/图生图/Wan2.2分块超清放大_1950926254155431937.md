---
key: 图片生成/图生图/Wan2.2分块超清放大_1950926254155431937.json
name: Wan2.2分块超清放大_1950926254155431937
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2分块超清放大_1950926254155431937.json
hash: 4496ce54a8cf779a
coverage: 0.846154
learned_at: 2026-10-23 11:28:15
nodes: [CLIPLoader, UNETLoader, ModelSamplingSD3, Anything Everywhere3, LoraLoader, VAELoader, ImageScaleToTotalPixels, ImageUpscaleWithModel, UpscaleModelLoader, TTP_Image_Tile_Batch, easy imageBatchToImageList, CLIPTextEncode, VAEEncode, VAEDecodeTiled, easy imageListToImageBatch, Florence2Run, Florence2ModelLoader, ShowText|pysssss, PreviewImage, CLIPTextEncode, TTP_Image_Assy, SaveImage, KSampler, Image Comparer (rgthree), LoadImage, TTP_Tile_image_size]
patterns: [image_to_image, lora]
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 3.5, "denoise": 0.10000000000000002, "lora_name": "Gundam_RX78_Flux.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 316430325547060, "steps": 10, "strength_clip": 0.85, "strength_model": 0.85}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 图片生成/图生图/Wan2.2分块超清放大_1950926254155431937.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2分块超清放大_1950926254155431937.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `Anything Everywhere3`
- `LoraLoader` ★核心
- `VAELoader`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `TTP_Image_Tile_Batch`
- `easy imageBatchToImageList`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `VAEDecodeTiled` ★核心
- `easy imageListToImageBatch`
- `Florence2Run`
- `Florence2ModelLoader`
- `ShowText|pysssss`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `TTP_Image_Assy`
- `SaveImage`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `TTP_Tile_image_size`

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `Gundam_RX78_Flux.safetensors`
- `strength_model` = `0.85`
- `strength_clip` = `0.85`
- `seed` = `316430325547060`
- `steps` = `10`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **85%**（22/26）

**有卡**：`CLIPLoader`、`UNETLoader`、`ModelSamplingSD3`、`LoraLoader`、`VAELoader`、`ImageScaleToTotalPixels`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`CLIPTextEncode`、`VAEEncode`、`VAEDecodeTiled`、`easy imageListToImageBatch`、`Florence2Run`、`Florence2ModelLoader`、`TTP_Image_Assy`、`SaveImage`、`KSampler`、`LoadImage`、`TTP_Tile_image_size`

**用到的条目**：KSampler、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEDecodeTiled、VAEEncode

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
