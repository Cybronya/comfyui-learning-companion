---
key: 图片生成/图生图/wan2.2图生图高质量_1987726436859621378.json
name: wan2.2图生图高质量_1987726436859621378
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.2图生图高质量_1987726436859621378.json
hash: c224128c7e53abe5
coverage: 0.906977
learned_at: 2026-10-23 11:46:05
nodes: [CLIPTextEncode, CLIPTextEncode, CLIPLoader, VAELoader, UNETLoader, TTP_Tile_image_size, TTP_Image_Tile_Batch, CLIPLoader, LoraLoaderModelOnly, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, VAELoader, KSampler, easy cleanGpuUsed, easy imageBatchToImageList, VAEEncode, UpscaleModelLoader, ImageScaleToTotalPixels, ImageUpscaleWithModel, VAEDecode, ImageListToImageBatch, PreviewImage, PreviewImage, PreviewImage, LayerUtility: PurgeVRAM, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, TTP_Image_Assy, workflow>wan2.2, ImageStitch, SaveImage, Text Multiline, VAEEncode, easy showAnything, RH_Captioner, Text Concatenate, LoadImage, SaveImagePlus, LayerUtility: PurgeVRAM, SaveImage, SaveImagePlus]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 12, "denoise": "bong_tangent", "sampler_name": 1, "scheduler": "res_2s", "seed": "disable", "steps": "fixed"}
---

# 图片生成/图生图/wan2.2图生图高质量_1987726436859621378.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.2图生图高质量_1987726436859621378.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`
- `VAEEncode` ★核心
- `UpscaleModelLoader`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `VAEDecode` ★核心
- `ImageListToImageBatch`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `TTP_Image_Assy`
- `workflow>wan2.2`
- `ImageStitch`
- `SaveImage`
- `Text Multiline`
- `VAEEncode` ★核心
- `easy showAnything`
- `RH_Captioner`
- `Text Concatenate`
- `LoadImage`
- `SaveImagePlus`
- `LayerUtility: PurgeVRAM`
- `SaveImage`
- `SaveImagePlus`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `res_2s`
- `denoise` = `bong_tangent`

## 知识

覆盖率 **91%**（39/43）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`KSampler`、`easy cleanGpuUsed`、`easy imageBatchToImageList`、`VAEEncode`、`UpscaleModelLoader`、`ImageScaleToTotalPixels`、`ImageUpscaleWithModel`、`VAEDecode`、`ImageListToImageBatch`、`LayerUtility: PurgeVRAM`、`KSamplerAdvanced`、`TTP_Image_Assy`、`workflow>wan2.2`、`ImageStitch`、`SaveImage`、`Text Multiline`、`RH_Captioner`、`Text Concatenate`、`LoadImage`、`SaveImagePlus`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
