---
key: 平台全量/SamsaLa AIGC视觉-Qwen Layerd图像分层_2002560440154636290.json
name: SamsaLa AIGC视觉-Qwen Layerd图像分层_2002560440154636290
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/SamsaLa AIGC视觉-Qwen Layerd图像分层_2002560440154636290.json
hash: 0ebe24205a707384
coverage: 0.827586
learned_at: 2026-11-14 00:56:54
nodes: [ReferenceLatent, ReferenceLatent, ModelSamplingAuraFlow, VAEEncode, Note, EmptyHunyuanLatentVideo, CLIPTextEncode, LatentCutToBatch, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, KSampler, CLIPTextEncode, LoraLoaderModelOnly, JWInteger, Note, Note, Float, Int, Note, Int, Note, UNETLoader, CLIPLoader, VAELoader, VAEDecode, LoadImage, VHS_VideoCombine, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 499594310529964, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/SamsaLa AIGC视觉-Qwen Layerd图像分层_2002560440154636290.json

> 来源文件 `comfyui_library/workflows/平台全量/SamsaLa AIGC视觉-Qwen Layerd图像分层_2002560440154636290.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `ReferenceLatent`
- `ReferenceLatent`
- `ModelSamplingAuraFlow`
- `VAEEncode` ★核心
- `Note`
- `EmptyHunyuanLatentVideo`
- `CLIPTextEncode` ★核心
- `LatentCutToBatch`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MathExpression|pysssss`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `JWInteger`
- `Note`
- `Note`
- `Float`
- `Int`
- `Note`
- `Int`
- `Note`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `LoadImage`
- `VHS_VideoCombine`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `499594310529964`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（24/29）

**有卡**：`ReferenceLatent`、`ModelSamplingAuraFlow`、`VAEEncode`、`EmptyHunyuanLatentVideo`、`CLIPTextEncode`、`LatentCutToBatch`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`KSampler`、`LoraLoaderModelOnly`、`JWInteger`、`Float`、`Int`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`VHS_VideoCombine`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
