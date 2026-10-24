---
key: 图片生成/图生图/双图编辑-Krea 2 Identity Edit v1.2_2080298483608801281.json
name: 双图编辑-Krea 2 Identity Edit v1.2_2080298483608801281
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/双图编辑-Krea 2 Identity Edit v1.2_2080298483608801281.json
hash: 4d492cafb1dc0bb1
coverage: 0.766667
learned_at: 2026-10-23 12:35:04
nodes: [LoraLoaderModelOnly, CLIPLoader, UNETLoader, KSampler, VAEDecode, 孤海注释, 孤海注释, MarkdownNote, VAELoader, VAEEncode, Krea2EditGroundedEncode, Krea2EditModelPatch, PreviewImage, VAEEncode, Krea2EditGroundedEncode, UNETLoader, EmptySD3LatentImage, Note, MaskPreview+, 孤海注释, image_scale_pixel_v2, ResolutionSelector, LoadImage, ImageConcatMulti, SaveImage, PreviewImage, LoadImage, CR Text, SaveImage, ColorMatch]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1056398625963451, "steps": 10}
---

# 图片生成/图生图/双图编辑-Krea 2 Identity Edit v1.2_2080298483608801281.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/双图编辑-Krea 2 Identity Edit v1.2_2080298483608801281.json`

## 结构

**生成流程**：Model → Encode → Latent → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `孤海注释`
- `孤海注释`
- `MarkdownNote`
- `VAELoader`
- `VAEEncode` ★核心
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `PreviewImage`
- `VAEEncode` ★核心
- `Krea2EditGroundedEncode`
- `UNETLoader` ★核心
- `EmptySD3LatentImage`
- `Note`
- `MaskPreview+`
- `孤海注释`
- `image_scale_pixel_v2`
- `ResolutionSelector`
- `LoadImage`
- `ImageConcatMulti`
- `SaveImage`
- `PreviewImage`
- `LoadImage`
- `CR Text`
- `SaveImage`
- `ColorMatch`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1056398625963451`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（23/30）

**有卡**：`LoraLoaderModelOnly`、`CLIPLoader`、`UNETLoader`、`KSampler`、`VAEDecode`、`VAELoader`、`VAEEncode`、`Krea2EditGroundedEncode`、`Krea2EditModelPatch`、`EmptySD3LatentImage`、`MaskPreview+`、`image_scale_pixel_v2`、`ResolutionSelector`、`LoadImage`、`ImageConcatMulti`、`SaveImage`、`CR Text`、`ColorMatch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader
