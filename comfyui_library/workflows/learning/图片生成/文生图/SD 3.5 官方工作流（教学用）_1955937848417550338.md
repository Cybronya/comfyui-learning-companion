---
key: 图片生成/文生图/SD 3.5 官方工作流（教学用）_1955937848417550338.json
name: SD 3.5 官方工作流（教学用）_1955937848417550338
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/SD 3.5 官方工作流（教学用）_1955937848417550338.json
hash: 64cc4a62c1f93f74
coverage: 1
learned_at: 2026-10-10 20:59:10
nodes: [VAEDecode, SaveImage, TripleCLIPLoader, CheckpointLoaderSimple, CLIPTextEncode, CLIPTextEncode, EmptySD3LatentImage, KSampler]
patterns: []
missing: []
parameters: {"cfg": 5.45, "checkpoint": "sd3.5_large.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 852247600353801, "steps": 20}
---

# 图片生成/文生图/SD 3.5 官方工作流（教学用）_1955937848417550338.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/SD 3.5 官方工作流（教学用）_1955937848417550338.json`

## 结构

**节点**（8 个）：
- `VAEDecode`
- `SaveImage`
- `TripleCLIPLoader`
- `CheckpointLoaderSimple`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`

## 关键参数

- `cfg` = `5.45`
- `checkpoint` = `sd3.5_large.safetensors`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `seed` = `852247600353801`
- `steps` = `20`

## 知识

覆盖率 **100%**（8/8）

**有卡**：`VAEDecode`、`SaveImage`、`TripleCLIPLoader`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`EmptySD3LatentImage`、`KSampler`
