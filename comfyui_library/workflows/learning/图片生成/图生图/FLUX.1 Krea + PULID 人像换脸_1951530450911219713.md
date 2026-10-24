---
key: 图片生成/图生图/FLUX.1 Krea + PULID 人像换脸_1951530450911219713.json
name: FLUX.1 Krea + PULID 人像换脸_1951530450911219713
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.1 Krea + PULID 人像换脸_1951530450911219713.json
hash: c6df6f7a2112bf71
coverage: 0.823529
learned_at: 2026-10-23 10:54:00
nodes: [VAELoader, VAEEncode, MaskToImage, SetLatentNoiseMask, PreviewImage, SegsToCombinedMask, ImageResize+, ConditioningZeroOut, ImageResize+, Note, GrowMaskWithBlur, Note, RepeatLatentBatch, PreviewImage, KSampler, SUPIR_Upscale, PreviewImage, Note, BboxDetectorSEGS, CLIPTextEncode, PulidFluxModelLoader, PulidFluxInsightFaceLoader, ApplyPulidFlux, UltralyticsDetectorProvider, DualCLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, SaveImage, LoadImage, LoadImage, PulidFluxEvaClipLoader, UNETLoader]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.7000000000000001, "sampler_name": "euler", "scheduler": "normal", "seed": 1046766596503338, "steps": 25}
---

# 图片生成/图生图/FLUX.1 Krea + PULID 人像换脸_1951530450911219713.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.1 Krea + PULID 人像换脸_1951530450911219713.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `VAELoader`
- `VAEEncode` ★核心
- `MaskToImage`
- `SetLatentNoiseMask`
- `PreviewImage`
- `SegsToCombinedMask`
- `ImageResize+`
- `ConditioningZeroOut`
- `ImageResize+`
- `Note`
- `GrowMaskWithBlur`
- `Note`
- `RepeatLatentBatch`
- `PreviewImage`
- `KSampler` ★核心
- `SUPIR_Upscale`
- `PreviewImage`
- `Note`
- `BboxDetectorSEGS`
- `CLIPTextEncode` ★核心
- `PulidFluxModelLoader`
- `PulidFluxInsightFaceLoader`
- `ApplyPulidFlux`
- `UltralyticsDetectorProvider`
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `PulidFluxEvaClipLoader`
- `UNETLoader` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1046766596503338`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `0.7000000000000001`

## 知识

覆盖率 **82%**（28/34）

**有卡**：`VAELoader`、`VAEEncode`、`MaskToImage`、`SetLatentNoiseMask`、`SegsToCombinedMask`、`ImageResize+`、`ConditioningZeroOut`、`GrowMaskWithBlur`、`RepeatLatentBatch`、`KSampler`、`SUPIR_Upscale`、`BboxDetectorSEGS`、`CLIPTextEncode`、`PulidFluxModelLoader`、`PulidFluxInsightFaceLoader`、`ApplyPulidFlux`、`UltralyticsDetectorProvider`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`VAEDecode`、`SaveImage`、`LoadImage`、`PulidFluxEvaClipLoader`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
