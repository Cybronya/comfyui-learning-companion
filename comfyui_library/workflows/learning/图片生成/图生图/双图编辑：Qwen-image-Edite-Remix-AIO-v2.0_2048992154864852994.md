---
key: 图片生成/图生图/双图编辑：Qwen-image-Edite-Remix-AIO-v2.0_2048992154864852994.json
name: 双图编辑：Qwen-image-Edite-Remix-AIO-v2.0_2048992154864852994
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/双图编辑：Qwen-image-Edite-Remix-AIO-v2.0_2048992154864852994.json
hash: 621a23dad11a0815
coverage: 0.909091
learned_at: 2026-10-23 12:35:14
nodes: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, ConditioningZeroOut, KSampler, VAEDecode, Image Comparer (rgthree), CheckpointLoaderSimple, SaveImage, LoadImage, LoadImage, TextEncodeQwenImageEditPlusAdvance_lrzjason]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Image-Edit-Remix-AIO-v2.0.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 91220933723261, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/双图编辑：Qwen-image-Edite-Remix-AIO-v2.0_2048992154864852994.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/双图编辑：Qwen-image-Edite-Remix-AIO-v2.0_2048992154864852994.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（11 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `CheckpointLoaderSimple` ★核心
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`

## 关键参数

- `seed` = `91220933723261`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `Qwen-Image-Edit-Remix-AIO-v2.0.safetensors`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`ConditioningZeroOut`、`KSampler`、`VAEDecode`、`CheckpointLoaderSimple`、`SaveImage`、`LoadImage`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、ConditioningZeroOut、LoadImage、TextEncodeQwenImageEditPlusAdvance_lrzjason、SaveImage、LayerUtility: ImageScaleByAspectRatio V2

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
