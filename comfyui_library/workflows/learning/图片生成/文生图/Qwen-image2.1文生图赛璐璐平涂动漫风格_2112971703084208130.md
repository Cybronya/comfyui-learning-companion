---
key: 图片生成/文生图/Qwen-image2.1文生图赛璐璐平涂动漫风格_2112971703084208130.json
name: Qwen-image2.1文生图赛璐璐平涂动漫风格_2112971703084208130
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-image2.1文生图赛璐璐平涂动漫风格_2112971703084208130.json
hash: 79891998372100a1
coverage: 0.857143
learned_at: 2026-10-26 22:08:46
nodes: [EmptyLatentImage, easy showAnything, easy showAnything, ResolutionSelector, QwenImage21Cache, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, VAEDecode, SaveImage, KSampler, LoraLoaderModelOnly, TextEncodeQwenImage21]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2048, "sampler_name": "euler_cfg_pp", "scheduler": "simple", "seed": 588501709484747, "steps": 9, "width": 1152}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen-image2.1文生图赛璐璐平涂动漫风格_2112971703084208130.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-image2.1文生图赛璐璐平涂动漫风格_2112971703084208130.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `EmptyLatentImage` ★核心
- `easy showAnything`
- `easy showAnything`
- `ResolutionSelector`
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImage21`

## 关键参数

- `width` = `1152`
- `height` = `2048`
- `batch_size` = `1`
- `seed` = `588501709484747`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler_cfg_pp`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`EmptyLatentImage`、`ResolutionSelector`、`QwenImage21Cache`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`VAEDecode`、`SaveImage`、`KSampler`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
