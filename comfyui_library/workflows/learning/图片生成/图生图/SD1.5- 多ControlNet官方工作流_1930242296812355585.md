---
key: 图片生成/图生图/SD1.5- 多ControlNet官方工作流_1930242296812355585.json
name: SD1.5- 多ControlNet官方工作流_1930242296812355585
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SD1.5- 多ControlNet官方工作流_1930242296812355585.json
hash: f4bf7a934d0e59ac
coverage: 0.823529
learned_at: 2026-10-23 11:23:32
nodes: [OpenposePreprocessor, ControlNetApplyAdvanced, PreviewImage, LineartStandardPreprocessor, ControlNetApplyAdvanced, PreviewImage, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, KSampler, VAEDecode, PreviewImage, SaveImage, CheckpointLoaderSimple, ControlNetLoader, ControlNetLoader, LoadImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 6, "checkpoint": "dreamshaper_8LCM.safetensors", "controlnet_strength": 1, "denoise": 1, "height": 768, "sampler_name": "euler", "scheduler": "karras", "seed": 34545047703050, "steps": 30, "width": 672}
---

# 图片生成/图生图/SD1.5- 多ControlNet官方工作流_1930242296812355585.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SD1.5- 多ControlNet官方工作流_1930242296812355585.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（17 个）：
- `OpenposePreprocessor`
- `ControlNetApplyAdvanced` ★核心
- `PreviewImage`
- `LineartStandardPreprocessor`
- `ControlNetApplyAdvanced` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `CheckpointLoaderSimple` ★核心
- `ControlNetLoader`
- `ControlNetLoader`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `controlnet_strength` = `1`
- `width` = `672`
- `height` = `768`
- `batch_size` = `1`
- `seed` = `34545047703050`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `euler`
- `scheduler` = `karras`
- `denoise` = `1`
- `checkpoint` = `dreamshaper_8LCM.safetensors`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`OpenposePreprocessor`、`ControlNetApplyAdvanced`、`LineartStandardPreprocessor`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImage`、`CheckpointLoaderSimple`、`ControlNetLoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced、ControlNetLoader
