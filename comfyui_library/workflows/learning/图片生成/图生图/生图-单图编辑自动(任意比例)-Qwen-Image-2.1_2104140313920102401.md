---
key: 图片生成/图生图/生图-单图编辑自动(任意比例)-Qwen-Image-2.1_2104140313920102401.json
name: 生图-单图编辑自动(任意比例)-Qwen-Image-2.1_2104140313920102401
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/生图-单图编辑自动(任意比例)-Qwen-Image-2.1_2104140313920102401.json
hash: aa1c56586e4dbe81
coverage: 0.923077
learned_at: 2026-10-21 00:55:07
nodes: [CLIPLoader, VAEDecode, GetImageSizeAndCount, SaveImage, PreviewImage, easy imageConcat, TextEncodeQwenImage21, KSampler, easy seed, CLIPLoader, TextGenerateLTX2Prompt, UNETLoader, VAELoader, GetImageSizeAndCount, easy int, EmptyLatentImage, LayerUtility: ImageScaleByAspectRatio V2, easy int, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, easy positive, easy anythingIndexSwitch, StringFunction|pysssss, easy showAnything, easy saveText, easy saveText]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 232571757838098, "steps": 40, "width": 1024}
---

# 图片生成/图生图/生图-单图编辑自动(任意比例)-Qwen-Image-2.1_2104140313920102401.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/生图-单图编辑自动(任意比例)-Qwen-Image-2.1_2104140313920102401.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `CLIPLoader`
- `VAEDecode` ★核心
- `GetImageSizeAndCount`
- `SaveImage`
- `PreviewImage`
- `easy imageConcat`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `easy seed`
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `UNETLoader` ★核心
- `VAELoader`
- `GetImageSizeAndCount`
- `easy int`
- `EmptyLatentImage` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `easy positive`
- `easy anythingIndexSwitch`
- `StringFunction|pysssss`
- `easy showAnything`
- `easy saveText`
- `easy saveText`

## 关键参数

- `seed` = `232571757838098`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（24/26）

**有卡**：`CLIPLoader`、`VAEDecode`、`GetImageSizeAndCount`、`SaveImage`、`easy imageConcat`、`TextEncodeQwenImage21`、`KSampler`、`easy seed`、`TextGenerateLTX2Prompt`、`UNETLoader`、`VAELoader`、`easy int`、`EmptyLatentImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`easy positive`、`easy anythingIndexSwitch`、`StringFunction|pysssss`、`easy saveText`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader
