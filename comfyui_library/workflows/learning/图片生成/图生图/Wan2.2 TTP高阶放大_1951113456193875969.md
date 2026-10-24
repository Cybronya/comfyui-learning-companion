---
key: 图片生成/图生图/Wan2.2 TTP高阶放大_1951113456193875969.json
name: Wan2.2 TTP高阶放大_1951113456193875969
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2 TTP高阶放大_1951113456193875969.json
hash: 7615a71232635c23
coverage: 0.846154
learned_at: 2026-10-23 11:28:00
nodes: [PreviewImage, CLIPTextEncode, CLIPTextEncode, easy imageBatchToImageList, PreviewImage, ImageListToImageBatch, VAEEncode, VAEDecode, PreviewImage, UNETLoader, KSampler, CLIPLoader, VAELoader, LoraLoaderModelOnly, ModelSamplingSD3, TTP_Tile_image_size, ImageScaleToTotalPixels, ImageUpscaleWithModel, UpscaleModelLoader, easy cleanGpuUsed, easy cleanGpuUsed, Reroute, SaveImage, TTP_Image_Assy, LoadImage, TTP_Image_Tile_Batch]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "sampler_name": "heun", "scheduler": "beta", "seed": 253116858930521, "steps": 10}
---

# 图片生成/图生图/Wan2.2 TTP高阶放大_1951113456193875969.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2 TTP高阶放大_1951113456193875969.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy imageBatchToImageList`
- `PreviewImage`
- `ImageListToImageBatch`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `TTP_Tile_image_size`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `Reroute`
- `SaveImage`
- `TTP_Image_Assy`
- `LoadImage`
- `TTP_Image_Tile_Batch`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `253116858930521`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **85%**（22/26）

**有卡**：`CLIPTextEncode`、`easy imageBatchToImageList`、`ImageListToImageBatch`、`VAEEncode`、`VAEDecode`、`UNETLoader`、`KSampler`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`TTP_Tile_image_size`、`ImageScaleToTotalPixels`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`easy cleanGpuUsed`、`SaveImage`、`TTP_Image_Assy`、`LoadImage`、`TTP_Image_Tile_Batch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
