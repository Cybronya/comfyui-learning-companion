---
key: 图片生成/图生图/F.Kontext电商万物光影融合溶图产品打光_2057709154202120193.json
name: F.Kontext电商万物光影融合溶图产品打光_2057709154202120193
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.Kontext电商万物光影融合溶图产品打光_2057709154202120193.json
hash: 56bcf764f8995661
coverage: 0.941176
learned_at: 2026-10-23 10:52:56
nodes: [UNETLoader, LoadImage, DualCLIPLoader, FluxGuidance, ConditioningZeroOut, VAEEncode, ReferenceLatent, VAEDecode, KSampler, CLIPTextEncode, ImpactInt, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, Image Comparer (rgthree), SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 377940627801976, "steps": 12}
---

# 图片生成/图生图/F.Kontext电商万物光影融合溶图产品打光_2057709154202120193.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.Kontext电商万物光影融合溶图产品打光_2057709154202120193.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `UNETLoader` ★核心
- `LoadImage`
- `DualCLIPLoader`
- `FluxGuidance`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `ImpactInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `Image Comparer (rgthree)`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `377940627801976`
- `steps` = `12`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`UNETLoader`、`LoadImage`、`DualCLIPLoader`、`FluxGuidance`、`ConditioningZeroOut`、`VAEEncode`、`ReferenceLatent`、`VAEDecode`、`KSampler`、`CLIPTextEncode`、`ImpactInt`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`SaveImage`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
