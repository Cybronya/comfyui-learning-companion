---
key: 平台全量/F.2 Klein万物电商光影融合溶图打光产品场景合成阴影生成细节迁移海报合成_2018259477744586754.json
name: F.2 Klein万物电商光影融合溶图打光产品场景合成阴影生成细节迁移海报合成_2018259477744586754
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/F.2 Klein万物电商光影融合溶图打光产品场景合成阴影生成细节迁移海报合成_2018259477744586754.json
hash: c58c037ac1443076
coverage: 0.934783
learned_at: 2026-11-14 00:24:05
nodes: [Fast Groups Bypasser (rgthree), LoadImage, Image Comparer (rgthree), CLIPLoader, LoraLoaderModelOnly, UNETLoader, CLIPTextEncode, ImpactInt, ConditioningZeroOut, KSampler, VAELoader, VAEDecode, ReferenceLatent, VAEEncode, LayerMask: LoadBiRefNetModelV2, LayerMask: BiRefNetUltraV2, LayerUtility: ImageMaskScaleAs, LayerUtility: HLFrequencyDetailRestore, LayerMask: MaskGrow, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, Image Comparer (rgthree), CLIPLoader, LoraLoaderModelOnly, CLIPTextEncode, ImpactInt, ConditioningZeroOut, KSampler, VAELoader, VAEDecode, ReferenceLatent, VAEEncode, LayerMask: LoadBiRefNetModelV2, LayerMask: BiRefNetUltraV2, UNETLoader, FastCanvasTool, ImageCropper, LoadImage, easy imageRemBg, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, FastCanvas, SaveImage, LayerUtility: ImageMaskScaleAs, LayerMask: MaskGrow, LayerUtility: HLFrequencyDetailRestore]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 407807370973685, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/F.2 Klein万物电商光影融合溶图打光产品场景合成阴影生成细节迁移海报合成_2018259477744586754.json

> 来源文件 `comfyui_library/workflows/平台全量/F.2 Klein万物电商光影融合溶图打光产品场景合成阴影生成细节迁移海报合成_2018259477744586754.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `Image Comparer (rgthree)`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
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
- `LayerUtility: HLFrequencyDetailRestore`
- `LayerMask: MaskGrow`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
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

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `407807370973685`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（43/46）

**有卡**：`LoadImage`、`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPTextEncode`、`ImpactInt`、`ConditioningZeroOut`、`KSampler`、`VAELoader`、`VAEDecode`、`ReferenceLatent`、`VAEEncode`、`LayerMask: LoadBiRefNetModelV2`、`LayerMask: BiRefNetUltraV2`、`LayerUtility: ImageMaskScaleAs`、`LayerUtility: HLFrequencyDetailRestore`、`LayerMask: MaskGrow`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`FastCanvasTool`、`ImageCropper`、`easy imageRemBg`、`FastCanvas`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
