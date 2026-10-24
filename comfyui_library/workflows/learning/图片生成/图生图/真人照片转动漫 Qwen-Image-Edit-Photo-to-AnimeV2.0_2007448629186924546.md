---
key: 图片生成/图生图/真人照片转动漫 Qwen-Image-Edit-Photo-to-AnimeV2.0_2007448629186924546.json
name: 真人照片转动漫 Qwen-Image-Edit-Photo-to-AnimeV2.0_2007448629186924546
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/真人照片转动漫 Qwen-Image-Edit-Photo-to-AnimeV2.0_2007448629186924546.json
hash: 14c4670834c17f2f
coverage: 1
learned_at: 2026-10-23 13:18:43
nodes: [ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, CFGNorm, EmptySD3LatentImage, VAEDecode, KSampler, SaveImage, TextEncodeQwenImageEditPlus, LoadImage, UNETLoader, CLIPLoader, LoraLoader, VAELoader, LoraLoader]
patterns: [lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "ZankuroIXLLight_v2.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 31404, "steps": 8, "strength_clip": 1, "strength_model": 1}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/真人照片转动漫 Qwen-Image-Edit-Photo-to-AnimeV2.0_2007448629186924546.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/真人照片转动漫 Qwen-Image-Edit-Photo-to-AnimeV2.0_2007448629186924546.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `CFGNorm`
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoader` ★核心
- `VAELoader`
- `LoraLoader` ★核心

**识别到的模式**：lora

## 关键参数

- `seed` = `31404`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `ZankuroIXLLight_v2.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`ModelSamplingAuraFlow`、`TextEncodeQwenImageEditPlus`、`CFGNorm`、`EmptySD3LatentImage`、`VAEDecode`、`KSampler`、`SaveImage`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`LoraLoader`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、LoadImage、UNETLoader、CFGNorm、TextEncodeQwenImageEditPlus

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
