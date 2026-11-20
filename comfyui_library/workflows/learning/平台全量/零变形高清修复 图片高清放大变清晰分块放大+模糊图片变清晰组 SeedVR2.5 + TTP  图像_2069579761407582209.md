---
key: 平台全量/零变形高清修复 图片高清放大变清晰分块放大+模糊图片变清晰组 SeedVR2.5 + TTP  图像_2069579761407582209.json
name: 零变形高清修复 图片高清放大变清晰分块放大+模糊图片变清晰组 SeedVR2.5 + TTP  图像_2069579761407582209
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/零变形高清修复 图片高清放大变清晰分块放大+模糊图片变清晰组 SeedVR2.5 + TTP  图像_2069579761407582209.json
hash: 79d5d44394a009d3
coverage: 0.842105
learned_at: 2026-11-14 02:49:56
nodes: [LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, ConditioningZeroOut, easy imageListToImageBatch, GetNode, KSampler, GetImageSize, CLIPLoader, VAELoader, GetImageSize, MemoryCleaner, SetNode, SimpleMath+, TTP_Image_Assy, Note, LCSLoadData, Note, UNETLoader, Image Comparer (rgthree), easy imageBatchToImageList, LayerUtility: ImageScaleByAspectRatio V2, easy imageColorMatch, LayerUtility: ImageScaleRestore V2, Flux2KleinEditTextEncode_EditUtils, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LCSColorAnchor, TTP_Image_Tile_Batch, INTConstant, TTP_Tile_image_size, PreviewImage, MathExpression|pysssss, MathExpression|pysssss, LCSSharpnessCalibrate, LCSSharpnessIntervene, LoadImage, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 296277071464552, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/零变形高清修复 图片高清放大变清晰分块放大+模糊图片变清晰组 SeedVR2.5 + TTP  图像_2069579761407582209.json

> 来源文件 `comfyui_library/workflows/平台全量/零变形高清修复 图片高清放大变清晰分块放大+模糊图片变清晰组 SeedVR2.5 + TTP  图像_2069579761407582209.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `easy imageListToImageBatch`
- `GetNode`
- `KSampler` ★核心
- `GetImageSize`
- `CLIPLoader`
- `VAELoader`
- `GetImageSize`
- `MemoryCleaner`
- `SetNode`
- `SimpleMath+`
- `TTP_Image_Assy`
- `Note`
- `LCSLoadData`
- `Note`
- `UNETLoader` ★核心
- `Image Comparer (rgthree)`
- `easy imageBatchToImageList`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy imageColorMatch`
- `LayerUtility: ImageScaleRestore V2`
- `Flux2KleinEditTextEncode_EditUtils`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LCSColorAnchor`
- `TTP_Image_Tile_Batch`
- `INTConstant`
- `TTP_Tile_image_size`
- `PreviewImage`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `LCSSharpnessCalibrate`
- `LCSSharpnessIntervene`
- `LoadImage`
- `SaveImage`

## 关键参数

- `seed` = `296277071464552`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **84%**（32/38）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`ConditioningZeroOut`、`easy imageListToImageBatch`、`KSampler`、`GetImageSize`、`CLIPLoader`、`VAELoader`、`MemoryCleaner`、`SimpleMath+`、`TTP_Image_Assy`、`LCSLoadData`、`UNETLoader`、`easy imageBatchToImageList`、`easy imageColorMatch`、`LayerUtility: ImageScaleRestore V2`、`Flux2KleinEditTextEncode_EditUtils`、`LoraLoaderModelOnly`、`LCSColorAnchor`、`TTP_Image_Tile_Batch`、`INTConstant`、`TTP_Tile_image_size`、`MathExpression|pysssss`、`LCSSharpnessCalibrate`、`LCSSharpnessIntervene`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
