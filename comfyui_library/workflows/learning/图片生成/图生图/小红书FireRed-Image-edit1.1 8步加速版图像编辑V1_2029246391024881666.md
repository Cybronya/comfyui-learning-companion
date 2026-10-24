---
key: 图片生成/图生图/小红书FireRed-Image-edit1.1 8步加速版图像编辑V1_2029246391024881666.json
name: 小红书FireRed-Image-edit1.1 8步加速版图像编辑V1_2029246391024881666
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1 8步加速版图像编辑V1_2029246391024881666.json
hash: 52818f8ec6b5e5a0
coverage: 0.852941
learned_at: 2026-10-23 12:49:09
nodes: [FluxKontextImageScale, VAEEncode, KSampler, VAELoader, ModelSamplingAuraFlow, CFGNorm, CLIPLoader, easy int, LayerUtility: ImageScaleByAspectRatio V2, Any Switch (rgthree), FluxKontextImageScale, TextEncodeQwenImageEditPlus, CR Prompt Text, LoadImage, Fast Groups Muter (rgthree), UNETLoader, LoraLoaderModelOnly, FluxKontextImageScale, Image Comparer (rgthree), PreviewImage, VAEDecode, SaveImage, Any Switch (rgthree), KOOK_SaveJPGImage, SaveImage, LoadImage, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageMaskScaleAsV2, AddLabel, CR Image Grid Panel, Image Batch, LayerUtility: ImageMaskScaleAsV2, LoadImage, TextEncodeQwenImageEditPlus]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 982491231876566, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/小红书FireRed-Image-edit1.1 8步加速版图像编辑V1_2029246391024881666.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1 8步加速版图像编辑V1_2029246391024881666.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `VAELoader`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `CLIPLoader`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Any Switch (rgthree)`
- `FluxKontextImageScale`
- `TextEncodeQwenImageEditPlus`
- `CR Prompt Text`
- `LoadImage`
- `Fast Groups Muter (rgthree)`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `Any Switch (rgthree)`
- `KOOK_SaveJPGImage`
- `SaveImage`
- `LoadImage`
- `LayerUtility: ImageMaskScaleAsV2`
- `LayerUtility: ImageMaskScaleAsV2`
- `AddLabel`
- `CR Image Grid Panel`
- `Image Batch`
- `LayerUtility: ImageMaskScaleAsV2`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `982491231876566`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（29/34）

**有卡**：`FluxKontextImageScale`、`VAEEncode`、`KSampler`、`VAELoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`CLIPLoader`、`easy int`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImageEditPlus`、`CR Prompt Text`、`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`VAEDecode`、`SaveImage`、`KOOK_SaveJPGImage`、`LayerUtility: ImageMaskScaleAsV2`、`AddLabel`、`CR Image Grid Panel`、`Image Batch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
