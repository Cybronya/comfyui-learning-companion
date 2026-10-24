---
key: 图片生成/图生图/Work-Fisher Qwen-Edit-AIO合集_1976167606266806273.json
name: Work-Fisher Qwen-Edit-AIO合集_1976167606266806273
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Work-Fisher Qwen-Edit-AIO合集_1976167606266806273.json
hash: 3f869d61e6e3986f
coverage: 0.8
learned_at: 2026-10-23 11:28:31
nodes: [LoadImage, ConditioningZeroOut, KSampler, LoadImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, ConditioningZeroOut, SaveImage, AIO_Preprocessor, KSampler, LayerUtility: ImageReel, VAEDecode, Image Comparer (rgthree), LoadImage, LayerUtility: ImageReelComposit, ImageColorMatch+, LayerUtility: ImageReelComposit, LayerUtility: ImageReel, SaveImage, VAEDecode, Image Comparer (rgthree), PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, TextEncodeQwenImageEditPlusAdvance_lrzjason, ConditioningZeroOut, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, ImageConcanate, Image Comparer (rgthree), LoadImage, LoadImage, VAEDecode, PreviewImage, SaveImage, CheckpointLoaderSimple, MarkdownNote, PreviewImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Rapid-AIO-v3.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 9527, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Work-Fisher Qwen-Edit-AIO合集_1976167606266806273.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Work-Fisher Qwen-Edit-AIO合集_1976167606266806273.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `LoadImage`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `LoadImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `ConditioningZeroOut`
- `SaveImage`
- `AIO_Preprocessor`
- `KSampler` ★核心
- `LayerUtility: ImageReel`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `LayerUtility: ImageReelComposit`
- `ImageColorMatch+`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageReel`
- `SaveImage`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `ImageConcanate`
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoadImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `CheckpointLoaderSimple` ★核心
- `MarkdownNote`
- `PreviewImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `9527`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-v3.safetensors`

## 知识

覆盖率 **80%**（32/40）

**有卡**：`LoadImage`、`ConditioningZeroOut`、`KSampler`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`SaveImage`、`AIO_Preprocessor`、`LayerUtility: ImageReel`、`VAEDecode`、`LayerUtility: ImageReelComposit`、`ImageColorMatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcanate`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`

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
