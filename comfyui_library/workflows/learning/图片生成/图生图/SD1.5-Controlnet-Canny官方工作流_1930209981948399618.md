---
key: 图片生成/图生图/SD1.5-Controlnet-Canny官方工作流_1930209981948399618.json
name: SD1.5-Controlnet-Canny官方工作流_1930209981948399618
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SD1.5-Controlnet-Canny官方工作流_1930209981948399618.json
hash: c0632f3e7e711cdc
coverage: 0.857143
learned_at: 2026-10-23 11:23:33
nodes: [KSampler, CLIPTextEncode, ControlNetApplyAdvanced, CLIPTextEncode, Canny, LoadImage, EmptyLatentImage, CheckpointLoaderSimple, ControlNetLoader, PreviewImage, VAEDecode, SaveImage, PreviewImage, VAELoader]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 7, "checkpoint": "SD1.5 dreamshaper_8.safetensors", "controlnet_strength": 1.0000000000000002, "denoise": 1, "height": 512, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 567909987322585, "steps": 25, "width": 512}
---

# 图片生成/图生图/SD1.5-Controlnet-Canny官方工作流_1930209981948399618.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SD1.5-Controlnet-Canny官方工作流_1930209981948399618.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（14 个）：
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `ControlNetApplyAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `Canny`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `CheckpointLoaderSimple` ★核心
- `ControlNetLoader`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `VAELoader`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `567909987322585`
- `steps` = `25`
- `cfg` = `7`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `1`
- `controlnet_strength` = `1.0000000000000002`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `checkpoint` = `SD1.5 dreamshaper_8.safetensors`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`KSampler`、`CLIPTextEncode`、`ControlNetApplyAdvanced`、`Canny`、`LoadImage`、`EmptyLatentImage`、`CheckpointLoaderSimple`、`ControlNetLoader`、`VAEDecode`、`SaveImage`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced
