---
key: 图片生成/文生图/FLUX.2万物生成高质感_2069427067028074497.json
name: FLUX.2万物生成高质感_2069427067028074497
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX.2万物生成高质感_2069427067028074497.json
hash: 619d0d1ba38ad140
coverage: 1
learned_at: 2026-10-19 23:40:56
nodes: [CLIPLoader, VAELoader, VAEDecode, SaveImage, KSampler, CLIPTextEncode, CLIPTextEncode, UNETLoader, LoraLoaderModelOnly, EmptyFlux2LatentImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 316229828415716, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/FLUX.2万物生成高质感_2069427067028074497.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX.2万物生成高质感_2069427067028074497.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output

**节点**（10 个）：
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyFlux2LatentImage`

## 关键参数

- `seed` = `316229828415716`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`SaveImage`、`KSampler`、`CLIPTextEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`EmptyFlux2LatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyFlux2LatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
