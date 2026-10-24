---
key: 图片生成/图生图/👾怪獸-wan2.2高清修复-去AI感_添加细节👾_2014548216443834370.json
name: 👾怪獸-wan2.2高清修复-去AI感_添加细节👾_2014548216443834370
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/👾怪獸-wan2.2高清修复-去AI感_添加细节👾_2014548216443834370.json
hash: 4f8d27ab7df39268
coverage: 0.925926
learned_at: 2026-10-23 13:39:32
nodes: [LayerUtility: ImageScaleByAspectRatio V2, TTP_Image_Tile_Batch, ImageUpscaleWithModel, ImageScaleToTotalPixels, TTP_Tile_image_size, UpscaleModelLoader, TTP_Image_Assy, UNETLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, FluxGuidance, PathchSageAttentionKJ, ModelSamplingSD3, VAEEncode, easy cleanGpuUsed, VAEDecode, ImageListToImageBatch, CLIPLoader, LoraLoaderModelOnly, SaveImage, Image Comparer (rgthree), LoadImage, easy imageBatchToImageList, PreviewImage, KSampler]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.020000000000000004, "sampler_name": "euler", "scheduler": "simple", "seed": 631909291665029, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/👾怪獸-wan2.2高清修复-去AI感_添加细节👾_2014548216443834370.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/👾怪獸-wan2.2高清修复-去AI感_添加细节👾_2014548216443834370.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TTP_Image_Tile_Batch`
- `ImageUpscaleWithModel`
- `ImageScaleToTotalPixels`
- `TTP_Tile_image_size`
- `UpscaleModelLoader`
- `TTP_Image_Assy`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `FluxGuidance`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `VAEEncode` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `ImageListToImageBatch`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `easy imageBatchToImageList`
- `PreviewImage`
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `631909291665029`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.020000000000000004`

## 知识

覆盖率 **93%**（25/27）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`TTP_Image_Tile_Batch`、`ImageUpscaleWithModel`、`ImageScaleToTotalPixels`、`TTP_Tile_image_size`、`UpscaleModelLoader`、`TTP_Image_Assy`、`UNETLoader`、`VAELoader`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`FluxGuidance`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VAEEncode`、`easy cleanGpuUsed`、`VAEDecode`、`ImageListToImageBatch`、`CLIPLoader`、`SaveImage`、`LoadImage`、`easy imageBatchToImageList`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
