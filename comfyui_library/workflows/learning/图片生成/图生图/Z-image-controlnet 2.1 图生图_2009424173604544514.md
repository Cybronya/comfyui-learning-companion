---
key: 图片生成/图生图/Z-image-controlnet 2.1 图生图_2009424173604544514.json
name: Z-image-controlnet 2.1 图生图_2009424173604544514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-image-controlnet 2.1 图生图_2009424173604544514.json
hash: d454af819863221a
coverage: 0.892857
learned_at: 2026-10-23 11:30:59
nodes: [ConditioningZeroOut, ZImageFunControlnet, KSampler, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, ModelPatchLoader, SaveImage, VAEDecode, CLIPLoader, UNETLoader, ModelSamplingAuraFlow, AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, Note, EmptySD3LatentImage, GetImageSize, AIO_Preprocessor, PreviewImage, CLIPTextEncode, easy conditioningIndexSwitch, easy showAnything, QwenVisionNode, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 314705418096616, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Z-image-controlnet 2.1 图生图_2009424173604544514.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-image-controlnet 2.1 图生图_2009424173604544514.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `ConditioningZeroOut`
- `ZImageFunControlnet`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `ModelPatchLoader`
- `SaveImage`
- `VAEDecode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `Note`
- `EmptySD3LatentImage`
- `GetImageSize`
- `AIO_Preprocessor`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `easy conditioningIndexSwitch`
- `easy showAnything`
- `QwenVisionNode`
- `LoadImage`

## 关键参数

- `seed` = `314705418096616`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（25/28）

**有卡**：`ConditioningZeroOut`、`ZImageFunControlnet`、`KSampler`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`ModelPatchLoader`、`SaveImage`、`VAEDecode`、`CLIPLoader`、`UNETLoader`、`ModelSamplingAuraFlow`、`AIO_Preprocessor`、`EmptySD3LatentImage`、`GetImageSize`、`easy conditioningIndexSwitch`、`QwenVisionNode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
