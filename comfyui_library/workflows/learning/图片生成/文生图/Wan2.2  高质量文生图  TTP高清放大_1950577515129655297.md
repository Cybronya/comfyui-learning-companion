---
key: 图片生成/文生图/Wan2.2  高质量文生图  TTP高清放大_1950577515129655297.json
name: Wan2.2  高质量文生图  TTP高清放大_1950577515129655297
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2  高质量文生图  TTP高清放大_1950577515129655297.json
hash: 855095a235584f6c
coverage: 0.974359
learned_at: 2026-10-15 22:27:34
nodes: [LoraLoaderModelOnly, CLIPTextEncode, UNETLoader, ModelSamplingSD3, UNETLoader, ModelSamplingSD3, CLIPLoader, VAELoader, easy cleanGpuUsed, VAEDecode, easy setNode, CLIPTextEncode, ImageListToImageBatch, easy cleanGpuUsed, SaveImage, EmptyHunyuanLatentVideo, KSamplerAdvanced, CLIPTextEncode, CLIPTextEncode, UNETLoader, CLIPLoader, VAELoader, easy cleanGpuUsed, ImageScaleToTotalPixels, UpscaleModelLoader, easy getNode, TTP_Image_Tile_Batch, TTP_Image_Assy, TTP_Tile_image_size, ImageUpscaleWithModel, SaveImage, Note, KSamplerAdvanced, VAEEncode, easy imageBatchToImageList, ModelSamplingSD3, KSampler, easy cleanGpuUsed, VAEDecode]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "sampler_name": "heun", "scheduler": "beta", "seed": 969501298874124, "steps": 10}
---

# 图片生成/文生图/Wan2.2  高质量文生图  TTP高清放大_1950577515129655297.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2  高质量文生图  TTP高清放大_1950577515129655297.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `easy setNode`
- `CLIPTextEncode` ★核心
- `ImageListToImageBatch`
- `easy cleanGpuUsed`
- `SaveImage`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `easy cleanGpuUsed`
- `ImageScaleToTotalPixels`
- `UpscaleModelLoader`
- `easy getNode`
- `TTP_Image_Tile_Batch`
- `TTP_Image_Assy`
- `TTP_Tile_image_size`
- `ImageUpscaleWithModel`
- `SaveImage`
- `Note`
- `KSamplerAdvanced` ★核心
- `VAEEncode` ★核心
- `easy imageBatchToImageList`
- `ModelSamplingSD3`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心

## 关键参数

- `seed` = `969501298874124`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`LoraLoaderModelOnly`、`CLIPTextEncode`、`UNETLoader`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`easy cleanGpuUsed`、`VAEDecode`、`easy setNode`、`ImageListToImageBatch`、`SaveImage`、`EmptyHunyuanLatentVideo`、`KSamplerAdvanced`、`ImageScaleToTotalPixels`、`UpscaleModelLoader`、`easy getNode`、`TTP_Image_Tile_Batch`、`TTP_Image_Assy`、`TTP_Tile_image_size`、`ImageUpscaleWithModel`、`VAEEncode`、`easy imageBatchToImageList`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced
