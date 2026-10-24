---
key: 图片生成/图生图/F.2kleir4b老照片修复高清_2053851913120174081.json
name: F.2kleir4b老照片修复高清_2053851913120174081
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2kleir4b老照片修复高清_2053851913120174081.json
hash: 3e2fd36c88616cf0
coverage: 0.939394
learned_at: 2026-10-23 10:52:55
nodes: [VAEEncode, CLIPLoader, VAELoader, UNETLoader, ModelSamplingAuraFlow, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, VAEEncode, ImageResize+, UNETLoader, ReferenceLatent, EmptyFlux2LatentImage, easy cleanGpuUsed, VAEDecode, VAEDecode, VAELoader, LoraLoaderModelOnly, CLIPTextEncode, ConditioningZeroOut, Image Comparer (rgthree), LoraLoaderModelOnly, CLIPLoader, LoadImage, RunningHub Deepcleaner, LoraLoaderModelOnly, Float, ImageScaleBy, Image Comparer (rgthree), KSampler, RH_Captioner, KSamplerAdvanced, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 9, "denoise": "beta57", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/F.2kleir4b老照片修复高清_2053851913120174081.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2kleir4b老照片修复高清_2053851913120174081.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `VAEEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEEncode` ★核心
- `ImageResize+`
- `UNETLoader` ★核心
- `ReferenceLatent`
- `EmptyFlux2LatentImage`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `LoadImage`
- `RunningHub Deepcleaner`
- `LoraLoaderModelOnly` ★核心
- `Float`
- `ImageScaleBy`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `RH_Captioner`
- `KSamplerAdvanced` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `9`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta57`

## 知识

覆盖率 **94%**（31/33）

**有卡**：`VAEEncode`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`ImageResize+`、`ReferenceLatent`、`EmptyFlux2LatentImage`、`easy cleanGpuUsed`、`VAEDecode`、`ConditioningZeroOut`、`LoadImage`、`RunningHub Deepcleaner`、`Float`、`ImageScaleBy`、`KSampler`、`RH_Captioner`、`KSamplerAdvanced`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
