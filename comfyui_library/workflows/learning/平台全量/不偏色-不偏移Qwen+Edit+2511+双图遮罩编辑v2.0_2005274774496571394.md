---
key: 平台全量/不偏色-不偏移Qwen+Edit+2511+双图遮罩编辑v2.0_2005274774496571394.json
name: 不偏色-不偏移Qwen+Edit+2511+双图遮罩编辑v2.0_2005274774496571394
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/不偏色-不偏移Qwen+Edit+2511+双图遮罩编辑v2.0_2005274774496571394.json
hash: 5e8d935cdc6d1c2e
coverage: 0.805556
learned_at: 2026-11-14 01:33:40
nodes: [CropWithPadInfo, ImageScaleBy, Image Comparer (rgthree), LoraLoaderModelOnly, CLIPLoader, UNETLoader, QwenEditConfigPreparer, QwenEditAdaptiveLongestEdge, PreviewImage, SaveImage, MarkdownNote, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, MarkdownNote, QwenEditAdaptiveLongestEdge, VAELoader, LoadImage, LoadImage, QwenEditConfigPreparer, PrimitiveStringMultiline, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, easy cleanGpuUsed, FluxKontextMultiReferenceLatentMethod, ImageConcanate, QwenEditOutputExtractor, PreviewImage, ImageConcanate, VAEDecode, FluxKontextMultiReferenceLatentMethod, MarkdownNote, ConditioningZeroOut, ReferenceLatent, SetLatentNoiseMask, VAEEncode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 992076494203892, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/不偏色-不偏移Qwen+Edit+2511+双图遮罩编辑v2.0_2005274774496571394.json

> 来源文件 `comfyui_library/workflows/平台全量/不偏色-不偏移Qwen+Edit+2511+双图遮罩编辑v2.0_2005274774496571394.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `CropWithPadInfo`
- `ImageScaleBy`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `QwenEditConfigPreparer`
- `QwenEditAdaptiveLongestEdge`
- `PreviewImage`
- `SaveImage`
- `MarkdownNote`
- `SaveImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `MarkdownNote`
- `QwenEditAdaptiveLongestEdge`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `QwenEditConfigPreparer`
- `PrimitiveStringMultiline`
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy cleanGpuUsed`
- `FluxKontextMultiReferenceLatentMethod`
- `ImageConcanate`
- `QwenEditOutputExtractor`
- `PreviewImage`
- `ImageConcanate`
- `VAEDecode` ★核心
- `FluxKontextMultiReferenceLatentMethod`
- `MarkdownNote`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `SetLatentNoiseMask`
- `VAEEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `992076494203892`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **81%**（29/36）

**有卡**：`CropWithPadInfo`、`ImageScaleBy`、`LoraLoaderModelOnly`、`CLIPLoader`、`UNETLoader`、`QwenEditConfigPreparer`、`QwenEditAdaptiveLongestEdge`、`SaveImage`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`VAELoader`、`LoadImage`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy cleanGpuUsed`、`FluxKontextMultiReferenceLatentMethod`、`ImageConcanate`、`QwenEditOutputExtractor`、`VAEDecode`、`ConditioningZeroOut`、`ReferenceLatent`、`SetLatentNoiseMask`、`VAEEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
