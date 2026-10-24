---
key: 图片生成/图生图/flux.2-klein-单图编辑工作流_2076574283811352577.json
name: flux.2-klein-单图编辑工作流_2076574283811352577
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/flux.2-klein-单图编辑工作流_2076574283811352577.json
hash: a68daa9b535c58e6
coverage: 0.928571
learned_at: 2026-10-23 11:35:53
nodes: [CLIPLoader, VAELoader, UNETLoader, ImageScaleToTotalPixels, VAEEncode, CLIPTextEncode, CLIPTextEncode, ReferenceLatent, KSampler, ReferenceLatent, VAEDecode, SaveImage, Image Comparer (rgthree), LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 316229828415722, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/flux.2-klein-单图编辑工作流_2076574283811352577.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/flux.2-klein-单图编辑工作流_2076574283811352577.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `KSampler` ★核心
- `ReferenceLatent`
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `316229828415722`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`ImageScaleToTotalPixels`、`VAEEncode`、`CLIPTextEncode`、`ReferenceLatent`、`KSampler`、`VAEDecode`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、ReferenceLatent

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
