---
key: 图片生成/图生图/SD1.5-Controlnet-Depth官方工作流_1930211789093421057.json
name: SD1.5-Controlnet-Depth官方工作流_1930211789093421057
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SD1.5-Controlnet-Depth官方工作流_1930211789093421057.json
hash: 87cba2827984374e
coverage: 0.846154
learned_at: 2026-10-23 11:23:34
nodes: [CLIPTextEncode, CLIPTextEncode, Zoe-DepthMapPreprocessor, PreviewImage, ControlNetApplyAdvanced, EmptyLatentImage, KSampler, VAEDecode, LoadImage, CheckpointLoaderSimple, ControlNetLoader, SaveImage, PreviewImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 6, "checkpoint": "SD1.5 dreamshaper_8.safetensors", "controlnet_strength": 1.0000000000000002, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "karras", "seed": 199357352380794, "steps": 30, "width": 768}
---

# 图片生成/图生图/SD1.5-Controlnet-Depth官方工作流_1930211789093421057.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SD1.5-Controlnet-Depth官方工作流_1930211789093421057.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（13 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Zoe-DepthMapPreprocessor`
- `PreviewImage`
- `ControlNetApplyAdvanced` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `ControlNetLoader`
- `SaveImage`
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `controlnet_strength` = `1.0000000000000002`
- `width` = `768`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `199357352380794`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `euler`
- `scheduler` = `karras`
- `denoise` = `1`
- `checkpoint` = `SD1.5 dreamshaper_8.safetensors`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`CLIPTextEncode`、`Zoe-DepthMapPreprocessor`、`ControlNetApplyAdvanced`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`LoadImage`、`CheckpointLoaderSimple`、`ControlNetLoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced、ControlNetLoader
