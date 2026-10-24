---
key: 图片生成/图生图/SD1.5-OpenPose（V2.0）官方工作流_1930214688452198401.json
name: SD1.5-OpenPose（V2.0）官方工作流_1930214688452198401
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SD1.5-OpenPose（V2.0）官方工作流_1930214688452198401.json
hash: 6075800de7d5f79d
coverage: 0.846154
learned_at: 2026-10-23 11:23:35
nodes: [EmptyLatentImage, CLIPTextEncode, CLIPTextEncode, KSampler, ControlNetApplyAdvanced, PreviewImage, CheckpointLoaderSimple, LoadImage, PreviewImage, OpenposePreprocessor, ControlNetLoader, VAEDecode, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 6, "checkpoint": "SD1.5 dreamshaper_8.safetensors", "controlnet_strength": 1, "denoise": 1, "height": 768, "sampler_name": "dpmpp_2m_sde_gpu", "scheduler": "karras", "seed": 8, "steps": 30, "width": 512}
---

# 图片生成/图生图/SD1.5-OpenPose（V2.0）官方工作流_1930214688452198401.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SD1.5-OpenPose（V2.0）官方工作流_1930214688452198401.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（13 个）：
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `ControlNetApplyAdvanced` ★核心
- `PreviewImage`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `PreviewImage`
- `OpenposePreprocessor`
- `ControlNetLoader`
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `512`
- `height` = `768`
- `batch_size` = `1`
- `seed` = `8`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `dpmpp_2m_sde_gpu`
- `scheduler` = `karras`
- `denoise` = `1`
- `controlnet_strength` = `1`
- `checkpoint` = `SD1.5 dreamshaper_8.safetensors`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`EmptyLatentImage`、`CLIPTextEncode`、`KSampler`、`ControlNetApplyAdvanced`、`CheckpointLoaderSimple`、`LoadImage`、`OpenposePreprocessor`、`ControlNetLoader`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced、ControlNetLoader
