---
key: 图片生成/文生图/Kontext Dev+LoRA 文生图  teaCache 加速_1938503902566506497.json
name: Kontext Dev+LoRA 文生图  teaCache 加速_1938503902566506497.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Kontext Dev+LoRA 文生图  teaCache 加速_1938503902566506497.json
hash: c589dc634ee7a52f
coverage: 1
learned_at: 2026-10-07 22:46:26
nodes: [FluxGuidance, VAELoader, KSampler, CLIPTextEncode, EmptySD3LatentImage, CLIPTextEncode, VAEDecode, SaveImage, DualCLIPLoader, CheckpointLoaderSimple, LoraLoaderModelOnly, TeaCache]
patterns: []
missing: []
parameters: {"cfg": 1, "checkpoint": "Flux_Kontext_dev_fp8.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1099178179153320, "steps": 10}
---

# 图片生成/文生图/Kontext Dev+LoRA 文生图  teaCache 加速_1938503902566506497.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1938503902566506497.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `FluxGuidance`
- `VAELoader`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `DualCLIPLoader`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `TeaCache`

## 关键参数

- `seed` = `1099178179153320`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `Flux_Kontext_dev_fp8.safetensors`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`FluxGuidance`、`VAELoader`、`KSampler`、`CLIPTextEncode`、`EmptySD3LatentImage`、`VAEDecode`、`SaveImage`、`DualCLIPLoader`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`TeaCache`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、FluxGuidance、DualCLIPLoader
