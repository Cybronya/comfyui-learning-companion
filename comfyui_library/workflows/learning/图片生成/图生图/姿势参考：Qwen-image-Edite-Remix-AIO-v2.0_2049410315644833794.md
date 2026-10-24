---
key: 图片生成/图生图/姿势参考：Qwen-image-Edite-Remix-AIO-v2.0_2049410315644833794.json
name: 姿势参考：Qwen-image-Edite-Remix-AIO-v2.0_2049410315644833794
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/姿势参考：Qwen-image-Edite-Remix-AIO-v2.0_2049410315644833794.json
hash: 3314df4e1de61a7d
coverage: 0.857143
learned_at: 2026-10-23 12:47:02
nodes: [ConditioningZeroOut, SDPoseOODLoader, LayerUtility: ImageScaleByAspectRatio V2, SDPoseOODProcessor, PreviewImage, VAEDecode, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, CheckpointLoaderSimple, Image Comparer (rgthree), TextEncodeQwenImageEditPlusAdvance_lrzjason, LoadImage, KSampler, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Image-Edit-Remix-AIO-v2.0.safetensors", "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 201280526082654, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/姿势参考：Qwen-image-Edite-Remix-AIO-v2.0_2049410315644833794.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/姿势参考：Qwen-image-Edite-Remix-AIO-v2.0_2049410315644833794.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `ConditioningZeroOut`
- `SDPoseOODLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SDPoseOODProcessor`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CheckpointLoaderSimple` ★核心
- `Image Comparer (rgthree)`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `LoadImage`
- `KSampler` ★核心
- `LoadImage`

## 关键参数

- `checkpoint` = `Qwen-Image-Edit-Remix-AIO-v2.0.safetensors`
- `seed` = `201280526082654`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`ConditioningZeroOut`、`SDPoseOODLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`SDPoseOODProcessor`、`VAEDecode`、`SaveImage`、`CheckpointLoaderSimple`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`LoadImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、ConditioningZeroOut、LoadImage、TextEncodeQwenImageEditPlusAdvance_lrzjason、SaveImage、SDPoseOODLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
