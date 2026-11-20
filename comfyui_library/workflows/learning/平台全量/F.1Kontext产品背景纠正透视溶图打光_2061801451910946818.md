---
key: 平台全量/F.1Kontext产品背景纠正透视溶图打光_2061801451910946818.json
name: F.1Kontext产品背景纠正透视溶图打光_2061801451910946818
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/F.1Kontext产品背景纠正透视溶图打光_2061801451910946818.json
hash: 8b8468610e4cc653
coverage: 0.891892
learned_at: 2026-11-14 00:24:03
nodes: [Label (rgthree), LoraLoaderModelOnly, FluxGuidance, UNETLoader, ConditioningZeroOut, Note, DualCLIPLoader, LoadImage, Image Comparer (rgthree), SaveImage, KSampler, VAELoader, CLIPTextEncode, ImpactInt, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, VAEDecode, ReferenceLatent, Label (rgthree), LoraLoaderModelOnly, FluxGuidance, UNETLoader, ConditioningZeroOut, DualCLIPLoader, KSampler, VAELoader, CLIPTextEncode, ImpactInt, VAEEncode, ReferenceLatent, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, RHUploadZip_V2, SaveImage, HAIGC_SaveImagesToZip, Fast Groups Bypasser (rgthree), Note]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 624114829655944, "steps": 30}
---

# 平台全量/F.1Kontext产品背景纠正透视溶图打光_2061801451910946818.json

> 来源文件 `comfyui_library/workflows/平台全量/F.1Kontext产品背景纠正透视溶图打光_2061801451910946818.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `Label (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `FluxGuidance`
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `Note`
- `DualCLIPLoader`
- `LoadImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `KSampler` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ImpactInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `ReferenceLatent`
- `Label (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `FluxGuidance`
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSampler` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ImpactInt`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `RHUploadZip_V2`
- `SaveImage`
- `HAIGC_SaveImagesToZip`
- `Fast Groups Bypasser (rgthree)`
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `624114829655944`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（33/37）

**有卡**：`Label (rgthree)`、`LoraLoaderModelOnly`、`FluxGuidance`、`UNETLoader`、`ConditioningZeroOut`、`DualCLIPLoader`、`LoadImage`、`SaveImage`、`KSampler`、`VAELoader`、`CLIPTextEncode`、`ImpactInt`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEEncode`、`VAEDecode`、`ReferenceLatent`、`RHUploadZip_V2`、`HAIGC_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
