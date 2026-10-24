---
key: 图片生成/图生图/LH-DMT版本-2.生图片类-042.Qwen-Edit-2511-支持 单图 双图 三图编辑_2016524711785664514.json
name: LH-DMT版本-2.生图片类-042.Qwen-Edit-2511-支持 单图 双图 三图编辑_2016524711785664514
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/LH-DMT版本-2.生图片类-042.Qwen-Edit-2511-支持 单图 双图 三图编辑_2016524711785664514.json
hash: e3b492cd30fbc49a
coverage: 0.66
learned_at: 2026-10-23 11:08:41
nodes: [INTConstant, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, Reroute, Reroute, TextEncodeQwenImageEditPlus, CR Prompt Text, Reroute, INTConstant, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, Reroute, ReferenceLatent, Reroute, Reroute, CFGNorm, ReferenceLatent, KSampler, Reroute, VAEDecode, PlaySound|pysssss, Reroute, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, Image Comparer (rgthree), SaveImage, PreviewImage, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, CR Prompt Text, TextEncodeQwenImageEditPlus, Reroute, Reroute, Reroute, TextEncodeQwenImageEditPlus, Reroute, VAEEncode, Reroute, TextEncodeQwenImageEditPlus, ReferenceLatent, ReferenceLatent, Reroute, CFGNorm, Reroute, KSampler, VAEDecode, Reroute, Reroute, PlaySound|pysssss, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, Image Comparer (rgthree), SaveImage, PreviewImage, UNETLoader, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, CR Prompt Text, LoadImage, LoadImage, LoadImage, Reroute, Reroute, Reroute, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, Reroute, Reroute, Reroute, CFGNorm, Reroute, ReferenceLatent, ReferenceLatent, Reroute, KSampler, Reroute, VAEDecode, PlaySound|pysssss, Reroute, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, Image Comparer (rgthree), SaveImage, PreviewImage, Fast Groups Bypasser (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 45170529660600, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/LH-DMT版本-2.生图片类-042.Qwen-Edit-2511-支持 单图 双图 三图编辑_2016524711785664514.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/LH-DMT版本-2.生图片类-042.Qwen-Edit-2511-支持 单图 双图 三图编辑_2016524711785664514.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（100 个）：
- `INTConstant`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `Reroute`
- `TextEncodeQwenImageEditPlus`
- `CR Prompt Text`
- `Reroute`
- `INTConstant`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEEncode` ★核心
- `Reroute`
- `ReferenceLatent`
- `Reroute`
- `Reroute`
- `CFGNorm`
- `ReferenceLatent`
- `KSampler` ★核心
- `Reroute`
- `VAEDecode` ★核心
- `PlaySound|pysssss`
- `Reroute`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `Image Comparer (rgthree)`
- `SaveImage`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `CR Prompt Text`
- `TextEncodeQwenImageEditPlus`
- `Reroute`
- `Reroute`
- `Reroute`
- `TextEncodeQwenImageEditPlus`
- `Reroute`
- `VAEEncode` ★核心
- `Reroute`
- `TextEncodeQwenImageEditPlus`
- `ReferenceLatent`
- `ReferenceLatent`
- `Reroute`
- `CFGNorm`
- `Reroute`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Reroute`
- `Reroute`
- `PlaySound|pysssss`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `Image Comparer (rgthree)`
- `SaveImage`
- `PreviewImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Reroute`
- `Reroute`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEEncode` ★核心
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `Reroute`
- `Reroute`
- `Reroute`
- `CFGNorm`
- `Reroute`
- `ReferenceLatent`
- `ReferenceLatent`
- `Reroute`
- `KSampler` ★核心
- `Reroute`
- `VAEDecode` ★核心
- `PlaySound|pysssss`
- `Reroute`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `Image Comparer (rgthree)`
- `SaveImage`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `45170529660600`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **66%**（66/100）

**有卡**：`INTConstant`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`TextEncodeQwenImageEditPlus`、`CR Prompt Text`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEEncode`、`ReferenceLatent`、`CFGNorm`、`KSampler`、`VAEDecode`、`PlaySound|pysssss`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
