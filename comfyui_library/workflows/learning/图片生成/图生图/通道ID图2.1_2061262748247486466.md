---
key: 图片生成/图生图/通道ID图2.1_2061262748247486466.json
name: 通道ID图2.1_2061262748247486466
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/通道ID图2.1_2061262748247486466.json
hash: 7f36f1c3d5af41c0
coverage: 0.913043
learned_at: 2026-10-23 13:30:45
nodes: [LayerMask: BiRefNetUltraV2, LayerUtility: ImageMaskScaleAs, LayerMask: LoadBiRefNetModelV2, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, LayerStyle: ColorOverlay V2, UNETLoader, LayerMask: MaskGrow, LoadImage, Image Comparer (rgthree), SaveImage, PreviewImage, CLIPTextEncode, ConditioningZeroOut, VAEEncode, Text, LoraLoaderModelOnly, ReferenceLatent, Text, LoraLoaderModelOnly, KSampler, VAEDecode]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 229291508764674, "steps": 10}
---

# 图片生成/图生图/通道ID图2.1_2061262748247486466.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/通道ID图2.1_2061262748247486466.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `LayerMask: BiRefNetUltraV2`
- `LayerUtility: ImageMaskScaleAs`
- `LayerMask: LoadBiRefNetModelV2`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `LayerStyle: ColorOverlay V2`
- `UNETLoader` ★核心
- `LayerMask: MaskGrow`
- `LoadImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `Text`
- `LoraLoaderModelOnly` ★核心
- `ReferenceLatent`
- `Text`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `229291508764674`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`LayerMask: BiRefNetUltraV2`、`LayerUtility: ImageMaskScaleAs`、`LayerMask: LoadBiRefNetModelV2`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`LayerStyle: ColorOverlay V2`、`UNETLoader`、`LayerMask: MaskGrow`、`LoadImage`、`SaveImage`、`CLIPTextEncode`、`ConditioningZeroOut`、`VAEEncode`、`Text`、`LoraLoaderModelOnly`、`ReferenceLatent`、`KSampler`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
