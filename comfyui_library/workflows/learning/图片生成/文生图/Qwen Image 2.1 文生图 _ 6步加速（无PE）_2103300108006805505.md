---
key: 图片生成/文生图/Qwen Image 2.1 文生图 _ 6步加速（无PE）_2103300108006805505.json
name: Qwen Image 2.1 文生图 _ 6步加速（无PE）_2103300108006805505
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 文生图 _ 6步加速（无PE）_2103300108006805505.json
hash: 0b1190cc623fa661
coverage: 0.909091
learned_at: 2026-10-06 22:36:57
nodes: [UNETLoader, LoraLoaderModelOnly, VAELoader, CLIPLoader, EmptyLatentImage, TextEncodeQwenImage21, SaveImage, KSampler, VAEDecode, PrimitiveStringMultiline, ResolutionSelector]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1001138963381157, "steps": 6, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1 文生图 _ 6步加速（无PE）_2103300108006805505.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 文生图 _ 6步加速（无PE）_2103300108006805505.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（11 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `SaveImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PrimitiveStringMultiline`
- `ResolutionSelector`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1001138963381157`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`SaveImage`、`KSampler`、`VAEDecode`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
