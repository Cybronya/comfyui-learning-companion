---
key: 图片生成/图生图/Z-Image-Turbo-最新控制生图-2.1_2004016764516245505.json
name: Z-Image-Turbo-最新控制生图-2.1_2004016764516245505
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-Image-Turbo-最新控制生图-2.1_2004016764516245505.json
hash: f250acff42f20fbe
coverage: 0.9375
learned_at: 2026-10-23 11:29:38
nodes: [CLIPLoader, UNETLoader, VAELoader, ConditioningZeroOut, ModelSamplingAuraFlow, VAEDecode, SaveImage, ModelPatchLoader, QwenImageDiffsynthControlnet, ImageScaleToMaxDimension, AIO_Preprocessor, PreviewImage, EmptySD3LatentImage, KSampler, LoadImage, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 170333217178004, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Z-Image-Turbo-最新控制生图-2.1_2004016764516245505.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-Image-Turbo-最新控制生图-2.1_2004016764516245505.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `SaveImage`
- `ModelPatchLoader`
- `QwenImageDiffsynthControlnet`
- `ImageScaleToMaxDimension`
- `AIO_Preprocessor`
- `PreviewImage`
- `EmptySD3LatentImage`
- `KSampler` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `170333217178004`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`CLIPLoader`、`UNETLoader`、`VAELoader`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`VAEDecode`、`SaveImage`、`ModelPatchLoader`、`QwenImageDiffsynthControlnet`、`ImageScaleToMaxDimension`、`AIO_Preprocessor`、`EmptySD3LatentImage`、`KSampler`、`LoadImage`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
