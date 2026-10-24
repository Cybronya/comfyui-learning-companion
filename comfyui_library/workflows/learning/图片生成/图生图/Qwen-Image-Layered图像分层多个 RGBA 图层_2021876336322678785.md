---
key: 图片生成/图生图/Qwen-Image-Layered图像分层多个 RGBA 图层_2021876336322678785.json
name: Qwen-Image-Layered图像分层多个 RGBA 图层_2021876336322678785
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-Layered图像分层多个 RGBA 图层_2021876336322678785.json
hash: 6ddd2a22d74fdbf9
coverage: 0.947368
learned_at: 2026-10-23 11:17:16
nodes: [CLIPLoader, VAELoader, KSampler, LatentCutToBatch, PreviewImage, VAEDecode, CLIPTextEncode, ModelSamplingAuraFlow, GetImageSize, EmptyQwenImageLayeredLatentImage, CLIPTextEncode, ImageScaleToTotalPixels, JWInteger, ReferenceLatent, ReferenceLatent, UNETLoader, VAEEncode, SaveImage, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 934054466628519, "steps": 20}
---

# 图片生成/图生图/Qwen-Image-Layered图像分层多个 RGBA 图层_2021876336322678785.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-Layered图像分层多个 RGBA 图层_2021876336322678785.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `LatentCutToBatch`
- `PreviewImage`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `GetImageSize`
- `EmptyQwenImageLayeredLatentImage`
- `CLIPTextEncode` ★核心
- `ImageScaleToTotalPixels`
- `JWInteger`
- `ReferenceLatent`
- `ReferenceLatent`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `SaveImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `934054466628519`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`CLIPLoader`、`VAELoader`、`KSampler`、`LatentCutToBatch`、`VAEDecode`、`CLIPTextEncode`、`ModelSamplingAuraFlow`、`GetImageSize`、`EmptyQwenImageLayeredLatentImage`、`ImageScaleToTotalPixels`、`JWInteger`、`ReferenceLatent`、`UNETLoader`、`VAEEncode`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、ReferenceLatent
