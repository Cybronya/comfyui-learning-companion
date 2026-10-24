---
key: 图片生成/图生图/Wan2.2TTP图像细节增强放大_1951193407014248449.json
name: Wan2.2TTP图像细节增强放大_1951193407014248449
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2TTP图像细节增强放大_1951193407014248449.json
hash: c9e5bfc74f5de521
coverage: 0.827586
learned_at: 2026-10-23 11:28:10
nodes: [easy imageBatchToImageList, PreviewImage, ModelSamplingSD3, VAEEncode, easy cleanGpuUsed, VAEDecode, TTP_Tile_image_size, ImageListToImageBatch, easy cleanGpuUsed, Reroute, PreviewImage, PreviewImage, TTP_Image_Tile_Batch, TTP_Image_Assy, CLIPTextEncode, ImageUpscaleWithModel, UpscaleModelLoader, ImageScaleToTotalPixels, easy cleanGpuUsed, KSampler, LoraLoaderModelOnly, UNETLoader, CLIPLoader, LoadImage, ImageResizeKJv2, SaveImage, VAELoader, CLIPTextEncode, Image Comparer (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "sampler_name": "heun", "scheduler": "beta", "seed": 664681699964871, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Wan2.2TTP图像细节增强放大_1951193407014248449.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2TTP图像细节增强放大_1951193407014248449.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `easy imageBatchToImageList`
- `PreviewImage`
- `ModelSamplingSD3`
- `VAEEncode` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `TTP_Tile_image_size`
- `ImageListToImageBatch`
- `easy cleanGpuUsed`
- `Reroute`
- `PreviewImage`
- `PreviewImage`
- `TTP_Image_Tile_Batch`
- `TTP_Image_Assy`
- `CLIPTextEncode` ★核心
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `ImageScaleToTotalPixels`
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoadImage`
- `ImageResizeKJv2`
- `SaveImage`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `664681699964871`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **83%**（24/29）

**有卡**：`easy imageBatchToImageList`、`ModelSamplingSD3`、`VAEEncode`、`easy cleanGpuUsed`、`VAEDecode`、`TTP_Tile_image_size`、`ImageListToImageBatch`、`TTP_Image_Tile_Batch`、`TTP_Image_Assy`、`CLIPTextEncode`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`ImageScaleToTotalPixels`、`KSampler`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`LoadImage`、`ImageResizeKJv2`、`SaveImage`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
