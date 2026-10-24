---
key: 图片生成/图生图/QwenEditRemix-AIO2.0-图片编辑_2042232077843701762.json
name: QwenEditRemix-AIO2.0-图片编辑_2042232077843701762
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QwenEditRemix-AIO2.0-图片编辑_2042232077843701762.json
hash: ff6e72eba37c6690
coverage: 0.888889
learned_at: 2026-10-23 11:20:32
nodes: [Any Switch (rgthree), LoadImage, KSampler, ConditioningZeroOut, Image Comparer (rgthree), SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, VAEDecode, CheckpointLoaderSimple, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, Int, Text, LayerUtility: ImageScaleByAspectRatio V2, CustomAddLabel, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Image-Edit-Remix-AIO-v2.0.safetensors", "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 65734077512344, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/QwenEditRemix-AIO2.0-图片编辑_2042232077843701762.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/QwenEditRemix-AIO2.0-图片编辑_2042232077843701762.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `Any Switch (rgthree)`
- `LoadImage`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `VAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CustomAddLabel`
- `SaveImage`

## 关键参数

- `seed` = `65734077512344`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `Qwen-Image-Edit-Remix-AIO-v2.0.safetensors`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`LoadImage`、`KSampler`、`ConditioningZeroOut`、`SaveImage`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`CheckpointLoaderSimple`、`Int`、`Text`、`CustomAddLabel`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、ConditioningZeroOut、LoadImage、TextEncodeQwenImageEditPlusAdvance_lrzjason、SaveImage、Int

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
