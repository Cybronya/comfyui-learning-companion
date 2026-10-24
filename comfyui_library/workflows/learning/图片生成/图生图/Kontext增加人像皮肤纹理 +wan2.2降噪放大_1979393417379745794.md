---
key: 图片生成/图生图/Kontext增加人像皮肤纹理 +wan2.2降噪放大_1979393417379745794.json
name: Kontext增加人像皮肤纹理 +wan2.2降噪放大_1979393417379745794
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Kontext增加人像皮肤纹理 +wan2.2降噪放大_1979393417379745794.json
hash: 07de6f0b47be525b
coverage: 0.926829
learned_at: 2026-10-23 11:07:11
nodes: [VAEDecode, Image Comparer (rgthree), ConditioningZeroOut, CLIPTextEncode, VAELoader, KSampler, FluxKontextImageScale, CLIPLoader, KSampler, Float, MarkdownNote, VAEEncode, VAELoader, Image Comparer (rgthree), SaveImage, LoadImage, LoadImage, ImpactInt, VAEDecode, VAEEncode, ReferenceLatent, FluxGuidance, CLIPTextEncode, CLIPTextEncode, easy imageBatchToImageList, ImageListToImageBatch, TTP_Image_Tile_Batch, ImageScaleToTotalPixels, LayerUtility: ImageScaleByAspectRatio V2, TTP_Tile_image_size, easy cleanGpuUsed, easy cleanGpuUsed, ImageUpscaleWithModel, TTP_Image_Assy, ModelSamplingSD3, DualCLIPLoader, UpscaleModelLoader, UNETLoader, UNETLoader, LoraLoaderModelOnly, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.1, "sampler_name": "heun", "scheduler": "beta", "seed": 1028436436850226, "steps": 10}
---

# 图片生成/图生图/Kontext增加人像皮肤纹理 +wan2.2降噪放大_1979393417379745794.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Kontext增加人像皮肤纹理 +wan2.2降噪放大_1979393417379745794.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `KSampler` ★核心
- `FluxKontextImageScale`
- `CLIPLoader`
- `KSampler` ★核心
- `Float`
- `MarkdownNote`
- `VAEEncode` ★核心
- `VAELoader`
- `Image Comparer (rgthree)`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `ImpactInt`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy imageBatchToImageList`
- `ImageListToImageBatch`
- `TTP_Image_Tile_Batch`
- `ImageScaleToTotalPixels`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TTP_Tile_image_size`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ImageUpscaleWithModel`
- `TTP_Image_Assy`
- `ModelSamplingSD3`
- `DualCLIPLoader`
- `UpscaleModelLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1028436436850226`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.1`

## 知识

覆盖率 **93%**（38/41）

**有卡**：`VAEDecode`、`ConditioningZeroOut`、`CLIPTextEncode`、`VAELoader`、`KSampler`、`FluxKontextImageScale`、`CLIPLoader`、`Float`、`VAEEncode`、`SaveImage`、`LoadImage`、`ImpactInt`、`ReferenceLatent`、`FluxGuidance`、`easy imageBatchToImageList`、`ImageListToImageBatch`、`TTP_Image_Tile_Batch`、`ImageScaleToTotalPixels`、`LayerUtility: ImageScaleByAspectRatio V2`、`TTP_Tile_image_size`、`easy cleanGpuUsed`、`ImageUpscaleWithModel`、`TTP_Image_Assy`、`ModelSamplingSD3`、`DualCLIPLoader`、`UpscaleModelLoader`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut
