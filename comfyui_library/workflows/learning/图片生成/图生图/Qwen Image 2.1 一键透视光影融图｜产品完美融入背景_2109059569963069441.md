---
key: 图片生成/图生图/Qwen Image 2.1 一键透视光影融图｜产品完美融入背景_2109059569963069441.json
name: Qwen Image 2.1 一键透视光影融图｜产品完美融入背景_2109059569963069441
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 一键透视光影融图｜产品完美融入背景_2109059569963069441.json
hash: 1114630927ff652a
coverage: 0.846154
learned_at: 2026-10-23 11:12:40
nodes: [UNETLoader, CLIPLoader, VAELoader, easy seed, KSampler (Efficient), 孤海注释, TextEncodeQwenImage21, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ImpactInt, LoraLoaderModelOnly, SaveImage, Image Comparer (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1087017653511199, "steps": 30}
---

# 图片生成/图生图/Qwen Image 2.1 一键透视光影融图｜产品完美融入背景_2109059569963069441.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 一键透视光影融图｜产品完美融入背景_2109059569963069441.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（13 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `easy seed`
- `KSampler (Efficient)` ★核心
- `孤海注释`
- `TextEncodeQwenImage21`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ImpactInt`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`

## 关键参数

- `seed` = `1087017653511199`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`easy seed`、`KSampler (Efficient)`、`TextEncodeQwenImage21`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`ImpactInt`、`LoraLoaderModelOnly`、`SaveImage`

**用到的条目**：TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、easy seed、KSampler (Efficient)
