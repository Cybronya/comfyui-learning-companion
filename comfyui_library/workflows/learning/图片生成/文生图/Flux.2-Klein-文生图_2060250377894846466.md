---
key: 图片生成/文生图/Flux.2-Klein-文生图_2060250377894846466.json
name: Flux.2-Klein-文生图_2060250377894846466
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.2-Klein-文生图_2060250377894846466.json
hash: 1a7e8687562756ff
coverage: 1
learned_at: 2026-10-19 23:02:22
nodes: [CLIPTextEncode, VAEDecode, VAELoader, EmptyFlux2LatentImage, SaveImage, CLIPLoader, KSampler, LoraLoader, CLIPTextEncode, UNETLoader, Seed (rgthree)]
patterns: [lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "flux2-klein\\flux-2-klein-9b_细节增加,0.4~0.8.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 19855, "steps": 8, "strength_clip": 1, "strength_model": 0.4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Flux.2-Klein-文生图_2060250377894846466.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.2-Klein-文生图_2060250377894846466.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（11 个）：
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `EmptyFlux2LatentImage`
- `SaveImage`
- `CLIPLoader`
- `KSampler` ★核心
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `Seed (rgthree)`

**识别到的模式**：lora

## 关键参数

- `seed` = `19855`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `flux2-klein\flux-2-klein-9b_细节增加,0.4~0.8.safetensors`
- `strength_model` = `0.4`
- `strength_clip` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`VAELoader`、`EmptyFlux2LatentImage`、`SaveImage`、`CLIPLoader`、`KSampler`、`LoraLoader`、`UNETLoader`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、Seed (rgthree)、EmptyFlux2LatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
