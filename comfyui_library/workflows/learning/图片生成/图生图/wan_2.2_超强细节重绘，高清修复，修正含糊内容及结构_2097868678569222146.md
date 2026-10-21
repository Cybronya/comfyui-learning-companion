---
key: 图片生成/图生图/wan_2.2_超强细节重绘，高清修复，修正含糊内容及结构_2097868678569222146.json
name: wan_2.2_超强细节重绘，高清修复，修正含糊内容及结构_2097868678569222146
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan_2.2_超强细节重绘，高清修复，修正含糊内容及结构_2097868678569222146.json
hash: 2e6ba924bfcd1baa
coverage: 0.708333
learned_at: 2026-10-21 00:46:29
nodes: [PreviewImage, CLIPTextEncode, PathchSageAttentionKJ, CLIPTextEncode, VAEEncode, Text Concatenate, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAEDecode, PreviewAny, easy showAnything, CR Text Replace, VAELoader, PreviewAny, PMRF, SaveImage, PreviewImage, LoadImage, ImageResizeKJv2, Image Comparer (rgthree), PrimitiveString, KSampler, Qwen3_VQA]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.12000000000000002, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 536939553297328, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/wan_2.2_超强细节重绘，高清修复，修正含糊内容及结构_2097868678569222146.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan_2.2_超强细节重绘，高清修复，修正含糊内容及结构_2097868678569222146.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `Text Concatenate`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `PreviewAny`
- `easy showAnything`
- `CR Text Replace`
- `VAELoader`
- `PreviewAny`
- `PMRF`
- `SaveImage`
- `PreviewImage`
- `LoadImage`
- `ImageResizeKJv2`
- `Image Comparer (rgthree)`
- `PrimitiveString`
- `KSampler` ★核心
- `Qwen3_VQA`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `536939553297328`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.12000000000000002`

## 知识

覆盖率 **71%**（17/24）

**有卡**：`CLIPTextEncode`、`PathchSageAttentionKJ`、`VAEEncode`、`Text Concatenate`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAEDecode`、`CR Text Replace`、`VAELoader`、`PMRF`、`SaveImage`、`LoadImage`、`ImageResizeKJv2`、`KSampler`、`Qwen3_VQA`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
