---
key: 图片生成/图生图/Flux Kontext Dev双人互动脸部一致性增强加速版V0.5_1940000386315096066.json
name: Flux Kontext Dev双人互动脸部一致性增强加速版V0.5_1940000386315096066
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev双人互动脸部一致性增强加速版V0.5_1940000386315096066.json
hash: 6dc89354b3639b95
coverage: 0.888889
learned_at: 2026-10-23 10:57:02
nodes: [FluxGuidance, ReferenceLatent, ShowText|pysssss, DualCLIPLoader, VAELoader, ConditioningZeroOut, ImageStitch, VAEEncode, CLIPTextEncode, RH_Translator, KSampler, ImageConcatMulti, VAEDecode, Text Multiline, UnetLoaderGGUF, MagCache, LoadImage, LoraLoaderModelOnly, LoadImage, Note, Note, SaveImage, SaveImage, FluxKontextImageScale, LoadImage, LoadImage, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 326028119372116, "steps": 20}
---

# 图片生成/图生图/Flux Kontext Dev双人互动脸部一致性增强加速版V0.5_1940000386315096066.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev双人互动脸部一致性增强加速版V0.5_1940000386315096066.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `FluxGuidance`
- `ReferenceLatent`
- `ShowText|pysssss`
- `DualCLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `ImageStitch`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `RH_Translator`
- `KSampler` ★核心
- `ImageConcatMulti`
- `VAEDecode` ★核心
- `Text Multiline`
- `UnetLoaderGGUF` ★核心
- `MagCache`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `Note`
- `Note`
- `SaveImage`
- `SaveImage`
- `FluxKontextImageScale`
- `LoadImage`
- `LoadImage`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `326028119372116`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`FluxGuidance`、`ReferenceLatent`、`DualCLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`ImageStitch`、`VAEEncode`、`CLIPTextEncode`、`RH_Translator`、`KSampler`、`ImageConcatMulti`、`VAEDecode`、`Text Multiline`、`UnetLoaderGGUF`、`MagCache`、`LoadImage`、`LoraLoaderModelOnly`、`SaveImage`、`FluxKontextImageScale`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
