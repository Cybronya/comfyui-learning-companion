---
key: 图片生成/图生图/New Depth ControlNet Models for SD 3.5 Large_1862922937178238977.json
name: New Depth ControlNet Models for SD 3.5 Large_1862922937178238977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/New Depth ControlNet Models for SD 3.5 Large_1862922937178238977.json
hash: a8d0bcc19ead1be0
coverage: 0.8
learned_at: 2026-10-23 11:09:50
nodes: [KSampler, ControlNetApplySD3, EmptySD3LatentImage, ControlNetLoader, PreviewImage, DepthAnythingPreprocessor, ImageScale, VAEDecode, SaveImage, CheckpointLoaderSimple, Anything Everywhere, Anything Everywhere, ConditioningZeroOut, LoadImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 5, "checkpoint": "sd3.5_large_fp8_scaled.safetensors", "controlnet_strength": 0.7000000000000001, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 542712525684954, "steps": 30}
---

# 图片生成/图生图/New Depth ControlNet Models for SD 3.5 Large_1862922937178238977.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/New Depth ControlNet Models for SD 3.5 Large_1862922937178238977.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `KSampler` ★核心
- `ControlNetApplySD3` ★核心
- `EmptySD3LatentImage`
- `ControlNetLoader`
- `PreviewImage`
- `DepthAnythingPreprocessor`
- `ImageScale`
- `VAEDecode` ★核心
- `SaveImage`
- `CheckpointLoaderSimple` ★核心
- `Anything Everywhere`
- `Anything Everywhere`
- `ConditioningZeroOut`
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `542712525684954`
- `steps` = `30`
- `cfg` = `5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `0.7000000000000001`
- `checkpoint` = `sd3.5_large_fp8_scaled.safetensors`

## 知识

覆盖率 **80%**（12/15）

**有卡**：`KSampler`、`ControlNetApplySD3`、`EmptySD3LatentImage`、`ControlNetLoader`、`DepthAnythingPreprocessor`、`ImageScale`、`VAEDecode`、`SaveImage`、`CheckpointLoaderSimple`、`ConditioningZeroOut`、`LoadImage`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetLoader、DepthAnythingPreprocessor
