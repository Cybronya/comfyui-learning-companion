---
key: 平台全量/人像精修-原生肌肤 qwen_image_2.1_1900186985972101122.json
name: 人像精修-原生肌肤 qwen_image_2.1_1900186985972101122
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/人像精修-原生肌肤 qwen_image_2.1_1900186985972101122.json
hash: 72481a9718be41b9
coverage: 0.733333
learned_at: 2026-11-14 01:36:26
nodes: [CLIPLoader, QwenImage21Cache, VAEDecode, UNETLoader, CR Text Concatenate, JjkText, ShowText|pysssss, TextEncodeQwenImage21, VAELoader, JjkText, KSampler, Image Comparer (rgthree), LoraLoaderModelOnly, LoadImage, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 721602398745282, "steps": 40}
---

# 平台全量/人像精修-原生肌肤 qwen_image_2.1_1900186985972101122.json

> 来源文件 `comfyui_library/workflows/平台全量/人像精修-原生肌肤 qwen_image_2.1_1900186985972101122.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（15 个）：
- `CLIPLoader`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CR Text Concatenate`
- `JjkText`
- `ShowText|pysssss`
- `TextEncodeQwenImage21`
- `VAELoader`
- `JjkText`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `SaveImage`

## 关键参数

- `seed` = `721602398745282`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **73%**（11/15）

**有卡**：`CLIPLoader`、`QwenImage21Cache`、`VAEDecode`、`UNETLoader`、`CR Text Concatenate`、`TextEncodeQwenImage21`、`VAELoader`、`KSampler`、`LoraLoaderModelOnly`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache
