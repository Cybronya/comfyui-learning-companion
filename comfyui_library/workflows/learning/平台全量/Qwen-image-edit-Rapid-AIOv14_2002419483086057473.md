---
key: 平台全量/Qwen-image-edit-Rapid-AIOv14_2002419483086057473.json
name: Qwen-image-edit-Rapid-AIOv14_2002419483086057473
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-image-edit-Rapid-AIOv14_2002419483086057473.json
hash: 95508f34bd4ba0ea
coverage: 0.909091
learned_at: 2026-11-14 00:52:10
nodes: [ConditioningZeroOut, VAEDecode, CheckpointLoaderSimple, TextEncodeQwenImageEditPlusPro_lrzjason, LoadImage, AIO_Preprocessor, PreviewImage, KSampler, LoadImage, SaveImage, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v14.1.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 585501527986682, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Qwen-image-edit-Rapid-AIOv14_2002419483086057473.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-image-edit-Rapid-AIOv14_2002419483086057473.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（11 个）：
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `TextEncodeQwenImageEditPlusPro_lrzjason`
- `LoadImage`
- `AIO_Preprocessor`
- `PreviewImage`
- `KSampler` ★核心
- `LoadImage`
- `SaveImage`
- `LoadImage`

## 关键参数

- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v14.1.safetensors`
- `seed` = `585501527986682`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`ConditioningZeroOut`、`VAEDecode`、`CheckpointLoaderSimple`、`TextEncodeQwenImageEditPlusPro_lrzjason`、`LoadImage`、`AIO_Preprocessor`、`KSampler`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、ConditioningZeroOut、LoadImage、TextEncodeQwenImageEditPlusPro_lrzjason、SaveImage、AIO_Preprocessor

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
