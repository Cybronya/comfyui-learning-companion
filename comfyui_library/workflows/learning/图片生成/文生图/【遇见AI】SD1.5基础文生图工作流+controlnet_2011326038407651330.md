---
key: 图片生成/文生图/【遇见AI】SD1.5基础文生图工作流+controlnet_2011326038407651330.json
name: 【遇见AI】SD1.5基础文生图工作流+controlnet_2011326038407651330
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【遇见AI】SD1.5基础文生图工作流+controlnet_2011326038407651330.json
hash: 7b043d37fa689e77
coverage: 0.916667
learned_at: 2026-10-19 22:01:21
nodes: [KSampler, VAEDecode, SaveImage, PreviewImage, AIO_Preprocessor, ControlNetLoader, CLIPTextEncode, ControlNetApplySD3, CheckpointLoaderSimple, CLIPTextEncode, LoadImage, EmptyLatentImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "checkpoint": "1.5D-majicMIX realistic 麦橘写实_v7.safetensors", "controlnet_strength": 1, "denoise": 1, "height": 768, "sampler_name": "euler", "scheduler": "normal", "seed": 772938719778265, "steps": 20, "width": 512}
---

# 图片生成/文生图/【遇见AI】SD1.5基础文生图工作流+controlnet_2011326038407651330.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【遇见AI】SD1.5基础文生图工作流+controlnet_2011326038407651330.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（12 个）：
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `AIO_Preprocessor`
- `ControlNetLoader`
- `CLIPTextEncode` ★核心
- `ControlNetApplySD3` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `EmptyLatentImage` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `772938719778265`
- `steps` = `20`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `controlnet_strength` = `1`
- `checkpoint` = `1.5D-majicMIX realistic 麦橘写实_v7.safetensors`
- `width` = `512`
- `height` = `768`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`KSampler`、`VAEDecode`、`SaveImage`、`AIO_Preprocessor`、`ControlNetLoader`、`CLIPTextEncode`、`ControlNetApplySD3`、`CheckpointLoaderSimple`、`LoadImage`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetLoader、ControlNetApplySD3
