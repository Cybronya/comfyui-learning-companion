---
key: 图片生成/图生图/AI漫剧角色三视图-盯盯盯-V2.0云端+本地三个版本_2026321552664432641.json
name: AI漫剧角色三视图-盯盯盯-V2.0云端+本地三个版本_2026321552664432641
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/AI漫剧角色三视图-盯盯盯-V2.0云端+本地三个版本_2026321552664432641.json
hash: f1723fd20a1db5bc
coverage: 0.961538
learned_at: 2026-10-23 10:50:45
nodes: [VAELoader, UNETLoader, VAEDecode, SaveImage, CLIPLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, UNETLoader, LoraLoaderModelOnly, CLIPLoader, ConditioningZeroOut, VAELoader, EmptySD3LatentImage, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, RH_Nano_Banana2_Image2Image, SaveImage, MuyeTextEditOutput, PainterFluxImageEdit, TextEncodeQwenImageEditPlusAdvance_lrzjason, KSampler, Fast Groups Bypasser (rgthree), LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "sa_solver", "scheduler": "simple", "seed": 47219992791305, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/AI漫剧角色三视图-盯盯盯-V2.0云端+本地三个版本_2026321552664432641.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/AI漫剧角色三视图-盯盯盯-V2.0云端+本地三个版本_2026321552664432641.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `VAELoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPLoader`
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `ConditioningZeroOut`
- `VAELoader`
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `RH_Nano_Banana2_Image2Image`
- `SaveImage`
- `MuyeTextEditOutput`
- `PainterFluxImageEdit`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `KSampler` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`

## 关键参数

- `seed` = `47219992791305`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **96%**（25/26）

**有卡**：`VAELoader`、`UNETLoader`、`VAEDecode`、`SaveImage`、`CLIPLoader`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`EmptySD3LatentImage`、`LoadImage`、`RH_Nano_Banana2_Image2Image`、`MuyeTextEditOutput`、`PainterFluxImageEdit`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、SaveImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
