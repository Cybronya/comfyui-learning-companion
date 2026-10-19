---
key: 图片生成/文生图/Z-Image-ControlNet+SDPOSE+二阶Refiner_1996596394481819649.json
name: Z-Image-ControlNet+SDPOSE+二阶Refiner_1996596394481819649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image-ControlNet+SDPOSE+二阶Refiner_1996596394481819649.json
hash: 3f196bfd7f5255b5
coverage: 0.825
learned_at: 2026-10-19 21:32:50
nodes: [CLIPLoader, ModelPatchLoader, EmptySD3LatentImage, Note, MarkdownNote, GetImageSize, easy cleanGpuUsed, CLIPTextEncode, Seed (rgthree), PreviewImage, KSampler, VAEDecode, ImageScaleBy, VAEEncode, LatentUpscaleBy, VAELoader, PreviewImage, VAEDecode, VAEDecode, UNETLoader, KSampler, KSampler, QwenImageDiffsynthControlnet, ConditioningZeroOut, JWStringConcat, easy showAnything, String Literal, LoraLoaderModelOnly, ModelSamplingAuraFlow, ModelSamplingAuraFlow, Qwen3_VQA, SDPoseOODLoader, MultiplePathsInput, SDPoseOODProcessor, YOLOModelLoader, ImageScaleToMaxDimension, ImageLoader, PreviewImage, Image Comparer (rgthree), SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.8500000000000002, "sampler_name": "euler", "scheduler": "simple", "seed": 1096871997057434, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-Image-ControlNet+SDPOSE+二阶Refiner_1996596394481819649.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image-ControlNet+SDPOSE+二阶Refiner_1996596394481819649.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `CLIPLoader`
- `ModelPatchLoader`
- `EmptySD3LatentImage`
- `Note`
- `MarkdownNote`
- `GetImageSize`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `Seed (rgthree)`
- `PreviewImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImageScaleBy`
- `VAEEncode` ★核心
- `LatentUpscaleBy`
- `VAELoader`
- `PreviewImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `QwenImageDiffsynthControlnet`
- `ConditioningZeroOut`
- `JWStringConcat`
- `easy showAnything`
- `String Literal`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `ModelSamplingAuraFlow`
- `Qwen3_VQA`
- `SDPoseOODLoader`
- `MultiplePathsInput`
- `SDPoseOODProcessor`
- `YOLOModelLoader`
- `ImageScaleToMaxDimension`
- `ImageLoader`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `SaveImage`

## 关键参数

- `seed` = `1096871997057434`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.8500000000000002`

## 知识

覆盖率 **82%**（33/40）

**有卡**：`CLIPLoader`、`ModelPatchLoader`、`EmptySD3LatentImage`、`GetImageSize`、`easy cleanGpuUsed`、`CLIPTextEncode`、`Seed (rgthree)`、`KSampler`、`VAEDecode`、`ImageScaleBy`、`VAEEncode`、`LatentUpscaleBy`、`VAELoader`、`UNETLoader`、`QwenImageDiffsynthControlnet`、`ConditioningZeroOut`、`JWStringConcat`、`String Literal`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`Qwen3_VQA`、`SDPoseOODLoader`、`MultiplePathsInput`、`SDPoseOODProcessor`、`YOLOModelLoader`、`ImageScaleToMaxDimension`、`ImageLoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、UNETLoader

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
