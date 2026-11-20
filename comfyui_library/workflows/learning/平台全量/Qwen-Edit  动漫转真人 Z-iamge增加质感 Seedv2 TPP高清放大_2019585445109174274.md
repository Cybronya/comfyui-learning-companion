---
key: 平台全量/Qwen-Edit  动漫转真人 Z-iamge增加质感 Seedv2 TPP高清放大_2019585445109174274.json
name: Qwen-Edit  动漫转真人 Z-iamge增加质感 Seedv2 TPP高清放大_2019585445109174274
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-Edit  动漫转真人 Z-iamge增加质感 Seedv2 TPP高清放大_2019585445109174274.json
hash: ded461da11ccdeea
coverage: 0.852941
learned_at: 2026-11-14 00:51:06
nodes: [ModelSamplingAuraFlow, CFGNorm, TextEncodeQwenImageEditPlus, KSampler, CLIPLoader, LoraLoaderModelOnly, UNETLoader, Image Comparer (rgthree), ImageScaleToTotalPixels, VAEEncode, FluxKontextMultiReferenceLatentMethod, ConditioningZeroOut, easy cleanGpuUsed, VAEDecode, UNETLoader, Image Comparer (rgthree), SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, ImageScaleBy, Note, KSampler, Note, PreviewImage, VAELoader, CLIPLoader, VAELoader, ConditioningZeroOut, VAEEncode, CLIPTextEncode, LoraLoaderModelOnly, VAEDecode, SaveImage, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.1, "sampler_name": "euler", "scheduler": "simple", "seed": 351330448865434, "steps": 20}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Qwen-Edit  动漫转真人 Z-iamge增加质感 Seedv2 TPP高清放大_2019585445109174274.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-Edit  动漫转真人 Z-iamge增加质感 Seedv2 TPP高清放大_2019585445109174274.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `FluxKontextMultiReferenceLatentMethod`
- `ConditioningZeroOut`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `Image Comparer (rgthree)`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `ImageScaleBy`
- `Note`
- `KSampler` ★核心
- `Note`
- `PreviewImage`
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `351330448865434`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.1`

## 知识

覆盖率 **85%**（29/34）

**有卡**：`ModelSamplingAuraFlow`、`CFGNorm`、`TextEncodeQwenImageEditPlus`、`KSampler`、`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`ImageScaleToTotalPixels`、`VAEEncode`、`FluxKontextMultiReferenceLatentMethod`、`ConditioningZeroOut`、`easy cleanGpuUsed`、`VAEDecode`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`ImageScaleBy`、`VAELoader`、`CLIPTextEncode`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
