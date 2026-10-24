---
key: 图片生成/图生图/Qwen2.1_漫转真_2110186652676222978.json
name: Qwen2.1_漫转真_2110186652676222978
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1_漫转真_2110186652676222978.json
hash: a6b862419c7c0518
coverage: 0.909091
learned_at: 2026-10-23 11:19:06
nodes: [CLIPLoader, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, KSampler, VAEDecode, LoraLoaderModelOnly, UNETLoader, SaveImage, LoadImage, TextEncodeQwenImage21, JjkText]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 688114272090238, "steps": 40}
---

# 图片生成/图生图/Qwen2.1_漫转真_2110186652676222978.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1_漫转真_2110186652676222978.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（11 个）：
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `JjkText`

## 关键参数

- `seed` = `688114272090238`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`CLIPLoader`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`VAEDecode`、`LoraLoaderModelOnly`、`UNETLoader`、`SaveImage`、`LoadImage`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader
