---
key: 图片生成/图生图/F.2_Klein万物电商光影融合溶图打光产品场景合成阴影生成细节迁移海报合成_2092059751491395585.json
name: F.2_Klein万物电商光影融合溶图打光产品场景合成阴影生成细节迁移海报合成_2092059751491395585
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2_Klein万物电商光影融合溶图打光产品场景合成阴影生成细节迁移海报合成_2092059751491395585.json
hash: 5917c369ee683b0d
coverage: 0.93617
learned_at: 2026-10-21 00:38:59
nodes: [ImpactInt, Image Comparer (rgthree), CLIPLoader, LoraLoaderModelOnly, CLIPTextEncode, ImpactInt, ConditioningZeroOut, KSampler, VAELoader, VAEDecode, ReferenceLatent, VAEEncode, LayerMask: LoadBiRefNetModelV2, LayerMask: BiRefNetUltraV2, UNETLoader, FastCanvasTool, ImageCropper, LoadImage, easy imageRemBg, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, LayerUtility: ImageMaskScaleAs, LayerMask: MaskGrow, LayerUtility: HLFrequencyDetailRestore, ReferenceLatent, LoadImage, CLIPLoader, FastCanvas, LoraLoaderModelOnly, UNETLoader, CLIPTextEncode, LoraLoaderModelOnly, Image Comparer (rgthree), SaveImage, Fast Groups Bypasser (rgthree), LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, VAELoader, KSampler, VAEDecode, ConditioningZeroOut, LayerMask: MaskGrow, LayerUtility: ImageMaskScaleAs, LayerMask: LoadBiRefNetModelV2, LayerUtility: HLFrequencyDetailRestore, LayerMask: BiRefNetUltraV2]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 220661967752502, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/F.2_Klein万物电商光影融合溶图打光产品场景合成阴影生成细节迁移海报合成_2092059751491395585.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2_Klein万物电商光影融合溶图打光产品场景合成阴影生成细节迁移海报合成_2092059751491395585.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `ImpactInt`
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
- `SaveImage`
- `LayerUtility: ImageMaskScaleAs`
- `LayerMask: MaskGrow`
- `LayerUtility: HLFrequencyDetailRestore`
- `ReferenceLatent`
- `LoadImage`
- `CLIPLoader`
- `FastCanvas`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEEncode` ★核心
- `VAELoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `LayerMask: MaskGrow`
- `LayerUtility: ImageMaskScaleAs`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerUtility: HLFrequencyDetailRestore`
- `LayerMask: BiRefNetUltraV2`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `220661967752502`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（44/47）

**有卡**：`ImpactInt`、`CLIPLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`ConditioningZeroOut`、`KSampler`、`VAELoader`、`VAEDecode`、`ReferenceLatent`、`VAEEncode`、`LayerMask: LoadBiRefNetModelV2`、`LayerMask: BiRefNetUltraV2`、`UNETLoader`、`FastCanvasTool`、`ImageCropper`、`LoadImage`、`easy imageRemBg`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`LayerUtility: ImageMaskScaleAs`、`LayerMask: MaskGrow`、`LayerUtility: HLFrequencyDetailRestore`、`FastCanvas`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
