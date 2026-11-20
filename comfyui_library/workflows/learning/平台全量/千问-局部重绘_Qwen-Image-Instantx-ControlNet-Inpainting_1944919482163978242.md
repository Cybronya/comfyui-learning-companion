---
key: 平台全量/千问-局部重绘_Qwen-Image-Instantx-ControlNet-Inpainting_1944919482163978242.json
name: 千问-局部重绘_Qwen-Image-Instantx-ControlNet-Inpainting_1944919482163978242
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/千问-局部重绘_Qwen-Image-Instantx-ControlNet-Inpainting_1944919482163978242.json
hash: 20708cbb506e162c
coverage: 0.888889
learned_at: 2026-11-14 01:47:23
nodes: [LayerUtility: RestoreCropBox, LayerUtility: CropByMask V2, LayerUtility: ImageScaleRestore V2, SaveImage, PreviewImage, MaskPreview+, Mask Fill Holes, JjkText, GrowMaskWithBlur, PreviewImage, CLIPLoader, CLIPTextEncode, VAEEncode, CLIPTextEncode, ModelSamplingAuraFlow, ControlNetInpaintingAliMamaApply, VAELoader, KSampler, VAEDecode, ImpactInt, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, LoraLoaderModelOnly, LoadImage, ControlNetLoader, RepeatLatentBatch]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 40063683617870, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/千问-局部重绘_Qwen-Image-Instantx-ControlNet-Inpainting_1944919482163978242.json

> 来源文件 `comfyui_library/workflows/平台全量/千问-局部重绘_Qwen-Image-Instantx-ControlNet-Inpainting_1944919482163978242.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `LayerUtility: RestoreCropBox`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleRestore V2`
- `SaveImage`
- `PreviewImage`
- `MaskPreview+`
- `Mask Fill Holes`
- `JjkText`
- `GrowMaskWithBlur`
- `PreviewImage`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `ControlNetInpaintingAliMamaApply`
- `VAELoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImpactInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `ControlNetLoader`
- `RepeatLatentBatch`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `40063683617870`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`LayerUtility: RestoreCropBox`、`LayerUtility: CropByMask V2`、`LayerUtility: ImageScaleRestore V2`、`SaveImage`、`MaskPreview+`、`Mask Fill Holes`、`GrowMaskWithBlur`、`CLIPLoader`、`CLIPTextEncode`、`VAEEncode`、`ModelSamplingAuraFlow`、`ControlNetInpaintingAliMamaApply`、`VAELoader`、`KSampler`、`VAEDecode`、`ImpactInt`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`、`ControlNetLoader`、`RepeatLatentBatch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
