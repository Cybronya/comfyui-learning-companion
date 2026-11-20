---
key: 平台全量/（TTP+Wan2.2）批量去油放大精修增加写实质感_1990616290475872258.json
name: （TTP+Wan2.2）批量去油放大精修增加写实质感_1990616290475872258
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/（TTP+Wan2.2）批量去油放大精修增加写实质感_1990616290475872258.json
hash: 51a81210df4fbffa
coverage: 0.913043
learned_at: 2026-11-14 02:53:47
nodes: [ModelSamplingSD3, CLIPTextEncode, ImageUpscaleWithModel, easy imageBatchToImageList, VAEEncode, ImageScaleToTotalPixels, UNETLoader, CLIPTextEncode, CLIPLoader, UpscaleModelLoader, VAELoader, LoadImage, Image Comparer (rgthree), ImageListToImageBatch, VAEDecode, TTP_Image_Tile_Batch, PreviewImage, easy cleanGpuUsed, easy cleanGpuUsed, TTP_Tile_image_size, SaveImage, TTP_Image_Assy, KSampler]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.1, "sampler_name": "heun", "scheduler": "beta", "seed": 927068168876136, "steps": 10}
---

# 平台全量/（TTP+Wan2.2）批量去油放大精修增加写实质感_1990616290475872258.json

> 来源文件 `comfyui_library/workflows/平台全量/（TTP+Wan2.2）批量去油放大精修增加写实质感_1990616290475872258.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `ImageUpscaleWithModel`
- `easy imageBatchToImageList`
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `UpscaleModelLoader`
- `VAELoader`
- `LoadImage`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `VAEDecode` ★核心
- `TTP_Image_Tile_Batch`
- `PreviewImage`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `TTP_Tile_image_size`
- `SaveImage`
- `TTP_Image_Assy`
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `927068168876136`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.1`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`ModelSamplingSD3`、`CLIPTextEncode`、`ImageUpscaleWithModel`、`easy imageBatchToImageList`、`VAEEncode`、`ImageScaleToTotalPixels`、`UNETLoader`、`CLIPLoader`、`UpscaleModelLoader`、`VAELoader`、`LoadImage`、`ImageListToImageBatch`、`VAEDecode`、`TTP_Image_Tile_Batch`、`easy cleanGpuUsed`、`TTP_Tile_image_size`、`SaveImage`、`TTP_Image_Assy`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、VAEEncode
