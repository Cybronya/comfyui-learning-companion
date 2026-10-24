---
key: 图片生成/图生图/小红书FireRed-Image-edit1.1 VS aio 2511(化妆)_2029500931573817345.json
name: 小红书FireRed-Image-edit1.1 VS aio 2511(化妆)_2029500931573817345
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1 VS aio 2511(化妆)_2029500931573817345.json
hash: c39ac4e3943c07be
coverage: 0.886364
learned_at: 2026-10-23 12:49:11
nodes: [VAELoader, ModelSamplingAuraFlow, CFGNorm, CLIPLoader, easy int, LayerUtility: ImageScaleByAspectRatio V2, TextEncodeQwenImageEditPlus, LoadImage, Fast Groups Muter (rgthree), FluxKontextImageScale, SaveImage, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageMaskScaleAsV2, TextEncodeQwenImageEditPlus, FluxKontextImageScale, FluxKontextImageScale, KSampler, Any Switch (rgthree), Image Batch, AddLabel, CR Image Grid Panel, CheckpointLoaderSimple, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, KSampler, Image Comparer (rgthree), LayerUtility: ImageMaskScaleAsV2, Image Batch, VAEDecode, easy cleanGpuUsed, easy cleanGpuUsed, VAEDecode, SaveImage, LoadImage, LoadImage, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, CR Prompt Text, VAEEncode, PreviewImage, Any Switch (rgthree), KOOK_SaveJPGImage, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "QwenRapidAIO 23-22-21_QwenRapidAIO 23.safetensors", "denoise": 1, "sampler_name": "er_sde", "scheduler": "beta", "seed": 432735939227399, "steps": 10}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/小红书FireRed-Image-edit1.1 VS aio 2511(化妆)_2029500931573817345.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1 VS aio 2511(化妆)_2029500931573817345.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `VAELoader`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `CLIPLoader`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `Fast Groups Muter (rgthree)`
- `FluxKontextImageScale`
- `SaveImage`
- `LayerUtility: ImageMaskScaleAsV2`
- `LayerUtility: ImageMaskScaleAsV2`
- `TextEncodeQwenImageEditPlus`
- `FluxKontextImageScale`
- `FluxKontextImageScale`
- `KSampler` ★核心
- `Any Switch (rgthree)`
- `Image Batch`
- `AddLabel`
- `CR Image Grid Panel`
- `CheckpointLoaderSimple` ★核心
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `LayerUtility: ImageMaskScaleAsV2`
- `Image Batch`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `VAEEncode` ★核心
- `PreviewImage`
- `Any Switch (rgthree)`
- `KOOK_SaveJPGImage`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `432735939227399`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `QwenRapidAIO 23-22-21_QwenRapidAIO 23.safetensors`

## 知识

覆盖率 **89%**（39/44）

**有卡**：`VAELoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`CLIPLoader`、`easy int`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImageEditPlus`、`LoadImage`、`FluxKontextImageScale`、`SaveImage`、`LayerUtility: ImageMaskScaleAsV2`、`KSampler`、`Image Batch`、`AddLabel`、`CR Image Grid Panel`、`CheckpointLoaderSimple`、`VAEDecode`、`easy cleanGpuUsed`、`LoraLoaderModelOnly`、`UNETLoader`、`CR Prompt Text`、`VAEEncode`、`KOOK_SaveJPGImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
