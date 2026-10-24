---
key: 图片生成/图生图/qwen-image-layered-image2image_2002227567119724545.json
name: qwen-image-layered-image2image_2002227567119724545
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image-layered-image2image_2002227567119724545.json
hash: 4e8569cd2d269c7c
coverage: 0.947368
learned_at: 2026-10-23 11:42:54
nodes: [LatentCutToBatch, ModelSamplingAuraFlow, LoadImage, Note, VAEDecode, UNETLoader, ImageScaleToTotalPixels, GetImageSize, EmptyHunyuanLatentVideo, CLIPLoader, VAELoader, ReferenceLatent, ReferenceLatent, CLIPTextEncode, CLIPTextEncode, SaveImage, LoraLoaderModelOnly, KSampler, VAEEncode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "lcm", "scheduler": "simple", "seed": 45007732636494, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen-image-layered-image2image_2002227567119724545.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-image-layered-image2image_2002227567119724545.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `LatentCutToBatch`
- `ModelSamplingAuraFlow`
- `LoadImage`
- `Note`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `EmptyHunyuanLatentVideo`
- `CLIPLoader`
- `VAELoader`
- `ReferenceLatent`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `VAEEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `45007732636494`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`LatentCutToBatch`、`ModelSamplingAuraFlow`、`LoadImage`、`VAEDecode`、`UNETLoader`、`ImageScaleToTotalPixels`、`GetImageSize`、`EmptyHunyuanLatentVideo`、`CLIPLoader`、`VAELoader`、`ReferenceLatent`、`CLIPTextEncode`、`SaveImage`、`LoraLoaderModelOnly`、`KSampler`、`VAEEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
