---
key: 图片生成/图生图/FireRed-Image-Edit 1.1图片编辑模型，最多三图_2026952933660696578.json
name: FireRed-Image-Edit 1.1图片编辑模型，最多三图_2026952933660696578
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1图片编辑模型，最多三图_2026952933660696578.json
hash: bff72d84017bea64
coverage: 0.681818
learned_at: 2026-10-23 10:55:38
nodes: [Fast Groups Bypasser (rgthree), CLIPLoader, VAELoader, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, KSampler, TextEncodeQwenImageEditPlusAdvance_lrzjason, Text, ConditioningZeroOut, Anything Everywhere3, Image Comparer (rgthree), LayerUtility: ImageReelComposit, VAEDecode, SaveImage, LayerUtility: ImageReel, LoadImage, LoadImage, PreviewImage, UNETLoader]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 411736159676985, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-Edit 1.1图片编辑模型，最多三图_2026952933660696578.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1图片编辑模型，最多三图_2026952933660696578.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `Fast Groups Bypasser (rgthree)`
- `CLIPLoader`
- `VAELoader`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `Text`
- `ConditioningZeroOut`
- `Anything Everywhere3`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageReelComposit`
- `VAEDecode` ★核心
- `SaveImage`
- `LayerUtility: ImageReel`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `UNETLoader` ★核心

## 关键参数

- `seed` = `411736159676985`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **68%**（15/22）

**有卡**：`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`LoadImage`、`KSampler`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`Text`、`ConditioningZeroOut`、`LayerUtility: ImageReelComposit`、`VAEDecode`、`SaveImage`、`LayerUtility: ImageReel`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
