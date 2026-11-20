---
key: 平台全量/F.2Kiein批量消除指定内容物品文字海报水印高清放大_2018638617152851970.json
name: F.2Kiein批量消除指定内容物品文字海报水印高清放大_2018638617152851970
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/F.2Kiein批量消除指定内容物品文字海报水印高清放大_2018638617152851970.json
hash: 4299f31e6acd84fe
coverage: 0.873418
learned_at: 2026-11-14 00:24:07
nodes: [RHUploadZip_V2, LoraLoaderModelOnly, UNETLoader, CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, ConditioningZeroOut, VAEEncode, VAELoader, KSampler, ReferenceLatent, VAEDecode, HAIGC_SaveImagesToZip, SaveImage, Image Comparer (rgthree), CLIPTextEncode, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, Note, Note, ReferenceLatent, VAEEncode, VAEDecode, LoraLoaderModelOnly, VAELoader, ConditioningZeroOut, LayerUtility: ImageScaleByAspectRatio V2, KSampler, ImageResize+, ImageResize+, Get Image Size, TTP_Image_Tile_Batch, DF_Integer, DF_Integer, SimpleMath+, ImageCASharpening+, easy cleanGpuUsed, SeedVR2, TTP_Image_Assy, ImageCASharpening+, HAIGC_SaveImagesToZip, SaveImage, Image Comparer (rgthree), ImpactMinMax, CLIPTextEncode, CLIPLoader, UNETLoader, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, CLIPTextEncode, UNETLoader, Note, Note, ConditioningZeroOut, VAEEncode, ReferenceLatent, KSampler, VAELoader, LoraLoaderModelOnly, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, ImageResize+, TTP_Image_Tile_Batch, Get Image Size, TTP_Image_Assy, ImageResize+, ImpactMinMax, ImageCASharpening+, easy cleanGpuUsed, SeedVR2, ImageCASharpening+, DF_Integer, DF_Integer, SimpleMath+, SaveImage, Image Comparer (rgthree), Fast Groups Bypasser (rgthree), RHUploadZip_V2]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 120088496122281, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/F.2Kiein批量消除指定内容物品文字海报水印高清放大_2018638617152851970.json

> 来源文件 `comfyui_library/workflows/平台全量/F.2Kiein批量消除指定内容物品文字海报水印高清放大_2018638617152851970.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（79 个）：
- `RHUploadZip_V2`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `VAELoader`
- `KSampler` ★核心
- `ReferenceLatent`
- `VAEDecode` ★核心
- `HAIGC_SaveImagesToZip`
- `SaveImage`
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `Note`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `ConditioningZeroOut`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `ImageResize+`
- `ImageResize+`
- `Get Image Size`
- `TTP_Image_Tile_Batch`
- `DF_Integer`
- `DF_Integer`
- `SimpleMath+`
- `ImageCASharpening+`
- `easy cleanGpuUsed`
- `SeedVR2`
- `TTP_Image_Assy`
- `ImageCASharpening+`
- `HAIGC_SaveImagesToZip`
- `SaveImage`
- `Image Comparer (rgthree)`
- `ImpactMinMax`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `Note`
- `Note`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `KSampler` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResize+`
- `TTP_Image_Tile_Batch`
- `Get Image Size`
- `TTP_Image_Assy`
- `ImageResize+`
- `ImpactMinMax`
- `ImageCASharpening+`
- `easy cleanGpuUsed`
- `SeedVR2`
- `ImageCASharpening+`
- `DF_Integer`
- `DF_Integer`
- `SimpleMath+`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `RHUploadZip_V2`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `120088496122281`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（69/79）

**有卡**：`RHUploadZip_V2`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ConditioningZeroOut`、`VAEEncode`、`VAELoader`、`KSampler`、`ReferenceLatent`、`VAEDecode`、`HAIGC_SaveImagesToZip`、`SaveImage`、`CLIPTextEncode`、`ImageResize+`、`Get Image Size`、`TTP_Image_Tile_Batch`、`DF_Integer`、`SimpleMath+`、`ImageCASharpening+`、`easy cleanGpuUsed`、`SeedVR2`、`TTP_Image_Assy`、`ImpactMinMax`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LayerUtility: ImageScaleByAspectRatio V2

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
