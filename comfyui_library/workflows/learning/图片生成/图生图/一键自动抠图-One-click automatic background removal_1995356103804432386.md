---
key: 图片生成/图生图/一键自动抠图-One-click automatic background removal_1995356103804432386.json
name: 一键自动抠图-One-click automatic background removal_1995356103804432386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/一键自动抠图-One-click automatic background removal_1995356103804432386.json
hash: 97c80e8eb9383081
coverage: 1
learned_at: 2026-10-23 11:58:41
nodes: [RH_Translator, easy int, LazySwitch1way, GetImageRangeFromBatch, easy sam3ImageSegmentation, easy batchAnything, LayerUtility: ImageRemoveAlpha, easy batchAnything, easy forLoopStart, MathExpression|pysssss, ImageListToBatch+, easy boolean, easy forLoopEnd, easy forLoopEnd, GetImageSizeAndCount, easy int, easy int, ImageListToBatch+, ResizeImageMixlab, LazySwitch2way, BiRefNetRMBG, BiRefNetRMBG, easy sam3ImageSegmentation, LoadImage, CR Text, RHUploadZip, easy boolean, CompressImages, CompressImages, easy sam3ModelLoader, LoadImage, ResizeImageMixlab]
patterns: []
missing: []
---

# 图片生成/图生图/一键自动抠图-One-click automatic background removal_1995356103804432386.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/一键自动抠图-One-click automatic background removal_1995356103804432386.json`

## 结构

**生成流程**：Model → Process → Other

**节点**（32 个）：
- `RH_Translator`
- `easy int`
- `LazySwitch1way`
- `GetImageRangeFromBatch`
- `easy sam3ImageSegmentation`
- `easy batchAnything`
- `LayerUtility: ImageRemoveAlpha`
- `easy batchAnything`
- `easy forLoopStart`
- `MathExpression|pysssss`
- `ImageListToBatch+`
- `easy boolean`
- `easy forLoopEnd`
- `easy forLoopEnd`
- `GetImageSizeAndCount`
- `easy int`
- `easy int`
- `ImageListToBatch+`
- `ResizeImageMixlab`
- `LazySwitch2way`
- `BiRefNetRMBG`
- `BiRefNetRMBG`
- `easy sam3ImageSegmentation`
- `LoadImage`
- `CR Text`
- `RHUploadZip`
- `easy boolean`
- `CompressImages`
- `CompressImages`
- `easy sam3ModelLoader`
- `LoadImage`
- `ResizeImageMixlab`

## 知识

覆盖率 **100%**（32/32）

**有卡**：`RH_Translator`、`easy int`、`LazySwitch1way`、`GetImageRangeFromBatch`、`easy sam3ImageSegmentation`、`easy batchAnything`、`LayerUtility: ImageRemoveAlpha`、`easy forLoopStart`、`MathExpression|pysssss`、`ImageListToBatch+`、`easy boolean`、`easy forLoopEnd`、`GetImageSizeAndCount`、`ResizeImageMixlab`、`LazySwitch2way`、`BiRefNetRMBG`、`LoadImage`、`CR Text`、`RHUploadZip`、`CompressImages`、`easy sam3ModelLoader`

**用到的条目**：LoadImage、GetImageSizeAndCount、ResizeImageMixlab、GetImageRangeFromBatch、RH_Translator、BiRefNetRMBG、LazySwitch2way、RHUploadZip
