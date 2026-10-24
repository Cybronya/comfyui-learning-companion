---
key: 图片生成/图生图/Qwen 一键多角度相机 多角度照明工作流 V1.0_2011096627490070530.json
name: Qwen 一键多角度相机 多角度照明工作流 V1.0_2011096627490070530
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen 一键多角度相机 多角度照明工作流 V1.0_2011096627490070530.json
hash: 5a3f7b8b980c7f46
coverage: 0.970588
learned_at: 2026-10-23 11:14:27
nodes: [CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, TextEncodeQwenImageEditPlus, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, VAEEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, TextEncodeQwenImageEditPlus, ImageScaleToTotalPixels, CR Text Concatenate, VAELoader, CFGNorm, ModelSamplingAuraFlow, QwenMultiangleLightningNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, easy promptList, QwenMultiangleLightningNode, QwenMultiangleCameraNode, QwenMultiangleLightningNode, QwenMultiangleLightningNode, easy showAnything, CLIPLoader, VAEDecode, KSampler, UNETLoader, LoadImage, QwenMultiangleCameraNode, QwenMultiangleLightningNode, QwenMultiangleCameraNode, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 857263754436264, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen 一键多角度相机 多角度照明工作流 V1.0_2011096627490070530.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen 一键多角度相机 多角度照明工作流 V1.0_2011096627490070530.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `TextEncodeQwenImageEditPlus`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImageEditPlus`
- `ImageScaleToTotalPixels`
- `CR Text Concatenate`
- `VAELoader`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `QwenMultiangleLightningNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `easy promptList`
- `QwenMultiangleLightningNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleLightningNode`
- `QwenMultiangleLightningNode`
- `easy showAnything`
- `CLIPLoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `QwenMultiangleCameraNode`
- `QwenMultiangleLightningNode`
- `QwenMultiangleCameraNode`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `857263754436264`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **97%**（33/34）

**有卡**：`CR Text Concatenate`、`TextEncodeQwenImageEditPlus`、`FluxKontextMultiReferenceLatentMethod`、`VAEEncode`、`LoraLoaderModelOnly`、`ImageScaleToTotalPixels`、`VAELoader`、`CFGNorm`、`ModelSamplingAuraFlow`、`QwenMultiangleLightningNode`、`QwenMultiangleCameraNode`、`easy promptList`、`CLIPLoader`、`VAEDecode`、`KSampler`、`UNETLoader`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
