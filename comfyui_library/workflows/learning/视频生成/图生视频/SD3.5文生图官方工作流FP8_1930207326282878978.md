---
key: 视频生成/图生视频/SD3.5文生图官方工作流FP8_1930207326282878978.json
name: SD3.5文生图官方工作流FP8_1930207326282878978.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1930207326282878978.json
hash: 1b970ca618ba0161
coverage: 0.769231
learned_at: 2026-10-15 22:30:03
nodes: [CheckpointLoaderSimple, KSampler, EmptySD3LatentImage, CLIPLoader, DualCLIPLoader, CLIPTextEncode, CLIPTextEncode, SaveImage, VAEDecode, PreviewImage, TripleCLIPLoader, Note, Note]
patterns: []
missing: []
parameters: {"cfg": 5.45, "checkpoint": "sd3.5_large_fp8_scaled.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 547696637878931, "steps": 30}
---

# 视频生成/图生视频/SD3.5文生图官方工作流FP8_1930207326282878978.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1930207326282878978.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `CheckpointLoaderSimple` ★核心
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `CLIPLoader`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `TripleCLIPLoader`
- `Note`
- `Note`

## 关键参数

- `checkpoint` = `sd3.5_large_fp8_scaled.safetensors`
- `seed` = `547696637878931`
- `steps` = `30`
- `cfg` = `5.45`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **77%**（10/13）

**有卡**：`CheckpointLoaderSimple`、`KSampler`、`EmptySD3LatentImage`、`CLIPLoader`、`DualCLIPLoader`、`CLIPTextEncode`、`SaveImage`、`VAEDecode`、`TripleCLIPLoader`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、DualCLIPLoader、TripleCLIPLoader、SaveImage
