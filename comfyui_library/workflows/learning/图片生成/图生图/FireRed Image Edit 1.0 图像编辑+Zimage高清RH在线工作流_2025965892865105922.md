---
key: 图片生成/图生图/FireRed Image Edit 1.0 图像编辑+Zimage高清RH在线工作流_2025965892865105922.json
name: FireRed Image Edit 1.0 图像编辑+Zimage高清RH在线工作流_2025965892865105922
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed Image Edit 1.0 图像编辑+Zimage高清RH在线工作流_2025965892865105922.json
hash: 05309d54feaf673e
coverage: 0.861111
learned_at: 2026-10-23 10:55:25
nodes: [GetImageSizeAndCount, VAEDecode, ConditioningZeroOut, VAEDecode, CLIPTextEncode, ModelSamplingAuraFlow, VAEEncode, KSampler, UNETLoader, LoraLoaderModelOnly, Note, LoraLoaderModelOnly, CLIPLoader, VAELoader, Note, KSampler, UNETLoader, LoraLoaderModelOnly, EmptySD3LatentImage, ImageScaleBy, Seed (rgthree), CFGNorm, ModelSamplingAuraFlow, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, VAELoader, Note, CLIPLoader, Reroute, SaveImage, SaveImage, LoadImage, Reroute, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 602596886192896, "steps": 12}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed Image Edit 1.0 图像编辑+Zimage高清RH在线工作流_2025965892865105922.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed Image Edit 1.0 图像编辑+Zimage高清RH在线工作流_2025965892865105922.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `GetImageSizeAndCount`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptySD3LatentImage`
- `ImageScaleBy`
- `Seed (rgthree)`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `VAELoader`
- `Note`
- `CLIPLoader`
- `Reroute`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `Reroute`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `602596886192896`
- `steps` = `12`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（31/36）

**有卡**：`GetImageSizeAndCount`、`VAEDecode`、`ConditioningZeroOut`、`CLIPTextEncode`、`ModelSamplingAuraFlow`、`VAEEncode`、`KSampler`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`EmptySD3LatentImage`、`ImageScaleBy`、`Seed (rgthree)`、`CFGNorm`、`FluxKontextMultiReferenceLatentMethod`、`TextEncodeQwenImageEditPlus`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
