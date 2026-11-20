---
key: 平台全量/Flux_ControlNet Upscaler 高清放大修复_1955922621080764417.json
name: Flux_ControlNet Upscaler 高清放大修复_1955922621080764417
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux_ControlNet Upscaler 高清放大修复_1955922621080764417.json
hash: dba5b476ac142ef6
coverage: 0.666667
learned_at: 2026-11-14 00:30:12
nodes: [Note, LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, DualCLIPLoader, Reroute, CLIPTextEncode, CLIPTextEncode, VAEEncode, ShowText|pysssss, PreviewImage, PreviewImage, Image Comparer (rgthree), Image Comparer (rgthree), Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, ImageScaleToTotalPixels, ImageScaleBy, VAELoader, FluxGuidance, KSampler, UNETLoader, ConditioningZeroOut, Note, VAEDecode, RHHiddenNodes, VAEDecode, RHHiddenNodes, SaveImage, Reroute, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1049993586825334, "steps": 20}
---

# 平台全量/Flux_ControlNet Upscaler 高清放大修复_1955922621080764417.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux_ControlNet Upscaler 高清放大修复_1955922621080764417.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `Note`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `DualCLIPLoader`
- `Reroute`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `ShowText|pysssss`
- `PreviewImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageScaleToTotalPixels`
- `ImageScaleBy`
- `VAELoader`
- `FluxGuidance`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `Note`
- `VAEDecode` ★核心
- `RHHiddenNodes`
- `VAEDecode` ★核心
- `RHHiddenNodes`
- `SaveImage`
- `Reroute`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1049993586825334`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **67%**（20/30）

**有卡**：`LayerUtility: JoyCaptionBeta1`、`LayerUtility: LoadJoyCaptionBeta1Model`、`DualCLIPLoader`、`CLIPTextEncode`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageScaleToTotalPixels`、`ImageScaleBy`、`VAELoader`、`FluxGuidance`、`KSampler`、`UNETLoader`、`ConditioningZeroOut`、`VAEDecode`、`RHHiddenNodes`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
