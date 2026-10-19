---
key: 图片生成/文生图/蒜-FLux1.D加载多个Lora生图工作流_1995009169252134914.json
name: 蒜-FLux1.D加载多个Lora生图工作流_1995009169252134914
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/蒜-FLux1.D加载多个Lora生图工作流_1995009169252134914.json
hash: af9ff1a29c27f7a8
coverage: 0.923077
learned_at: 2026-10-19 21:33:42
nodes: [EmptySD3LatentImage, CLIPTextEncode, LoraLoader, CLIPTextEncode, SaveImage, DualCLIPLoader, VAELoader, VAEDecode, FluxGuidance, UNETLoader, KSampler, LoraLoader, Note]
patterns: [lora]
missing: []
parameters: {"cfg": 1, "denoise": 1, "lora_name": "Retro_Synth_Noir_Flux-000021.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 347976382564096, "steps": 20, "strength_clip": 1, "strength_model": 0.8000000000000002}
---

# 图片生成/文生图/蒜-FLux1.D加载多个Lora生图工作流_1995009169252134914.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/蒜-FLux1.D加载多个Lora生图工作流_1995009169252134914.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `DualCLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `FluxGuidance`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `LoraLoader` ★核心
- `Note`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `Retro_Synth_Noir_Flux-000021.safetensors`
- `strength_model` = `0.8000000000000002`
- `strength_clip` = `1`
- `seed` = `347976382564096`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`EmptySD3LatentImage`、`CLIPTextEncode`、`LoraLoader`、`SaveImage`、`DualCLIPLoader`、`VAELoader`、`VAEDecode`、`FluxGuidance`、`UNETLoader`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、FluxGuidance、LoraLoader、LoraLoader
