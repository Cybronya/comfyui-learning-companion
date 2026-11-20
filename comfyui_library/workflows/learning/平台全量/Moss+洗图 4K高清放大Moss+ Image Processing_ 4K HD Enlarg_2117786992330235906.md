---
key: 平台全量/Moss+洗图 4K高清放大Moss+ Image Processing_ 4K HD Enlarg_2117786992330235906.json
name: Moss+洗图 4K高清放大Moss+ Image Processing_ 4K HD Enlarg_2117786992330235906
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Moss+洗图 4K高清放大Moss+ Image Processing_ 4K HD Enlarg_2117786992330235906.json
hash: 63156b6f4f1ddd42
coverage: 0.923077
learned_at: 2026-11-14 00:46:40
nodes: [UNETLoader, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, SkipLayerGuidanceDiTSimple, KSampler, VAELoader, Note, VAEDecode, SaveImage, SaveImage, CLIPLoader, ResizeImageMaskNode, UNETLoader, VAELoader, VAEEncodeTiled, KSampler, SeedVR2Conditioning, VAEDecodeTiled, SeedVR2PostProcessing, 忽略多组孤海, LoadImage, VAEEncode, SeedVR2Preprocess, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 720131540241317, "steps": 1}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Moss+洗图 4K高清放大Moss+ Image Processing_ 4K HD Enlarg_2117786992330235906.json

> 来源文件 `comfyui_library/workflows/平台全量/Moss+洗图 4K高清放大Moss+ Image Processing_ 4K HD Enlarg_2117786992330235906.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SkipLayerGuidanceDiTSimple`
- `KSampler` ★核心
- `VAELoader`
- `Note`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `CLIPLoader`
- `ResizeImageMaskNode`
- `UNETLoader` ★核心
- `VAELoader`
- `VAEEncodeTiled` ★核心
- `KSampler` ★核心
- `SeedVR2Conditioning`
- `VAEDecodeTiled` ★核心
- `SeedVR2PostProcessing`
- `忽略多组孤海`
- `LoadImage`
- `VAEEncode` ★核心
- `SeedVR2Preprocess`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `720131540241317`
- `steps` = `1`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（24/26）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`SkipLayerGuidanceDiTSimple`、`KSampler`、`VAELoader`、`VAEDecode`、`SaveImage`、`CLIPLoader`、`ResizeImageMaskNode`、`VAEEncodeTiled`、`SeedVR2Conditioning`、`VAEDecodeTiled`、`SeedVR2PostProcessing`、`忽略多组孤海`、`LoadImage`、`VAEEncode`、`SeedVR2Preprocess`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
