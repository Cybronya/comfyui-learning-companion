---
key: 图片生成/图生图/小红书FireRed-Image-edit1.1 VS aio 2511（文字排版）_2029499925364482049.json
name: 小红书FireRed-Image-edit1.1 VS aio 2511（文字排版）_2029499925364482049
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1 VS aio 2511（文字排版）_2029499925364482049.json
hash: 815d1020bbd9eb9c
coverage: 0.886364
learned_at: 2026-10-23 12:49:11
nodes: [VAEEncode, VAELoader, ModelSamplingAuraFlow, CFGNorm, CLIPLoader, easy int, LayerUtility: ImageScaleByAspectRatio V2, Any Switch (rgthree), TextEncodeQwenImageEditPlus, LoadImage, Fast Groups Muter (rgthree), FluxKontextImageScale, PreviewImage, SaveImage, SaveImage, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageMaskScaleAsV2, TextEncodeQwenImageEditPlus, FluxKontextImageScale, FluxKontextImageScale, KSampler, Any Switch (rgthree), AddLabel, CR Image Grid Panel, CheckpointLoaderSimple, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, KSampler, Image Comparer (rgthree), LayerUtility: ImageMaskScaleAsV2, Image Batch, VAEDecode, easy cleanGpuUsed, easy cleanGpuUsed, VAEDecode, SaveImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, LoadImage, CR Prompt Text, Image Batch, KOOK_SaveJPGImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "QwenRapidAIO 23-22-21_QwenRapidAIO 23.safetensors", "denoise": 1, "sampler_name": "er_sde", "scheduler": "beta", "seed": 1054714523848441, "steps": 10}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/小红书FireRed-Image-edit1.1 VS aio 2511（文字排版）_2029499925364482049.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1 VS aio 2511（文字排版）_2029499925364482049.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `VAEEncode` ★核心
- `VAELoader`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `CLIPLoader`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Any Switch (rgthree)`
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `Fast Groups Muter (rgthree)`
- `FluxKontextImageScale`
- `PreviewImage`
- `SaveImage`
- `SaveImage`
- `LayerUtility: ImageMaskScaleAsV2`
- `LayerUtility: ImageMaskScaleAsV2`
- `TextEncodeQwenImageEditPlus`
- `FluxKontextImageScale`
- `FluxKontextImageScale`
- `KSampler` ★核心
- `Any Switch (rgthree)`
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
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `Image Batch`
- `KOOK_SaveJPGImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1054714523848441`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `QwenRapidAIO 23-22-21_QwenRapidAIO 23.safetensors`

## 知识

覆盖率 **89%**（39/44）

**有卡**：`VAEEncode`、`VAELoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`CLIPLoader`、`easy int`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImageEditPlus`、`LoadImage`、`FluxKontextImageScale`、`SaveImage`、`LayerUtility: ImageMaskScaleAsV2`、`KSampler`、`AddLabel`、`CR Image Grid Panel`、`CheckpointLoaderSimple`、`Image Batch`、`VAEDecode`、`easy cleanGpuUsed`、`UNETLoader`、`LoraLoaderModelOnly`、`CR Prompt Text`、`KOOK_SaveJPGImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
