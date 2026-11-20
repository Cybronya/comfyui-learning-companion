---
key: 平台全量/【Wan2.2图像放大】 人物模特超清8K真实纹理_2046533363250503682.json
name: 【Wan2.2图像放大】 人物模特超清8K真实纹理_2046533363250503682
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/【Wan2.2图像放大】 人物模特超清8K真实纹理_2046533363250503682.json
hash: aa0474e665f9dc52
coverage: 0.875
learned_at: 2026-11-14 01:22:23
nodes: [CLIPLoader, CLIPTextEncode, VAEEncode, VAELoader, CLIPTextEncode, Image Comparer (rgthree), TTP_Image_Assy, VAEDecode, ImageListToImageBatch, easy imageBatchToImageList, easy cleanGpuUsed, ImageUpscaleWithModel, easy cleanGpuUsed, SaveImage, KSampler, TTP_Image_Tile_Batch, TTP_Tile_image_size, ImageScaleToTotalPixels, UpscaleModelLoader, ModelSamplingSD3, UNETLoader, LoadImage, PrimitiveFloat, PreviewImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.1, "sampler_name": "heun", "scheduler": "beta", "seed": 438521785130370, "steps": 10}
---

# 平台全量/【Wan2.2图像放大】 人物模特超清8K真实纹理_2046533363250503682.json

> 来源文件 `comfyui_library/workflows/平台全量/【Wan2.2图像放大】 人物模特超清8K真实纹理_2046533363250503682.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `TTP_Image_Assy`
- `VAEDecode` ★核心
- `ImageListToImageBatch`
- `easy imageBatchToImageList`
- `easy cleanGpuUsed`
- `ImageUpscaleWithModel`
- `easy cleanGpuUsed`
- `SaveImage`
- `KSampler` ★核心
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `ImageScaleToTotalPixels`
- `UpscaleModelLoader`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `LoadImage`
- `PrimitiveFloat`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `438521785130370`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.1`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`VAEEncode`、`VAELoader`、`TTP_Image_Assy`、`VAEDecode`、`ImageListToImageBatch`、`easy imageBatchToImageList`、`easy cleanGpuUsed`、`ImageUpscaleWithModel`、`SaveImage`、`KSampler`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`ImageScaleToTotalPixels`、`UpscaleModelLoader`、`ModelSamplingSD3`、`UNETLoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、VAEEncode
