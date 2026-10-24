---
key: 图片生成/图生图/FLUX.2 Klein光影溶图+细节迁移+打光+放大_2046159873519394818.json
name: FLUX.2 Klein光影溶图+细节迁移+打光+放大_2046159873519394818
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2 Klein光影溶图+细节迁移+打光+放大_2046159873519394818.json
hash: 874ed77b305e4d2d
coverage: 0.923077
learned_at: 2026-10-23 10:54:06
nodes: [CLIPLoader, LoraLoaderModelOnly, CLIPTextEncode, ImpactInt, ConditioningZeroOut, KSampler, VAELoader, VAEDecode, ReferenceLatent, VAEEncode, LayerMask: LoadBiRefNetModelV2, LayerMask: BiRefNetUltraV2, LayerUtility: ImageMaskScaleAs, LayerMask: MaskGrow, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, Image Comparer (rgthree), SaveImage, LayerUtility: HLFrequencyDetailRestore, SeedVR2LoadDiTModel, ImageScaleBy, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SaveImage, Image Comparer (rgthree), LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 372371707997791, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FLUX.2 Klein光影溶图+细节迁移+打光+放大_2046159873519394818.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2 Klein光影溶图+细节迁移+打光+放大_2046159873519394818.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ImpactInt`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `LayerMask: LoadBiRefNetModelV2`
- `LayerMask: BiRefNetUltraV2`
- `LayerUtility: ImageMaskScaleAs`
- `LayerMask: MaskGrow`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `LayerUtility: HLFrequencyDetailRestore`
- `SeedVR2LoadDiTModel`
- `ImageScaleBy`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `372371707997791`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（24/26）

**有卡**：`CLIPLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`ImpactInt`、`ConditioningZeroOut`、`KSampler`、`VAELoader`、`VAEDecode`、`ReferenceLatent`、`VAEEncode`、`LayerMask: LoadBiRefNetModelV2`、`LayerMask: BiRefNetUltraV2`、`LayerUtility: ImageMaskScaleAs`、`LayerMask: MaskGrow`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`SaveImage`、`LayerUtility: HLFrequencyDetailRestore`、`SeedVR2LoadDiTModel`、`ImageScaleBy`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
