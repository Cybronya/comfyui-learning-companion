---
key: 图片生成/文生图/文生图+LoRA 1.0_2004786865167368194.json
name: 文生图+LoRA 1.0_2004786865167368194
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图+LoRA 1.0_2004786865167368194.json
hash: 9821459e1eb1bc8a
coverage: 1
learned_at: 2026-10-19 22:01:34
nodes: [VAEDecode, CheckpointLoaderSimple, CLIPTextEncode, EmptyLatentImage, LoraLoader, CLIPTextEncode, SaveImage, KSampler]
patterns: [text_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "checkpoint": "oneObsession_17RED.safetensors", "denoise": 1, "height": 752, "lora_name": "ma1ma1helmes_b-000014.safetensors", "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 20471339882095, "steps": 30, "strength_clip": 1, "strength_model": 0.7000000000000002, "width": 560}
---

# 图片生成/文生图/文生图+LoRA 1.0_2004786865167368194.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图+LoRA 1.0_2004786865167368194.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output

**节点**（8 个）：
- `VAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `KSampler` ★核心

**识别到的模式**：text_to_image、lora

## 关键参数

- `checkpoint` = `oneObsession_17RED.safetensors`
- `width` = `560`
- `height` = `752`
- `batch_size` = `1`
- `lora_name` = `ma1ma1helmes_b-000014.safetensors`
- `strength_model` = `0.7000000000000002`
- `strength_clip` = `1`
- `seed` = `20471339882095`
- `steps` = `30`
- `cfg` = `8`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `1`

## 知识

覆盖率 **100%**（8/8）

**有卡**：`VAEDecode`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`EmptyLatentImage`、`LoraLoader`、`SaveImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoraLoader、LoraLoader、SaveImage
