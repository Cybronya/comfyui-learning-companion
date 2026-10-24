---
key: 图片生成/图生图/Qwen image 2.1 一键模特换装｜服装迁移_2111691946950483969.json
name: Qwen image 2.1 一键模特换装｜服装迁移_2111691946950483969
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 一键模特换装｜服装迁移_2111691946950483969.json
hash: 2a3803aeba28df54
coverage: 0.857143
learned_at: 2026-10-23 11:13:55
nodes: [LayerUtility: ImageScaleByAspectRatio V2, 孤海注释, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, TextEncodeQwenImage21, VAEDecode, Image Comparer (rgthree), SaveImage, Int, LoadImage, KSampler, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 247352141489410, "steps": 25}
---

# 图片生成/图生图/Qwen image 2.1 一键模特换装｜服装迁移_2111691946950483969.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 一键模特换装｜服装迁移_2111691946950483969.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `Int`
- `LoadImage`
- `KSampler` ★核心
- `LoadImage`

## 关键参数

- `seed` = `247352141489410`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`VAEDecode`、`SaveImage`、`Int`、`LoadImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader
