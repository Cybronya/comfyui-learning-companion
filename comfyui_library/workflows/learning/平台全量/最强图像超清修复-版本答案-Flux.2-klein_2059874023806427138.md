---
key: 平台全量/最强图像超清修复-版本答案-Flux.2-klein_2059874023806427138.json
name: 最强图像超清修复-版本答案-Flux.2-klein_2059874023806427138
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/最强图像超清修复-版本答案-Flux.2-klein_2059874023806427138.json
hash: d5756b38f7bf9373
coverage: 0.857143
learned_at: 2026-11-14 02:14:39
nodes: [CLIPLoader, ReferenceLatent, VAEDecodeTiled, VAEEncodeTiled, VAEEncodeTiled, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, VAELoader, SZ_KleinTiledKSampler, UNETLoader, easy imageColorMatch, easy int, ConditioningZeroOut, ReferenceLatent, Anything Everywhere3, FluxKVCache, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, LoraLoaderModelOnly, GetNode, Image Comparer (rgthree), SaveImage, SaveImage, LoadImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "simple", "seed": 1019940584593052, "steps": 4}
---

# 平台全量/最强图像超清修复-版本答案-Flux.2-klein_2059874023806427138.json

> 来源文件 `comfyui_library/workflows/平台全量/最强图像超清修复-版本答案-Flux.2-klein_2059874023806427138.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `CLIPLoader`
- `ReferenceLatent`
- `VAEDecodeTiled` ★核心
- `VAEEncodeTiled` ★核心
- `VAEEncodeTiled` ★核心
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `VAELoader`
- `SZ_KleinTiledKSampler` ★核心
- `UNETLoader` ★核心
- `easy imageColorMatch`
- `easy int`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `Anything Everywhere3`
- `FluxKVCache`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `1019940584593052`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（24/28）

**有卡**：`CLIPLoader`、`ReferenceLatent`、`VAEDecodeTiled`、`VAEEncodeTiled`、`LayerUtility: ImageMaskScaleAs`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`VAELoader`、`SZ_KleinTiledKSampler`、`UNETLoader`、`easy imageColorMatch`、`easy int`、`ConditioningZeroOut`、`FluxKVCache`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoaderModelOnly`、`SaveImage`、`LoadImage`、`CLIPTextEncode`

**用到的条目**：VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、SZ_KleinTiledKSampler
