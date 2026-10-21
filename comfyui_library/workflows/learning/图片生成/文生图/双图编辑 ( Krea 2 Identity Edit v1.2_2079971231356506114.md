---
key: 图片生成/文生图/双图编辑 ( Krea 2 Identity Edit v1.2_2079971231356506114.json
name: 双图编辑 ( Krea 2 Identity Edit v1.2_2079971231356506114
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/双图编辑 ( Krea 2 Identity Edit v1.2_2079971231356506114.json
hash: edef5ff250fce7bc
coverage: 0.826087
learned_at: 2026-10-20 00:40:21
nodes: [Krea2EditGroundedEncode, UNETLoader, Note, PreviewImage, GetImageSize, VAEEncode, EmptySD3LatentImage, VAEEncode, VAEDecode, PreviewImage, CLIPLoader, ImageScaleBy, VAELoader, KSampler, LoraLoaderModelOnly, image_scale_pixel_v2, image_scale_pixel_v2, SaveImage, LoadImage, Krea2EditModelPatch, LoadImage, Krea2EditGroundedEncode, JjkText]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 253584292255538, "steps": 10}
---

# 图片生成/文生图/双图编辑 ( Krea 2 Identity Edit v1.2_2079971231356506114.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/双图编辑 ( Krea 2 Identity Edit v1.2_2079971231356506114.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `Krea2EditGroundedEncode`
- `UNETLoader` ★核心
- `Note`
- `PreviewImage`
- `GetImageSize`
- `VAEEncode` ★核心
- `EmptySD3LatentImage`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `CLIPLoader`
- `ImageScaleBy`
- `VAELoader`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `image_scale_pixel_v2`
- `image_scale_pixel_v2`
- `SaveImage`
- `LoadImage`
- `Krea2EditModelPatch`
- `LoadImage`
- `Krea2EditGroundedEncode`
- `JjkText`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `253584292255538`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（19/23）

**有卡**：`Krea2EditGroundedEncode`、`UNETLoader`、`GetImageSize`、`VAEEncode`、`EmptySD3LatentImage`、`VAEDecode`、`CLIPLoader`、`ImageScaleBy`、`VAELoader`、`KSampler`、`LoraLoaderModelOnly`、`image_scale_pixel_v2`、`SaveImage`、`LoadImage`、`Krea2EditModelPatch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、VAEEncode
