---
key: 图片生成/图生图/局部重绘：Qwen-image-Edite-Remix-AIO-v2.0_2049400083560534017.json
name: 局部重绘：Qwen-image-Edite-Remix-AIO-v2.0_2049400083560534017
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/局部重绘：Qwen-image-Edite-Remix-AIO-v2.0_2049400083560534017.json
hash: 3a09e457663faae2
coverage: 0.846154
learned_at: 2026-10-23 12:50:14
nodes: [Mask Fill Holes, LayerMask: MaskGrow, DrawMaskOnImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, ConditioningZeroOut, KSampler, VAEDecode, Image Comparer (rgthree), CheckpointLoaderSimple, SaveImage, LoadImage, TextEncodeQwenImageEditPlusAdvance_lrzjason]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Image-Edit-Remix-AIO-v2.0.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 682672033021176, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/局部重绘：Qwen-image-Edite-Remix-AIO-v2.0_2049400083560534017.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/局部重绘：Qwen-image-Edite-Remix-AIO-v2.0_2049400083560534017.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `Mask Fill Holes`
- `LayerMask: MaskGrow`
- `DrawMaskOnImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `CheckpointLoaderSimple` ★核心
- `SaveImage`
- `LoadImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`

## 关键参数

- `seed` = `682672033021176`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `Qwen-Image-Edit-Remix-AIO-v2.0.safetensors`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`Mask Fill Holes`、`LayerMask: MaskGrow`、`DrawMaskOnImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`ConditioningZeroOut`、`KSampler`、`VAEDecode`、`CheckpointLoaderSimple`、`SaveImage`、`LoadImage`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、ConditioningZeroOut、LoadImage、TextEncodeQwenImageEditPlusAdvance_lrzjason、SaveImage、DrawMaskOnImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
