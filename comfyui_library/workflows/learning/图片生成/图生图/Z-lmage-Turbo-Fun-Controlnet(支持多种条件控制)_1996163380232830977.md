---
key: 图片生成/图生图/Z-lmage-Turbo-Fun-Controlnet(支持多种条件控制)_1996163380232830977.json
name: Z-lmage-Turbo-Fun-Controlnet(支持多种条件控制)_1996163380232830977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-lmage-Turbo-Fun-Controlnet(支持多种条件控制)_1996163380232830977.json
hash: a495b19fdc1a21c4
coverage: 0.846154
learned_at: 2026-10-23 11:32:38
nodes: [ConditioningZeroOut, EmptySD3LatentImage, KSampler, VAELoader, ModelSamplingAuraFlow, QwenImageDiffsynthControlnet, ImageStitch, VAEDecode, PreviewImage, LoadImage, CLIPLoader, UNETLoader, ModelPatchLoader, LoadImage, GetImageSize, ImageScaleToTotalPixels, CLIPTextEncode, JWInteger, AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, PreviewImage, PreviewImage, CR Image Input Switch (4 way), SaveImage, PreviewImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 331594914895486, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Z-lmage-Turbo-Fun-Controlnet(支持多种条件控制)_1996163380232830977.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-lmage-Turbo-Fun-Controlnet(支持多种条件控制)_1996163380232830977.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `KSampler` ★核心
- `VAELoader`
- `ModelSamplingAuraFlow`
- `QwenImageDiffsynthControlnet`
- `ImageStitch`
- `VAEDecode` ★核心
- `PreviewImage`
- `LoadImage`
- `CLIPLoader`
- `UNETLoader` ★核心
- `ModelPatchLoader`
- `LoadImage`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `CLIPTextEncode` ★核心
- `JWInteger`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `PreviewImage`
- `PreviewImage`
- `CR Image Input Switch (4 way)`
- `SaveImage`
- `PreviewImage`

## 关键参数

- `seed` = `331594914895486`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（22/26）

**有卡**：`ConditioningZeroOut`、`EmptySD3LatentImage`、`KSampler`、`VAELoader`、`ModelSamplingAuraFlow`、`QwenImageDiffsynthControlnet`、`ImageStitch`、`VAEDecode`、`LoadImage`、`CLIPLoader`、`UNETLoader`、`ModelPatchLoader`、`GetImageSize`、`ImageScaleToTotalPixels`、`CLIPTextEncode`、`JWInteger`、`AIO_Preprocessor`、`CR Image Input Switch (4 way)`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
