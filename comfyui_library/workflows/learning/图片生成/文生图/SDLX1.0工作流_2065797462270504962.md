---
key: 图片生成/文生图/SDLX1.0工作流_2065797462270504962.json
name: SDLX1.0工作流_2065797462270504962
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/SDLX1.0工作流_2065797462270504962.json
hash: a93d4b680e26ae5a
coverage: 1
learned_at: 2026-10-19 23:21:44
nodes: [CLIPTextEncode, EmptyLatentImage, CheckpointLoaderSimple, VAEDecode, SaveImage, CLIPTextEncode, KSampler]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 2, "cfg": 8, "checkpoint": "LEOSAM HelloWorld 新世界 - V7.safetensors", "denoise": 1, "height": 1280, "sampler_name": "dpmpp_sde", "scheduler": "karras", "seed": 649, "steps": 25, "width": 768}
---

# 图片生成/文生图/SDLX1.0工作流_2065797462270504962.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/SDLX1.0工作流_2065797462270504962.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output

**节点**（7 个）：
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `768`
- `height` = `1280`
- `batch_size` = `2`
- `checkpoint` = `LEOSAM HelloWorld 新世界 - V7.safetensors`
- `seed` = `649`
- `steps` = `25`
- `cfg` = `8`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `karras`
- `denoise` = `1`

## 知识

覆盖率 **100%**（7/7）

**有卡**：`CLIPTextEncode`、`EmptyLatentImage`、`CheckpointLoaderSimple`、`VAEDecode`、`SaveImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、SaveImage、sd15-t2i-basic、sd15-t2i-lora
