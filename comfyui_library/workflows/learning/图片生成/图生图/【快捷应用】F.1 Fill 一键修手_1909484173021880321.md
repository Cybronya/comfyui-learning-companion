---
key: 图片生成/图生图/【快捷应用】F.1 Fill 一键修手_1909484173021880321.json
name: 【快捷应用】F.1 Fill 一键修手_1909484173021880321
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【快捷应用】F.1 Fill 一键修手_1909484173021880321.json
hash: 1255f5b6b1d6332a
coverage: 0.848485
learned_at: 2026-10-23 11:50:05
nodes: [MaskPreview+, MaskToSEGS, preview_mask, GrowMaskWithBlur, easy cleanGpuUsed, ConstrainImage|pysssss, DualCLIPLoader, UNETLoader, JjkText, VAELoader, VAEEncode, SetLatentNoiseMask, CLIPTextEncodeFlux, CLIPTextEncode, LoraLoader, KSampler, LayerMask: SegmentAnythingUltra V2, GrowMaskWithBlur, PreviewImage, LayerUtility: RestoreCropBox, PreviewImage, PreviewImage, VAEDecode, easy cleanGpuUsed, SaveImage, Image Comparer (rgthree), GetImageSize, ImageScale, LayerUtility: CropByMask V2, DetailerForEach, LayerColor: ColorAdapter, LayerUtility: ImageScaleByAspectRatio V2, LoadImage]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 1, "denoise": 0.7500000000000001, "lora_name": "AWPortrait CN_1.0.safetensors", "sampler_name": "euler", "scheduler": "normal", "seed": 447761187948130, "steps": 20, "strength_clip": 1, "strength_model": 0.8000000000000002}
---

# 图片生成/图生图/【快捷应用】F.1 Fill 一键修手_1909484173021880321.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【快捷应用】F.1 Fill 一键修手_1909484173021880321.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `MaskPreview+`
- `MaskToSEGS`
- `preview_mask`
- `GrowMaskWithBlur`
- `easy cleanGpuUsed`
- `ConstrainImage|pysssss`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `JjkText`
- `VAELoader`
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `CLIPTextEncodeFlux` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `KSampler` ★核心
- `LayerMask: SegmentAnythingUltra V2`
- `GrowMaskWithBlur`
- `PreviewImage`
- `LayerUtility: RestoreCropBox`
- `PreviewImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `SaveImage`
- `Image Comparer (rgthree)`
- `GetImageSize`
- `ImageScale`
- `LayerUtility: CropByMask V2`
- `DetailerForEach`
- `LayerColor: ColorAdapter`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `AWPortrait CN_1.0.safetensors`
- `strength_model` = `0.8000000000000002`
- `strength_clip` = `1`
- `seed` = `447761187948130`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `0.7500000000000001`

## 知识

覆盖率 **85%**（28/33）

**有卡**：`MaskPreview+`、`MaskToSEGS`、`preview_mask`、`GrowMaskWithBlur`、`easy cleanGpuUsed`、`ConstrainImage|pysssss`、`DualCLIPLoader`、`UNETLoader`、`VAELoader`、`VAEEncode`、`SetLatentNoiseMask`、`CLIPTextEncodeFlux`、`CLIPTextEncode`、`LoraLoader`、`KSampler`、`LayerMask: SegmentAnythingUltra V2`、`LayerUtility: RestoreCropBox`、`VAEDecode`、`SaveImage`、`GetImageSize`、`ImageScale`、`LayerUtility: CropByMask V2`、`DetailerForEach`、`LayerColor: ColorAdapter`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、CLIPTextEncodeFlux、SetLatentNoiseMask
