---
key: Qwen+朋友圈、海报设计+V1.0文生图_2100404141968412674.json
name: Qwen+朋友圈、海报设计+V1.0文生图_2100404141968412674
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen+朋友圈、海报设计+V1.0文生图_2100404141968412674.json
hash: 22de668103cb8f54
coverage: 0.866667
learned_at: 2026-10-10 20:58:58
nodes: [ModelSamplingAuraFlow, UpscaleModelLoader, UltimateSDUpscale, PreviewImage, CLIPTextEncode, VAEDecode, CLIPTextEncode, EmptySD3LatentImage, VAELoader, UNETLoader, CLIPLoader, LoraLoader, SaveImage, KSampler, Note]
patterns: [lora]
missing: []
parameters: {"cfg": 3.5, "denoise": 1, "lora_name": "Qwen-Image 3D IP XIAOXIAOloRA.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 819489811679281, "steps": 30, "strength_clip": 0.8000000000000002, "strength_model": 0.8000000000000002}
---

# Qwen+朋友圈、海报设计+V1.0文生图_2100404141968412674.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen+朋友圈、海报设计+V1.0文生图_2100404141968412674.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `ModelSamplingAuraFlow`
- `UpscaleModelLoader`
- `UltimateSDUpscale`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoader` ★核心
- `SaveImage`
- `KSampler` ★核心
- `Note`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `Qwen-Image 3D IP XIAOXIAOloRA.safetensors`
- `strength_model` = `0.8000000000000002`
- `strength_clip` = `0.8000000000000002`
- `seed` = `819489811679281`
- `steps` = `30`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`ModelSamplingAuraFlow`、`UpscaleModelLoader`、`UltimateSDUpscale`、`CLIPTextEncode`、`VAEDecode`、`EmptySD3LatentImage`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`LoraLoader`、`SaveImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、LoraLoader、LoraLoader
