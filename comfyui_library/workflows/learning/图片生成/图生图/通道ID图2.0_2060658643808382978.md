---
key: 图片生成/图生图/通道ID图2.0_2060658643808382978.json
name: 通道ID图2.0_2060658643808382978
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/通道ID图2.0_2060658643808382978.json
hash: d81a3591a86ae57e
coverage: 0.95
learned_at: 2026-10-23 13:30:45
nodes: [LayerMask: BiRefNetUltraV2, LayerMask: MaskGrow, LayerUtility: ImageMaskScaleAs, KSampler, VAEEncode, ConditioningZeroOut, ReferenceLatent, LayerMask: LoadBiRefNetModelV2, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, LayerStyle: ColorOverlay V2, UNETLoader, LoadImage, Image Comparer (rgthree), SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 272339493563970, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/通道ID图2.0_2060658643808382978.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/通道ID图2.0_2060658643808382978.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: MaskGrow`
- `LayerUtility: ImageMaskScaleAs`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `ReferenceLatent`
- `LayerMask: LoadBiRefNetModelV2`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `LayerStyle: ColorOverlay V2`
- `UNETLoader` ★核心
- `LoadImage`
- `Image Comparer (rgthree)`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `272339493563970`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`LayerMask: BiRefNetUltraV2`、`LayerMask: MaskGrow`、`LayerUtility: ImageMaskScaleAs`、`KSampler`、`VAEEncode`、`ConditioningZeroOut`、`ReferenceLatent`、`LayerMask: LoadBiRefNetModelV2`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`VAEDecode`、`LayerStyle: ColorOverlay V2`、`UNETLoader`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
