---
key: 图片生成/文生图/生图-海报生成自动-Qwen-Image-2.1_2110189318915575810.json
name: 生图-海报生成自动-Qwen-Image-2.1_2110189318915575810
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/生图-海报生成自动-Qwen-Image-2.1_2110189318915575810.json
hash: cc33555b3d7f67de
coverage: 0.833333
learned_at: 2026-10-21 03:01:56
nodes: [easy int, EmptyImage, easy showAnything, UNETLoader, TextEncodeQwenImage21, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, ImpactInt, ImpactInt, CLIPLoader, easy showAnything, SetNode, easy saveText, StringFunction|pysssss, GetImageSizeAndCount, easy showAnything, SaveImage, RH_LLMAPI_NODE, StringFunction|pysssss, Text Multiline, easy seed, easy showAnything, easy positive, KSampler, TextGenerateLTX2Prompt, easy int, easy int, easy anythingIndexSwitch]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 146783941371260, "steps": 50, "width": 1024}
---

# 图片生成/文生图/生图-海报生成自动-Qwen-Image-2.1_2110189318915575810.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/生图-海报生成自动-Qwen-Image-2.1_2110189318915575810.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `easy int`
- `EmptyImage`
- `easy showAnything`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `ImpactInt`
- `ImpactInt`
- `CLIPLoader`
- `easy showAnything`
- `SetNode`
- `easy saveText`
- `StringFunction|pysssss`
- `GetImageSizeAndCount`
- `easy showAnything`
- `SaveImage`
- `RH_LLMAPI_NODE`
- `StringFunction|pysssss`
- `Text Multiline`
- `easy seed`
- `easy showAnything`
- `easy positive`
- `KSampler` ★核心
- `TextGenerateLTX2Prompt`
- `easy int`
- `easy int`
- `easy anythingIndexSwitch`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `146783941371260`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（25/30）

**有卡**：`easy int`、`EmptyImage`、`UNETLoader`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`ImpactInt`、`easy saveText`、`StringFunction|pysssss`、`GetImageSizeAndCount`、`SaveImage`、`RH_LLMAPI_NODE`、`Text Multiline`、`easy seed`、`easy positive`、`KSampler`、`TextGenerateLTX2Prompt`、`easy anythingIndexSwitch`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、UNETLoader、easy seed
