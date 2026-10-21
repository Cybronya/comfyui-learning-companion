---
key: 图片生成/图生图/生图-单图编辑自动-Qwen-Image-2.1_2104100007581409282.json
name: 生图-单图编辑自动-Qwen-Image-2.1_2104100007581409282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/生图-单图编辑自动-Qwen-Image-2.1_2104100007581409282.json
hash: b611a044ccb6f408
coverage: 0.916667
learned_at: 2026-10-21 00:55:07
nodes: [CLIPLoader, VAEDecode, GetImageSizeAndCount, SaveImage, PreviewImage, easy imageConcat, TextEncodeQwenImage21, KSampler, easy seed, easy int, LoadImage, CLIPLoader, TextGenerateLTX2Prompt, UNETLoader, VAELoader, GetImageSizeAndCount, easy positive, easy int, LayerUtility: ImageScaleByAspectRatio V2, easy anythingIndexSwitch, easy saveText, StringFunction|pysssss, easy saveText, easy showAnything]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 823703743464113, "steps": 40}
---

# 图片生成/图生图/生图-单图编辑自动-Qwen-Image-2.1_2104100007581409282.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/生图-单图编辑自动-Qwen-Image-2.1_2104100007581409282.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `CLIPLoader`
- `VAEDecode` ★核心
- `GetImageSizeAndCount`
- `SaveImage`
- `PreviewImage`
- `easy imageConcat`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `easy seed`
- `easy int`
- `LoadImage`
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `UNETLoader` ★核心
- `VAELoader`
- `GetImageSizeAndCount`
- `easy positive`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy anythingIndexSwitch`
- `easy saveText`
- `StringFunction|pysssss`
- `easy saveText`
- `easy showAnything`

## 关键参数

- `seed` = `823703743464113`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（22/24）

**有卡**：`CLIPLoader`、`VAEDecode`、`GetImageSizeAndCount`、`SaveImage`、`easy imageConcat`、`TextEncodeQwenImage21`、`KSampler`、`easy seed`、`easy int`、`LoadImage`、`TextGenerateLTX2Prompt`、`UNETLoader`、`VAELoader`、`easy positive`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy anythingIndexSwitch`、`easy saveText`、`StringFunction|pysssss`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、easy seed
