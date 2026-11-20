---
key: 平台全量/图片高清修复wan2.2_1986341262846558209.json
name: 图片高清修复wan2.2_1986341262846558209
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/图片高清修复wan2.2_1986341262846558209.json
hash: 79bae86b5861a88b
coverage: 0.888889
learned_at: 2026-11-14 01:55:53
nodes: [UNETLoader, TTP_Tile_image_size, TTP_Image_Tile_Batch, CLIPLoader, LoraLoaderModelOnly, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList, VAEEncode, UpscaleModelLoader, ImageScaleToTotalPixels, VAEDecode, ImageListToImageBatch, LayerUtility: PurgeVRAM, PreviewImage, PreviewImage, PreviewImage, TTP_Image_Assy, LayerUtility: PurgeVRAM, ImageUpscaleWithModel, LoadImage, KSampler, SaveImagePlus, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.010000000000000002, "sampler_name": "heun", "scheduler": "beta", "seed": 1087863744310001, "steps": 10}
---

# 平台全量/图片高清修复wan2.2_1986341262846558209.json

> 来源文件 `comfyui_library/workflows/平台全量/图片高清修复wan2.2_1986341262846558209.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `UNETLoader` ★核心
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`
- `VAEEncode` ★核心
- `UpscaleModelLoader`
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `ImageListToImageBatch`
- `LayerUtility: PurgeVRAM`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `TTP_Image_Assy`
- `LayerUtility: PurgeVRAM`
- `ImageUpscaleWithModel`
- `LoadImage`
- `KSampler` ★核心
- `SaveImagePlus`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1087863744310001`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.010000000000000002`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`UNETLoader`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`CLIPLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`CLIPTextEncode`、`VAELoader`、`easy cleanGpuUsed`、`easy imageBatchToImageList`、`VAEEncode`、`UpscaleModelLoader`、`ImageScaleToTotalPixels`、`VAEDecode`、`ImageListToImageBatch`、`LayerUtility: PurgeVRAM`、`TTP_Image_Assy`、`ImageUpscaleWithModel`、`LoadImage`、`KSampler`、`SaveImagePlus`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader
