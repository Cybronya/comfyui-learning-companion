---
key: 图片生成/图生图/wan2.2高清放大修复高质量,4K_1983123878350352386.json
name: wan2.2高清放大修复高质量,4K_1983123878350352386
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.2高清放大修复高质量,4K_1983123878350352386.json
hash: 1e9131130e478e67
coverage: 0.88
learned_at: 2026-10-23 11:46:12
nodes: [TTP_Tile_image_size, TTP_Image_Tile_Batch, CLIPLoader, VAELoader, easy cleanGpuUsed, VAEEncode, ImageScaleToTotalPixels, ImageListToImageBatch, PreviewImage, PreviewImage, TTP_Image_Assy, ImageUpscaleWithModel, SaveImage, SaveImagePlus, VAEDecode, PreviewImage, UpscaleModelLoader, UNETLoader, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, easy imageBatchToImageList, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "sampler_name": "heun", "scheduler": "beta", "seed": 94587386730613, "steps": 10}
---

# 图片生成/图生图/wan2.2高清放大修复高质量,4K_1983123878350352386.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.2高清放大修复高质量,4K_1983123878350352386.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `CLIPLoader`
- `VAELoader`
- `easy cleanGpuUsed`
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `ImageListToImageBatch`
- `PreviewImage`
- `PreviewImage`
- `TTP_Image_Assy`
- `ImageUpscaleWithModel`
- `SaveImage`
- `SaveImagePlus`
- `VAEDecode` ★核心
- `PreviewImage`
- `UpscaleModelLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `easy imageBatchToImageList`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `94587386730613`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **88%**（22/25）

**有卡**：`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`CLIPLoader`、`VAELoader`、`easy cleanGpuUsed`、`VAEEncode`、`ImageScaleToTotalPixels`、`ImageListToImageBatch`、`TTP_Image_Assy`、`ImageUpscaleWithModel`、`SaveImage`、`SaveImagePlus`、`VAEDecode`、`UpscaleModelLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`ModelSamplingSD3`、`easy imageBatchToImageList`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
