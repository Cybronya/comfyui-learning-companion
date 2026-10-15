---
key: 图片生成/文生图/SD3.5文生图官方工作流FP16_1930199196047982593.json
name: SD3.5文生图官方工作流FP16_1930199196047982593
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/SD3.5文生图官方工作流FP16_1930199196047982593.json
hash: cd1636e853facc56
coverage: 0.769231
learned_at: 2026-10-10 20:59:10
nodes: [Note, DualCLIPLoader, Note, SaveImage, TripleCLIPLoader, CheckpointLoaderSimple, CLIPTextEncode, CLIPTextEncode, KSampler, VAEDecode, EmptySD3LatentImage, PreviewImage, CLIPLoader]
patterns: []
missing: []
parameters: {"cfg": 5.45, "checkpoint": "sd3.5_large.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 753747895600699, "steps": 30}
---

# 图片生成/文生图/SD3.5文生图官方工作流FP16_1930199196047982593.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/SD3.5文生图官方工作流FP16_1930199196047982593.json`

## 结构

**节点**（13 个）：
- `Note`
- `DualCLIPLoader`
- `Note`
- `SaveImage`
- `TripleCLIPLoader`
- `CheckpointLoaderSimple`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `KSampler`
- `VAEDecode`
- `EmptySD3LatentImage`
- `PreviewImage`
- `CLIPLoader`

## 关键参数

- `cfg` = `5.45`
- `checkpoint` = `sd3.5_large.safetensors`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `seed` = `753747895600699`
- `steps` = `30`

## 知识

覆盖率 **77%**（10/13）

**有卡**：`Note`、`DualCLIPLoader`、`SaveImage`、`TripleCLIPLoader`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`KSampler`、`VAEDecode`
