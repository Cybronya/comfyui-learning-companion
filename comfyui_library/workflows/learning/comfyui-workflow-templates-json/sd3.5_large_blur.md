---
key: comfyui-workflow-templates-json/sd3.5_large_blur.json
name: sd3.5_large_blur
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/sd3.5_large_blur.json
hash: 1080bd0dc2fd3ed9
official: true
coverage: 0.833333
learned_at: 2026-10-10 22:48:50
nodes: [ConditioningZeroOut, CLIPTextEncode, VAEDecode, LoadImage, EmptySD3LatentImage, ControlNetLoader, CheckpointLoaderSimple, MarkdownNote, MarkdownNote, KSampler, SaveImage, ControlNetApplyAdvanced]
patterns: []
missing: []
parameters: {"cfg": 4, "checkpoint": "sd3.5_large_fp8_scaled.safetensors", "controlnet_strength": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 268264726798396, "steps": 30}
---

# comfyui-workflow-templates-json/sd3.5_large_blur.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/sd3.5_large_blur.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `EmptySD3LatentImage`
- `ControlNetLoader`
- `CheckpointLoaderSimple` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `KSampler` ★核心
- `SaveImage`
- `ControlNetApplyAdvanced` ★核心

## 关键参数

- `checkpoint` = `sd3.5_large_fp8_scaled.safetensors`
- `seed` = `268264726798396`
- `steps` = `30`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `1`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`ConditioningZeroOut`、`CLIPTextEncode`、`VAEDecode`、`LoadImage`、`EmptySD3LatentImage`、`ControlNetLoader`、`CheckpointLoaderSimple`、`KSampler`、`SaveImage`、`ControlNetApplyAdvanced`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetApplyAdvanced、ControlNetLoader
