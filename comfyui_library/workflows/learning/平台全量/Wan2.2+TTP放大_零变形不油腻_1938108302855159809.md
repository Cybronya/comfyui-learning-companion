---
key: 平台全量/Wan2.2+TTP放大_零变形不油腻_1938108302855159809.json
name: Wan2.2+TTP放大_零变形不油腻_1938108302855159809
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2+TTP放大_零变形不油腻_1938108302855159809.json
hash: 69e0b442345f8958
coverage: 0.774194
learned_at: 2026-11-14 01:05:52
nodes: [VAELoader, CLIPLoader, TTP_Image_Tile_Batch, VAEDecode, easy imageBatchToImageList, ImageScaleToTotalPixels, easy cleanGpuUsed, TTP_Tile_image_size, VAEEncode, easy cleanGpuUsed, SetNode, ImageListToImageBatch, GetNode, SetNode, TTP_Image_Assy, PreviewImage, GetNode, ImageUpscaleWithModel, UpscaleModelLoader, SaveImage, Image Comparer (rgthree), UNETLoader, PathchSageAttentionKJ, ModelSamplingSD3, Anything Everywhere3, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, CLIPTextEncode, KSampler, CLIPTextEncode]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.06000000000000001, "sampler_name": "euler", "scheduler": "beta", "seed": 1040177052062545, "steps": 10}
---

# 平台全量/Wan2.2+TTP放大_零变形不油腻_1938108302855159809.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2+TTP放大_零变形不油腻_1938108302855159809.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `VAELoader`
- `CLIPLoader`
- `TTP_Image_Tile_Batch`
- `VAEDecode` ★核心
- `easy imageBatchToImageList`
- `ImageScaleToTotalPixels`
- `easy cleanGpuUsed`
- `TTP_Tile_image_size`
- `VAEEncode` ★核心
- `easy cleanGpuUsed`
- `SetNode`
- `ImageListToImageBatch`
- `GetNode`
- `SetNode`
- `TTP_Image_Assy`
- `PreviewImage`
- `GetNode`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `SaveImage`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `Anything Everywhere3`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1040177052062545`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `0.06000000000000001`

## 知识

覆盖率 **77%**（24/31）

**有卡**：`VAELoader`、`CLIPLoader`、`TTP_Image_Tile_Batch`、`VAEDecode`、`easy imageBatchToImageList`、`ImageScaleToTotalPixels`、`easy cleanGpuUsed`、`TTP_Tile_image_size`、`VAEEncode`、`ImageListToImageBatch`、`TTP_Image_Assy`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`SaveImage`、`UNETLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader
