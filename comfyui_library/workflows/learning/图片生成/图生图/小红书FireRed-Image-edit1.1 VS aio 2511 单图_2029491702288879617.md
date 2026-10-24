---
key: 图片生成/图生图/小红书FireRed-Image-edit1.1 VS aio 2511 单图_2029491702288879617.json
name: 小红书FireRed-Image-edit1.1 VS aio 2511 单图_2029491702288879617
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1 VS aio 2511 单图_2029491702288879617.json
hash: 80a4ac7392709c59
coverage: 0.883721
learned_at: 2026-10-23 12:49:09
nodes: [VAEEncode, VAELoader, ModelSamplingAuraFlow, CFGNorm, CLIPLoader, easy int, LayerUtility: ImageScaleByAspectRatio V2, Any Switch (rgthree), TextEncodeQwenImageEditPlus, LoadImage, Fast Groups Muter (rgthree), UNETLoader, LoraLoaderModelOnly, FluxKontextImageScale, PreviewImage, SaveImage, SaveImage, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageMaskScaleAsV2, TextEncodeQwenImageEditPlus, FluxKontextImageScale, KSampler, Any Switch (rgthree), Image Batch, AddLabel, CR Image Grid Panel, CheckpointLoaderSimple, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, KSampler, VAEDecode, easy cleanGpuUsed, VAEDecode, SaveImage, LoadImage, FluxKontextImageScale, Image Comparer (rgthree), LayerUtility: ImageMaskScaleAsV2, easy cleanGpuUsed, Image Batch, LoadImage, CR Prompt Text, KOOK_SaveJPGImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "QwenRapidAIO 23-22-21_QwenRapidAIO 23.safetensors", "denoise": 1, "sampler_name": "er_sde", "scheduler": "beta", "seed": 85284919947980, "steps": 10}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/小红书FireRed-Image-edit1.1 VS aio 2511 单图_2029491702288879617.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1 VS aio 2511 单图_2029491702288879617.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
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
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `FluxKontextImageScale`
- `PreviewImage`
- `SaveImage`
- `SaveImage`
- `LayerUtility: ImageMaskScaleAsV2`
- `LayerUtility: ImageMaskScaleAsV2`
- `TextEncodeQwenImageEditPlus`
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
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageMaskScaleAsV2`
- `easy cleanGpuUsed`
- `Image Batch`
- `LoadImage`
- `CR Prompt Text`
- `KOOK_SaveJPGImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `85284919947980`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `QwenRapidAIO 23-22-21_QwenRapidAIO 23.safetensors`

## 知识

覆盖率 **88%**（38/43）

**有卡**：`VAEEncode`、`VAELoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`CLIPLoader`、`easy int`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImageEditPlus`、`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`FluxKontextImageScale`、`SaveImage`、`LayerUtility: ImageMaskScaleAsV2`、`KSampler`、`Image Batch`、`AddLabel`、`CR Image Grid Panel`、`CheckpointLoaderSimple`、`VAEDecode`、`easy cleanGpuUsed`、`CR Prompt Text`、`KOOK_SaveJPGImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
