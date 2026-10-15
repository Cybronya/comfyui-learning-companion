---
key: 图片生成/文生图/Wan2.2质量文生图+TTP高阶放大（全网ID ：楚门的AI世界）_1950100592413818881.json
name: Wan2.2质量文生图+TTP高阶放大（全网ID ：楚门的AI世界）_1950100592413818881
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2质量文生图+TTP高阶放大（全网ID ：楚门的AI世界）_1950100592413818881.json
hash: 29aa3a6b6681b011
coverage: 0.886364
learned_at: 2026-10-15 22:27:37
nodes: [SaveAnimatedWEBP, CLIPTextEncode, LoraLoaderModelOnly, UNETLoader, UNETLoader, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, CLIPLoader, VAELoader, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, easy imageBatchToImageList, PreviewImage, UNETLoader, ModelSamplingSD3, LoraLoaderModelOnly, CLIPLoader, VAELoader, VAEEncode, SaveImage, VAEDecode, easy cleanGpuUsed, easy cleanGpuUsed, VAEDecode, CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, TTP_Tile_image_size, UpscaleModelLoader, ImageScaleToTotalPixels, easy cleanGpuUsed, ImageListToImageBatch, easy cleanGpuUsed, TTP_Image_Assy, Reroute, SaveImage, KSampler, CLIPTextEncode, Image Comparer (rgthree), ImageUpscaleWithModel, PreviewImage, PreviewImage, TTP_Image_Tile_Batch]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "sampler_name": "heun", "scheduler": "beta", "seed": 942487783663977, "steps": 10}
---

# 图片生成/文生图/Wan2.2质量文生图+TTP高阶放大（全网ID ：楚门的AI世界）_1950100592413818881.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2质量文生图+TTP高阶放大（全网ID ：楚门的AI世界）_1950100592413818881.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `SaveAnimatedWEBP`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `easy imageBatchToImageList`
- `PreviewImage`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEEncode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `TTP_Tile_image_size`
- `UpscaleModelLoader`
- `ImageScaleToTotalPixels`
- `easy cleanGpuUsed`
- `ImageListToImageBatch`
- `easy cleanGpuUsed`
- `TTP_Image_Assy`
- `Reroute`
- `SaveImage`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `PreviewImage`
- `PreviewImage`
- `TTP_Image_Tile_Batch`

## 关键参数

- `seed` = `942487783663977`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **89%**（39/44）

**有卡**：`SaveAnimatedWEBP`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`UNETLoader`、`EmptyHunyuanLatentVideo`、`CLIPLoader`、`VAELoader`、`KSamplerAdvanced`、`easy imageBatchToImageList`、`ModelSamplingSD3`、`VAEEncode`、`SaveImage`、`VAEDecode`、`easy cleanGpuUsed`、`TTP_Tile_image_size`、`UpscaleModelLoader`、`ImageScaleToTotalPixels`、`ImageListToImageBatch`、`TTP_Image_Assy`、`KSampler`、`ImageUpscaleWithModel`、`TTP_Image_Tile_Batch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced
