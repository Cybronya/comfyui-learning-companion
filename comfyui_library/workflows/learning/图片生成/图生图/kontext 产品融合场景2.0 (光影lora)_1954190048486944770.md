---
key: 图片生成/图生图/kontext 产品融合场景2.0 (光影lora)_1954190048486944770.json
name: kontext 产品融合场景2.0 (光影lora)_1954190048486944770
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/kontext 产品融合场景2.0 (光影lora)_1954190048486944770.json
hash: 8a012763158698d0
coverage: 0.823529
learned_at: 2026-10-23 11:38:49
nodes: [CLIPTextEncode, FluxGuidance, LayerMask: BiRefNetUltraV2, FastCanvasTool, LayerMask: LoadBiRefNetModelV2, easy cleanGpuUsed, ConditioningZeroOut, ReferenceLatent, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, ImpactInt, VAEEncode, KSampler, UNETLoader, DualCLIPLoader, VAELoader, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), TextInput_, LoadImage, LoadImage, VAEDecode, FluxKontextImageScale, TextInput_, Anything Everywhere3, LoraLoaderModelOnly, SaveImage, LoadImage, Image Comparer (rgthree), easy imageDetailTransfer, PreviewImage, Fast Groups Bypasser (rgthree), FastCanvas, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 604257487947533, "steps": 20}
---

# 图片生成/图生图/kontext 产品融合场景2.0 (光影lora)_1954190048486944770.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/kontext 产品融合场景2.0 (光影lora)_1954190048486944770.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `LayerMask: BiRefNetUltraV2`
- `FastCanvasTool`
- `LayerMask: LoadBiRefNetModelV2`
- `easy cleanGpuUsed`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImpactInt`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `TextInput_`
- `LoadImage`
- `LoadImage`
- `VAEDecode` ★核心
- `FluxKontextImageScale`
- `TextInput_`
- `Anything Everywhere3`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `easy imageDetailTransfer`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `FastCanvas`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `604257487947533`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（28/34）

**有卡**：`CLIPTextEncode`、`FluxGuidance`、`LayerMask: BiRefNetUltraV2`、`FastCanvasTool`、`LayerMask: LoadBiRefNetModelV2`、`easy cleanGpuUsed`、`ConditioningZeroOut`、`ReferenceLatent`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImpactInt`、`VAEEncode`、`KSampler`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`TextInput_`、`LoadImage`、`VAEDecode`、`FluxKontextImageScale`、`LoraLoaderModelOnly`、`SaveImage`、`easy imageDetailTransfer`、`FastCanvas`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
