---
key: 图片生成/文生图/Wan2.2 TTP高阶放大（全网ID ：楚门的AI世界）_1950100432455647233.json
name: Wan2.2 TTP高阶放大（全网ID ：楚门的AI世界）_1950100432455647233
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2 TTP高阶放大（全网ID ：楚门的AI世界）_1950100432455647233.json
hash: bf277d07a2e30465
coverage: 0.846154
learned_at: 2026-10-15 22:27:35
nodes: [TTP_Image_Tile_Batch, PreviewImage, CLIPTextEncode, CLIPTextEncode, easy imageBatchToImageList, PreviewImage, ImageListToImageBatch, VAEEncode, VAEDecode, PreviewImage, UNETLoader, KSampler, CLIPLoader, VAELoader, LoraLoaderModelOnly, ModelSamplingSD3, TTP_Tile_image_size, ImageScaleToTotalPixels, ImageUpscaleWithModel, UpscaleModelLoader, easy cleanGpuUsed, LoadImage, easy cleanGpuUsed, Reroute, SaveImage, TTP_Image_Assy]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "sampler_name": "heun", "scheduler": "beta", "seed": 254894341020511, "steps": 10}
---

# 图片生成/文生图/Wan2.2 TTP高阶放大（全网ID ：楚门的AI世界）_1950100432455647233.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2 TTP高阶放大（全网ID ：楚门的AI世界）_1950100432455647233.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `TTP_Image_Tile_Batch`
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
- `LoadImage`
- `easy cleanGpuUsed`
- `Reroute`
- `SaveImage`
- `TTP_Image_Assy`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `254894341020511`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **85%**（22/26）

**有卡**：`TTP_Image_Tile_Batch`、`CLIPTextEncode`、`easy imageBatchToImageList`、`ImageListToImageBatch`、`VAEEncode`、`VAEDecode`、`UNETLoader`、`KSampler`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`TTP_Tile_image_size`、`ImageScaleToTotalPixels`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`easy cleanGpuUsed`、`LoadImage`、`SaveImage`、`TTP_Image_Assy`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
