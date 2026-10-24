---
key: 图片生成/图生图/ComfyUI产品精修｜Flux.2 Klein去背景透明输出，全节点注释_2061069418087669761.json
name: ComfyUI产品精修｜Flux.2 Klein去背景透明输出，全节点注释_2061069418087669761
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/ComfyUI产品精修｜Flux.2 Klein去背景透明输出，全节点注释_2061069418087669761.json
hash: aa76d6d2865ff602
coverage: 0.482759
learned_at: 2026-10-23 10:51:59
nodes: [LayerMask: BiRefNetUltraV2, GrowMask, InvertMask, LayerMask: LoadBiRefNetModelV2, JjkText, easy promptConcat, CLIPLoader, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, UNETLoader, Float, FluxGuidance, VAEEncode, ImpactInt, LoraLoaderModelOnly, Float, ReferenceLatent, ConditioningZeroOut, EmptyFlux2LatentImage, KSampler, JoinImageWithAlpha, SaveImage, SaveImage, LoadImage, VAEDecode, CR Text, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, LoadImage, LoadImage, JjkText]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 903953545887025, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/ComfyUI产品精修｜Flux.2 Klein去背景透明输出，全节点注释_2061069418087669761.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/ComfyUI产品精修｜Flux.2 Klein去背景透明输出，全节点注释_2061069418087669761.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `LayerMask: BiRefNetUltraV2`
- `GrowMask`
- `InvertMask`
- `LayerMask: LoadBiRefNetModelV2`
- `JjkText`
- `easy promptConcat`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `UNETLoader` ★核心
- `Float`
- `FluxGuidance`
- `VAEEncode` ★核心
- `ImpactInt`
- `LoraLoaderModelOnly` ★核心
- `Float`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `KSampler` ★核心
- `JoinImageWithAlpha`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `VAEDecode` ★核心
- `CR Text`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`
- `JjkText`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `903953545887025`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **48%**（28/58）

**有卡**：`LayerMask: BiRefNetUltraV2`、`GrowMask`、`InvertMask`、`LayerMask: LoadBiRefNetModelV2`、`easy promptConcat`、`CLIPLoader`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`UNETLoader`、`Float`、`FluxGuidance`、`VAEEncode`、`ImpactInt`、`LoraLoaderModelOnly`、`ReferenceLatent`、`ConditioningZeroOut`、`EmptyFlux2LatentImage`、`KSampler`、`JoinImageWithAlpha`、`SaveImage`、`LoadImage`、`VAEDecode`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
