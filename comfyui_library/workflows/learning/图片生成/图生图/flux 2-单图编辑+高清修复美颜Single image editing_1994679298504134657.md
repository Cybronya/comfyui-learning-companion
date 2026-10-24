---
key: 图片生成/图生图/flux 2-单图编辑+高清修复美颜Single image editing_1994679298504134657.json
name: flux 2-单图编辑+高清修复美颜Single image editing_1994679298504134657
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/flux 2-单图编辑+高清修复美颜Single image editing_1994679298504134657.json
hash: 26f4fe47565c0b45
coverage: 0.833333
learned_at: 2026-10-23 11:34:59
nodes: [RandomNoise, BasicGuider, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, Anything Everywhere, CLIPLoader, FluxGuidance, VAELoader, ReferenceLatent, VAEEncode, ImageScaleToTotalPixels, FluxGuidance, ConditioningZeroOut, CLIPTextEncode, ModelSamplingSD3, TTP_Image_Tile_Batch, easy imageBatchToImageList, VAEEncode, VAEDecode, easy cleanGpuUsed, easy cleanGpuUsed, CLIPTextEncode, TTP_Tile_image_size, ImageListToImageBatch, VAELoader, CLIPTextEncode, ReferenceLatent, VAEEncode, KSampler, KSampler, Image Comparer (rgthree), FluxKontextImageScale, Float, PreviewImage, PreviewImage, Image Comparer (rgthree), PreviewImage, Image Comparer (rgthree), LoraLoaderModelOnly, DualCLIPLoader, UpscaleModelLoader, UNETLoader, UNETLoader, CLIPLoader, VAELoader, SaveImage, SamplerCustomAdvanced, easy cleanGpuUsed, VAEDecode, easy cleanGpuUsed, easy cleanGpuUsed, ImageUpscaleWithModel, ImageScaleToTotalPixels, TTP_Image_Assy, easy cleanGpuUsed, CLIPTextEncode, Float, PrimitiveInt, Reroute, LayerUtility: ImageScaleByAspectRatio V2, MarkdownNote, LoadImage, VAEDecode, easy clearCacheAll, PrimitiveInt, PrimitiveInt, UNETLoader, CR Text, easy imageConcat, SaveImage, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.15, "sampler_name": "heun", "scheduler": "beta", "seed": 986010259544920, "steps": 10}
---

# 图片生成/图生图/flux 2-单图编辑+高清修复美颜Single image editing_1994679298504134657.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/flux 2-单图编辑+高清修复美颜Single image editing_1994679298504134657.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（72 个）：
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `Anything Everywhere`
- `CLIPLoader`
- `FluxGuidance`
- `VAELoader`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `FluxGuidance`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `TTP_Image_Tile_Batch`
- `easy imageBatchToImageList`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `TTP_Tile_image_size`
- `ImageListToImageBatch`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `FluxKontextImageScale`
- `Float`
- `PreviewImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `UpscaleModelLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ImageUpscaleWithModel`
- `ImageScaleToTotalPixels`
- `TTP_Image_Assy`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `Float`
- `PrimitiveInt`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MarkdownNote`
- `LoadImage`
- `VAEDecode` ★核心
- `easy clearCacheAll`
- `PrimitiveInt`
- `PrimitiveInt`
- `UNETLoader` ★核心
- `CR Text`
- `easy imageConcat`
- `SaveImage`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `986010259544920`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.15`

## 知识

覆盖率 **83%**（60/72）

**有卡**：`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`CLIPLoader`、`FluxGuidance`、`VAELoader`、`ReferenceLatent`、`VAEEncode`、`ImageScaleToTotalPixels`、`ConditioningZeroOut`、`CLIPTextEncode`、`ModelSamplingSD3`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`VAEDecode`、`easy cleanGpuUsed`、`TTP_Tile_image_size`、`ImageListToImageBatch`、`KSampler`、`FluxKontextImageScale`、`Float`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`UpscaleModelLoader`、`UNETLoader`、`SaveImage`、`SamplerCustomAdvanced`、`ImageUpscaleWithModel`、`TTP_Image_Assy`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`easy clearCacheAll`、`CR Text`、`easy imageConcat`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut
