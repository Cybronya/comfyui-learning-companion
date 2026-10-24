---
key: 图片生成/图生图/qwen-image-layered-image2image-分层式生图-图生图_2003438837143642113.json
name: qwen-image-layered-image2image-分层式生图-图生图_2003438837143642113
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image-layered-image2image-分层式生图-图生图_2003438837143642113.json
hash: 04f52d2f1f37f6cf
coverage: 0.947368
learned_at: 2026-10-23 11:42:53
nodes: [LatentCutToBatch, ReferenceLatent, KSampler, UNETLoader, GetImageSize, LoadImage, LoraLoaderModelOnly, VAELoader, VAEEncode, CLIPLoader, ModelSamplingAuraFlow, CLIPTextEncode, CLIPTextEncode, EmptyHunyuanLatentVideo, ImageScaleToTotalPixels, ReferenceLatent, Note, VAEDecode, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "lcm", "scheduler": "simple", "seed": 993932884387244, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen-image-layered-image2image-分层式生图-图生图_2003438837143642113.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-image-layered-image2image-分层式生图-图生图_2003438837143642113.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `LatentCutToBatch`
- `ReferenceLatent`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `GetImageSize`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `VAEEncode` ★核心
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `ImageScaleToTotalPixels`
- `ReferenceLatent`
- `Note`
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `993932884387244`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`LatentCutToBatch`、`ReferenceLatent`、`KSampler`、`UNETLoader`、`GetImageSize`、`LoadImage`、`LoraLoaderModelOnly`、`VAELoader`、`VAEEncode`、`CLIPLoader`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`ImageScaleToTotalPixels`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
