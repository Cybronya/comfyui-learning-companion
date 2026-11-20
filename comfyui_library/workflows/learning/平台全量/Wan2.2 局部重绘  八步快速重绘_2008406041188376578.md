---
key: 平台全量/Wan2.2 局部重绘  八步快速重绘_2008406041188376578.json
name: Wan2.2 局部重绘  八步快速重绘_2008406041188376578
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 局部重绘  八步快速重绘_2008406041188376578.json
hash: 620f958f5e59c746
coverage: 0.90625
learned_at: 2026-11-14 01:05:45
nodes: [VAEEncode, PathchSageAttentionKJ, VAELoader, CLIPTextEncode, ConditioningZeroOut, ModelSamplingSD3, SetLatentNoiseMask, RepeatLatentBatch, VAEDecode, GrowMaskWithBlur, KSampler, easy float, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, CLIPLoader, JjkText, LayerUtility: ImageScaleByAspectRatio V2, Mask Fill Holes, LayerUtility: CropByMask V2, ImpactInt, LayerUtility: ImageScaleRestore V2, SaveImage, PreviewImage, PreviewImage, LayerUtility: RestoreCropBox, LoadImage, LoadImage, MaskPreview+]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.43999999999999995, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 1090981573056637, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Wan2.2 局部重绘  八步快速重绘_2008406041188376578.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 局部重绘  八步快速重绘_2008406041188376578.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `VAEEncode` ★核心
- `PathchSageAttentionKJ`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ModelSamplingSD3`
- `SetLatentNoiseMask`
- `RepeatLatentBatch`
- `VAEDecode` ★核心
- `GrowMaskWithBlur`
- `KSampler` ★核心
- `easy float`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `CLIPLoader`
- `JjkText`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Mask Fill Holes`
- `LayerUtility: CropByMask V2`
- `ImpactInt`
- `LayerUtility: ImageScaleRestore V2`
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoadImage`
- `MaskPreview+`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1090981573056637`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.43999999999999995`

## 知识

覆盖率 **91%**（29/32）

**有卡**：`VAEEncode`、`PathchSageAttentionKJ`、`VAELoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`ModelSamplingSD3`、`SetLatentNoiseMask`、`RepeatLatentBatch`、`VAEDecode`、`GrowMaskWithBlur`、`KSampler`、`easy float`、`UNETLoader`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`CLIPLoader`、`Mask Fill Holes`、`LayerUtility: CropByMask V2`、`ImpactInt`、`LayerUtility: ImageScaleRestore V2`、`SaveImage`、`LayerUtility: RestoreCropBox`、`MaskPreview+`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
