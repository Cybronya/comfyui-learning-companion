---
key: 图片生成/图生图/⭐️⭐️⭐️⭐️⭐️——Qwen-Image-Layered图像分层，将图片拆成多个 RGBA 图层_2008824799061090306.json
name: ⭐️⭐️⭐️⭐️⭐️——Qwen-Image-Layered图像分层，将图片拆成多个 RGBA 图层_2008824799061090306
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/⭐️⭐️⭐️⭐️⭐️——Qwen-Image-Layered图像分层，将图片拆成多个 RGBA 图层_2008824799061090306.json
hash: 94972beb904e8367
coverage: 1
learned_at: 2026-10-23 11:47:50
nodes: [KSampler, EmptyQwenImageLayeredLatentImage, UNETLoader, LatentCutToBatch, VAEEncode, VAEDecode, LoadImage, CLIPLoader, CLIPTextEncode, GetImageSize, VAELoader, ReferenceLatent, CLIPTextEncode, ReferenceLatent, ModelSamplingAuraFlow, ImageScaleToTotalPixels, JWInteger, SaveImage, HAIGC_Layer, HAIGC_CombineUnits, HAIGC_SavePSD]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 952285156355217, "steps": 20}
---

# 图片生成/图生图/⭐️⭐️⭐️⭐️⭐️——Qwen-Image-Layered图像分层，将图片拆成多个 RGBA 图层_2008824799061090306.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/⭐️⭐️⭐️⭐️⭐️——Qwen-Image-Layered图像分层，将图片拆成多个 RGBA 图层_2008824799061090306.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `KSampler` ★核心
- `EmptyQwenImageLayeredLatentImage`
- `UNETLoader` ★核心
- `LatentCutToBatch`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `GetImageSize`
- `VAELoader`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `ModelSamplingAuraFlow`
- `ImageScaleToTotalPixels`
- `JWInteger`
- `SaveImage`
- `HAIGC_Layer`
- `HAIGC_CombineUnits`
- `HAIGC_SavePSD`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `952285156355217`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`KSampler`、`EmptyQwenImageLayeredLatentImage`、`UNETLoader`、`LatentCutToBatch`、`VAEEncode`、`VAEDecode`、`LoadImage`、`CLIPLoader`、`CLIPTextEncode`、`GetImageSize`、`VAELoader`、`ReferenceLatent`、`ModelSamplingAuraFlow`、`ImageScaleToTotalPixels`、`JWInteger`、`SaveImage`、`HAIGC_Layer`、`HAIGC_CombineUnits`、`HAIGC_SavePSD`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、ReferenceLatent
