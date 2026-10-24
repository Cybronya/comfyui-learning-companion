---
key: 图片生成/图生图/Flux.2-Klein图生图洗图工作流_2075029554900586497.json
name: Flux.2-Klein图生图洗图工作流_2075029554900586497
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.2-Klein图生图洗图工作流_2075029554900586497.json
hash: 0d8a3de52232c967
coverage: 0.909091
learned_at: 2026-10-23 10:58:51
nodes: [CLIPLoader, UNETLoader, CLIPTextEncode, VAELoader, VAEDecode, CLIPTextEncode, LoadImage, VAEEncode, Image Comparer (rgthree), SaveImage, KSampler]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.3500000000000001, "sampler_name": "euler", "scheduler": "simple", "seed": 316229828415718, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Flux.2-Klein图生图洗图工作流_2075029554900586497.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.2-Klein图生图洗图工作流_2075029554900586497.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（11 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `VAEEncode` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `316229828415718`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.3500000000000001`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`CLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`VAELoader`、`VAEDecode`、`LoadImage`、`VAEEncode`、`SaveImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
