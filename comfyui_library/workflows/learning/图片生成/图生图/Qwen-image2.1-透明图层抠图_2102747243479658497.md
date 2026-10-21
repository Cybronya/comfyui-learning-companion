---
key: 图片生成/图生图/Qwen-image2.1-透明图层抠图_2102747243479658497.json
name: Qwen-image2.1-透明图层抠图_2102747243479658497
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-透明图层抠图_2102747243479658497.json
hash: 78bc71165ab05a9e
coverage: 0.9
learned_at: 2026-10-21 00:43:28
nodes: [CLIPLoader, VAEDecode, LoadImage, KSampler, UNETLoader, LoraLoaderModelOnly, VAELoader, PreviewImage, TextEncodeQwenImage21, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 719014370849792, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-image2.1-透明图层抠图_2102747243479658497.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-透明图层抠图_2102747243479658497.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（10 个）：
- `CLIPLoader`
- `VAEDecode` ★核心
- `LoadImage`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `PreviewImage`
- `TextEncodeQwenImage21`
- `SaveImage`

## 关键参数

- `seed` = `719014370849792`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`CLIPLoader`、`VAEDecode`、`LoadImage`、`KSampler`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`TextEncodeQwenImage21`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
