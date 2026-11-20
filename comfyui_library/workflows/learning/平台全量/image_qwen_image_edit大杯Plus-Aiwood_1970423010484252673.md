---
key: 平台全量/image_qwen_image_edit大杯Plus-Aiwood_1970423010484252673.json
name: image_qwen_image_edit大杯Plus-Aiwood_1970423010484252673
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/image_qwen_image_edit大杯Plus-Aiwood_1970423010484252673.json
hash: b2e69c4f6cb31eb9
coverage: 0.589744
learned_at: 2026-11-14 01:12:45
nodes: [CFGNorm, GetNode, GetNode, GetNode, GetNode, LoadImage, ImageScaleToTotalPixels, SetNode, ImageScaleToTotalPixels, SetNode, GetNode, SetNode, SetNode, SetNode, ImageStitch, ImageScaleToTotalPixels, SetNode, SetNode, VAEDecode, PreviewImage, DWPreprocessor, GetNode, GetNode, ImageScaleToTotalPixels, LoadImage, GetNode, ModelSamplingAuraFlow, VAEEncode, SaveImage, KSampler, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoadImage, LoadImage, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, EmptySD3LatentImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 897, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/image_qwen_image_edit大杯Plus-Aiwood_1970423010484252673.json

> 来源文件 `comfyui_library/workflows/平台全量/image_qwen_image_edit大杯Plus-Aiwood_1970423010484252673.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `CFGNorm`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `SetNode`
- `ImageScaleToTotalPixels`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageStitch`
- `ImageScaleToTotalPixels`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `PreviewImage`
- `DWPreprocessor`
- `GetNode`
- `GetNode`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `GetNode`
- `ModelSamplingAuraFlow`
- `VAEEncode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `EmptySD3LatentImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `897`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **59%**（23/39）

**有卡**：`CFGNorm`、`LoadImage`、`ImageScaleToTotalPixels`、`ImageStitch`、`VAEDecode`、`DWPreprocessor`、`ModelSamplingAuraFlow`、`VAEEncode`、`SaveImage`、`KSampler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`TextEncodeQwenImageEditPlus`、`EmptySD3LatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
