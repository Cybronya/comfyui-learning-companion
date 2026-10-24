---
key: 图片生成/图生图/批量图片+放大+wan2.2增加质感（v1.0）_1993322777830768641.json
name: 批量图片+放大+wan2.2增加质感（v1.0）_1993322777830768641
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/批量图片+放大+wan2.2增加质感（v1.0）_1993322777830768641.json
hash: 9d81fb81e4edd514
coverage: 0.96875
learned_at: 2026-10-23 12:54:26
nodes: [Anything Everywhere, VAELoader, LoraLoader, LoraLoader, UNETLoader, CLIPLoader, LoraLoader, LoraLoader, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, VAEDecode, KSampler, VAEEncode, ImageListToImageBatch, easy cleanGpuUsed, easy forLoopEnd, TTP_Image_Tile_Batch, easy imageBatchToImageList, easy cleanGpuUsed, UpscaleModelLoader, ImageUpscaleWithModel, RHExtractImage, easy forLoopStart, easy imageCount, RHBatchImages:, CompressImages, TTP_Tile_image_size, ImageScaleToTotalPixels, easy batchAnything, TTP_Image_Assy, RHUploadZip]
patterns: [lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "lora_name": "largear-e8.safetensors", "sampler_name": "er_sde", "scheduler": "beta", "seed": 622047961235011, "steps": 8, "strength_clip": 0.8000000000000002, "strength_model": 0.8000000000000002}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/批量图片+放大+wan2.2增加质感（v1.0）_1993322777830768641.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/批量图片+放大+wan2.2增加质感（v1.0）_1993322777830768641.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（32 个）：
- `Anything Everywhere`
- `VAELoader`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `VAEEncode` ★核心
- `ImageListToImageBatch`
- `easy cleanGpuUsed`
- `easy forLoopEnd`
- `TTP_Image_Tile_Batch`
- `easy imageBatchToImageList`
- `easy cleanGpuUsed`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `RHExtractImage`
- `easy forLoopStart`
- `easy imageCount`
- `RHBatchImages:`
- `CompressImages`
- `TTP_Tile_image_size`
- `ImageScaleToTotalPixels`
- `easy batchAnything`
- `TTP_Image_Assy`
- `RHUploadZip`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `largear-e8.safetensors`
- `strength_model` = `0.8000000000000002`
- `strength_clip` = `0.8000000000000002`
- `seed` = `622047961235011`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **97%**（31/32）

**有卡**：`VAELoader`、`LoraLoader`、`UNETLoader`、`CLIPLoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`VAEDecode`、`KSampler`、`VAEEncode`、`ImageListToImageBatch`、`easy cleanGpuUsed`、`easy forLoopEnd`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`RHExtractImage`、`easy forLoopStart`、`easy imageCount`、`RHBatchImages:`、`CompressImages`、`TTP_Tile_image_size`、`ImageScaleToTotalPixels`、`easy batchAnything`、`TTP_Image_Assy`、`RHUploadZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、VAEEncode、LoraLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
