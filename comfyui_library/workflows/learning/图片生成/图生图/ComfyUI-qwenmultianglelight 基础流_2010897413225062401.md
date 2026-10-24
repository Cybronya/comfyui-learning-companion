---
key: 图片生成/图生图/ComfyUI-qwenmultianglelight 基础流_2010897413225062401.json
name: ComfyUI-qwenmultianglelight 基础流_2010897413225062401
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/ComfyUI-qwenmultianglelight 基础流_2010897413225062401.json
hash: 9a0e9e3901f45fbb
coverage: 0.925926
learned_at: 2026-10-23 10:51:58
nodes: [ModelSamplingAuraFlow, CFGNorm, Note, EmptySD3LatentImage, ReferenceLatent, ReferenceLatent, VAELoader, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, ImageScaleToTotalPixels, VAEEncode, TextEncodeQwenImageEditPlus, easy showAnything, UNETLoader, QwenMultiangleLightningNode, QwenMultiangleLightningNode, QwenMultiangleLightningNode, easy promptList, LoadImage, CLIPLoader, LoraLoaderModelOnly, TextEncodeQwenImageEditPlus, QwenMultiangleLightningNode, QwenMultiangleLightningNode, VAEDecode, SaveImage, KSampler]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1000, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/ComfyUI-qwenmultianglelight 基础流_2010897413225062401.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/ComfyUI-qwenmultianglelight 基础流_2010897413225062401.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `Note`
- `EmptySD3LatentImage`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAELoader`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `TextEncodeQwenImageEditPlus`
- `easy showAnything`
- `UNETLoader` ★核心
- `QwenMultiangleLightningNode`
- `QwenMultiangleLightningNode`
- `QwenMultiangleLightningNode`
- `easy promptList`
- `LoadImage`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImageEditPlus`
- `QwenMultiangleLightningNode`
- `QwenMultiangleLightningNode`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1000`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（25/27）

**有卡**：`ModelSamplingAuraFlow`、`CFGNorm`、`EmptySD3LatentImage`、`ReferenceLatent`、`VAELoader`、`FluxKontextMultiReferenceLatentMethod`、`ImageScaleToTotalPixels`、`VAEEncode`、`TextEncodeQwenImageEditPlus`、`UNETLoader`、`QwenMultiangleLightningNode`、`easy promptList`、`LoadImage`、`CLIPLoader`、`LoraLoaderModelOnly`、`VAEDecode`、`SaveImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
