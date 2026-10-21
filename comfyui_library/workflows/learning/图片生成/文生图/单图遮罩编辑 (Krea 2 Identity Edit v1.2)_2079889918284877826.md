---
key: 图片生成/文生图/单图遮罩编辑 (Krea 2 Identity Edit v1.2)_2079889918284877826.json
name: 单图遮罩编辑 (Krea 2 Identity Edit v1.2)_2079889918284877826
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/单图遮罩编辑 (Krea 2 Identity Edit v1.2)_2079889918284877826.json
hash: ff1592e895ba5b39
coverage: 0.869565
learned_at: 2026-10-20 00:40:21
nodes: [Krea2EditGroundedEncode, UNETLoader, Note, CLIPLoader, VAEEncode, ImageToMask, VAEDecode, MaskToImage, MaskPreview+, PreviewImage, GetImageSize, EmptySD3LatentImage, VAELoader, KSampler, Krea2EditModelPatch, GrowMask, ImageBlur, LoadImage, image_scale_pixel_v2, LoraLoaderModelOnly, SaveImage, Krea2EditGroundedEncode, JjkText]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1102605451988273, "steps": 10}
---

# 图片生成/文生图/单图遮罩编辑 (Krea 2 Identity Edit v1.2)_2079889918284877826.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/单图遮罩编辑 (Krea 2 Identity Edit v1.2)_2079889918284877826.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `Krea2EditGroundedEncode`
- `UNETLoader` ★核心
- `Note`
- `CLIPLoader`
- `VAEEncode` ★核心
- `ImageToMask`
- `VAEDecode` ★核心
- `MaskToImage`
- `MaskPreview+`
- `PreviewImage`
- `GetImageSize`
- `EmptySD3LatentImage`
- `VAELoader`
- `KSampler` ★核心
- `Krea2EditModelPatch`
- `GrowMask`
- `ImageBlur`
- `LoadImage`
- `image_scale_pixel_v2`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `Krea2EditGroundedEncode`
- `JjkText`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1102605451988273`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`Krea2EditGroundedEncode`、`UNETLoader`、`CLIPLoader`、`VAEEncode`、`ImageToMask`、`VAEDecode`、`MaskToImage`、`MaskPreview+`、`GetImageSize`、`EmptySD3LatentImage`、`VAELoader`、`KSampler`、`Krea2EditModelPatch`、`GrowMask`、`ImageBlur`、`LoadImage`、`image_scale_pixel_v2`、`LoraLoaderModelOnly`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、VAEEncode
