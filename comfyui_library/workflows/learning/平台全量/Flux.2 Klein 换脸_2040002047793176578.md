---
key: 平台全量/Flux.2 Klein 换脸_2040002047793176578.json
name: Flux.2 Klein 换脸_2040002047793176578
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux.2 Klein 换脸_2040002047793176578.json
hash: 06d35ec5978a6eba
coverage: 0.884615
learned_at: 2026-11-14 00:28:51
nodes: [Image Comparer (rgthree), SaveImage, easy imageRemBg, CLIPLoader, VAELoader, UNETLoader, LoraLoaderModelOnly, easy isMaskEmpty, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PainterFluxImageEdit, KSampler, ImageConcanate, ImageConcanate, SolidMask, easy ifElse, VAEDecode, MaskPreview+, ColorMatch, CompressImages, DuckHideNode, SaveImage, Image Comparer (rgthree), SaveImage, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 279755822824331, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Flux.2 Klein 换脸_2040002047793176578.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux.2 Klein 换脸_2040002047793176578.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `Image Comparer (rgthree)`
- `SaveImage`
- `easy imageRemBg`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy isMaskEmpty`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PainterFluxImageEdit`
- `KSampler` ★核心
- `ImageConcanate`
- `ImageConcanate`
- `SolidMask`
- `easy ifElse`
- `VAEDecode` ★核心
- `MaskPreview+`
- `ColorMatch`
- `CompressImages`
- `DuckHideNode`
- `SaveImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `LoadImage`

## 关键参数

- `seed` = `279755822824331`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（23/26）

**有卡**：`SaveImage`、`easy imageRemBg`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`easy isMaskEmpty`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`PainterFluxImageEdit`、`KSampler`、`ImageConcanate`、`SolidMask`、`VAEDecode`、`MaskPreview+`、`ColorMatch`、`CompressImages`、`DuckHideNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、PainterFluxImageEdit

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
