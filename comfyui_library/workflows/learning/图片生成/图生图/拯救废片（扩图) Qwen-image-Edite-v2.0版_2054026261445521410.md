---
key: 图片生成/图生图/拯救废片（扩图) Qwen-image-Edite-v2.0版_2054026261445521410.json
name: 拯救废片（扩图) Qwen-image-Edite-v2.0版_2054026261445521410
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/拯救废片（扩图) Qwen-image-Edite-v2.0版_2054026261445521410.json
hash: e40e48c04a459388
coverage: 0.818182
learned_at: 2026-10-23 12:55:36
nodes: [ConditioningZeroOut, ImagePadForOutpaint, CheckpointLoaderSimple, PreviewImage, KSampler, VAEDecode, TextEncodeQwenImageEditPlusAdvance_lrzjason, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, Image Comparer (rgthree)]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Image-Edit-Remix-AIO-v2.0.safetensors", "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 286728138481227, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/拯救废片（扩图) Qwen-image-Edite-v2.0版_2054026261445521410.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/拯救废片（扩图) Qwen-image-Edite-v2.0版_2054026261445521410.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（11 个）：
- `ConditioningZeroOut`
- `ImagePadForOutpaint`
- `CheckpointLoaderSimple` ★核心
- `PreviewImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `Image Comparer (rgthree)`

## 关键参数

- `checkpoint` = `Qwen-Image-Edit-Remix-AIO-v2.0.safetensors`
- `seed` = `286728138481227`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **82%**（9/11）

**有卡**：`ConditioningZeroOut`、`ImagePadForOutpaint`、`CheckpointLoaderSimple`、`KSampler`、`VAEDecode`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、ConditioningZeroOut、LoadImage、TextEncodeQwenImageEditPlusAdvance_lrzjason、SaveImage、ImagePadForOutpaint

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
