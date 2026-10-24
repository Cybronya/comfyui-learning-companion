---
key: 图片生成/图生图/【遇见AI】SDXL基础文生图+SDXL版Union多合一ControlNet_2012828647471718402.json
name: 【遇见AI】SDXL基础文生图+SDXL版Union多合一ControlNet_2012828647471718402
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】SDXL基础文生图+SDXL版Union多合一ControlNet_2012828647471718402.json
hash: 4c4a44f4a8a6062c
coverage: 0.846154
learned_at: 2026-10-23 11:52:12
nodes: [KSampler, VAEDecode, CLIPTextEncode, SaveImage, EmptyLatentImage, ControlNetApplySD3, PreviewImage, Note, AIO_Preprocessor, ControlNetLoader, LoadImage, CLIPTextEncode, CheckpointLoaderSimple]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "checkpoint": "RealVisXL_V5.0_fp16.safetensors", "controlnet_strength": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "normal", "seed": 1091284840176798, "steps": 20, "width": 512}
---

# 图片生成/图生图/【遇见AI】SDXL基础文生图+SDXL版Union多合一ControlNet_2012828647471718402.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】SDXL基础文生图+SDXL版Union多合一ControlNet_2012828647471718402.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（13 个）：
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `EmptyLatentImage` ★核心
- `ControlNetApplySD3` ★核心
- `PreviewImage`
- `Note`
- `AIO_Preprocessor`
- `ControlNetLoader`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `1091284840176798`
- `steps` = `20`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `width` = `512`
- `height` = `1024`
- `batch_size` = `1`
- `controlnet_strength` = `1`
- `checkpoint` = `RealVisXL_V5.0_fp16.safetensors`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`KSampler`、`VAEDecode`、`CLIPTextEncode`、`SaveImage`、`EmptyLatentImage`、`ControlNetApplySD3`、`AIO_Preprocessor`、`ControlNetLoader`、`LoadImage`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetLoader、ControlNetApplySD3
