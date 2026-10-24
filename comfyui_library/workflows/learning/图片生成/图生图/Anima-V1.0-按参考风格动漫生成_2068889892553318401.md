---
key: 图片生成/图生图/Anima-V1.0-按参考风格动漫生成_2068889892553318401.json
name: Anima-V1.0-按参考风格动漫生成_2068889892553318401
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Anima-V1.0-按参考风格动漫生成_2068889892553318401.json
hash: 6685e15ca373c7bf
coverage: 0.95
learned_at: 2026-10-23 10:51:10
nodes: [UNETLoader, LoraLoaderModelOnly, CLIPLoader, ImageScaleBy, ImageResizeKJv2, CLIPTextEncode, VAEEncode, VAELoader, PreviewImage, RFInversion, UnofficialExtensions, KSampler, CLIPTextEncode, EmptyLatentImage, LoadImage, UntwistingRoPE, VAEDecode, SaveImage, Int, Int]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler_ancestral", "scheduler": "simple", "seed": 1028097381653091, "steps": 10, "width": 1024}
---

# 图片生成/图生图/Anima-V1.0-按参考风格动漫生成_2068889892553318401.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Anima-V1.0-按参考风格动漫生成_2068889892553318401.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `ImageScaleBy`
- `ImageResizeKJv2`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `VAELoader`
- `PreviewImage`
- `RFInversion`
- `UnofficialExtensions`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `LoadImage`
- `UntwistingRoPE`
- `VAEDecode` ★核心
- `SaveImage`
- `Int`
- `Int`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `1028097381653091`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`ImageScaleBy`、`ImageResizeKJv2`、`CLIPTextEncode`、`VAEEncode`、`VAELoader`、`RFInversion`、`UnofficialExtensions`、`KSampler`、`EmptyLatentImage`、`LoadImage`、`UntwistingRoPE`、`VAEDecode`、`SaveImage`、`Int`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage
