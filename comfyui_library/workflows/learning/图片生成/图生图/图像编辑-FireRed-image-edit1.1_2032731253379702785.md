---
key: 图片生成/图生图/图像编辑-FireRed-image-edit1.1_2032731253379702785.json
name: 图像编辑-FireRed-image-edit1.1_2032731253379702785
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图像编辑-FireRed-image-edit1.1_2032731253379702785.json
hash: 4a2423a8ef7512da
coverage: 0.959184
learned_at: 2026-10-23 12:38:59
nodes: [ConstrainImage|pysssss, ModelSamplingAuraFlow, RH_LLMAPI_NODE, easy boolean, RH_LLMAPI_NODE, SeedVR2, easy boolean, LoraLoaderModelOnly, easy boolean, LoraLoaderModelOnly, easy boolean, Bjornulf_IfElse, CLIPLoader, LoraLoaderModelOnly, LazySwitch1way, KSampler, LazySwitch1way, LazySwitch1way, easy boolean, LoadImage, LoadImage, SeedVR2BlockSwap, VAELoader, SaveImage, Image Comparer (rgthree), easy int, UnetLoaderGGUF, UNETLoader, LoadImage, CR Text, ConstrainImage|pysssss, LazySwitch1way, LazySwitch1way, TextEncodeQwenImageEditPlus, CFGNorm, VAEEncode, VAEDecode, TextEncodeQwenImageEditPlus, easy boolean, easy boolean, easy boolean, LazySwitch1way, LayerUtility: ImageScaleByAspectRatio V2, FluxKontextImageScale, Bjornulf_IfElse, PreviewAny, CR Text, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 659981665038851, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/图像编辑-FireRed-image-edit1.1_2032731253379702785.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图像编辑-FireRed-image-edit1.1_2032731253379702785.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `ConstrainImage|pysssss`
- `ModelSamplingAuraFlow`
- `RH_LLMAPI_NODE`
- `easy boolean`
- `RH_LLMAPI_NODE`
- `SeedVR2`
- `easy boolean`
- `LoraLoaderModelOnly` ★核心
- `easy boolean`
- `LoraLoaderModelOnly` ★核心
- `easy boolean`
- `Bjornulf_IfElse`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LazySwitch1way`
- `KSampler` ★核心
- `LazySwitch1way`
- `LazySwitch1way`
- `easy boolean`
- `LoadImage`
- `LoadImage`
- `SeedVR2BlockSwap`
- `VAELoader`
- `SaveImage`
- `Image Comparer (rgthree)`
- `easy int`
- `UnetLoaderGGUF` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `CR Text`
- `ConstrainImage|pysssss`
- `LazySwitch1way`
- `LazySwitch1way`
- `TextEncodeQwenImageEditPlus`
- `CFGNorm`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `TextEncodeQwenImageEditPlus`
- `easy boolean`
- `easy boolean`
- `easy boolean`
- `LazySwitch1way`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FluxKontextImageScale`
- `Bjornulf_IfElse`
- `PreviewAny`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `659981665038851`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **96%**（47/49）

**有卡**：`ConstrainImage|pysssss`、`ModelSamplingAuraFlow`、`RH_LLMAPI_NODE`、`easy boolean`、`SeedVR2`、`LoraLoaderModelOnly`、`Bjornulf_IfElse`、`CLIPLoader`、`LazySwitch1way`、`KSampler`、`LoadImage`、`SeedVR2BlockSwap`、`VAELoader`、`SaveImage`、`easy int`、`UnetLoaderGGUF`、`UNETLoader`、`CR Text`、`TextEncodeQwenImageEditPlus`、`CFGNorm`、`VAEEncode`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`FluxKontextImageScale`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
