---
key: 图片生成/图生图/SD1.5-Controlnet-OpenPose官方工作流_1930213476415782914.json
name: SD1.5-Controlnet-OpenPose官方工作流_1930213476415782914
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SD1.5-Controlnet-OpenPose官方工作流_1930213476415782914.json
hash: a4da54b5c52985fa
coverage: 0.909091
learned_at: 2026-10-23 11:23:34
nodes: [CLIPTextEncode, CLIPTextEncode, KSampler, ControlNetApplyAdvanced, EmptyLatentImage, LoadImage, VAEDecode, SaveImage, CheckpointLoaderSimple, ControlNetLoader, PreviewImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 6, "checkpoint": "dreamshaper_8LCM.safetensors", "controlnet_strength": 1, "denoise": 1, "height": 768, "sampler_name": "dpmpp_2m_sde_gpu", "scheduler": "karras", "seed": 8, "steps": 30, "width": 512}
---

# 图片生成/图生图/SD1.5-Controlnet-OpenPose官方工作流_1930213476415782914.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SD1.5-Controlnet-OpenPose官方工作流_1930213476415782914.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（11 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `ControlNetApplyAdvanced` ★核心
- `EmptyLatentImage` ★核心
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`
- `CheckpointLoaderSimple` ★核心
- `ControlNetLoader`
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `8`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `dpmpp_2m_sde_gpu`
- `scheduler` = `karras`
- `denoise` = `1`
- `controlnet_strength` = `1`
- `width` = `512`
- `height` = `768`
- `batch_size` = `1`
- `checkpoint` = `dreamshaper_8LCM.safetensors`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`CLIPTextEncode`、`KSampler`、`ControlNetApplyAdvanced`、`EmptyLatentImage`、`LoadImage`、`VAEDecode`、`SaveImage`、`CheckpointLoaderSimple`、`ControlNetLoader`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced、ControlNetLoader
