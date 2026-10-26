---
key: 数字人/数字人/Dataset gen - QWEN - Icekiub v4_1978295273489326081.json
name: Dataset gen - QWEN - Icekiub v4_1978295273489326081
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Dataset gen - QWEN - Icekiub v4_1978295273489326081.json
hash: 43e5ff73328325f6
coverage: 0.965517
learned_at: 2026-10-26 01:54:08
nodes: [UNETLoader, Text Multiline, CR Prompt List, TextEncodeQwenImageEditPlus, KSampler, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Label (rgthree), StringConcatenate, Label (rgthree), Text Multiline, Label (rgthree), SaveImageKJ, Label (rgthree), ImageScaleToTotalPixels, GetImageSize, EmptyLatentImage, PreviewImage, Label (rgthree), ModelSamplingAuraFlow, Label (rgthree), Label (rgthree), CLIPLoader, VAELoader, LoadImage, Label (rgthree), VAEDecode, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "beta", "seed": 884578149671194, "steps": 4, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/Dataset gen - QWEN - Icekiub v4_1978295273489326081.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Dataset gen - QWEN - Icekiub v4_1978295273489326081.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `UNETLoader` ★核心
- `Text Multiline`
- `CR Prompt List`
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Label (rgthree)`
- `StringConcatenate`
- `Label (rgthree)`
- `Text Multiline`
- `Label (rgthree)`
- `SaveImageKJ`
- `Label (rgthree)`
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `Label (rgthree)`
- `ModelSamplingAuraFlow`
- `Label (rgthree)`
- `Label (rgthree)`
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `Label (rgthree)`
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `884578149671194`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **97%**（28/29）

**有卡**：`UNETLoader`、`Text Multiline`、`CR Prompt List`、`TextEncodeQwenImageEditPlus`、`KSampler`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`Label (rgthree)`、`StringConcatenate`、`SaveImageKJ`、`ImageScaleToTotalPixels`、`GetImageSize`、`EmptyLatentImage`、`ModelSamplingAuraFlow`、`CLIPLoader`、`VAELoader`、`LoadImage`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
