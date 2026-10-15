---
key: 图片生成/文生图/sd3.5_large 满血版 官方文生图示例_1848750522676416513.json
name: sd3.5_large 满血版 官方文生图示例_1848750522676416513
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/sd3.5_large 满血版 官方文生图示例_1848750522676416513.json
hash: 304e45cb64d68f25
coverage: 0.846154
learned_at: 2026-10-10 20:59:26
nodes: [VAEDecode, SaveImage, CLIPTextEncode, EmptySD3LatentImage, Note, CLIPLoader, DualCLIPLoader, KSampler, Note, TripleCLIPLoader, CheckpointLoaderSimple, CLIPTextEncode, SeargePromptText]
patterns: []
missing: []
parameters: {"cfg": 5.45, "checkpoint": "sd3.5_large.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 728169240323889, "steps": 20}
---

# 图片生成/文生图/sd3.5_large 满血版 官方文生图示例_1848750522676416513.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/sd3.5_large 满血版 官方文生图示例_1848750522676416513.json`

## 结构

**节点**（13 个）：
- `VAEDecode`
- `SaveImage`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `Note`
- `CLIPLoader`
- `DualCLIPLoader`
- `KSampler`
- `Note`
- `TripleCLIPLoader`
- `CheckpointLoaderSimple`
- `CLIPTextEncode`
- `SeargePromptText`

## 关键参数

- `cfg` = `5.45`
- `checkpoint` = `sd3.5_large.safetensors`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `seed` = `728169240323889`
- `steps` = `20`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`EmptySD3LatentImage`、`Note`、`CLIPLoader`、`DualCLIPLoader`、`KSampler`、`TripleCLIPLoader`、`CheckpointLoaderSimple`
