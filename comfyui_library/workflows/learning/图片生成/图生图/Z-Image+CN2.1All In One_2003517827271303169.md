---
key: 图片生成/图生图/Z-Image+CN2.1All In One_2003517827271303169.json
name: Z-Image+CN2.1All In One_2003517827271303169
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-Image+CN2.1All In One_2003517827271303169.json
hash: 01b76dd590dcf39d
coverage: 0.88
learned_at: 2026-10-23 11:29:25
nodes: [ModelSamplingAuraFlow, ConditioningZeroOut, CLIPTextEncode, KSampler, AIO_Preprocessor, GetImageSize, Canny, PixelPerfectResolution, Label (rgthree), ImageConcatMulti, SaveImage, AIO_Preprocessor, ImpactSwitch, UNETLoader, CLIPLoader, VAELoader, ModelPatchLoader, LoadImage, ImageConcatMulti, PreviewImage, PreviewAny, AILab_QwenVL, EmptySD3LatentImage, ZImageFunControlnet, VAEDecode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 676932674552667, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Z-Image+CN2.1All In One_2003517827271303169.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-Image+CN2.1All In One_2003517827271303169.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `ModelSamplingAuraFlow`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `AIO_Preprocessor`
- `GetImageSize`
- `Canny`
- `PixelPerfectResolution`
- `Label (rgthree)`
- `ImageConcatMulti`
- `SaveImage`
- `AIO_Preprocessor`
- `ImpactSwitch`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelPatchLoader`
- `LoadImage`
- `ImageConcatMulti`
- `PreviewImage`
- `PreviewAny`
- `AILab_QwenVL`
- `EmptySD3LatentImage`
- `ZImageFunControlnet`
- `VAEDecode` ★核心

## 关键参数

- `seed` = `676932674552667`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（22/25）

**有卡**：`ModelSamplingAuraFlow`、`ConditioningZeroOut`、`CLIPTextEncode`、`KSampler`、`AIO_Preprocessor`、`GetImageSize`、`Canny`、`PixelPerfectResolution`、`Label (rgthree)`、`ImageConcatMulti`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ModelPatchLoader`、`LoadImage`、`AILab_QwenVL`、`EmptySD3LatentImage`、`ZImageFunControlnet`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
