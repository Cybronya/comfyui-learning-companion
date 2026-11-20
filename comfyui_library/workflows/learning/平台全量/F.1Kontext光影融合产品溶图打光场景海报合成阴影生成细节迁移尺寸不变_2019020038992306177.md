---
key: 平台全量/F.1Kontext光影融合产品溶图打光场景海报合成阴影生成细节迁移尺寸不变_2019020038992306177.json
name: F.1Kontext光影融合产品溶图打光场景海报合成阴影生成细节迁移尺寸不变_2019020038992306177
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/F.1Kontext光影融合产品溶图打光场景海报合成阴影生成细节迁移尺寸不变_2019020038992306177.json
hash: 14cf9c675f39da06
coverage: 0.909091
learned_at: 2026-11-14 00:24:03
nodes: [Label (rgthree), SaveImage, Image Comparer (rgthree), LoraLoaderModelOnly, KSampler, LayerUtility: HLFrequencyDetailRestore, LayerUtility: ImageMaskScaleAs, LayerMask: MaskGrow, InspyrenetRembg, FluxGuidance, UNETLoader, LoadImage, DualCLIPLoader, ConditioningZeroOut, CLIPTextEncode, VAELoader, VAEDecode, VAEEncode, ImpactInt, LayerUtility: ImageScaleByAspectRatio V2, ReferenceLatent, LayerMask: MaskGrow, DualCLIPLoader, CLIPTextEncode, VAEEncode, FluxGuidance, LoraLoaderModelOnly, UNETLoader, LayerUtility: HLFrequencyDetailRestore, LayerUtility: ImageScaleByAspectRatio V2, ReferenceLatent, ImpactInt, ConditioningZeroOut, VAELoader, KSampler, LayerUtility: ImageMaskScaleAs, InspyrenetRembg, VAEDecode, HAIGC_SaveImagesToZip, SaveImage, RHUploadZip_V2, Fast Groups Bypasser (rgthree), Note, Note]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 849987416730093, "steps": 30}
---

# 平台全量/F.1Kontext光影融合产品溶图打光场景海报合成阴影生成细节迁移尺寸不变_2019020038992306177.json

> 来源文件 `comfyui_library/workflows/平台全量/F.1Kontext光影融合产品溶图打光场景海报合成阴影生成细节迁移尺寸不变_2019020038992306177.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `Label (rgthree)`
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `LayerUtility: HLFrequencyDetailRestore`
- `LayerUtility: ImageMaskScaleAs`
- `LayerMask: MaskGrow`
- `InspyrenetRembg`
- `FluxGuidance`
- `UNETLoader` ★核心
- `LoadImage`
- `DualCLIPLoader`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `ImpactInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ReferenceLatent`
- `LayerMask: MaskGrow`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `FluxGuidance`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LayerUtility: HLFrequencyDetailRestore`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ReferenceLatent`
- `ImpactInt`
- `ConditioningZeroOut`
- `VAELoader`
- `KSampler` ★核心
- `LayerUtility: ImageMaskScaleAs`
- `InspyrenetRembg`
- `VAEDecode` ★核心
- `HAIGC_SaveImagesToZip`
- `SaveImage`
- `RHUploadZip_V2`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `849987416730093`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（40/44）

**有卡**：`Label (rgthree)`、`SaveImage`、`LoraLoaderModelOnly`、`KSampler`、`LayerUtility: HLFrequencyDetailRestore`、`LayerUtility: ImageMaskScaleAs`、`LayerMask: MaskGrow`、`InspyrenetRembg`、`FluxGuidance`、`UNETLoader`、`LoadImage`、`DualCLIPLoader`、`ConditioningZeroOut`、`CLIPTextEncode`、`VAELoader`、`VAEDecode`、`VAEEncode`、`ImpactInt`、`LayerUtility: ImageScaleByAspectRatio V2`、`ReferenceLatent`、`HAIGC_SaveImagesToZip`、`RHUploadZip_V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
