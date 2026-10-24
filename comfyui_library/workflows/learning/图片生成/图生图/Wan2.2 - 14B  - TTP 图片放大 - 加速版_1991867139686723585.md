---
key: 图片生成/图生图/Wan2.2 - 14B  - TTP 图片放大 - 加速版_1991867139686723585.json
name: Wan2.2 - 14B  - TTP 图片放大 - 加速版_1991867139686723585
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2 - 14B  - TTP 图片放大 - 加速版_1991867139686723585.json
hash: c5c440e3e5bca298
coverage: 0.851852
learned_at: 2026-10-23 11:27:56
nodes: [CLIPTextEncode, CLIPTextEncode, VAEEncode, ImageListToImageBatch, VAEDecode, ModelSamplingSD3, CLIPLoader, Anything Everywhere3, VAELoader, LoraLoaderModelOnly, easy imageBatchToImageList, TTP_Image_Tile_Batch, TTP_Tile_image_size, ImageScaleToTotalPixels, UpscaleModelLoader, easy cleanGpuUsed, ImageUpscaleWithModel, UNETLoader, KSampler, PreviewImage, Int, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, TTP_Image_Assy, PreviewImage, SaveImage, Image Comparer (rgthree)]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "sampler_name": "heun", "scheduler": "beta", "seed": 1056932241996225, "steps": 10}
---

# 图片生成/图生图/Wan2.2 - 14B  - TTP 图片放大 - 加速版_1991867139686723585.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2 - 14B  - TTP 图片放大 - 加速版_1991867139686723585.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `ImageListToImageBatch`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `CLIPLoader`
- `Anything Everywhere3`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `easy imageBatchToImageList`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `ImageScaleToTotalPixels`
- `UpscaleModelLoader`
- `easy cleanGpuUsed`
- `ImageUpscaleWithModel`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `Int`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TTP_Image_Assy`
- `PreviewImage`
- `SaveImage`
- `Image Comparer (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1056932241996225`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **85%**（23/27）

**有卡**：`CLIPTextEncode`、`VAEEncode`、`ImageListToImageBatch`、`VAEDecode`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`easy imageBatchToImageList`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`ImageScaleToTotalPixels`、`UpscaleModelLoader`、`easy cleanGpuUsed`、`ImageUpscaleWithModel`、`UNETLoader`、`KSampler`、`Int`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`TTP_Image_Assy`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
