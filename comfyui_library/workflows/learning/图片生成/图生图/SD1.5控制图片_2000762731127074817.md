---
key: 图片生成/图生图/SD1.5控制图片_2000762731127074817.json
name: SD1.5控制图片_2000762731127074817
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SD1.5控制图片_2000762731127074817.json
hash: bc9837732de2475e
coverage: 1
learned_at: 2026-10-23 11:23:42
nodes: [VAEDecode, KSampler, VAEEncode, EmptyLatentImage, ControlNetApplyAdvanced, SaveImage, CLIPTextEncode, CLIPTextEncode, LoraLoader, CheckpointLoaderSimple, LoadImage, AIO_Preprocessor, ControlNetLoader]
patterns: [text_to_image, image_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "checkpoint": "majicmixRealistic_v7.safetensors", "controlnet_strength": 1, "denoise": 1, "height": 512, "lora_name": "GameIconResearch_PLANT2_Lora.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 834208693678396, "steps": 20, "strength_clip": 1, "strength_model": 1, "width": 512}
---

# 图片生成/图生图/SD1.5控制图片_2000762731127074817.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SD1.5控制图片_2000762731127074817.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（13 个）：
- `VAEDecode` ★核心
- `KSampler` ★核心
- `VAEEncode` ★核心
- `EmptyLatentImage` ★核心
- `ControlNetApplyAdvanced` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `AIO_Preprocessor`
- `ControlNetLoader`

**识别到的模式**：text_to_image、image_to_image、lora

## 关键参数

- `seed` = `834208693678396`
- `steps` = `20`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `controlnet_strength` = `1`
- `lora_name` = `GameIconResearch_PLANT2_Lora.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `checkpoint` = `majicmixRealistic_v7.safetensors`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`VAEDecode`、`KSampler`、`VAEEncode`、`EmptyLatentImage`、`ControlNetApplyAdvanced`、`SaveImage`、`CLIPTextEncode`、`LoraLoader`、`CheckpointLoaderSimple`、`LoadImage`、`AIO_Preprocessor`、`ControlNetLoader`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced、ControlNetLoader
