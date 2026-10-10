---
key: Qwen 电商小票创意海报 工作流 V1.0_1959790560150237186.json
name: Qwen 电商小票创意海报 工作流 V1.0_1959790560150237186
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen 电商小票创意海报 工作流 V1.0_1959790560150237186.json
hash: c5db0b81e0cb377a
coverage: 0.866667
learned_at: 2026-10-10 20:58:58
nodes: [ModelSamplingAuraFlow, UpscaleModelLoader, UltimateSDUpscale, PreviewImage, Note, CLIPTextEncode, VAEDecode, SaveImage, KSampler, VAELoader, UNETLoader, CLIPLoader, CLIPTextEncode, LoraLoader, EmptySD3LatentImage]
patterns: [lora]
missing: []
parameters: {"cfg": 3.5, "denoise": 1, "lora_name": "Qwen-Image loRA ONEART美学Master 电商创意小票海报设计模型 LIXIAOXIAO.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 876901494252275, "steps": 30, "strength_clip": 1.0000000000000002, "strength_model": 0.8000000000000002}
---

# Qwen 电商小票创意海报 工作流 V1.0_1959790560150237186.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen 电商小票创意海报 工作流 V1.0_1959790560150237186.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `ModelSamplingAuraFlow`
- `UpscaleModelLoader`
- `UltimateSDUpscale`
- `PreviewImage`
- `Note`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `EmptySD3LatentImage`

**识别到的模式**：lora

## 关键参数

- `seed` = `876901494252275`
- `steps` = `30`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `Qwen-Image loRA ONEART美学Master 电商创意小票海报设计模型 LIXIAOXIAO.safetensors`
- `strength_model` = `0.8000000000000002`
- `strength_clip` = `1.0000000000000002`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`ModelSamplingAuraFlow`、`UpscaleModelLoader`、`UltimateSDUpscale`、`CLIPTextEncode`、`VAEDecode`、`SaveImage`、`KSampler`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`LoraLoader`、`EmptySD3LatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、LoraLoader、LoraLoader
