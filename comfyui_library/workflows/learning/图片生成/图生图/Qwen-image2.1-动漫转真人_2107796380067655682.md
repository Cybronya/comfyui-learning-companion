---
key: 图片生成/图生图/Qwen-image2.1-动漫转真人_2107796380067655682.json
name: Qwen-image2.1-动漫转真人_2107796380067655682
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-动漫转真人_2107796380067655682.json
hash: 7046f824927ec516
coverage: 0.909091
learned_at: 2026-10-21 00:43:26
nodes: [VAELoader, LoraLoaderModelOnly, LoadImage, KSampler, Image Comparer (rgthree), UNETLoader, CLIPLoader, TextEncodeQwenImage21, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 755272989138121, "steps": 25}
---

# 图片生成/图生图/Qwen-image2.1-动漫转真人_2107796380067655682.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-动漫转真人_2107796380067655682.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（11 个）：
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `755272989138121`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`VAELoader`、`LoraLoaderModelOnly`、`LoadImage`、`KSampler`、`UNETLoader`、`CLIPLoader`、`TextEncodeQwenImage21`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader
