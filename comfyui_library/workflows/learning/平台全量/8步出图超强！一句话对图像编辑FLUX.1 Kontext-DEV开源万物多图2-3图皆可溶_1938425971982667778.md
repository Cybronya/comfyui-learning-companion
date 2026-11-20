---
key: 平台全量/8步出图超强！一句话对图像编辑FLUX.1 Kontext-DEV开源万物多图2-3图皆可溶_1938425971982667778.json
name: 8步出图超强！一句话对图像编辑FLUX.1 Kontext-DEV开源万物多图2-3图皆可溶_1938425971982667778
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/8步出图超强！一句话对图像编辑FLUX.1 Kontext-DEV开源万物多图2-3图皆可溶_1938425971982667778.json
hash: 0e2a5c37e2b3aff0
coverage: 0.863636
learned_at: 2026-11-14 00:14:13
nodes: [LoadImage, easy imageRemBg, easy imageRemBg, LoadImage, PreviewImage, VAEDecode, RH_Translator, ImageConcatMulti, Note, easy showAnything, UNETLoader, LoraLoaderModelOnly, DualCLIPLoader, VAELoader, workflow>1, KSampler (Efficient), SaveImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, EmptyLatentImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 59053874728107, "steps": 8, "width": 1024}
---

# 平台全量/8步出图超强！一句话对图像编辑FLUX.1 Kontext-DEV开源万物多图2-3图皆可溶_1938425971982667778.json

> 来源文件 `comfyui_library/workflows/平台全量/8步出图超强！一句话对图像编辑FLUX.1 Kontext-DEV开源万物多图2-3图皆可溶_1938425971982667778.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `LoadImage`
- `easy imageRemBg`
- `easy imageRemBg`
- `LoadImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `RH_Translator`
- `ImageConcatMulti`
- `Note`
- `easy showAnything`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `workflow>1`
- `KSampler (Efficient)` ★核心
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `EmptyLatentImage` ★核心

## 关键参数

- `seed` = `59053874728107`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（19/22）

**有卡**：`LoadImage`、`easy imageRemBg`、`VAEDecode`、`RH_Translator`、`ImageConcatMulti`、`UNETLoader`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`VAELoader`、`workflow>1`、`KSampler (Efficient)`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyLatentImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、EmptyLatentImage、LoadImage、UNETLoader、KSampler (Efficient)、SaveImage
