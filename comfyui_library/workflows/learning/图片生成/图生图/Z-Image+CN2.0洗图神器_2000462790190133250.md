---
key: 图片生成/图生图/Z-Image+CN2.0洗图神器_2000462790190133250.json
name: Z-Image+CN2.0洗图神器_2000462790190133250
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-Image+CN2.0洗图神器_2000462790190133250.json
hash: ea932904afc52a73
coverage: 0.883721
learned_at: 2026-10-23 11:29:25
nodes: [MarkdownNote, VAEDecode, ModelSamplingAuraFlow, ConditioningZeroOut, KSampler, GetImageSize, QwenImageDiffsynthControlnet, VAEDecode, ImageSharpen, SaveImage, VAEDecode, ImageSharpen, ModelSamplingAuraFlow, QwenImageDiffsynthControlnet, QwenImageDiffsynthControlnet, ModelSamplingAuraFlow, Canny, GetImageSize, AIO_Preprocessor, PixelPerfectResolution, PixelPerfectResolution, GetImageSize, AILab_QwenVL, AIO_Preprocessor, KSampler, CLIPTextEncode, EmptySD3LatentImage, CLIPLoader, UNETLoader, VAELoader, ShowText|pysssss, SaveImage, KSampler, Label (rgthree), PreviewImage, PreviewImage, SaveImage, SaveImage, ModelPatchLoader, Label (rgthree), PreviewImage, LoadImage, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 471809315564294, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Z-Image+CN2.0洗图神器_2000462790190133250.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-Image+CN2.0洗图神器_2000462790190133250.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `MarkdownNote`
- `VAEDecode` ★核心
- `ModelSamplingAuraFlow`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `GetImageSize`
- `QwenImageDiffsynthControlnet`
- `VAEDecode` ★核心
- `ImageSharpen`
- `SaveImage`
- `VAEDecode` ★核心
- `ImageSharpen`
- `ModelSamplingAuraFlow`
- `QwenImageDiffsynthControlnet`
- `QwenImageDiffsynthControlnet`
- `ModelSamplingAuraFlow`
- `Canny`
- `GetImageSize`
- `AIO_Preprocessor`
- `PixelPerfectResolution`
- `PixelPerfectResolution`
- `GetImageSize`
- `AILab_QwenVL`
- `AIO_Preprocessor`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `ShowText|pysssss`
- `SaveImage`
- `KSampler` ★核心
- `Label (rgthree)`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `SaveImage`
- `ModelPatchLoader`
- `Label (rgthree)`
- `PreviewImage`
- `LoadImage`
- `SaveImage`

## 关键参数

- `seed` = `471809315564294`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **88%**（38/43）

**有卡**：`VAEDecode`、`ModelSamplingAuraFlow`、`ConditioningZeroOut`、`KSampler`、`GetImageSize`、`QwenImageDiffsynthControlnet`、`ImageSharpen`、`SaveImage`、`Canny`、`AIO_Preprocessor`、`PixelPerfectResolution`、`AILab_QwenVL`、`CLIPTextEncode`、`EmptySD3LatentImage`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`Label (rgthree)`、`ModelPatchLoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
