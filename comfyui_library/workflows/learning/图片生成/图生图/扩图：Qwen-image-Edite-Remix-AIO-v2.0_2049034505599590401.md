---
key: 图片生成/图生图/扩图：Qwen-image-Edite-Remix-AIO-v2.0_2049034505599590401.json
name: 扩图：Qwen-image-Edite-Remix-AIO-v2.0_2049034505599590401
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/扩图：Qwen-image-Edite-Remix-AIO-v2.0_2049034505599590401.json
hash: 5a4fe62275e5b864
coverage: 0.818182
learned_at: 2026-10-23 12:54:09
nodes: [TextEncodeQwenImageEditPlusAdvance_lrzjason, ConditioningZeroOut, VAEDecode, SaveImage, Image Comparer (rgthree), ImagePadForOutpaint, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, CheckpointLoaderSimple, PreviewImage, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Image-Edit-Remix-AIO-v2.0.safetensors", "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 508892448567738, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/扩图：Qwen-image-Edite-Remix-AIO-v2.0_2049034505599590401.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/扩图：Qwen-image-Edite-Remix-AIO-v2.0_2049034505599590401.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（11 个）：
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `ImagePadForOutpaint`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CheckpointLoaderSimple` ★核心
- `PreviewImage`
- `KSampler` ★核心

## 关键参数

- `checkpoint` = `Qwen-Image-Edit-Remix-AIO-v2.0.safetensors`
- `seed` = `508892448567738`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **82%**（9/11）

**有卡**：`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`ConditioningZeroOut`、`VAEDecode`、`SaveImage`、`ImagePadForOutpaint`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`CheckpointLoaderSimple`、`KSampler`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、ConditioningZeroOut、LoadImage、TextEncodeQwenImageEditPlusAdvance_lrzjason、SaveImage、ImagePadForOutpaint

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
