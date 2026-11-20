---
key: 平台全量/Wan2.2 - 14B - 加速版 - TTP 图片放大_1950200138313678850.json
name: Wan2.2 - 14B - 加速版 - TTP 图片放大_1950200138313678850
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 - 14B - 加速版 - TTP 图片放大_1950200138313678850.json
hash: f8ed32e12ab8435d
coverage: 0.88
learned_at: 2026-11-14 01:04:49
nodes: [CLIPTextEncode, UpscaleModelLoader, easy cleanGpuUsed, ImageScaleToTotalPixels, TTP_Image_Tile_Batch, easy imageBatchToImageList, TTP_Tile_image_size, VAELoader, CLIPLoader, LoraLoaderModelOnly, UNETLoader, PreviewImage, CLIPTextEncode, VAEEncode, KSampler, ImageListToImageBatch, VAEDecode, TTP_Image_Assy, Anything Everywhere3, Image Comparer (rgthree), SaveImage, LoadImage, ModelSamplingSD3, ImageUpscaleWithModel, ConstrainImage|pysssss]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "sampler_name": "heun", "scheduler": "beta", "seed": 96704037906048, "steps": 10}
---

# 平台全量/Wan2.2 - 14B - 加速版 - TTP 图片放大_1950200138313678850.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 - 14B - 加速版 - TTP 图片放大_1950200138313678850.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `CLIPTextEncode` ★核心
- `UpscaleModelLoader`
- `easy cleanGpuUsed`
- `ImageScaleToTotalPixels`
- `TTP_Image_Tile_Batch`
- `easy imageBatchToImageList`
- `TTP_Tile_image_size`
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `KSampler` ★核心
- `ImageListToImageBatch`
- `VAEDecode` ★核心
- `TTP_Image_Assy`
- `Anything Everywhere3`
- `Image Comparer (rgthree)`
- `SaveImage`
- `LoadImage`
- `ModelSamplingSD3`
- `ImageUpscaleWithModel`
- `ConstrainImage|pysssss`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `96704037906048`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **88%**（22/25）

**有卡**：`CLIPTextEncode`、`UpscaleModelLoader`、`easy cleanGpuUsed`、`ImageScaleToTotalPixels`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`TTP_Tile_image_size`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`VAEEncode`、`KSampler`、`ImageListToImageBatch`、`VAEDecode`、`TTP_Image_Assy`、`SaveImage`、`LoadImage`、`ModelSamplingSD3`、`ImageUpscaleWithModel`、`ConstrainImage|pysssss`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader
