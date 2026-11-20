---
key: 平台全量/Flux2 Klein+Qwen 模糊图变高清去油腻 图像高清放大全能图片2.0  4k超清细节修复_2030832469687144449.json
name: Flux2 Klein+Qwen 模糊图变高清去油腻 图像高清放大全能图片2.0  4k超清细节修复_2030832469687144449
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux2 Klein+Qwen 模糊图变高清去油腻 图像高清放大全能图片2.0  4k超清细节修复_2030832469687144449.json
hash: 628b1794bb7ee6d8
coverage: 0.870968
learned_at: 2026-11-14 00:29:13
nodes: [UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, ReferenceLatent, VAEEncode, ConditioningZeroOut, CLIPTextEncode, ModelSamplingAuraFlow, UNETLoader, CLIPTextEncode, VAELoader, CLIPLoader, LoraLoaderModelOnly, VAEEncode, KSamplerAdvanced, KSampler, CLIPTextEncode, easy showAnything, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, GetImageSize, EmptyFlux2LatentImage, Image Comparer (rgthree), SaveImage, Image Comparer (rgthree), VAEDecode, LoadImage, VAEDecode, PreviewImage, RH_Captioner]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 852456, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Flux2 Klein+Qwen 模糊图变高清去油腻 图像高清放大全能图片2.0  4k超清细节修复_2030832469687144449.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux2 Klein+Qwen 模糊图变高清去油腻 图像高清放大全能图片2.0  4k超清细节修复_2030832469687144449.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `VAEEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSize`
- `EmptyFlux2LatentImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `LoadImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `RH_Captioner`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `852456`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（27/31）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`ReferenceLatent`、`VAEEncode`、`ConditioningZeroOut`、`CLIPTextEncode`、`ModelSamplingAuraFlow`、`KSamplerAdvanced`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSize`、`EmptyFlux2LatentImage`、`SaveImage`、`VAEDecode`、`LoadImage`、`RH_Captioner`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
