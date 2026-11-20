---
key: 平台全量/dress up games V2.0_1863853295336095746.json
name: dress up games V2.0_1863853295336095746
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/dress up games V2.0_1863853295336095746.json
hash: 2c00ff0cfd3d175d
coverage: 0.941176
learned_at: 2026-11-14 01:10:17
nodes: [RescaleCFG, LoadImage, EmptyLatentImage, Get Image Size, PreviewImage, ControlNetApplyAdvanced, ControlNetApplyAdvanced, VAEDecode, KSampler, CheckpointLoaderSimple, AIO_Preprocessor, ControlNetLoader, ControlNetLoader, CLIPTextEncode, DF_Image_scale_to_side, CLIPTextEncode, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 3, "checkpoint": "realisticVisionV60B1_v51VAE.safetensors", "controlnet_strength": 0.7000000000000001, "denoise": 1, "height": 768, "sampler_name": "dpmpp_sde", "scheduler": "karras", "seed": 1034439690960973, "steps": 15, "width": 512}
---

# 平台全量/dress up games V2.0_1863853295336095746.json

> 来源文件 `comfyui_library/workflows/平台全量/dress up games V2.0_1863853295336095746.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `RescaleCFG`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `Get Image Size`
- `PreviewImage`
- `ControlNetApplyAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `AIO_Preprocessor`
- `ControlNetLoader`
- `ControlNetLoader`
- `CLIPTextEncode` ★核心
- `DF_Image_scale_to_side`
- `CLIPTextEncode` ★核心
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `512`
- `height` = `768`
- `batch_size` = `1`
- `controlnet_strength` = `0.7000000000000001`
- `seed` = `1034439690960973`
- `steps` = `15`
- `cfg` = `3`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `karras`
- `denoise` = `1`
- `checkpoint` = `realisticVisionV60B1_v51VAE.safetensors`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`RescaleCFG`、`LoadImage`、`EmptyLatentImage`、`Get Image Size`、`ControlNetApplyAdvanced`、`VAEDecode`、`KSampler`、`CheckpointLoaderSimple`、`AIO_Preprocessor`、`ControlNetLoader`、`CLIPTextEncode`、`DF_Image_scale_to_side`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced、ControlNetLoader
