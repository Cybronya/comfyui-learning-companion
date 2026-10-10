---
key: sd3.5_Large 模型的基础工作流_1891736065517203458.json
name: sd3.5_Large 模型的基础工作流_1891736065517203458
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/sd3.5_Large 模型的基础工作流_1891736065517203458.json
hash: 93a9d600e8d33346
coverage: 0.833333
learned_at: 2026-10-10 20:59:26
nodes: [CLIPTextEncode, EmptySD3LatentImage, VAEDecode, Note, Note, CLIPTextEncode, KSampler, SaveImage, CheckpointLoaderSimple, DualCLIPLoader, TripleCLIPLoader, CLIPLoader]
patterns: []
missing: []
parameters: {"cfg": 5.45, "checkpoint": "sd3.5_large.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 377580771008877, "steps": 20}
---

# sd3.5_Large 模型的基础工作流_1891736065517203458.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/sd3.5_Large 模型的基础工作流_1891736065517203458.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `CheckpointLoaderSimple` ★核心
- `DualCLIPLoader`
- `TripleCLIPLoader`
- `CLIPLoader`

## 关键参数

- `seed` = `377580771008877`
- `steps` = `20`
- `cfg` = `5.45`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `sd3.5_large.safetensors`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`CLIPTextEncode`、`EmptySD3LatentImage`、`VAEDecode`、`KSampler`、`SaveImage`、`CheckpointLoaderSimple`、`DualCLIPLoader`、`TripleCLIPLoader`、`CLIPLoader`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、DualCLIPLoader、TripleCLIPLoader、SaveImage
