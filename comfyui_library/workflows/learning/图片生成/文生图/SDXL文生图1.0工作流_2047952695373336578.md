---
key: 图片生成/文生图/SDXL文生图1.0工作流_2047952695373336578.json
name: SDXL文生图1.0工作流_2047952695373336578
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/SDXL文生图1.0工作流_2047952695373336578.json
hash: 94f829e144b3469c
coverage: 1
learned_at: 2026-10-21 02:55:00
nodes: [VAEDecode, EmptyLatentImage, CLIPTextEncode, KSampler, CheckpointLoaderSimple, SaveImage, CLIPTextEncode]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 2, "cfg": 6, "checkpoint": "LEOSAM HelloWorld 新世界 - V7.safetensors", "denoise": 1, "height": 1280, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 196080507678911, "steps": 20, "width": 768}
---

# 图片生成/文生图/SDXL文生图1.0工作流_2047952695373336578.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/SDXL文生图1.0工作流_2047952695373336578.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output

**节点**（7 个）：
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `768`
- `height` = `1280`
- `batch_size` = `2`
- `seed` = `196080507678911`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `1`
- `checkpoint` = `LEOSAM HelloWorld 新世界 - V7.safetensors`

## 知识

覆盖率 **100%**（7/7）

**有卡**：`VAEDecode`、`EmptyLatentImage`、`CLIPTextEncode`、`KSampler`、`CheckpointLoaderSimple`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、SaveImage、sd15-t2i-basic、sd15-t2i-lora
