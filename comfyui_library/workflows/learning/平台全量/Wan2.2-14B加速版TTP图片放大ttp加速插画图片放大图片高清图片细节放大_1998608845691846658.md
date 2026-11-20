---
key: 平台全量/Wan2.2-14B加速版TTP图片放大ttp加速插画图片放大图片高清图片细节放大_1998608845691846658.json
name: Wan2.2-14B加速版TTP图片放大ttp加速插画图片放大图片高清图片细节放大_1998608845691846658
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2-14B加速版TTP图片放大ttp加速插画图片放大图片高清图片细节放大_1998608845691846658.json
hash: 3d546ad258c2ffcb
coverage: 0.88
learned_at: 2026-11-14 01:05:52
nodes: [CLIPTextEncode, UpscaleModelLoader, easy cleanGpuUsed, ImageScaleToTotalPixels, TTP_Image_Tile_Batch, easy imageBatchToImageList, TTP_Tile_image_size, VAELoader, CLIPLoader, LoraLoaderModelOnly, UNETLoader, CLIPTextEncode, VAEEncode, KSampler, ImageListToImageBatch, VAEDecode, TTP_Image_Assy, Anything Everywhere3, ModelSamplingSD3, ImageUpscaleWithModel, ConstrainImage|pysssss, LoadImage, SaveImage, PreviewImage, Image Comparer (rgthree)]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "sampler_name": "heun", "scheduler": "beta", "seed": 182694260077525, "steps": 10}
---

# 平台全量/Wan2.2-14B加速版TTP图片放大ttp加速插画图片放大图片高清图片细节放大_1998608845691846658.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2-14B加速版TTP图片放大ttp加速插画图片放大图片高清图片细节放大_1998608845691846658.json`

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
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `KSampler` ★核心
- `ImageListToImageBatch`
- `VAEDecode` ★核心
- `TTP_Image_Assy`
- `Anything Everywhere3`
- `ModelSamplingSD3`
- `ImageUpscaleWithModel`
- `ConstrainImage|pysssss`
- `LoadImage`
- `SaveImage`
- `PreviewImage`
- `Image Comparer (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `182694260077525`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **88%**（22/25）

**有卡**：`CLIPTextEncode`、`UpscaleModelLoader`、`easy cleanGpuUsed`、`ImageScaleToTotalPixels`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`TTP_Tile_image_size`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`VAEEncode`、`KSampler`、`ImageListToImageBatch`、`VAEDecode`、`TTP_Image_Assy`、`ModelSamplingSD3`、`ImageUpscaleWithModel`、`ConstrainImage|pysssss`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader
