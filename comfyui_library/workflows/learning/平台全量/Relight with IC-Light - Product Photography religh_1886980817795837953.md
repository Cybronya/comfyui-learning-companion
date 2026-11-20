---
key: 平台全量/Relight with IC-Light - Product Photography religh_1886980817795837953.json
name: Relight with IC-Light - Product Photography religh_1886980817795837953
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Relight with IC-Light - Product Photography religh_1886980817795837953.json
hash: 88f8dd037c2f7fb7
coverage: 0.617647
learned_at: 2026-11-14 00:54:53
nodes: [KSampler, VAEEncode, ICLightConditioning, VAEEncode, GrowMaskWithBlur, Note, RemapMaskRange, MaskToImage, CLIPTextEncode, Note, Reroute, Note, Note, Note, LoadImageMask, Note, CLIPTextEncode, Note, EmptyLatentImage, Note, PreviewImage, CLIPTextEncode, CheckpointLoaderSimple, CLIPTextEncode, LoadImage, Note, PreviewImage, VAEDecode, LoadAndApplyICLightUnet, Note, CheckpointLoaderSimple, VAEDecode, SaveImage, KSampler]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 3, "checkpoint": "majicmixRealistic_v7.safetensors", "denoise": 1, "height": 512, "sampler_name": "dpmpp_2m_sde", "scheduler": "karras", "seed": 100361857014348, "steps": 20, "width": 512}
---

# 平台全量/Relight with IC-Light - Product Photography religh_1886980817795837953.json

> 来源文件 `comfyui_library/workflows/平台全量/Relight with IC-Light - Product Photography religh_1886980817795837953.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（34 个）：
- `KSampler` ★核心
- `VAEEncode` ★核心
- `ICLightConditioning`
- `VAEEncode` ★核心
- `GrowMaskWithBlur`
- `Note`
- `RemapMaskRange`
- `MaskToImage`
- `CLIPTextEncode` ★核心
- `Note`
- `Reroute`
- `Note`
- `Note`
- `Note`
- `LoadImageMask`
- `Note`
- `CLIPTextEncode` ★核心
- `Note`
- `EmptyLatentImage` ★核心
- `Note`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `Note`
- `PreviewImage`
- `VAEDecode` ★核心
- `LoadAndApplyICLightUnet`
- `Note`
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `100361857014348`
- `steps` = `20`
- `cfg` = `3`
- `sampler_name` = `dpmpp_2m_sde`
- `scheduler` = `karras`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `checkpoint` = `majicmixRealistic_v7.safetensors`

## 知识

覆盖率 **62%**（21/34）

**有卡**：`KSampler`、`VAEEncode`、`ICLightConditioning`、`GrowMaskWithBlur`、`RemapMaskRange`、`MaskToImage`、`CLIPTextEncode`、`LoadImageMask`、`EmptyLatentImage`、`CheckpointLoaderSimple`、`LoadImage`、`VAEDecode`、`LoadAndApplyICLightUnet`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、VAEEncode、ICLightConditioning
