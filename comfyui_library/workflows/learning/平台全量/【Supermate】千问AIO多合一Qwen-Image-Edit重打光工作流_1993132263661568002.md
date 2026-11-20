---
key: 平台全量/【Supermate】千问AIO多合一Qwen-Image-Edit重打光工作流_1993132263661568002.json
name: 【Supermate】千问AIO多合一Qwen-Image-Edit重打光工作流_1993132263661568002
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【Supermate】千问AIO多合一Qwen-Image-Edit重打光工作流_1993132263661568002.json
hash: 34babe8a58b37350
coverage: 0.842105
learned_at: 2026-11-14 01:22:18
nodes: [Label (rgthree), ImageScaleToTotalPixels, VAEDecode, ConditioningZeroOut, ModelSamplingAuraFlow, Image Comparer (rgthree), SaveImage, SeedVR2ExtraArgs, ImageScaleBy, Note, CFGNorm, KSampler, TextEncodeQwenImageEditPlusPro_lrzjason, CheckpointLoaderSimple, Reroute, LoadImage, SeedVR2BlockSwap, LoraLoaderModelOnly, SeedVR2]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v11.1.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 519754925120703, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/【Supermate】千问AIO多合一Qwen-Image-Edit重打光工作流_1993132263661568002.json

> 来源文件 `comfyui_library/workflows/平台全量/【Supermate】千问AIO多合一Qwen-Image-Edit重打光工作流_1993132263661568002.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `Label (rgthree)`
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SeedVR2ExtraArgs`
- `ImageScaleBy`
- `Note`
- `CFGNorm`
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlusPro_lrzjason`
- `CheckpointLoaderSimple` ★核心
- `Reroute`
- `LoadImage`
- `SeedVR2BlockSwap`
- `LoraLoaderModelOnly` ★核心
- `SeedVR2`

## 关键参数

- `seed` = `519754925120703`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v11.1.safetensors`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`Label (rgthree)`、`ImageScaleToTotalPixels`、`VAEDecode`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`SaveImage`、`SeedVR2ExtraArgs`、`ImageScaleBy`、`CFGNorm`、`KSampler`、`TextEncodeQwenImageEditPlusPro_lrzjason`、`CheckpointLoaderSimple`、`LoadImage`、`SeedVR2BlockSwap`、`LoraLoaderModelOnly`、`SeedVR2`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、ConditioningZeroOut、LoadImage、CFGNorm、SeedVR2

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
