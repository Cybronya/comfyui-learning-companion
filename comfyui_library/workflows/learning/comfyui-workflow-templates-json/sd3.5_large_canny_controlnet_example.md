---
key: comfyui-workflow-templates-json/sd3.5_large_canny_controlnet_example.json
name: sd3.5_large_canny_controlnet_example
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/sd3.5_large_canny_controlnet_example.json
hash: 45f3606abb069c53
official: true
coverage: 0.857143
learned_at: 2026-10-07 21:36:16
nodes: [CheckpointLoaderSimple, ControlNetLoader, ConditioningZeroOut, LoadImage, EmptySD3LatentImage, ControlNetApplyAdvanced, VAEDecode, KSampler, SaveImage, MarkdownNote, ImageScale, CLIPTextEncode, Canny, PreviewImage]
patterns: []
missing: []
parameters: {"cfg": 4.5, "checkpoint": "sd3.5_large_fp8_scaled.safetensors", "controlnet_strength": 0.66, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 840657187058661, "steps": 32}
---

# comfyui-workflow-templates-json/sd3.5_large_canny_controlnet_example.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/sd3.5_large_canny_controlnet_example.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `CheckpointLoaderSimple` ★核心
- `ControlNetLoader`
- `ConditioningZeroOut`
- `LoadImage`
- `EmptySD3LatentImage`
- `ControlNetApplyAdvanced` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `MarkdownNote`
- `ImageScale`
- `CLIPTextEncode` ★核心
- `Canny`
- `PreviewImage`

## 关键参数

- `checkpoint` = `sd3.5_large_fp8_scaled.safetensors`
- `controlnet_strength` = `0.66`
- `seed` = `840657187058661`
- `steps` = `32`
- `cfg` = `4.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`CheckpointLoaderSimple`、`ControlNetLoader`、`ConditioningZeroOut`、`LoadImage`、`EmptySD3LatentImage`、`ControlNetApplyAdvanced`、`VAEDecode`、`KSampler`、`SaveImage`、`ImageScale`、`CLIPTextEncode`、`Canny`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetApplyAdvanced、ControlNetLoader
