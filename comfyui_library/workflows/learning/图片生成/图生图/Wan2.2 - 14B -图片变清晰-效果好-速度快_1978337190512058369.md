---
key: 图片生成/图生图/Wan2.2 - 14B -图片变清晰-效果好-速度快_1978337190512058369.json
name: Wan2.2 - 14B -图片变清晰-效果好-速度快_1978337190512058369
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2 - 14B -图片变清晰-效果好-速度快_1978337190512058369.json
hash: 6b3174a42e228683
coverage: 0.888889
learned_at: 2026-10-23 11:27:57
nodes: [CLIPTextEncode, easy cleanGpuUsed, ImageScaleToTotalPixels, TTP_Image_Tile_Batch, easy imageBatchToImageList, TTP_Tile_image_size, VAELoader, CLIPLoader, LoraLoaderModelOnly, UNETLoader, PreviewImage, KSampler, ImageListToImageBatch, VAEDecode, TTP_Image_Assy, Anything Everywhere3, ModelSamplingSD3, ImageUpscaleWithModel, ConstrainImage|pysssss, CLIPTextEncode, VAEEncode, UpscaleModelLoader, UpscaleModelLoader, UpscaleModelLoader, Image Comparer (rgthree), LoadImage, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "sampler_name": "heun", "scheduler": "beta", "seed": 868423794638694, "steps": 10}
---

# 图片生成/图生图/Wan2.2 - 14B -图片变清晰-效果好-速度快_1978337190512058369.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2 - 14B -图片变清晰-效果好-速度快_1978337190512058369.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `CLIPTextEncode` ★核心
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
- `KSampler` ★核心
- `ImageListToImageBatch`
- `VAEDecode` ★核心
- `TTP_Image_Assy`
- `Anything Everywhere3`
- `ModelSamplingSD3`
- `ImageUpscaleWithModel`
- `ConstrainImage|pysssss`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `UpscaleModelLoader`
- `UpscaleModelLoader`
- `UpscaleModelLoader`
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `868423794638694`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`CLIPTextEncode`、`easy cleanGpuUsed`、`ImageScaleToTotalPixels`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`TTP_Tile_image_size`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`KSampler`、`ImageListToImageBatch`、`VAEDecode`、`TTP_Image_Assy`、`ModelSamplingSD3`、`ImageUpscaleWithModel`、`ConstrainImage|pysssss`、`VAEEncode`、`UpscaleModelLoader`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
