---
key: 图片生成/图生图/【遇见AI】SD3.5 blur_2042810005010780161.json
name: 【遇见AI】SD3.5 blur_2042810005010780161
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】SD3.5 blur_2042810005010780161.json
hash: bb99b0eb7eb1cba0
coverage: 0.833333
learned_at: 2026-10-23 11:52:12
nodes: [ConditioningZeroOut, KSampler, VAEDecode, SaveImage, ImpactSwitch, Note, EmptySD3LatentImage, ACN_AdvancedControlNetApply, Note, LoadImage, LoadImage, CheckpointLoaderSimple, CLIPLoader, DualCLIPLoader, TripleCLIPLoader, ControlNetLoader, LoadImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 4, "checkpoint": "sd3.5_large.safetensors", "controlnet_strength": 0.7, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 655608714607510, "steps": 30}
---

# 图片生成/图生图/【遇见AI】SD3.5 blur_2042810005010780161.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】SD3.5 blur_2042810005010780161.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ImpactSwitch`
- `Note`
- `EmptySD3LatentImage`
- `ACN_AdvancedControlNetApply` ★核心
- `Note`
- `LoadImage`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `CLIPLoader`
- `DualCLIPLoader`
- `TripleCLIPLoader`
- `ControlNetLoader`
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `655608714607510`
- `steps` = `30`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `0.7`
- `checkpoint` = `sd3.5_large.safetensors`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`ConditioningZeroOut`、`KSampler`、`VAEDecode`、`SaveImage`、`EmptySD3LatentImage`、`ACN_AdvancedControlNetApply`、`LoadImage`、`CheckpointLoaderSimple`、`CLIPLoader`、`DualCLIPLoader`、`TripleCLIPLoader`、`ControlNetLoader`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、ControlNetLoader
