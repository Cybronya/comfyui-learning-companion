---
key: 图片生成/图生图/qwen  精准镜头控制器 图生图 多视角  Qwen Multiangle Camera_2041768515669069826.json
name: qwen  精准镜头控制器 图生图 多视角  Qwen Multiangle Camera_2041768515669069826
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen  精准镜头控制器 图生图 多视角  Qwen Multiangle Camera_2041768515669069826.json
hash: e3bed540f2586d07
coverage: 0.75
learned_at: 2026-10-23 11:41:43
nodes: [FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, SetNode, ImpactMakeAnyList, GetNode, SetNode, GetNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingAuraFlow, ImageScaleToTotalPixels, easy showAnything, GetNode, CLIPLoader, VAELoader, CFGNorm, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, SaveImage, KSampler, VAEDecode, GetNode, VAEEncode, SetNode, PreviewImage, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1002, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen  精准镜头控制器 图生图 多视角  Qwen Multiangle Camera_2041768515669069826.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen  精准镜头控制器 图生图 多视角  Qwen Multiangle Camera_2041768515669069826.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `SetNode`
- `ImpactMakeAnyList`
- `GetNode`
- `SetNode`
- `GetNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `ImageScaleToTotalPixels`
- `easy showAnything`
- `GetNode`
- `CLIPLoader`
- `VAELoader`
- `CFGNorm`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `SaveImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `VAEEncode` ★核心
- `SetNode`
- `PreviewImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1002`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`FluxKontextMultiReferenceLatentMethod`、`ImpactMakeAnyList`、`QwenMultiangleCameraNode`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`ImageScaleToTotalPixels`、`CLIPLoader`、`VAELoader`、`CFGNorm`、`TextEncodeQwenImageEditPlus`、`SaveImage`、`KSampler`、`VAEDecode`、`VAEEncode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
