---
key: 平台全量/Wan2.2 局部重绘_1954192513697497090.json
name: Wan2.2 局部重绘_1954192513697497090
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 局部重绘_1954192513697497090.json
hash: eeaaddcdff0444dd
coverage: 0.9
learned_at: 2026-11-14 01:05:45
nodes: [VAEEncode, PathchSageAttentionKJ, LayerUtility: RestoreCropBox, LayerUtility: CropByMask V2, VAELoader, CLIPTextEncode, ConditioningZeroOut, LayerUtility: ImageScaleRestore V2, ModelSamplingSD3, CLIPLoader, SetLatentNoiseMask, RepeatLatentBatch, SaveImage, VAEDecode, PreviewImage, MaskPreview+, Mask Fill Holes, JjkText, GrowMaskWithBlur, KSampler, PreviewImage, ImpactInt, easy float, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.43999999999999995, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 580910729356565, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Wan2.2 局部重绘_1954192513697497090.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 局部重绘_1954192513697497090.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `VAEEncode` ★核心
- `PathchSageAttentionKJ`
- `LayerUtility: RestoreCropBox`
- `LayerUtility: CropByMask V2`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `LayerUtility: ImageScaleRestore V2`
- `ModelSamplingSD3`
- `CLIPLoader`
- `SetLatentNoiseMask`
- `RepeatLatentBatch`
- `SaveImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `MaskPreview+`
- `Mask Fill Holes`
- `JjkText`
- `GrowMaskWithBlur`
- `KSampler` ★核心
- `PreviewImage`
- `ImpactInt`
- `easy float`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `580910729356565`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.43999999999999995`

## 知识

覆盖率 **90%**（27/30）

**有卡**：`VAEEncode`、`PathchSageAttentionKJ`、`LayerUtility: RestoreCropBox`、`LayerUtility: CropByMask V2`、`VAELoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`LayerUtility: ImageScaleRestore V2`、`ModelSamplingSD3`、`CLIPLoader`、`SetLatentNoiseMask`、`RepeatLatentBatch`、`SaveImage`、`VAEDecode`、`MaskPreview+`、`Mask Fill Holes`、`GrowMaskWithBlur`、`KSampler`、`ImpactInt`、`easy float`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
