---
key: 平台全量/Flux.1-Fill-OneReward无损消除元素_1958473949078306818.json
name: Flux.1-Fill-OneReward无损消除元素_1958473949078306818
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux.1-Fill-OneReward无损消除元素_1958473949078306818.json
hash: c911eaea4b32f0c6
coverage: 0.896552
learned_at: 2026-11-14 00:28:49
nodes: [FluxGuidance, DifferentialDiffusion, InpaintModelConditioning, easy int, ConditioningZeroOut, easy int, ModelSamplingFlux, EmptySD3LatentImage, FluxGuidance, CLIPTextEncode, DualCLIPLoader, PreviewImage, VAEEncode, KSampler, VAEDecode, VAELoader, ConditioningZeroOut, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, ImageConcatMulti, PreviewImage, UNETLoader, KSampler, LoadImage, UNETLoader, CLIPTextEncode, SaveImage, PreviewImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.4100000000000001, "sampler_name": "euler", "scheduler": "simple", "seed": 10086, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Flux.1-Fill-OneReward无损消除元素_1958473949078306818.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux.1-Fill-OneReward无损消除元素_1958473949078306818.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `FluxGuidance`
- `DifferentialDiffusion`
- `InpaintModelConditioning`
- `easy int`
- `ConditioningZeroOut`
- `easy int`
- `ModelSamplingFlux`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `PreviewImage`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `PreviewImage`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `10086`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4100000000000001`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`FluxGuidance`、`DifferentialDiffusion`、`InpaintModelConditioning`、`easy int`、`ConditioningZeroOut`、`ModelSamplingFlux`、`EmptySD3LatentImage`、`CLIPTextEncode`、`DualCLIPLoader`、`VAEEncode`、`KSampler`、`VAEDecode`、`VAELoader`、`LoraLoaderModelOnly`、`ImageConcatMulti`、`UNETLoader`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
