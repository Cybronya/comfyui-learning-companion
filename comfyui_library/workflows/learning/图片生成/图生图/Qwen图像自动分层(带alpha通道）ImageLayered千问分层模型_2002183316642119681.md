---
key: 图片生成/图生图/Qwen图像自动分层(带alpha通道）ImageLayered千问分层模型_2002183316642119681.json
name: Qwen图像自动分层(带alpha通道）ImageLayered千问分层模型_2002183316642119681
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen图像自动分层(带alpha通道）ImageLayered千问分层模型_2002183316642119681.json
hash: 90760a3b43a25484
coverage: 0.892857
learned_at: 2026-10-23 11:22:12
nodes: [ReferenceLatent, CLIPTextEncode, ModelSamplingAuraFlow, CLIPLoader, VAELoader, VAEEncode, ReferenceLatent, CLIPTextEncode, VAEDecode, VAEDecode, ImageScaleToTotalPixels, GetImageSize, EmptyHunyuanLatentVideo, MathExpression|pysssss, Int, Fast Groups Bypasser (rgthree), LoadImage, UNETLoader, Note, LatentCutToBatch, LatentFromBatch, Note, SaveImage, SaveImage, LoadImage, Int, LoraLoaderModelOnly, KSampler]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 831811930776229, "steps": 40}
---

# 图片生成/图生图/Qwen图像自动分层(带alpha通道）ImageLayered千问分层模型_2002183316642119681.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen图像自动分层(带alpha通道）ImageLayered千问分层模型_2002183316642119681.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `VAELoader`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `EmptyHunyuanLatentVideo`
- `MathExpression|pysssss`
- `Int`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `UNETLoader` ★核心
- `Note`
- `LatentCutToBatch`
- `LatentFromBatch`
- `Note`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `Int`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `831811930776229`
- `steps` = `40`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（25/28）

**有卡**：`ReferenceLatent`、`CLIPTextEncode`、`ModelSamplingAuraFlow`、`CLIPLoader`、`VAELoader`、`VAEEncode`、`VAEDecode`、`ImageScaleToTotalPixels`、`GetImageSize`、`EmptyHunyuanLatentVideo`、`MathExpression|pysssss`、`Int`、`LoadImage`、`UNETLoader`、`LatentCutToBatch`、`LatentFromBatch`、`SaveImage`、`LoraLoaderModelOnly`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
