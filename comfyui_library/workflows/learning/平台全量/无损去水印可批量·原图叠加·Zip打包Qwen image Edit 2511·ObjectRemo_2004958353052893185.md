---
key: 平台全量/无损去水印可批量·原图叠加·Zip打包Qwen image Edit 2511·ObjectRemo_2004958353052893185.json
name: 无损去水印可批量·原图叠加·Zip打包Qwen image Edit 2511·ObjectRemo_2004958353052893185
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/无损去水印可批量·原图叠加·Zip打包Qwen image Edit 2511·ObjectRemo_2004958353052893185.json
hash: 24329db930734ddd
coverage: 0.565217
learned_at: 2026-11-14 02:12:47
nodes: [QwenEditConfigPreparer, CLIPLoader, VAELoader, SetNode, VAEDecode, easy forLoopEnd, ConditioningZeroOut, TextEncodeQwenImageEditPlusCustom_lrzjason, QwenEditOutputExtractor, CropWithPadInfo, KSampler, GetImageSize+, MaskPreview, PreviewImage, SetNode, GetNode, PreviewAny, easy sam3ImageSegmentation, MaskPreview, GrowMask, easy sam3ModelLoader, GetNode, easy showAnything, GetNode, LayerUtility: PurgeVRAM, GetNode, easy batchAnything, CR Text, CR Text, PreviewAny, LoloSaveDirToZip, PreviewImage, SetNode, ImageResizeKJv2, LoraLoaderModelOnly, UNETLoader, PreviewImage, GrowMaskWithBlur, MaskPreview, SetNode, CR Image Input Switch, GetNode, SetNode, CR String To Number, QwenEditAdaptiveLongestEdge, PreviewAny, GetNode, PreviewImage, SaveImageKJ, ImageResizeKJv2, SetNode, GetNode, SetNode, CR Text, SetNode, CR Text, GetNode, Any Switch (rgthree), easy loadImagesForLoop, Reroute, GetNode, MaskPreview, LoadImage, SaveImage, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, PreviewImage, ImageComposite+, Image Comparer (rgthree)]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 1091359629774735, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/无损去水印可批量·原图叠加·Zip打包Qwen image Edit 2511·ObjectRemo_2004958353052893185.json

> 来源文件 `comfyui_library/workflows/平台全量/无损去水印可批量·原图叠加·Zip打包Qwen image Edit 2511·ObjectRemo_2004958353052893185.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `QwenEditConfigPreparer`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `VAEDecode` ★核心
- `easy forLoopEnd`
- `ConditioningZeroOut`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `QwenEditOutputExtractor`
- `CropWithPadInfo`
- `KSampler` ★核心
- `GetImageSize+`
- `MaskPreview`
- `PreviewImage`
- `SetNode`
- `GetNode`
- `PreviewAny`
- `easy sam3ImageSegmentation`
- `MaskPreview`
- `GrowMask`
- `easy sam3ModelLoader`
- `GetNode`
- `easy showAnything`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `easy batchAnything`
- `CR Text`
- `CR Text`
- `PreviewAny`
- `LoloSaveDirToZip`
- `PreviewImage`
- `SetNode`
- `ImageResizeKJv2`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `PreviewImage`
- `GrowMaskWithBlur`
- `MaskPreview`
- `SetNode`
- `CR Image Input Switch`
- `GetNode`
- `SetNode`
- `CR String To Number`
- `QwenEditAdaptiveLongestEdge`
- `PreviewAny`
- `GetNode`
- `PreviewImage`
- `SaveImageKJ`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `SetNode`
- `CR Text`
- `SetNode`
- `CR Text`
- `GetNode`
- `Any Switch (rgthree)`
- `easy loadImagesForLoop`
- `Reroute`
- `GetNode`
- `MaskPreview`
- `LoadImage`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `ImageComposite+`
- `Image Comparer (rgthree)`

## 关键参数

- `seed` = `1091359629774735`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **57%**（39/69）

**有卡**：`QwenEditConfigPreparer`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`easy forLoopEnd`、`ConditioningZeroOut`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`QwenEditOutputExtractor`、`CropWithPadInfo`、`KSampler`、`GetImageSize+`、`MaskPreview`、`easy sam3ImageSegmentation`、`GrowMask`、`easy sam3ModelLoader`、`LayerUtility: PurgeVRAM`、`easy batchAnything`、`CR Text`、`LoloSaveDirToZip`、`ImageResizeKJv2`、`LoraLoaderModelOnly`、`UNETLoader`、`GrowMaskWithBlur`、`CR Image Input Switch`、`CR String To Number`、`QwenEditAdaptiveLongestEdge`、`SaveImageKJ`、`easy loadImagesForLoop`、`LoadImage`、`SaveImage`、`ImageComposite+`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、SaveImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
