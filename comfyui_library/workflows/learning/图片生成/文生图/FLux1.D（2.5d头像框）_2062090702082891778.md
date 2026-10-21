---
key: 图片生成/文生图/FLux1.D（2.5d头像框）_2062090702082891778.json
name: FLux1.D（2.5d头像框）_2062090702082891778
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLux1.D（2.5d头像框）_2062090702082891778.json
hash: 05c09f36c83f4dda
coverage: 1
learned_at: 2026-10-19 23:02:20
nodes: [UNETLoader, DualCLIPLoader, VAELoader, VAEDecode, CLIPTextEncode, FluxGuidance, CLIPTextEncode, StringFunction|pysssss, SaveImage, LoraLoader, LoraLoader, KSampler, EmptySD3LatentImage, DeepTranslatorTextNode]
patterns: [lora]
missing: []
parameters: {"cfg": 1, "denoise": 1, "lora_name": "语音房运营活动头像框_v1.0.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 485388095081024, "steps": 25, "strength_clip": 1, "strength_model": 0.8000000000000002}
---

# 图片生成/文生图/FLux1.D（2.5d头像框）_2062090702082891778.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLux1.D（2.5d头像框）_2062090702082891778.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `StringFunction|pysssss`
- `SaveImage`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `DeepTranslatorTextNode`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `语音房运营活动头像框_v1.0.safetensors`
- `strength_model` = `0.8000000000000002`
- `strength_clip` = `1`
- `seed` = `485388095081024`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`VAEDecode`、`CLIPTextEncode`、`FluxGuidance`、`StringFunction|pysssss`、`SaveImage`、`LoraLoader`、`KSampler`、`EmptySD3LatentImage`、`DeepTranslatorTextNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、FluxGuidance、LoraLoader、LoraLoader
