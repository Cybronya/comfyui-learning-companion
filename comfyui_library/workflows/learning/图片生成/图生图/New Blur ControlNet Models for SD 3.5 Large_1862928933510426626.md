---
key: 图片生成/图生图/New Blur ControlNet Models for SD 3.5 Large_1862928933510426626.json
name: New Blur ControlNet Models for SD 3.5 Large_1862928933510426626
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/New Blur ControlNet Models for SD 3.5 Large_1862928933510426626.json
hash: bd8ec85106ade227
coverage: 0.833333
learned_at: 2026-10-23 11:09:50
nodes: [CLIPTextEncode, ControlNetApplySD3, KSampler, VAEDecode, EmptySD3LatentImage, ConditioningZeroOut, ControlNetLoader, LoadImage, Anything Everywhere, Anything Everywhere, CheckpointLoaderSimple, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 4, "checkpoint": "sd3.5_large_fp8_scaled.safetensors", "controlnet_strength": 0.7000000000000001, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 10141814692023, "steps": 30}
---

# 图片生成/图生图/New Blur ControlNet Models for SD 3.5 Large_1862928933510426626.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/New Blur ControlNet Models for SD 3.5 Large_1862928933510426626.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `CLIPTextEncode` ★核心
- `ControlNetApplySD3` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `EmptySD3LatentImage`
- `ConditioningZeroOut`
- `ControlNetLoader`
- `LoadImage`
- `Anything Everywhere`
- `Anything Everywhere`
- `CheckpointLoaderSimple` ★核心
- `SaveImage`

## 关键参数

- `controlnet_strength` = `0.7000000000000001`
- `seed` = `10141814692023`
- `steps` = `30`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `sd3.5_large_fp8_scaled.safetensors`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`CLIPTextEncode`、`ControlNetApplySD3`、`KSampler`、`VAEDecode`、`EmptySD3LatentImage`、`ConditioningZeroOut`、`ControlNetLoader`、`LoadImage`、`CheckpointLoaderSimple`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetLoader、ControlNetApplySD3
