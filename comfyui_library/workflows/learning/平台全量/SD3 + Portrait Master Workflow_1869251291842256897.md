---
key: 平台全量/SD3 + Portrait Master Workflow_1869251291842256897.json
name: SD3 + Portrait Master Workflow_1869251291842256897
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SD3 + Portrait Master Workflow_1869251291842256897.json
hash: 29b9ed41850e7a7f
coverage: 0.9
learned_at: 2026-11-14 00:56:03
nodes: [EmptySD3LatentImage, CLIPTextEncode, CLIPTextEncode, VAEDecode, KSampler, TripleCLIPLoader, CheckpointLoaderSimple, SaveImage, PreviewImage, PortraitMaster]
patterns: []
missing: []
parameters: {"cfg": 5.45, "checkpoint": "sd3_medium_incl_clips_t5xxlfp8.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 41721248094869, "steps": 30}
---

# 平台全量/SD3 + Portrait Master Workflow_1869251291842256897.json

> 来源文件 `comfyui_library/workflows/平台全量/SD3 + Portrait Master Workflow_1869251291842256897.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（10 个）：
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `TripleCLIPLoader`
- `CheckpointLoaderSimple` ★核心
- `SaveImage`
- `PreviewImage`
- `PortraitMaster`

## 关键参数

- `seed` = `41721248094869`
- `steps` = `30`
- `cfg` = `5.45`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `sd3_medium_incl_clips_t5xxlfp8.safetensors`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`EmptySD3LatentImage`、`CLIPTextEncode`、`VAEDecode`、`KSampler`、`TripleCLIPLoader`、`CheckpointLoaderSimple`、`SaveImage`、`PortraitMaster`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、TripleCLIPLoader、SaveImage、EmptySD3LatentImage、PortraitMaster
