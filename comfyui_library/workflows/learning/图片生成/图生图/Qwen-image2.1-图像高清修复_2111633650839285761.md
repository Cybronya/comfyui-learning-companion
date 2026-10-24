---
key: 图片生成/图生图/Qwen-image2.1-图像高清修复_2111633650839285761.json
name: Qwen-image2.1-图像高清修复_2111633650839285761
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-图像高清修复_2111633650839285761.json
hash: d24abe6f67c30779
coverage: 0.916667
learned_at: 2026-10-23 11:18:27
nodes: [UNETLoader, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, LoadImage, Int, CLIPLoader, LoraLoaderModelOnly, TextEncodeQwenImage21, KSampler, Image Comparer (rgthree), SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 478488991128650, "steps": 25}
---

# 图片生成/图生图/Qwen-image2.1-图像高清修复_2111633650839285761.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-图像高清修复_2111633650839285761.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `LoadImage`
- `Int`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`

## 关键参数

- `seed` = `478488991128650`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`UNETLoader`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`LoadImage`、`Int`、`CLIPLoader`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`KSampler`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader
