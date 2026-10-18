---
key: 视频生成/文生视频/Wan2.1+t2v Lora文生视频工作流_1951460131294883841.json
name: Wan2.1+t2v Lora文生视频工作流_1951460131294883841.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1+t2v Lora文生视频工作流_1951460131294883841.json
hash: 6ae817c5d43e56d0
coverage: 1
learned_at: 2026-10-15 22:43:37
nodes: [CLIPTextEncode, VAELoader, VHS_VideoCombine, VAEDecode, KSampler, UNETLoader, CLIPLoader, CLIPTextEncode, LoraLoader, EmptyHunyuanLatentVideo]
patterns: [lora]
missing: []
parameters: {"cfg": 6, "denoise": 1, "lora_name": "SDlitgkreagirl_wan2.1_lora_k20.safetensors", "sampler_name": "uni_pc", "scheduler": "simple", "seed": 444682310152846, "steps": 30, "strength_clip": 1, "strength_model": 1}
---

# 视频生成/文生视频/Wan2.1+t2v Lora文生视频工作流_1951460131294883841.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1951460131294883841.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（10 个）：
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `EmptyHunyuanLatentVideo`

**识别到的模式**：lora

## 关键参数

- `seed` = `444682310152846`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `SDlitgkreagirl_wan2.1_lora_k20.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`CLIPTextEncode`、`VAELoader`、`VHS_VideoCombine`、`VAEDecode`、`KSampler`、`UNETLoader`、`CLIPLoader`、`LoraLoader`、`EmptyHunyuanLatentVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo、LoraLoader
