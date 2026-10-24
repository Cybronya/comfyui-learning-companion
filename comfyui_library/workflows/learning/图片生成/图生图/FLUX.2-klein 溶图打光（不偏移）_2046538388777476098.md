---
key: 图片生成/图生图/FLUX.2-klein 溶图打光（不偏移）_2046538388777476098.json
name: FLUX.2-klein 溶图打光（不偏移）_2046538388777476098
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2-klein 溶图打光（不偏移）_2046538388777476098.json
hash: a42a088e571afc38
coverage: 0.923077
learned_at: 2026-10-23 10:54:14
nodes: [Image Comparer (rgthree), SaveImage, LoadImage, UNETLoader, CLIPLoader, VAELoader, GetImageSize+, ResizeImagesByLongerEdge, PainterFluxImageEdit, VAEDecode, KSampler, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 0.7000000000000001, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 12521090160738, "steps": 5}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FLUX.2-klein 溶图打光（不偏移）_2046538388777476098.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2-klein 溶图打光（不偏移）_2046538388777476098.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `Image Comparer (rgthree)`
- `SaveImage`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `GetImageSize+`
- `ResizeImagesByLongerEdge`
- `PainterFluxImageEdit`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `12521090160738`
- `steps` = `5`
- `cfg` = `0.7000000000000001`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`SaveImage`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`GetImageSize+`、`ResizeImagesByLongerEdge`、`PainterFluxImageEdit`、`VAEDecode`、`KSampler`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、PainterFluxImageEdit

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
