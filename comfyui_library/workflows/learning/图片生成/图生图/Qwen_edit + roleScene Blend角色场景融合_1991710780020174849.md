---
key: 图片生成/图生图/Qwen_edit + roleScene Blend角色场景融合_1991710780020174849.json
name: Qwen_edit + roleScene Blend角色场景融合_1991710780020174849
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_edit + roleScene Blend角色场景融合_1991710780020174849.json
hash: fd02760d991c991e
coverage: 0.77551
learned_at: 2026-10-23 11:21:22
nodes: [CLIPLoader, VAELoader, Anything Everywhere3, LoraLoaderModelOnly, LoraLoaderModelOnly, CFGNorm, ModelSamplingAuraFlow, PathchSageAttentionKJ, KSampler, QwenEditOutputExtractor, VAEEncode, ImageUpscaleWithModel, ImageScaleBy, VAEEncode, KSampler, ConditioningZeroOut, UNETLoader, easy imageRemBg, LayerUtility: ImageScaleByAspectRatio V2, ImageScaleToTotalPixels, QwenEditConfigPreparer, AIO_Preprocessor, PreviewImage, VAEDecode, Image Comparer (rgthree), SaveImage, UpscaleModelLoader, VAEDecode, CropWithPadInfo, LoadImage, LoadImage, PreviewImage, SaveImage, ImageConcanate, ImageConcanate, PreviewImage, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, QwenEditConfigPreparer, PreviewImage, ImageResizeKJ, DrawMaskOnImage, BlockifyMask, Fast Groups Bypasser (rgthree), LayerUtility: ImageBlend, PreviewImage, Image Comparer (rgthree), TextEncodeQwenImageEditPlusCustom_lrzjason, PrimitiveStringMultiline]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "sampler_name": "euler", "scheduler": "beta57", "seed": 468211931528317, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen_edit + roleScene Blend角色场景融合_1991710780020174849.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_edit + roleScene Blend角色场景融合_1991710780020174849.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `CLIPLoader`
- `VAELoader`
- `Anything Everywhere3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `KSampler` ★核心
- `QwenEditOutputExtractor`
- `VAEEncode` ★核心
- `ImageUpscaleWithModel`
- `ImageScaleBy`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `easy imageRemBg`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageScaleToTotalPixels`
- `QwenEditConfigPreparer`
- `AIO_Preprocessor`
- `PreviewImage`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode` ★核心
- `CropWithPadInfo`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `ImageConcanate`
- `ImageConcanate`
- `PreviewImage`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `QwenEditConfigPreparer`
- `PreviewImage`
- `ImageResizeKJ`
- `DrawMaskOnImage`
- `BlockifyMask`
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: ImageBlend`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `PrimitiveStringMultiline`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `468211931528317`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **78%**（38/49）

**有卡**：`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`CFGNorm`、`ModelSamplingAuraFlow`、`PathchSageAttentionKJ`、`KSampler`、`QwenEditOutputExtractor`、`VAEEncode`、`ImageUpscaleWithModel`、`ImageScaleBy`、`ConditioningZeroOut`、`UNETLoader`、`easy imageRemBg`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageScaleToTotalPixels`、`QwenEditConfigPreparer`、`AIO_Preprocessor`、`VAEDecode`、`SaveImage`、`UpscaleModelLoader`、`CropWithPadInfo`、`LoadImage`、`ImageConcanate`、`ImageResizeKJ`、`DrawMaskOnImage`、`BlockifyMask`、`LayerUtility: ImageBlend`、`TextEncodeQwenImageEditPlusCustom_lrzjason`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、SaveImage、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
