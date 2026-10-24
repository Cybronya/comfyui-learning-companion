---
key: 图片生成/图生图/F.2Klein控油真实高清放大增强细节_2053805824715309057.json
name: F.2Klein控油真实高清放大增强细节_2053805824715309057
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2Klein控油真实高清放大增强细节_2053805824715309057.json
hash: 80cab66a32e1ee9b
coverage: 0.969697
learned_at: 2026-10-23 10:52:46
nodes: [CLIPLoader, VAELoader, CLIPTextEncode, CLIPLoader, VAELoader, VAEEncode, VAEDecode, UNETLoader, CLIPTextEncode, CLIPTextEncode, RH_Captioner, ImageScaleBy, EmptyFlux2LatentImage, VAEEncode, ReferenceLatent, GetImageSize, ConditioningZeroOut, KSampler, VAEDecode, easy cleanGpuUsed, PreviewImage, easy cleanGpuUsed, CR Prompt Text, LoadImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingAuraFlow, RunningHub Deepcleaner, KSamplerAdvanced, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 10, "denoise": "beta57", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/F.2Klein控油真实高清放大增强细节_2053805824715309057.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2Klein控油真实高清放大增强细节_2053805824715309057.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `RH_Captioner`
- `ImageScaleBy`
- `EmptyFlux2LatentImage`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `GetImageSize`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `PreviewImage`
- `easy cleanGpuUsed`
- `CR Prompt Text`
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `RunningHub Deepcleaner`
- `KSamplerAdvanced` ★核心
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta57`

## 知识

覆盖率 **97%**（32/33）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`VAEEncode`、`VAEDecode`、`UNETLoader`、`RH_Captioner`、`ImageScaleBy`、`EmptyFlux2LatentImage`、`ReferenceLatent`、`GetImageSize`、`ConditioningZeroOut`、`KSampler`、`easy cleanGpuUsed`、`CR Prompt Text`、`LoadImage`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`RunningHub Deepcleaner`、`KSamplerAdvanced`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
