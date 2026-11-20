---
key: 平台全量/Flux.2+Klein+究极换头&换脸，零违和感_2031893920250077185.json
name: Flux.2+Klein+究极换头&换脸，零违和感_2031893920250077185
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux.2+Klein+究极换头&换脸，零违和感_2031893920250077185.json
hash: 33c59888989fa1f2
coverage: 0.782609
learned_at: 2026-11-14 00:28:57
nodes: [Image Comparer (rgthree), ImageConcanate, MaskPreview+, KSampler, PainterFluxImageEdit, easy imageRemBg, LayerUtility: ImageScaleByAspectRatio V2, easy ifElse, Image Comparer (rgthree), easy isMaskEmpty, SolidMask, ColorMatch, CLIPLoader, ImageConcanate, PreviewImage, VAEDecode, PreviewImage, SaveImage, VAELoader, LoadImage, LoadImage, LoraLoaderModelOnly, UNETLoader]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 498364497356386, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Flux.2+Klein+究极换头&换脸，零违和感_2031893920250077185.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux.2+Klein+究极换头&换脸，零违和感_2031893920250077185.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `MaskPreview+`
- `KSampler` ★核心
- `PainterFluxImageEdit`
- `easy imageRemBg`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy ifElse`
- `Image Comparer (rgthree)`
- `easy isMaskEmpty`
- `SolidMask`
- `ColorMatch`
- `CLIPLoader`
- `ImageConcanate`
- `PreviewImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `498364497356386`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（18/23）

**有卡**：`ImageConcanate`、`MaskPreview+`、`KSampler`、`PainterFluxImageEdit`、`easy imageRemBg`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy isMaskEmpty`、`SolidMask`、`ColorMatch`、`CLIPLoader`、`VAEDecode`、`SaveImage`、`VAELoader`、`LoadImage`、`LoraLoaderModelOnly`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、PainterFluxImageEdit

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
