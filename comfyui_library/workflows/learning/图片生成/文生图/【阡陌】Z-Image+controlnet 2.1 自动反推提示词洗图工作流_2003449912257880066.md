---
key: 图片生成/文生图/【阡陌】Z-Image+controlnet 2.1 自动反推提示词洗图工作流_2003449912257880066.json
name: 【阡陌】Z-Image+controlnet 2.1 自动反推提示词洗图工作流_2003449912257880066
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【阡陌】Z-Image+controlnet 2.1 自动反推提示词洗图工作流_2003449912257880066.json
hash: 4754ffbd49241b97
coverage: 0.833333
learned_at: 2026-10-19 21:47:27
nodes: [UNETLoader, EmptySD3LatentImage, VAEDecode, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, Note, LoadImage, CLIPTextEncode, CLIPTextEncode, GetImageSize, LoadImage, CLIPLoader, VAELoader, ModelPatchLoader, ModelSamplingAuraFlow, KSampler, easy conditioningIndexSwitch, ConditioningZeroOut, PreviewImage, ZImageFunControlnet, Note, AIO_Preprocessor, easy showAnything, QwenVisionNode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1094626068510861, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/【阡陌】Z-Image+controlnet 2.1 自动反推提示词洗图工作流_2003449912257880066.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【阡陌】Z-Image+controlnet 2.1 自动反推提示词洗图工作流_2003449912257880066.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `UNETLoader` ★核心
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetImageSize`
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `easy conditioningIndexSwitch`
- `ConditioningZeroOut`
- `PreviewImage`
- `ZImageFunControlnet`
- `Note`
- `AIO_Preprocessor`
- `easy showAnything`
- `QwenVisionNode`

## 关键参数

- `seed` = `1094626068510861`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`UNETLoader`、`EmptySD3LatentImage`、`VAEDecode`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`CLIPTextEncode`、`GetImageSize`、`CLIPLoader`、`VAELoader`、`ModelPatchLoader`、`ModelSamplingAuraFlow`、`KSampler`、`easy conditioningIndexSwitch`、`ConditioningZeroOut`、`ZImageFunControlnet`、`AIO_Preprocessor`、`QwenVisionNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
