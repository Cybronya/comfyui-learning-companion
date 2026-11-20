---
key: 平台全量/老照片修复+图片高清放大 FLUX.2-klein-9b+Zimage高清修复细节 去除AI感极致_2031937095199100930.json
name: 老照片修复+图片高清放大 FLUX.2-klein-9b+Zimage高清修复细节 去除AI感极致_2031937095199100930
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/老照片修复+图片高清放大 FLUX.2-klein-9b+Zimage高清修复细节 去除AI感极致_2031937095199100930.json
hash: 0f5af0c5b36fbb44
coverage: 0.885714
learned_at: 2026-11-14 02:30:03
nodes: [VAEEncode, CLIPLoader, VAELoader, UNETLoader, ModelSamplingAuraFlow, CLIPTextEncode, CLIPTextEncode, RunningHub Deepcleaner, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEEncode, UNETLoader, ReferenceLatent, EmptyFlux2LatentImage, RH_Captioner, easy cleanGpuUsed, VAEDecode, Float, KSamplerAdvanced, VAELoader, LoraLoaderModelOnly, ConditioningZeroOut, PreviewImage, KSampler, LoraLoaderModelOnly, CLIPLoader, ImageResize+, ImageScaleBy, VAEDecode, Image Comparer (rgthree), Image Comparer (rgthree), SaveImage, PreviewImage, LoadImage, CLIPTextEncode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 959019173930606, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/老照片修复+图片高清放大 FLUX.2-klein-9b+Zimage高清修复细节 去除AI感极致_2031937095199100930.json

> 来源文件 `comfyui_library/workflows/平台全量/老照片修复+图片高清放大 FLUX.2-klein-9b+Zimage高清修复细节 去除AI感极致_2031937095199100930.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `VAEEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `RunningHub Deepcleaner`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `ReferenceLatent`
- `EmptyFlux2LatentImage`
- `RH_Captioner`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `Float`
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `PreviewImage`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `ImageResize+`
- `ImageScaleBy`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `SaveImage`
- `PreviewImage`
- `LoadImage`
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `959019173930606`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（31/35）

**有卡**：`VAEEncode`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`RunningHub Deepcleaner`、`LoraLoaderModelOnly`、`ReferenceLatent`、`EmptyFlux2LatentImage`、`RH_Captioner`、`easy cleanGpuUsed`、`VAEDecode`、`Float`、`KSamplerAdvanced`、`ConditioningZeroOut`、`KSampler`、`ImageResize+`、`ImageScaleBy`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
