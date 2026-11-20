---
key: 平台全量/wan2.2图像高清放大 ttp版本_1950337532607291394.json
name: wan2.2图像高清放大 ttp版本_1950337532607291394
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2图像高清放大 ttp版本_1950337532607291394.json
hash: 980860a0400f8b3a
coverage: 0.88
learned_at: 2026-11-14 01:19:46
nodes: [ModelSamplingSD3, SaveImage, ImageUpscaleWithModel, easy cleanGpuUsed, ImageScaleToTotalPixels, TTP_Tile_image_size, TTP_Image_Tile_Batch, easy imageBatchToImageList, CLIPTextEncode, CLIPTextEncode, VAEEncode, KSampler, VAEDecode, PreviewImage, easy cleanGpuUsed, ImageListToImageBatch, TTP_Image_Assy, LoraLoaderModelOnly, PreviewImage, UNETLoader, CLIPLoader, VAELoader, UpscaleModelLoader, LoadImage, Image Comparer (rgthree)]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "sampler_name": "heun", "scheduler": "beta", "seed": 724015016118676, "steps": 10}
---

# 平台全量/wan2.2图像高清放大 ttp版本_1950337532607291394.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2图像高清放大 ttp版本_1950337532607291394.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `ModelSamplingSD3`
- `SaveImage`
- `ImageUpscaleWithModel`
- `easy cleanGpuUsed`
- `ImageScaleToTotalPixels`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `easy imageBatchToImageList`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `easy cleanGpuUsed`
- `ImageListToImageBatch`
- `TTP_Image_Assy`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `UpscaleModelLoader`
- `LoadImage`
- `Image Comparer (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `724015016118676`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **88%**（22/25）

**有卡**：`ModelSamplingSD3`、`SaveImage`、`ImageUpscaleWithModel`、`easy cleanGpuUsed`、`ImageScaleToTotalPixels`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`CLIPTextEncode`、`VAEEncode`、`KSampler`、`VAEDecode`、`ImageListToImageBatch`、`TTP_Image_Assy`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`UpscaleModelLoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader
