---
key: 图片生成/图生图/推荐提示词： 【Wan2.2图像放大】 图像高清放大，人像放大去AI感，增加皮肤纹理，去瑕疵，图像一_1985251520163758082.json
name: 推荐提示词： 【Wan2.2图像放大】 图像高清放大，人像放大去AI感，增加皮肤纹理，去瑕疵，图像一_1985251520163758082
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/推荐提示词： 【Wan2.2图像放大】 图像高清放大，人像放大去AI感，增加皮肤纹理，去瑕疵，图像一_1985251520163758082.json
hash: 635c2b0e56d20cf4
coverage: 0.913043
learned_at: 2026-10-23 13:02:28
nodes: [CLIPLoader, ModelSamplingSD3, CLIPTextEncode, ImageUpscaleWithModel, easy imageBatchToImageList, VAEEncode, ImageScaleToTotalPixels, VAEDecode, easy cleanGpuUsed, Image Comparer (rgthree), CLIPTextEncode, VAELoader, LoadImage, UpscaleModelLoader, UNETLoader, ImageListToImageBatch, KSampler, TTP_Image_Tile_Batch, easy cleanGpuUsed, TTP_Tile_image_size, TTP_Image_Assy, SaveImage, PreviewImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.1, "sampler_name": "heun", "scheduler": "beta", "seed": 857159133734385, "steps": 10}
---

# 图片生成/图生图/推荐提示词： 【Wan2.2图像放大】 图像高清放大，人像放大去AI感，增加皮肤纹理，去瑕疵，图像一_1985251520163758082.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/推荐提示词： 【Wan2.2图像放大】 图像高清放大，人像放大去AI感，增加皮肤纹理，去瑕疵，图像一_1985251520163758082.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `CLIPLoader`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `ImageUpscaleWithModel`
- `easy imageBatchToImageList`
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LoadImage`
- `UpscaleModelLoader`
- `UNETLoader` ★核心
- `ImageListToImageBatch`
- `KSampler` ★核心
- `TTP_Image_Tile_Batch`
- `easy cleanGpuUsed`
- `TTP_Tile_image_size`
- `TTP_Image_Assy`
- `SaveImage`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `857159133734385`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.1`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`CLIPLoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`ImageUpscaleWithModel`、`easy imageBatchToImageList`、`VAEEncode`、`ImageScaleToTotalPixels`、`VAEDecode`、`easy cleanGpuUsed`、`VAELoader`、`LoadImage`、`UpscaleModelLoader`、`UNETLoader`、`ImageListToImageBatch`、`KSampler`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`TTP_Image_Assy`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEEncode
