---
key: 平台全量/Style Transfer Canny Controlnet for Room Design!_1889135446880935938.json
name: Style Transfer Canny Controlnet for Room Design!_1889135446880935938
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Style Transfer Canny Controlnet for Room Design!_1889135446880935938.json
hash: 817a05d6f3c17d3f
coverage: 0.785714
learned_at: 2026-11-14 01:01:16
nodes: [VAEDecode, CLIPTextEncodeFlux, Note, Note, CLIPTextEncodeFlux, Image Comparer (rgthree), StyleModelApplyAdvanced, ControlNetApplySD3, UNETLoader, DualCLIPLoader, VAELoader, CLIPVisionLoader, StyleModelLoader, Note, SetUnionControlNetType, AIO_Preprocessor, KSampler, easy cleanGpuUsed, LoadImage, LoadImage, SaveImage, ImageScale, EmptyLatentImage, CLIPVisionEncode, DF_Get_image_size, PreviewImage, Note, ControlNetLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 0.8, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "normal", "seed": 1113855010285458, "steps": 25, "width": 1024}
---

# 平台全量/Style Transfer Canny Controlnet for Room Design!_1889135446880935938.json

> 来源文件 `comfyui_library/workflows/平台全量/Style Transfer Canny Controlnet for Room Design!_1889135446880935938.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `VAEDecode` ★核心
- `CLIPTextEncodeFlux` ★核心
- `Note`
- `Note`
- `CLIPTextEncodeFlux` ★核心
- `Image Comparer (rgthree)`
- `StyleModelApplyAdvanced`
- `ControlNetApplySD3` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `StyleModelLoader`
- `Note`
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `ImageScale`
- `EmptyLatentImage` ★核心
- `CLIPVisionEncode`
- `DF_Get_image_size`
- `PreviewImage`
- `Note`
- `ControlNetLoader`

## 关键参数

- `controlnet_strength` = `0.8`
- `seed` = `1113855010285458`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（22/28）

**有卡**：`VAEDecode`、`CLIPTextEncodeFlux`、`StyleModelApplyAdvanced`、`ControlNetApplySD3`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`StyleModelLoader`、`SetUnionControlNetType`、`AIO_Preprocessor`、`KSampler`、`easy cleanGpuUsed`、`LoadImage`、`SaveImage`、`ImageScale`、`EmptyLatentImage`、`CLIPVisionEncode`、`DF_Get_image_size`、`ControlNetLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、EmptyLatentImage、LoadImage、ControlNetApplySD3、ControlNetLoader
