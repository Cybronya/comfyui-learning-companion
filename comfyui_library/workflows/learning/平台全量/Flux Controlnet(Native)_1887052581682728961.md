---
key: 平台全量/Flux Controlnet(Native)_1887052581682728961.json
name: Flux Controlnet(Native)_1887052581682728961
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux Controlnet(Native)_1887052581682728961.json
hash: 2c77769209df8b28
coverage: 0.8
learned_at: 2026-11-14 00:27:34
nodes: [easy imageSize, ImageScaleToTotalPixels, ImageResizeKJ, FluxGuidance, ConditioningZeroOut, ControlNetApplySD3, EmptySD3LatentImage, VAEDecode, Note, Note, Note, ControlNetLoader, DepthAnythingV2Preprocessor, CheckpointLoaderSimple, PreviewImage, KSampler, SaveImage, LoadImage, LoraLoader, CLIPTextEncode]
patterns: [lora]
missing: []
parameters: {"cfg": 1, "checkpoint": "flux1-dev-fp8.safetensors", "controlnet_strength": 0.4, "denoise": 1, "lora_name": "【F.1】2D美式卡通游戏插画风格_v1.safetensors", "sampler_name": "euler", "scheduler": "normal", "seed": 252729370393007, "steps": 20, "strength_clip": 1, "strength_model": 1}
---

# 平台全量/Flux Controlnet(Native)_1887052581682728961.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux Controlnet(Native)_1887052581682728961.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `easy imageSize`
- `ImageScaleToTotalPixels`
- `ImageResizeKJ`
- `FluxGuidance`
- `ConditioningZeroOut`
- `ControlNetApplySD3` ★核心
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `Note`
- `Note`
- `Note`
- `ControlNetLoader`
- `DepthAnythingV2Preprocessor`
- `CheckpointLoaderSimple` ★核心
- `PreviewImage`
- `KSampler` ★核心
- `SaveImage`
- `LoadImage`
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：lora

## 关键参数

- `controlnet_strength` = `0.4`
- `checkpoint` = `flux1-dev-fp8.safetensors`
- `seed` = `252729370393007`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `lora_name` = `【F.1】2D美式卡通游戏插画风格_v1.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **80%**（16/20）

**有卡**：`easy imageSize`、`ImageScaleToTotalPixels`、`ImageResizeKJ`、`FluxGuidance`、`ConditioningZeroOut`、`ControlNetApplySD3`、`EmptySD3LatentImage`、`VAEDecode`、`ControlNetLoader`、`DepthAnythingV2Preprocessor`、`CheckpointLoaderSimple`、`KSampler`、`SaveImage`、`LoadImage`、`LoraLoader`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetApplySD3、ControlNetLoader
