---
key: 数字人/数字人/高清修复(wan2.2)-去AI感_添加细节_2103481336999800834.json
name: 高清修复(wan2.2)-去AI感_添加细节_2103481336999800834
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/高清修复(wan2.2)-去AI感_添加细节_2103481336999800834.json
hash: a64d8c9261e8f960
coverage: 0.90625
learned_at: 2026-10-19 00:41:13
nodes: [VAELoader, CLIPLoader, TTP_Image_Tile_Batch, CLIPTextEncode, ImageFromBatch, PathchSageAttentionKJ, UpscaleModelLoader, ImageUpscaleWithModel, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, TTP_Image_Assy, ShowText|pysssss, LoraLoaderModelOnly, ModelSamplingSD3, ImageListToImageBatch, VAEDecode, LoraLoaderModelOnly, FluxGuidance, UNETLoader, TTP_Tile_image_size, ImageScaleToTotalPixels, Florence2Run, Florence2ModelLoader, easy imageBatchToImageList, PreviewImage, InjectLatentNoise+, easy cleanGpuUsed, CLIPTextEncode, LoadImage, KSampler, Image Comparer (rgthree), SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.06000000000000001, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 815529874438380, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/高清修复(wan2.2)-去AI感_添加细节_2103481336999800834.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/高清修复(wan2.2)-去AI感_添加细节_2103481336999800834.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `VAELoader`
- `CLIPLoader`
- `TTP_Image_Tile_Batch`
- `CLIPTextEncode` ★核心
- `ImageFromBatch`
- `PathchSageAttentionKJ`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEEncode` ★核心
- `TTP_Image_Assy`
- `ShowText|pysssss`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ImageListToImageBatch`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `FluxGuidance`
- `UNETLoader` ★核心
- `TTP_Tile_image_size`
- `ImageScaleToTotalPixels`
- `Florence2Run`
- `Florence2ModelLoader`
- `easy imageBatchToImageList`
- `PreviewImage`
- `InjectLatentNoise+`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `815529874438380`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.06000000000000001`

## 知识

覆盖率 **91%**（29/32）

**有卡**：`VAELoader`、`CLIPLoader`、`TTP_Image_Tile_Batch`、`CLIPTextEncode`、`ImageFromBatch`、`PathchSageAttentionKJ`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEEncode`、`TTP_Image_Assy`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`ImageListToImageBatch`、`VAEDecode`、`FluxGuidance`、`UNETLoader`、`TTP_Tile_image_size`、`ImageScaleToTotalPixels`、`Florence2Run`、`Florence2ModelLoader`、`easy imageBatchToImageList`、`InjectLatentNoise+`、`easy cleanGpuUsed`、`LoadImage`、`KSampler`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
