---
key: 平台全量/手部修复 完美修手 修手 wan2.2 万相低噪模型修复_2001192188497326081.json
name: 手部修复 完美修手 修手 wan2.2 万相低噪模型修复_2001192188497326081
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/手部修复 完美修手 修手 wan2.2 万相低噪模型修复_2001192188497326081.json
hash: 1676e66142049faf
coverage: 0.95
learned_at: 2026-11-14 02:04:56
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAEEncode, ConditioningZeroOut, SetLatentNoiseMask, CLIPTextEncode, KSampler, VAELoader, DualCLIPLoader, UNETLoader, DifferentialDiffusion, FluxGuidance, ConditioningZeroOut, InpaintModelConditioning, KSampler, GrowMaskWithBlur, MaskPreview+, GrowMaskWithBlur, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: RestoreCropBox, Int, RepeatLatentBatch, VAELoader, LayerUtility: ImageScaleRestore V2, Mask Fill Holes, PreviewImage, PreviewImage, VAEDecode, ModelSamplingSD3, RepeatLatentBatch, CLIPTextEncode, SaveImage, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 911146197157821, "steps": 20}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/手部修复 完美修手 修手 wan2.2 万相低噪模型修复_2001192188497326081.json

> 来源文件 `comfyui_library/workflows/平台全量/手部修复 完美修手 修手 wan2.2 万相低噪模型修复_2001192188497326081.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `SetLatentNoiseMask`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `DifferentialDiffusion`
- `FluxGuidance`
- `ConditioningZeroOut`
- `InpaintModelConditioning`
- `KSampler` ★核心
- `GrowMaskWithBlur`
- `MaskPreview+`
- `GrowMaskWithBlur`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: RestoreCropBox`
- `Int`
- `RepeatLatentBatch`
- `VAELoader`
- `LayerUtility: ImageScaleRestore V2`
- `Mask Fill Holes`
- `PreviewImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `RepeatLatentBatch`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `911146197157821`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（38/40）

**有卡**：`LoraLoaderModelOnly`、`CLIPLoader`、`VAEEncode`、`ConditioningZeroOut`、`SetLatentNoiseMask`、`CLIPTextEncode`、`KSampler`、`VAELoader`、`DualCLIPLoader`、`UNETLoader`、`DifferentialDiffusion`、`FluxGuidance`、`InpaintModelConditioning`、`GrowMaskWithBlur`、`MaskPreview+`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: CropByMask V2`、`LayerUtility: RestoreCropBox`、`Int`、`RepeatLatentBatch`、`LayerUtility: ImageScaleRestore V2`、`Mask Fill Holes`、`ModelSamplingSD3`、`SaveImage`、`PathchSageAttentionKJ`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
