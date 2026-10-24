---
key: 图片生成/图生图/【遇见AI】SD3.5 canny和depth_2042802452788944897.json
name: 【遇见AI】SD3.5 canny和depth_2042802452788944897
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】SD3.5 canny和depth_2042802452788944897.json
hash: 30d1d008034dd498
coverage: 0.761905
learned_at: 2026-10-23 11:52:12
nodes: [ConditioningZeroOut, KSampler, VAEDecode, SaveImage, Note, CLIPTextEncode, Note, ImpactSwitch, EmptySD3LatentImage, ACN_AdvancedControlNetApply, Canny, PreviewImage, Note, LoadImage, LoadImage, CLIPLoader, DualCLIPLoader, TripleCLIPLoader, CheckpointLoaderSimple, LoadImage, ControlNetLoader]
patterns: []
missing: []
parameters: {"cfg": 4, "checkpoint": "sd3.5_large.safetensors", "controlnet_strength": 0.7000000000000001, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 67773456290684, "steps": 30}
---

# 图片生成/图生图/【遇见AI】SD3.5 canny和depth_2042802452788944897.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】SD3.5 canny和depth_2042802452788944897.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Note`
- `CLIPTextEncode` ★核心
- `Note`
- `ImpactSwitch`
- `EmptySD3LatentImage`
- `ACN_AdvancedControlNetApply` ★核心
- `Canny`
- `PreviewImage`
- `Note`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `DualCLIPLoader`
- `TripleCLIPLoader`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `ControlNetLoader`

## 关键参数

- `seed` = `67773456290684`
- `steps` = `30`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `0.7000000000000001`
- `checkpoint` = `sd3.5_large.safetensors`

## 知识

覆盖率 **76%**（16/21）

**有卡**：`ConditioningZeroOut`、`KSampler`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`EmptySD3LatentImage`、`ACN_AdvancedControlNetApply`、`Canny`、`LoadImage`、`CLIPLoader`、`DualCLIPLoader`、`TripleCLIPLoader`、`CheckpointLoaderSimple`、`ControlNetLoader`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、ControlNetLoader
