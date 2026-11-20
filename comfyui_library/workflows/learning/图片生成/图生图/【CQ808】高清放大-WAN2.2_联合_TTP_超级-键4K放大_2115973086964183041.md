---
key: 图片生成/图生图/【CQ808】高清放大-WAN2.2_联合_TTP_超级-键4K放大_2115973086964183041.json
name: 【CQ808】高清放大-WAN2.2_联合_TTP_超级-键4K放大_2115973086964183041
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【CQ808】高清放大-WAN2.2_联合_TTP_超级-键4K放大_2115973086964183041.json
hash: f3d563bcfa0e5afc
coverage: 0.857143
learned_at: 2026-10-30 23:24:58
nodes: [CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, ImageUpscaleWithModel, easy cleanGpuUsed, ImageScaleToTotalPixels, TTP_Tile_image_size, TTP_Image_Tile_Batch, PreviewImage, easy imageBatchToImageList, PreviewImage, VAEEncode, KSampler, VAEDecode, TTP_Image_Assy, ImageListToImageBatch, easy cleanGpuUsed, Label (rgthree), Reroute, UpscaleModelLoader, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, Label (rgthree), LoadImage, PreviewImage, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "sampler_name": "heun", "scheduler": "beta", "seed": 898879018815377, "steps": 10}
---

# 图片生成/图生图/【CQ808】高清放大-WAN2.2_联合_TTP_超级-键4K放大_2115973086964183041.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【CQ808】高清放大-WAN2.2_联合_TTP_超级-键4K放大_2115973086964183041.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ImageUpscaleWithModel`
- `easy cleanGpuUsed`
- `ImageScaleToTotalPixels`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `PreviewImage`
- `easy imageBatchToImageList`
- `PreviewImage`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `TTP_Image_Assy`
- `ImageListToImageBatch`
- `easy cleanGpuUsed`
- `Label (rgthree)`
- `Reroute`
- `UpscaleModelLoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `Label (rgthree)`
- `LoadImage`
- `PreviewImage`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `898879018815377`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **86%**（24/28）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`ImageUpscaleWithModel`、`easy cleanGpuUsed`、`ImageScaleToTotalPixels`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`VAEEncode`、`KSampler`、`VAEDecode`、`TTP_Image_Assy`、`ImageListToImageBatch`、`Label (rgthree)`、`UpscaleModelLoader`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader
