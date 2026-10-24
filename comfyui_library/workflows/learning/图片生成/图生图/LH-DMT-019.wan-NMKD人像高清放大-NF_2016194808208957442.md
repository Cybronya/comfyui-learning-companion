---
key: 图片生成/图生图/LH-DMT-019.wan-NMKD人像高清放大-NF_2016194808208957442.json
name: LH-DMT-019.wan-NMKD人像高清放大-NF_2016194808208957442
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/LH-DMT-019.wan-NMKD人像高清放大-NF_2016194808208957442.json
hash: 85bc92b945ea5bd0
coverage: 0.90625
learned_at: 2026-10-23 11:08:38
nodes: [ModelSamplingSD3, TTP_Image_Tile_Batch, UpscaleModelLoader, easy imageBatchToImageList, KSampler, CLIPTextEncode, FluxGuidance, InjectLatentNoise+, ImageUpscaleWithModel, ImageListToImageBatch, VAEDecode, Florence2Run, SaveImage, Image Comparer (rgthree), TTP_Tile_image_size, ImageScaleToTotalPixels, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, TTP_Image_Assy, ShowText|pysssss, Florence2ModelLoader, LoadImage, CLIPLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, easy cleanGpuUsed, ImageFromBatch, LoraLoaderModelOnly, VAELoader, VAEEncode, CLIPTextEncode, UNETLoader]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.05000000000000001, "sampler_name": "euler", "scheduler": "simple", "seed": 593823531718307, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/LH-DMT-019.wan-NMKD人像高清放大-NF_2016194808208957442.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/LH-DMT-019.wan-NMKD人像高清放大-NF_2016194808208957442.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `ModelSamplingSD3`
- `TTP_Image_Tile_Batch`
- `UpscaleModelLoader`
- `easy imageBatchToImageList`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `InjectLatentNoise+`
- `ImageUpscaleWithModel`
- `ImageListToImageBatch`
- `VAEDecode` ★核心
- `Florence2Run`
- `SaveImage`
- `Image Comparer (rgthree)`
- `TTP_Tile_image_size`
- `ImageScaleToTotalPixels`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `TTP_Image_Assy`
- `ShowText|pysssss`
- `Florence2ModelLoader`
- `LoadImage`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `easy cleanGpuUsed`
- `ImageFromBatch`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `593823531718307`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.05000000000000001`

## 知识

覆盖率 **91%**（29/32）

**有卡**：`ModelSamplingSD3`、`TTP_Image_Tile_Batch`、`UpscaleModelLoader`、`easy imageBatchToImageList`、`KSampler`、`CLIPTextEncode`、`FluxGuidance`、`InjectLatentNoise+`、`ImageUpscaleWithModel`、`ImageListToImageBatch`、`VAEDecode`、`Florence2Run`、`SaveImage`、`TTP_Tile_image_size`、`ImageScaleToTotalPixels`、`LayerUtility: ImageScaleByAspectRatio V2`、`TTP_Image_Assy`、`Florence2ModelLoader`、`LoadImage`、`CLIPLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`easy cleanGpuUsed`、`ImageFromBatch`、`VAELoader`、`VAEEncode`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
