---
key: 图片生成/图生图/Joy3反推提示词+Wan2.2TTP细节增强放大_1951297958203609090.json
name: Joy3反推提示词+Wan2.2TTP细节增强放大_1951297958203609090
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Joy3反推提示词+Wan2.2TTP细节增强放大_1951297958203609090.json
hash: 14344ed8ab2e020c
coverage: 0.782609
learned_at: 2026-10-23 11:03:49
nodes: [easy cleanGpuUsed, LayerUtility: JoyCaptionBeta1, Note, Note, LayerUtility: LoadJoyCaptionBeta1Model, DeepTranslatorTextNode, ShowText|pysssss, SaveImage, LayerUtility: JoyCaptionBeta1ExtraOptions, easy imageBatchToImageList, PreviewImage, ModelSamplingSD3, VAEEncode, easy cleanGpuUsed, VAEDecode, TTP_Tile_image_size, ImageListToImageBatch, easy cleanGpuUsed, PreviewImage, TTP_Image_Tile_Batch, CLIPTextEncode, ImageUpscaleWithModel, UpscaleModelLoader, ImageScaleToTotalPixels, easy cleanGpuUsed, LoraLoaderModelOnly, UNETLoader, ImageResizeKJv2, CLIPLoader, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, DeepTranslatorTextNode, TTP_Image_Assy, Reroute, LoadImage, Reroute, ImageConcanate, CLIPTextEncode, SaveImage, Image Comparer (rgthree), SaveImage, LayerUtility: ImageScaleByAspectRatio V2, KSampler, PreviewImage, ShowText|pysssss]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.05000000000000001, "sampler_name": "heun", "scheduler": "beta", "seed": 383895505357068, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Joy3反推提示词+Wan2.2TTP细节增强放大_1951297958203609090.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Joy3反推提示词+Wan2.2TTP细节增强放大_1951297958203609090.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `easy cleanGpuUsed`
- `LayerUtility: JoyCaptionBeta1`
- `Note`
- `Note`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `DeepTranslatorTextNode`
- `ShowText|pysssss`
- `SaveImage`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `easy imageBatchToImageList`
- `PreviewImage`
- `ModelSamplingSD3`
- `VAEEncode` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `TTP_Tile_image_size`
- `ImageListToImageBatch`
- `easy cleanGpuUsed`
- `PreviewImage`
- `TTP_Image_Tile_Batch`
- `CLIPTextEncode` ★核心
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `ImageScaleToTotalPixels`
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ImageResizeKJv2`
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `DeepTranslatorTextNode`
- `TTP_Image_Assy`
- `Reroute`
- `LoadImage`
- `Reroute`
- `ImageConcanate`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `PreviewImage`
- `ShowText|pysssss`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `383895505357068`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.05000000000000001`

## 知识

覆盖率 **78%**（36/46）

**有卡**：`easy cleanGpuUsed`、`LayerUtility: JoyCaptionBeta1`、`LayerUtility: LoadJoyCaptionBeta1Model`、`DeepTranslatorTextNode`、`SaveImage`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`easy imageBatchToImageList`、`ModelSamplingSD3`、`VAEEncode`、`VAEDecode`、`TTP_Tile_image_size`、`ImageListToImageBatch`、`TTP_Image_Tile_Batch`、`CLIPTextEncode`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`ImageScaleToTotalPixels`、`LoraLoaderModelOnly`、`UNETLoader`、`ImageResizeKJv2`、`CLIPLoader`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`TTP_Image_Assy`、`ImageConcanate`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
