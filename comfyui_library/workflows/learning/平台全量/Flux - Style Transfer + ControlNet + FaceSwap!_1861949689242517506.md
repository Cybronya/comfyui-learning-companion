---
key: 平台全量/Flux - Style Transfer + ControlNet + FaceSwap!_1861949689242517506.json
name: Flux - Style Transfer + ControlNet + FaceSwap!_1861949689242517506
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux - Style Transfer + ControlNet + FaceSwap!_1861949689242517506.json
hash: d029b01a8b18a81a
coverage: 0.78125
learned_at: 2026-11-14 00:27:29
nodes: [StyleModelLoader, CLIPTextEncodeFlux, CLIPTextEncodeFlux, LoadImage, ImageScale, UNETLoader, VAELoader, DualCLIPLoader, CLIPVisionLoader, LoadImage, CLIPVisionEncode, Note, SetUnionControlNetType, ControlNetLoader, EmptyLatentImage, LoadImage, ImageScale, Note, AIO_Preprocessor, PreviewImage, VAEDecode, StyleModelApplyAdvanced, Note, SaveImage, DF_Get_image_size, KSampler, Note, SaveImage, ControlNetApplySD3, Image Comparer (rgthree), ReActorFaceSwap, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 0.6, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "normal", "seed": 145565168573641, "steps": 30, "width": 1024}
---

# 平台全量/Flux - Style Transfer + ControlNet + FaceSwap!_1861949689242517506.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux - Style Transfer + ControlNet + FaceSwap!_1861949689242517506.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `StyleModelLoader`
- `CLIPTextEncodeFlux` ★核心
- `CLIPTextEncodeFlux` ★核心
- `LoadImage`
- `ImageScale`
- `UNETLoader` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `CLIPVisionLoader`
- `LoadImage`
- `CLIPVisionEncode`
- `Note`
- `SetUnionControlNetType`
- `ControlNetLoader`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `ImageScale`
- `Note`
- `AIO_Preprocessor`
- `PreviewImage`
- `VAEDecode` ★核心
- `StyleModelApplyAdvanced`
- `Note`
- `SaveImage`
- `DF_Get_image_size`
- `KSampler` ★核心
- `Note`
- `SaveImage`
- `ControlNetApplySD3` ★核心
- `Image Comparer (rgthree)`
- `ReActorFaceSwap`
- `PreviewImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `145565168573641`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `controlnet_strength` = `0.6`

## 知识

覆盖率 **78%**（25/32）

**有卡**：`StyleModelLoader`、`CLIPTextEncodeFlux`、`LoadImage`、`ImageScale`、`UNETLoader`、`VAELoader`、`DualCLIPLoader`、`CLIPVisionLoader`、`CLIPVisionEncode`、`SetUnionControlNetType`、`ControlNetLoader`、`EmptyLatentImage`、`AIO_Preprocessor`、`VAEDecode`、`StyleModelApplyAdvanced`、`SaveImage`、`DF_Get_image_size`、`KSampler`、`ControlNetApplySD3`、`ReActorFaceSwap`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、EmptyLatentImage、LoadImage、ControlNetApplySD3、ControlNetLoader
