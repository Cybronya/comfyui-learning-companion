---
key: 图片生成/图生图/多图编辑替换神器FireRed-Image-Edit+1.1_2034432725708447746.json
name: 多图编辑替换神器FireRed-Image-Edit+1.1_2034432725708447746
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/多图编辑替换神器FireRed-Image-Edit+1.1_2034432725708447746.json
hash: 6ee75dec8b366a00
coverage: 0.681818
learned_at: 2026-10-23 12:45:12
nodes: [Fast Groups Bypasser (rgthree), CLIPLoader, VAELoader, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), KSampler, TextEncodeQwenImageEditPlusAdvance_lrzjason, ConditioningZeroOut, Anything Everywhere3, Image Comparer (rgthree), LayerUtility: ImageReelComposit, VAEDecode, LayerUtility: ImageReel, LoadImage, PreviewImage, UNETLoader, LoadImage, LoadImage, Text, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 470554860061600, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/多图编辑替换神器FireRed-Image-Edit+1.1_2034432725708447746.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/多图编辑替换神器FireRed-Image-Edit+1.1_2034432725708447746.json`

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
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `ConditioningZeroOut`
- `Anything Everywhere3`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageReelComposit`
- `VAEDecode` ★核心
- `LayerUtility: ImageReel`
- `LoadImage`
- `PreviewImage`
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `Text`
- `SaveImage`

## 关键参数

- `seed` = `470554860061600`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **68%**（15/22）

**有卡**：`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`KSampler`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`ConditioningZeroOut`、`LayerUtility: ImageReelComposit`、`VAEDecode`、`LayerUtility: ImageReel`、`LoadImage`、`UNETLoader`、`Text`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
