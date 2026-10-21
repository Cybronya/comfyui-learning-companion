---
key: 图片生成/图生图/溶图打光-F.2_Klein人像细节迁移_2096170592125939714.json
name: 溶图打光-F.2_Klein人像细节迁移_2096170592125939714
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/溶图打光-F.2_Klein人像细节迁移_2096170592125939714.json
hash: 25894a7a74eda3f3
coverage: 0.95
learned_at: 2026-10-21 00:54:56
nodes: [CLIPLoader, LoraLoaderModelOnly, UNETLoader, ImpactInt, ConditioningZeroOut, KSampler, VAELoader, VAEDecode, ReferenceLatent, VAEEncode, LayerMask: LoadBiRefNetModelV2, LayerUtility: ImageMaskScaleAs, LayerUtility: HLFrequencyDetailRestore, LayerMask: MaskGrow, Image Comparer (rgthree), CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, LayerMask: BiRefNetUltraV2, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1089784239158163, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/溶图打光-F.2_Klein人像细节迁移_2096170592125939714.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/溶图打光-F.2_Klein人像细节迁移_2096170592125939714.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
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
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `LayerMask: BiRefNetUltraV2`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1089784239158163`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`ImpactInt`、`ConditioningZeroOut`、`KSampler`、`VAELoader`、`VAEDecode`、`ReferenceLatent`、`VAEEncode`、`LayerMask: LoadBiRefNetModelV2`、`LayerUtility: ImageMaskScaleAs`、`LayerUtility: HLFrequencyDetailRestore`、`LayerMask: MaskGrow`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`LayerMask: BiRefNetUltraV2`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
