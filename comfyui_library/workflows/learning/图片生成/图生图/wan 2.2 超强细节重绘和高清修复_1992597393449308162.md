---
key: 图片生成/图生图/wan 2.2 超强细节重绘和高清修复_1992597393449308162.json
name: wan 2.2 超强细节重绘和高清修复_1992597393449308162
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan 2.2 超强细节重绘和高清修复_1992597393449308162.json
hash: 3d0e4c208b64540b
coverage: 0.708333
learned_at: 2026-10-23 11:45:47
nodes: [PreviewImage, CLIPTextEncode, PathchSageAttentionKJ, Text Concatenate, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAEDecode, easy showAnything, CR Text Replace, VAELoader, PreviewAny, SaveImage, PreviewImage, ImageResizeKJv2, PrimitiveString, KSampler, Qwen3_VQA, VAEEncode, CLIPTextEncode, PMRF, PreviewAny, Image Comparer (rgthree), LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.12000000000000002, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 305036398037235, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/wan 2.2 超强细节重绘和高清修复_1992597393449308162.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan 2.2 超强细节重绘和高清修复_1992597393449308162.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `Text Concatenate`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `easy showAnything`
- `CR Text Replace`
- `VAELoader`
- `PreviewAny`
- `SaveImage`
- `PreviewImage`
- `ImageResizeKJv2`
- `PrimitiveString`
- `KSampler` ★核心
- `Qwen3_VQA`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `PMRF`
- `PreviewAny`
- `Image Comparer (rgthree)`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `305036398037235`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.12000000000000002`

## 知识

覆盖率 **71%**（17/24）

**有卡**：`CLIPTextEncode`、`PathchSageAttentionKJ`、`Text Concatenate`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAEDecode`、`CR Text Replace`、`VAELoader`、`SaveImage`、`ImageResizeKJv2`、`KSampler`、`Qwen3_VQA`、`VAEEncode`、`PMRF`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
