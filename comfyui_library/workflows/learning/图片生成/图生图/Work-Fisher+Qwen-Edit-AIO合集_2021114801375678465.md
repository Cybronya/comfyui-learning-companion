---
key: 图片生成/图生图/Work-Fisher+Qwen-Edit-AIO合集_2021114801375678465.json
name: Work-Fisher+Qwen-Edit-AIO合集_2021114801375678465
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Work-Fisher+Qwen-Edit-AIO合集_2021114801375678465.json
hash: 9b5c32be804be039
coverage: 0.820513
learned_at: 2026-10-23 11:28:31
nodes: [ConditioningZeroOut, LoadImage, ConditioningZeroOut, AIO_Preprocessor, ConditioningZeroOut, ImageConcanate, LoadImage, VAEDecode, CheckpointLoaderSimple, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, ImageColorMatch+, Image Comparer (rgthree), LoadImage, LoadImage, LoadImage, PreviewImage, SaveImage, SaveImage, PreviewImage, SaveImage, Image Comparer (rgthree), Image Comparer (rgthree), KSampler, TextEncodeQwenImageEditPlusAdvance_lrzjason, LayerUtility: ImageReelComposit, LayerUtility: ImageReel, VAEDecode, KSampler, TextEncodeQwenImageEditPlusAdvance_lrzjason, LayerUtility: ImageReelComposit, VAEDecode, LayerUtility: ImageReel, LayerUtility: ImageScaleByAspectRatio V2, TextEncodeQwenImageEditPlusAdvance_lrzjason, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, PreviewImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Rapid-AIO-v3.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 9527, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Work-Fisher+Qwen-Edit-AIO合集_2021114801375678465.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Work-Fisher+Qwen-Edit-AIO合集_2021114801375678465.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `ConditioningZeroOut`
- `LoadImage`
- `ConditioningZeroOut`
- `AIO_Preprocessor`
- `ConditioningZeroOut`
- `ImageConcanate`
- `LoadImage`
- `VAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `ImageColorMatch+`
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SaveImage`
- `PreviewImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageReel`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `LayerUtility: ImageReelComposit`
- `VAEDecode` ★核心
- `LayerUtility: ImageReel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `KSampler` ★核心
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `PreviewImage`

## 关键参数

- `checkpoint` = `Qwen-Rapid-AIO-v3.safetensors`
- `seed` = `9527`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **82%**（32/39）

**有卡**：`ConditioningZeroOut`、`LoadImage`、`AIO_Preprocessor`、`ImageConcanate`、`VAEDecode`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`ImageColorMatch+`、`SaveImage`、`KSampler`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、ConditioningZeroOut、LoadImage、TextEncodeQwenImageEditPlusAdvance_lrzjason、SaveImage

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
