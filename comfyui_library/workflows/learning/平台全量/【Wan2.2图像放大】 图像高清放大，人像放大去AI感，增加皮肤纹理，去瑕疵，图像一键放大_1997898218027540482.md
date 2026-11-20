---
key: 平台全量/【Wan2.2图像放大】 图像高清放大，人像放大去AI感，增加皮肤纹理，去瑕疵，图像一键放大_1997898218027540482.json
name: 【Wan2.2图像放大】 图像高清放大，人像放大去AI感，增加皮肤纹理，去瑕疵，图像一键放大_1997898218027540482
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/【Wan2.2图像放大】 图像高清放大，人像放大去AI感，增加皮肤纹理，去瑕疵，图像一键放大_1997898218027540482.json
hash: 45929615a15830f6
coverage: 0.916667
learned_at: 2026-11-14 01:22:24
nodes: [ModelSamplingSD3, CLIPTextEncode, ImageUpscaleWithModel, easy imageBatchToImageList, VAEEncode, ImageScaleToTotalPixels, easy cleanGpuUsed, CLIPTextEncode, KSampler, ImageListToImageBatch, VAEDecode, TTP_Image_Tile_Batch, easy cleanGpuUsed, TTP_Tile_image_size, TTP_Image_Assy, SaveImage, Image Comparer (rgthree), UpscaleModelLoader, VAELoader, UNETLoader, CLIPLoader, PreviewImage, LoadImage, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.1, "sampler_name": "heun", "scheduler": "beta", "seed": 63174151678913, "steps": 10}
---

# 平台全量/【Wan2.2图像放大】 图像高清放大，人像放大去AI感，增加皮肤纹理，去瑕疵，图像一键放大_1997898218027540482.json

> 来源文件 `comfyui_library/workflows/平台全量/【Wan2.2图像放大】 图像高清放大，人像放大去AI感，增加皮肤纹理，去瑕疵，图像一键放大_1997898218027540482.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `ImageUpscaleWithModel`
- `easy imageBatchToImageList`
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `ImageListToImageBatch`
- `VAEDecode` ★核心
- `TTP_Image_Tile_Batch`
- `easy cleanGpuUsed`
- `TTP_Tile_image_size`
- `TTP_Image_Assy`
- `SaveImage`
- `Image Comparer (rgthree)`
- `UpscaleModelLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `PreviewImage`
- `LoadImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `63174151678913`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.1`

## 知识

覆盖率 **92%**（22/24）

**有卡**：`ModelSamplingSD3`、`CLIPTextEncode`、`ImageUpscaleWithModel`、`easy imageBatchToImageList`、`VAEEncode`、`ImageScaleToTotalPixels`、`easy cleanGpuUsed`、`KSampler`、`ImageListToImageBatch`、`VAEDecode`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`TTP_Image_Assy`、`SaveImage`、`UpscaleModelLoader`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、VAEEncode
