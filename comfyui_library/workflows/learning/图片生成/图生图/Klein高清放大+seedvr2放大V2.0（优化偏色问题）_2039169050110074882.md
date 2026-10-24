---
key: 图片生成/图生图/Klein高清放大+seedvr2放大V2.0（优化偏色问题）_2039169050110074882.json
name: Klein高清放大+seedvr2放大V2.0（优化偏色问题）_2039169050110074882
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Klein高清放大+seedvr2放大V2.0（优化偏色问题）_2039169050110074882.json
hash: e64d7b9023919640
coverage: 0.826923
learned_at: 2026-10-23 11:05:15
nodes: [VAELoader, easy showAnything, easy showAnything, ImageResize+, ImageResize+, easy showAnything, easy showAnything, SeedVR2VideoUpscaler, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, CLIPLoader, VAELoader, ReferenceLatent, ConditioningZeroOut, PreviewImage, CLIPTextEncode, CLIPTextEncode, Note, GetImageSize+, ImageScaleBy, GetImageSize+, easy cleanGpuUsed, PrimitiveFloat, TTP_Image_Assy, RunningHub Deepcleaner, VAEEncode, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, VAEEncode, VAEDecode, CLIPLoader, KSamplerAdvanced, VAEDecode, RH_Captioner, ModelSamplingAuraFlow, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, LoraLoaderModelOnly, ImageCASharpening+, LoadImage, LatentUpscaleBy, SaveImage, KSampler, ImageScaleBy, SaveImage, Image Comparer (rgthree), UNETLoader, CLIPTextEncode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "simple", "seed": 330295661416002, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Klein高清放大+seedvr2放大V2.0（优化偏色问题）_2039169050110074882.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Klein高清放大+seedvr2放大V2.0（优化偏色问题）_2039169050110074882.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `VAELoader`
- `easy showAnything`
- `easy showAnything`
- `ImageResize+`
- `ImageResize+`
- `easy showAnything`
- `easy showAnything`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `GetImageSize+`
- `ImageScaleBy`
- `GetImageSize+`
- `easy cleanGpuUsed`
- `PrimitiveFloat`
- `TTP_Image_Assy`
- `RunningHub Deepcleaner`
- `VAEEncode` ★核心
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `RH_Captioner`
- `ModelSamplingAuraFlow`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `LoraLoaderModelOnly` ★核心
- `ImageCASharpening+`
- `LoadImage`
- `LatentUpscaleBy`
- `SaveImage`
- `KSampler` ★核心
- `ImageScaleBy`
- `SaveImage`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `330295661416002`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（43/52）

**有卡**：`VAELoader`、`ImageResize+`、`SeedVR2VideoUpscaler`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`UNETLoader`、`CLIPLoader`、`ReferenceLatent`、`ConditioningZeroOut`、`CLIPTextEncode`、`GetImageSize+`、`ImageScaleBy`、`easy cleanGpuUsed`、`TTP_Image_Assy`、`RunningHub Deepcleaner`、`VAEEncode`、`LayerUtility: ImageMaskScaleAs`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`VAEDecode`、`KSamplerAdvanced`、`RH_Captioner`、`ModelSamplingAuraFlow`、`LayerUtility: ImageScaleByAspectRatio V2`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`LoraLoaderModelOnly`、`ImageCASharpening+`、`LoadImage`、`LatentUpscaleBy`、`SaveImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
