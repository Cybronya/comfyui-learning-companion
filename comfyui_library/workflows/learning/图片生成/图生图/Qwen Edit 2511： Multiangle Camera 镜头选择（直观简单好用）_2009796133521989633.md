---
key: 图片生成/图生图/Qwen Edit 2511： Multiangle Camera 镜头选择（直观简单好用）_2009796133521989633.json
name: Qwen Edit 2511： Multiangle Camera 镜头选择（直观简单好用）_2009796133521989633
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Edit 2511： Multiangle Camera 镜头选择（直观简单好用）_2009796133521989633.json
hash: e964c911321996c9
coverage: 0.857143
learned_at: 2026-10-23 11:12:12
nodes: [FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, Note, EmptySD3LatentImage, ImageScaleToTotalPixels, VAEDecode, QwenMultiangleCameraNode, VAELoader, CLIPLoader, SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly, QwenMultiangleCameraNode, easy showAnything, QwenMultiangleCameraNode, easy promptList, QwenMultiangleCameraNode, Note, Note, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, VAEEncode, KSampler, ModelSamplingAuraFlow, CFGNorm, UNETLoader, LoadImage, QwenMultiangleCameraNode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1002, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Edit 2511： Multiangle Camera 镜头选择（直观简单好用）_2009796133521989633.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Edit 2511： Multiangle Camera 镜头选择（直观简单好用）_2009796133521989633.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `Note`
- `EmptySD3LatentImage`
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `QwenMultiangleCameraNode`
- `VAELoader`
- `CLIPLoader`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `QwenMultiangleCameraNode`
- `easy showAnything`
- `QwenMultiangleCameraNode`
- `easy promptList`
- `QwenMultiangleCameraNode`
- `Note`
- `Note`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `UNETLoader` ★核心
- `LoadImage`
- `QwenMultiangleCameraNode`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1002`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（24/28）

**有卡**：`FluxKontextMultiReferenceLatentMethod`、`EmptySD3LatentImage`、`ImageScaleToTotalPixels`、`VAEDecode`、`QwenMultiangleCameraNode`、`VAELoader`、`CLIPLoader`、`SaveImage`、`LoraLoaderModelOnly`、`easy promptList`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`KSampler`、`ModelSamplingAuraFlow`、`CFGNorm`、`UNETLoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
