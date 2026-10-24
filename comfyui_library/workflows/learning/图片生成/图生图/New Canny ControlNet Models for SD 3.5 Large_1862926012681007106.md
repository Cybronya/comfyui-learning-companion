---
key: 图片生成/图生图/New Canny ControlNet Models for SD 3.5 Large_1862926012681007106.json
name: New Canny ControlNet Models for SD 3.5 Large_1862926012681007106
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/New Canny ControlNet Models for SD 3.5 Large_1862926012681007106.json
hash: d68f4d6a8c06b9d7
coverage: 0.8
learned_at: 2026-10-23 11:09:50
nodes: [SaveImage, VAEDecode, KSampler, ControlNetApplySD3, EmptySD3LatentImage, ConditioningZeroOut, ControlNetLoader, Canny, ImageScale, PreviewImage, Anything Everywhere, Anything Everywhere, CheckpointLoaderSimple, LoadImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 4, "checkpoint": "sd3.5_large_fp8_scaled.safetensors", "controlnet_strength": 0.7000000000000001, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 101944136311431, "steps": 30}
---

# 图片生成/图生图/New Canny ControlNet Models for SD 3.5 Large_1862926012681007106.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/New Canny ControlNet Models for SD 3.5 Large_1862926012681007106.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ControlNetApplySD3` ★核心
- `EmptySD3LatentImage`
- `ConditioningZeroOut`
- `ControlNetLoader`
- `Canny`
- `ImageScale`
- `PreviewImage`
- `Anything Everywhere`
- `Anything Everywhere`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `101944136311431`
- `steps` = `30`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `0.7000000000000001`
- `checkpoint` = `sd3.5_large_fp8_scaled.safetensors`

## 知识

覆盖率 **80%**（12/15）

**有卡**：`SaveImage`、`VAEDecode`、`KSampler`、`ControlNetApplySD3`、`EmptySD3LatentImage`、`ConditioningZeroOut`、`ControlNetLoader`、`Canny`、`ImageScale`、`CheckpointLoaderSimple`、`LoadImage`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetLoader、Canny
