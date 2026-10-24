---
key: 图片生成/图生图/FireRed-Image-edit1.1双图编辑（商业服装换装放大）_1978001893874171906.json
name: FireRed-Image-edit1.1双图编辑（商业服装换装放大）_1978001893874171906
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-edit1.1双图编辑（商业服装换装放大）_1978001893874171906.json
hash: 616f1f0c95dab851
coverage: 0.923077
learned_at: 2026-10-23 10:55:51
nodes: [UNETLoader, CLIPLoader, ModelSamplingAuraFlow, VAELoader, CFGNorm, LoraLoaderModelOnly, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, VAEEncode, KSampler, VAEDecode, LoadImage, FluxKontextImageScale, LoadImage, FluxKontextImageScale, FluxKontextImageScale, easy cleanGpuUsed, PreviewImage, LoadImage, easy int, LayerUtility: ImageScaleByAspectRatio V2, Any Switch (rgthree), ImageResize+, LayerUtility: PurgeVRAM V2, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ImageResize+, ImageScaleBy, Get resolution [Crystools], TTP_Image_Tile_Batch, Get resolution [Crystools], TTP_Tile_image_size, CLIPLoader, TTP_Image_Assy, VAELoader, UltimateSDUpscaleCustomSample, Upscale Model Loader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UpscaleModelLoader, AdvancedLyingSigmaSampler, KSamplerSelect, ConditioningZeroOut, CLIPTextEncode, LayerUtility: PurgeVRAM V2, PreviewImage, SaveImage, ImageUpscaleWithModel, Image Comparer (rgthree), CR Prompt Text]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 972396971819708, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-edit1.1双图编辑（商业服装换装放大）_1978001893874171906.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-edit1.1双图编辑（商业服装换装放大）_1978001893874171906.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `VAELoader`
- `CFGNorm`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `FluxKontextImageScale`
- `LoadImage`
- `FluxKontextImageScale`
- `FluxKontextImageScale`
- `easy cleanGpuUsed`
- `PreviewImage`
- `LoadImage`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Any Switch (rgthree)`
- `ImageResize+`
- `LayerUtility: PurgeVRAM V2`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ImageResize+`
- `ImageScaleBy`
- `Get resolution [Crystools]`
- `TTP_Image_Tile_Batch`
- `Get resolution [Crystools]`
- `TTP_Tile_image_size`
- `CLIPLoader`
- `TTP_Image_Assy`
- `VAELoader`
- `UltimateSDUpscaleCustomSample`
- `Upscale Model Loader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UpscaleModelLoader`
- `AdvancedLyingSigmaSampler` ★核心
- `KSamplerSelect` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
- `SaveImage`
- `ImageUpscaleWithModel`
- `Image Comparer (rgthree)`
- `CR Prompt Text`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `972396971819708`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（48/52）

**有卡**：`UNETLoader`、`CLIPLoader`、`ModelSamplingAuraFlow`、`VAELoader`、`CFGNorm`、`LoraLoaderModelOnly`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`KSampler`、`VAEDecode`、`LoadImage`、`FluxKontextImageScale`、`easy cleanGpuUsed`、`easy int`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResize+`、`LayerUtility: PurgeVRAM V2`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`ImageScaleBy`、`Get resolution [Crystools]`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`TTP_Image_Assy`、`UltimateSDUpscaleCustomSample`、`Upscale Model Loader`、`UpscaleModelLoader`、`AdvancedLyingSigmaSampler`、`KSamplerSelect`、`ConditioningZeroOut`、`CLIPTextEncode`、`SaveImage`、`ImageUpscaleWithModel`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
