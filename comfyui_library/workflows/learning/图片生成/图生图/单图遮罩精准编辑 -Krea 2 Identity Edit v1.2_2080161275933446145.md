---
key: 图片生成/图生图/单图遮罩精准编辑 -Krea 2 Identity Edit v1.2_2080161275933446145.json
name: 单图遮罩精准编辑 -Krea 2 Identity Edit v1.2_2080161275933446145
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/单图遮罩精准编辑 -Krea 2 Identity Edit v1.2_2080161275933446145.json
hash: 817c33395a2b9026
coverage: 0.714286
learned_at: 2026-10-23 12:32:41
nodes: [image_scale_pixel_v2, GetImageSize, LoraLoaderModelOnly, CLIPLoader, UNETLoader, UNETLoader, VAELoader, VAEEncode, Krea2EditModelPatch, Krea2EditGroundedEncode, Krea2EditGroundedEncode, EmptySD3LatentImage, MaskPreview+, SaveImage, PreviewImage, PreviewImage, KSampler, VAEDecode, LG_Color_Match_V2, PreviewImage, ColorMatch, Note, CR Text, LoadImage, 孤海注释, 孤海注释, 孤海注释, MarkdownNote]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 976482271834226, "steps": 10}
---

# 图片生成/图生图/单图遮罩精准编辑 -Krea 2 Identity Edit v1.2_2080161275933446145.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/单图遮罩精准编辑 -Krea 2 Identity Edit v1.2_2080161275933446145.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `image_scale_pixel_v2`
- `GetImageSize`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `VAEEncode` ★核心
- `Krea2EditModelPatch`
- `Krea2EditGroundedEncode`
- `Krea2EditGroundedEncode`
- `EmptySD3LatentImage`
- `MaskPreview+`
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LG_Color_Match_V2`
- `PreviewImage`
- `ColorMatch`
- `Note`
- `CR Text`
- `LoadImage`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `MarkdownNote`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `976482271834226`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **71%**（20/28）

**有卡**：`image_scale_pixel_v2`、`GetImageSize`、`LoraLoaderModelOnly`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`VAEEncode`、`Krea2EditModelPatch`、`Krea2EditGroundedEncode`、`EmptySD3LatentImage`、`MaskPreview+`、`SaveImage`、`KSampler`、`VAEDecode`、`LG_Color_Match_V2`、`ColorMatch`、`CR Text`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、VAEEncode
