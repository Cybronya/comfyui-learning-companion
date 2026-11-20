---
key: 平台全量/F.2 Klein人像溶图打光光影融合溶图打光产品场景合成阴影生成细节迁移海报合成_2044633210293850114.json
name: F.2 Klein人像溶图打光光影融合溶图打光产品场景合成阴影生成细节迁移海报合成_2044633210293850114
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/F.2 Klein人像溶图打光光影融合溶图打光产品场景合成阴影生成细节迁移海报合成_2044633210293850114.json
hash: 89704e92bcb902ee
coverage: 0.934783
learned_at: 2026-11-14 00:24:06
nodes: [Fast Groups Bypasser (rgthree), CLIPLoader, LoraLoaderModelOnly, UNETLoader, ImpactInt, ConditioningZeroOut, KSampler, VAELoader, VAEDecode, ReferenceLatent, VAEEncode, LayerMask: LoadBiRefNetModelV2, LayerUtility: ImageMaskScaleAs, LayerUtility: HLFrequencyDetailRestore, LayerMask: MaskGrow, Image Comparer (rgthree), CLIPLoader, LoraLoaderModelOnly, CLIPTextEncode, ImpactInt, ConditioningZeroOut, KSampler, VAELoader, VAEDecode, ReferenceLatent, VAEEncode, LayerMask: LoadBiRefNetModelV2, LayerMask: BiRefNetUltraV2, UNETLoader, FastCanvasTool, ImageCropper, LoadImage, easy imageRemBg, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, FastCanvas, SaveImage, LayerUtility: ImageMaskScaleAs, LayerMask: MaskGrow, LayerUtility: HLFrequencyDetailRestore, Image Comparer (rgthree), CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, LayerMask: BiRefNetUltraV2, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 703608832437165, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/F.2 Klein人像溶图打光光影融合溶图打光产品场景合成阴影生成细节迁移海报合成_2044633210293850114.json

> 来源文件 `comfyui_library/workflows/平台全量/F.2 Klein人像溶图打光光影融合溶图打光产品场景合成阴影生成细节迁移海报合成_2044633210293850114.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `Fast Groups Bypasser (rgthree)`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ImpactInt`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `LayerMask: LoadBiRefNetModelV2`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: HLFrequencyDetailRestore`
- `LayerMask: MaskGrow`
- `Image Comparer (rgthree)`
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
- `UNETLoader` ★核心
- `FastCanvasTool`
- `ImageCropper`
- `LoadImage`
- `easy imageRemBg`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FastCanvas`
- `SaveImage`
- `LayerUtility: ImageMaskScaleAs`
- `LayerMask: MaskGrow`
- `LayerUtility: HLFrequencyDetailRestore`
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `LayerMask: BiRefNetUltraV2`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `703608832437165`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（43/46）

**有卡**：`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`ImpactInt`、`ConditioningZeroOut`、`KSampler`、`VAELoader`、`VAEDecode`、`ReferenceLatent`、`VAEEncode`、`LayerMask: LoadBiRefNetModelV2`、`LayerUtility: ImageMaskScaleAs`、`LayerUtility: HLFrequencyDetailRestore`、`LayerMask: MaskGrow`、`CLIPTextEncode`、`LayerMask: BiRefNetUltraV2`、`FastCanvasTool`、`ImageCropper`、`LoadImage`、`easy imageRemBg`、`LayerUtility: ImageScaleByAspectRatio V2`、`FastCanvas`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
