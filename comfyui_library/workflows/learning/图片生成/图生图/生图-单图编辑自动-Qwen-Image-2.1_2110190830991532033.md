---
key: 图片生成/图生图/生图-单图编辑自动-Qwen-Image-2.1_2110190830991532033.json
name: 生图-单图编辑自动-Qwen-Image-2.1_2110190830991532033
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/生图-单图编辑自动-Qwen-Image-2.1_2110190830991532033.json
hash: 2773703240973f9f
coverage: 0.916667
learned_at: 2026-10-23 13:15:01
nodes: [CLIPLoader, VAEDecode, GetImageSizeAndCount, SaveImage, PreviewImage, easy imageConcat, TextEncodeQwenImage21, KSampler, easy seed, easy int, LoadImage, CLIPLoader, TextGenerateLTX2Prompt, UNETLoader, VAELoader, GetImageSizeAndCount, easy positive, easy int, LayerUtility: ImageScaleByAspectRatio V2, easy anythingIndexSwitch, easy saveText, StringFunction|pysssss, easy saveText, easy showAnything]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1007212216472920, "steps": 40}
---

# 图片生成/图生图/生图-单图编辑自动-Qwen-Image-2.1_2110190830991532033.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/生图-单图编辑自动-Qwen-Image-2.1_2110190830991532033.json`

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

- `seed` = `1007212216472920`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（22/24）

**有卡**：`CLIPLoader`、`VAEDecode`、`GetImageSizeAndCount`、`SaveImage`、`easy imageConcat`、`TextEncodeQwenImage21`、`KSampler`、`easy seed`、`easy int`、`LoadImage`、`TextGenerateLTX2Prompt`、`UNETLoader`、`VAELoader`、`easy positive`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy anythingIndexSwitch`、`easy saveText`、`StringFunction|pysssss`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、easy seed
