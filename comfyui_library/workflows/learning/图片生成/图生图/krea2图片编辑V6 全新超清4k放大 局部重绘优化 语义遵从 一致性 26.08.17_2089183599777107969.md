---
key: 图片生成/图生图/krea2图片编辑V6 全新超清4k放大 局部重绘优化 语义遵从 一致性 26.08.17_2089183599777107969.json
name: krea2图片编辑V6 全新超清4k放大 局部重绘优化 语义遵从 一致性 26.08.17_2089183599777107969
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/krea2图片编辑V6 全新超清4k放大 局部重绘优化 语义遵从 一致性 26.08.17_2089183599777107969.json
hash: f6827e7e6cb39052
coverage: 0.766667
learned_at: 2026-10-15 22:25:35
nodes: [ExecutionBlocker, ExecutionBlocker, SaveLatent, PlaySound|pysssss, VAELoader, JjkText, Note, ImpactNeg, ExecutionBlocker, Reroute, ImageScaleToTotalPixels, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释, ImageRGBA2RGB, LoraLoaderModelOnly, CLIPLoader, VAEEncode, LoraLoaderModelOnly, KSampler, CM_BoolToInt, easy anythingIndexSwitch, VAELoader, CFGNorm, LoraLoaderModelOnly, VAELoader, GetImageSize, CM_BoolToInt, ImpactNeg, RH_RFMSR_ModelLoader, Int, Int, Int, 孤海注释, VAEEncode, VAEDecode, IntConditions, IntConditions, easy anythingIndexSwitch, 孤海注释, ImageScaleToTotalPixels, LayerUtility: PurgeVRAM, ExecutionBlocker, ExecutionBlocker, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, RH_RFMSR_Upscale, PrimitiveBoolean, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, ImageScaleToTotalPixels, GrowMaskWithBlur, UNETLoader, EmptySD3LatentImage, LoadImage, 1hew_TextToAny, 1hew_TextToAny, 孤海注释, 孤海注释, PrimitiveFloat, PrimitiveBoolean, 图像缩放V2_孤海, UpscaleModelLoader, Krea2EditGroundedEncode, JjkText, JjkText, easy mathString, easy mathString, CM_BoolToInt, easy anythingIndexSwitch, JjkText, StringReplace, StringReplace, Krea2EditModelPatch, Krea2EditModelPatch, PrimitiveFloat, PixelKSampleUpscalerProvider, IterativeImageUpscale, SaveImage, easy anythingIndexSwitch, RHLLMChatNode, easy anythingIndexSwitch, PreviewAny, Krea2EditGroundedEncode, StringReplace, PreviewAny]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 9565952208932, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/krea2图片编辑V6 全新超清4k放大 局部重绘优化 语义遵从 一致性 26.08.17_2089183599777107969.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/krea2图片编辑V6 全新超清4k放大 局部重绘优化 语义遵从 一致性 26.08.17_2089183599777107969.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（90 个）：
- `ExecutionBlocker`
- `ExecutionBlocker`
- `SaveLatent`
- `PlaySound|pysssss`
- `VAELoader`
- `JjkText`
- `Note`
- `ImpactNeg`
- `ExecutionBlocker`
- `Reroute`
- `ImageScaleToTotalPixels`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `ImageRGBA2RGB`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CM_BoolToInt`
- `easy anythingIndexSwitch`
- `VAELoader`
- `CFGNorm`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `GetImageSize`
- `CM_BoolToInt`
- `ImpactNeg`
- `RH_RFMSR_ModelLoader`
- `Int`
- `Int`
- `Int`
- `孤海注释`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `IntConditions`
- `IntConditions`
- `easy anythingIndexSwitch`
- `孤海注释`
- `ImageScaleToTotalPixels`
- `LayerUtility: PurgeVRAM`
- `ExecutionBlocker`
- `ExecutionBlocker`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly` ★核心
- `RH_RFMSR_Upscale`
- `PrimitiveBoolean`
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageScaleToTotalPixels`
- `GrowMaskWithBlur`
- `UNETLoader` ★核心
- `EmptySD3LatentImage`
- `LoadImage`
- `1hew_TextToAny`
- `1hew_TextToAny`
- `孤海注释`
- `孤海注释`
- `PrimitiveFloat`
- `PrimitiveBoolean`
- `图像缩放V2_孤海`
- `UpscaleModelLoader`
- `Krea2EditGroundedEncode`
- `JjkText`
- `JjkText`
- `easy mathString`
- `easy mathString`
- `CM_BoolToInt`
- `easy anythingIndexSwitch`
- `JjkText`
- `StringReplace`
- `StringReplace`
- `Krea2EditModelPatch`
- `Krea2EditModelPatch`
- `PrimitiveFloat`
- `PixelKSampleUpscalerProvider`
- `IterativeImageUpscale`
- `SaveImage`
- `easy anythingIndexSwitch`
- `RHLLMChatNode`
- `easy anythingIndexSwitch`
- `PreviewAny`
- `Krea2EditGroundedEncode`
- `StringReplace`
- `PreviewAny`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `9565952208932`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（69/90）

**有卡**：`ExecutionBlocker`、`SaveLatent`、`PlaySound|pysssss`、`VAELoader`、`ImpactNeg`、`ImageScaleToTotalPixels`、`ImageRGBA2RGB`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAEEncode`、`KSampler`、`CM_BoolToInt`、`easy anythingIndexSwitch`、`CFGNorm`、`GetImageSize`、`RH_RFMSR_ModelLoader`、`Int`、`VAEDecode`、`IntConditions`、`LayerUtility: PurgeVRAM`、`RH_RFMSR_Upscale`、`PrimitiveBoolean`、`LayerUtility: ImageScaleByAspectRatio V2`、`GrowMaskWithBlur`、`UNETLoader`、`EmptySD3LatentImage`、`LoadImage`、`1hew_TextToAny`、`图像缩放V2_孤海`、`UpscaleModelLoader`、`Krea2EditGroundedEncode`、`easy mathString`、`StringReplace`、`Krea2EditModelPatch`、`PixelKSampleUpscalerProvider`、`IterativeImageUpscale`、`SaveImage`、`RHLLMChatNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
