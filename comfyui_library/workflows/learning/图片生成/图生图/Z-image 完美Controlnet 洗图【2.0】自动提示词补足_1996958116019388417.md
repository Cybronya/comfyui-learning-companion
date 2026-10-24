---
key: 图片生成/图生图/Z-image 完美Controlnet 洗图【2.0】自动提示词补足_1996958116019388417.json
name: Z-image 完美Controlnet 洗图【2.0】自动提示词补足_1996958116019388417
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-image 完美Controlnet 洗图【2.0】自动提示词补足_1996958116019388417.json
hash: e1b100156ac6a6be
coverage: 0.725
learned_at: 2026-10-23 11:30:25
nodes: [CLIPLoader, ConditioningZeroOut, ModelSamplingAuraFlow, QwenImageDiffsynthControlnet, VAEDecode, SetNode, VAEDecode, SetNode, CR Prompt Text, SetNode, GetNode, SetNode, Text Concatenate, GetNode, GetNode, LoadImage, Qwen3_VQA, SaveImage, CLIPTextEncode, GetNode, KSampler, GetNode, ImageScaleToMaxDimension, VAELoader, ModelPatchLoader, LayerUtility: PurgeVRAM V2, SetNode, GetImageSize, EmptySD3LatentImage, KSampler, UNETLoader, GetNode, AIO_Preprocessor, SaveImage, LoadImage, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "ddim_uniform", "seed": 484548477389562, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Z-image 完美Controlnet 洗图【2.0】自动提示词补足_1996958116019388417.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-image 完美Controlnet 洗图【2.0】自动提示词补足_1996958116019388417.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `CLIPLoader`
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `QwenImageDiffsynthControlnet`
- `VAEDecode` ★核心
- `SetNode`
- `VAEDecode` ★核心
- `SetNode`
- `CR Prompt Text`
- `SetNode`
- `GetNode`
- `SetNode`
- `Text Concatenate`
- `GetNode`
- `GetNode`
- `LoadImage`
- `Qwen3_VQA`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `GetNode`
- `KSampler` ★核心
- `GetNode`
- `ImageScaleToMaxDimension`
- `VAELoader`
- `ModelPatchLoader`
- `LayerUtility: PurgeVRAM V2`
- `SetNode`
- `GetImageSize`
- `EmptySD3LatentImage`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `GetNode`
- `AIO_Preprocessor`
- `SaveImage`
- `LoadImage`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`

## 关键参数

- `seed` = `484548477389562`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `ddim_uniform`
- `denoise` = `1`

## 知识

覆盖率 **72%**（29/40）

**有卡**：`CLIPLoader`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`QwenImageDiffsynthControlnet`、`VAEDecode`、`CR Prompt Text`、`Text Concatenate`、`LoadImage`、`Qwen3_VQA`、`SaveImage`、`CLIPTextEncode`、`KSampler`、`ImageScaleToMaxDimension`、`VAELoader`、`ModelPatchLoader`、`LayerUtility: PurgeVRAM V2`、`GetImageSize`、`EmptySD3LatentImage`、`UNETLoader`、`AIO_Preprocessor`、`RHHiddenNodes`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
