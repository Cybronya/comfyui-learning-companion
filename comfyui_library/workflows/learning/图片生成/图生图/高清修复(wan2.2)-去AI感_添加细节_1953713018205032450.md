---
key: 图片生成/图生图/高清修复(wan2.2)-去AI感_添加细节_1953713018205032450.json
name: 高清修复(wan2.2)-去AI感_添加细节_1953713018205032450
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/高清修复(wan2.2)-去AI感_添加细节_1953713018205032450.json
hash: 6511155ad13eba8c
coverage: 0.909091
learned_at: 2026-10-23 13:33:57
nodes: [LayerUtility: ImageScaleByAspectRatio V2, ImageUpscaleWithModel, UpscaleModelLoader, TTP_Tile_image_size, UNETLoader, VAELoader, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, InjectLatentNoise+, VAEEncode, easy cleanGpuUsed, Image Comparer (rgthree), SaveImage, CLIPTextEncode, ImageFromBatch, TTP_Image_Tile_Batch, Florence2ModelLoader, Florence2Run, VAEDecode, easy imageBatchToImageList, TTP_Image_Assy, CLIPTextEncode, PreviewImage, ShowText|pysssss, ImageListToImageBatch, KSampler, LoadImage, LoadImage, FluxGuidance, ImageScaleToTotalPixels]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.05000000000000001, "sampler_name": "euler", "scheduler": "simple", "seed": 750774110868221, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/高清修复(wan2.2)-去AI感_添加细节_1953713018205032450.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/高清修复(wan2.2)-去AI感_添加细节_1953713018205032450.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `TTP_Tile_image_size`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `InjectLatentNoise+`
- `VAEEncode` ★核心
- `easy cleanGpuUsed`
- `Image Comparer (rgthree)`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `ImageFromBatch`
- `TTP_Image_Tile_Batch`
- `Florence2ModelLoader`
- `Florence2Run`
- `VAEDecode` ★核心
- `easy imageBatchToImageList`
- `TTP_Image_Assy`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `ShowText|pysssss`
- `ImageListToImageBatch`
- `KSampler` ★核心
- `LoadImage`
- `LoadImage`
- `FluxGuidance`
- `ImageScaleToTotalPixels`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `750774110868221`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.05000000000000001`

## 知识

覆盖率 **91%**（30/33）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`TTP_Tile_image_size`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`InjectLatentNoise+`、`VAEEncode`、`easy cleanGpuUsed`、`SaveImage`、`CLIPTextEncode`、`ImageFromBatch`、`TTP_Image_Tile_Batch`、`Florence2ModelLoader`、`Florence2Run`、`VAEDecode`、`easy imageBatchToImageList`、`TTP_Image_Assy`、`ImageListToImageBatch`、`KSampler`、`LoadImage`、`FluxGuidance`、`ImageScaleToTotalPixels`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
