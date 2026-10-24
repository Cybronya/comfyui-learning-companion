---
key: 图片生成/图生图/LH-DMT版本-2.生图片类-041.QwenEdit2511单图编辑+双图互动_2016524689539076098.json
name: LH-DMT版本-2.生图片类-041.QwenEdit2511单图编辑+双图互动_2016524689539076098
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/LH-DMT版本-2.生图片类-041.QwenEdit2511单图编辑+双图互动_2016524689539076098.json
hash: 03eade02ed1d9f42
coverage: 0.77551
learned_at: 2026-10-23 11:08:41
nodes: [Anything Everywhere, CLIPLoader, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, ConditioningZeroOut, LayerUtility: ImageReelComposit, GetNode, LoraLoaderModelOnly, KSampler, LayerUtility: ImageReel, LoraLoaderModelOnly, SaveImage, Image Comparer (rgthree), PreviewImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, KSampler, VAEDecode, LayerUtility: ImageReelComposit, ConditioningZeroOut, LayerUtility: ImageReel, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, DWPreprocessor, TextEncodeQwenImageEditPlusAdvance_lrzjason, KSampler, LayerUtility: ImageReel, ConditioningZeroOut, PreviewImage, LayerUtility: ImageReelComposit, VAEDecode, SaveImage, PreviewImage, GetNode, SetNode, GetNode, LoadImage, UnetLoaderGGUF, LoraLoaderModelOnly, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, VAELoader]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 91420756438600, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/LH-DMT版本-2.生图片类-041.QwenEdit2511单图编辑+双图互动_2016524689539076098.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/LH-DMT版本-2.生图片类-041.QwenEdit2511单图编辑+双图互动_2016524689539076098.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `Anything Everywhere`
- `CLIPLoader`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ConditioningZeroOut`
- `LayerUtility: ImageReelComposit`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `LayerUtility: ImageReel`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageReelComposit`
- `ConditioningZeroOut`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DWPreprocessor`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `KSampler` ★核心
- `LayerUtility: ImageReel`
- `ConditioningZeroOut`
- `PreviewImage`
- `LayerUtility: ImageReelComposit`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `GetNode`
- `SetNode`
- `GetNode`
- `LoadImage`
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `VAELoader`

## 关键参数

- `seed` = `91420756438600`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（38/49）

**有卡**：`CLIPLoader`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`ConditioningZeroOut`、`LayerUtility: ImageReelComposit`、`LoraLoaderModelOnly`、`KSampler`、`LayerUtility: ImageReel`、`SaveImage`、`DWPreprocessor`、`LoadImage`、`UnetLoaderGGUF`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、TextEncodeQwenImageEditPlusAdvance_lrzjason

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
