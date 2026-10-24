---
key: 图片生成/图生图/Qwen-image-2511-Multiple-Angles-LoRA_2013960041979715586.json
name: Qwen-image-2511-Multiple-Angles-LoRA_2013960041979715586
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image-2511-Multiple-Angles-LoRA_2013960041979715586.json
hash: ec87c6c86ceaa716
coverage: 1
learned_at: 2026-10-23 11:18:01
nodes: [easy promptLine, Text Multiline, VAEDecode, AddLabel, KSampler, CFGNorm, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus_lrzjason, Text Multiline, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, ImageScaleToTotalPixels, TextEncodeQwenImageEditPlus, VAEEncode, SaveImage, LoadImage, LoraLoaderModelOnly]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 390351765371351, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-image-2511-Multiple-Angles-LoRA_2013960041979715586.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image-2511-Multiple-Angles-LoRA_2013960041979715586.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `easy promptLine`
- `Text Multiline`
- `VAEDecode` ★核心
- `AddLabel`
- `KSampler` ★核心
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus_lrzjason`
- `Text Multiline`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ImageScaleToTotalPixels`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `SaveImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `390351765371351`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`easy promptLine`、`Text Multiline`、`VAEDecode`、`AddLabel`、`KSampler`、`CFGNorm`、`ModelSamplingAuraFlow`、`TextEncodeQwenImageEditPlus_lrzjason`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ImageScaleToTotalPixels`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
