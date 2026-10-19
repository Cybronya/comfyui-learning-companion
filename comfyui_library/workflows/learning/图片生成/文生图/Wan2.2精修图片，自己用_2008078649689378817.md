---
key: 图片生成/文生图/Wan2.2精修图片，自己用_2008078649689378817.json
name: Wan2.2精修图片，自己用_2008078649689378817
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2精修图片，自己用_2008078649689378817.json
hash: 40a5782451516fc6
coverage: 0.944444
learned_at: 2026-10-19 22:00:57
nodes: [CLIPTextEncode, CLIPLoader, Text Concatenate, PathchSageAttentionKJ, ModelSamplingSD3, UNETLoader, LoraLoader, VAEDecode, LoraLoader, SaveImage, Image Comparer (rgthree), LoraLoader, Image Comparer (rgthree), CLIPTextEncode, VAEEncode, LoraLoader, LoadImage, CLIPTextEncode, CLIPTextEncode, ModelSamplingAuraFlow, SaveImage, KSampler, EmptySD3LatentImage, VAELoader, CLIPLoader, Text Multiline, VAELoader, LoraLoaderModelOnly, Text Multiline, VAEDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoraLoader, KSampler, LoraLoader]
patterns: [image_to_image, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.30000000000000004, "lora_name": "胸部效果.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 690149045641190, "steps": 10, "strength_clip": 0.7000000000000002, "strength_model": 0.7000000000000002}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Wan2.2精修图片，自己用_2008078649689378817.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2精修图片，自己用_2008078649689378817.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `Text Concatenate`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `VAEDecode` ★核心
- `LoraLoader` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoraLoader` ★核心
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `LoraLoader` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `SaveImage`
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `VAELoader`
- `CLIPLoader`
- `Text Multiline`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `Text Multiline`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `KSampler` ★核心
- `LoraLoader` ★核心

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `胸部效果.safetensors`
- `strength_model` = `0.7000000000000002`
- `strength_clip` = `0.7000000000000002`
- `seed` = `690149045641190`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **94%**（34/36）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`Text Concatenate`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`UNETLoader`、`LoraLoader`、`VAEDecode`、`SaveImage`、`VAEEncode`、`LoadImage`、`ModelSamplingAuraFlow`、`KSampler`、`EmptySD3LatentImage`、`VAELoader`、`Text Multiline`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
