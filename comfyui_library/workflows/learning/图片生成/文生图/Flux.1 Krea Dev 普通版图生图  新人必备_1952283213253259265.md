---
key: 图片生成/文生图/Flux.1 Krea Dev 普通版图生图  新人必备_1952283213253259265.json
name: Flux.1 Krea Dev 普通版图生图  新人必备_1952283213253259265
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1 Krea Dev 普通版图生图  新人必备_1952283213253259265.json
hash: 00de43d0fe215fd3
coverage: 0.708333
learned_at: 2026-10-15 22:26:25
nodes: [ShowText|pysssss, DeepTranslatorTextNode, Anything Everywhere, Seed Everywhere, ShowText|pysssss, StringFunction|pysssss, CLIPTextEncode, Anything Everywhere, ConditioningZeroOut, VAELoader, PreviewImage, DualCLIPLoader, Anything Everywhere3, ModelSamplingFlux, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, VAEEncode, KSampler (Efficient), DeepTranslatorTextNode, LoadImage, SaveImage, LayerFilter: HDREffects, Note]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.8500000000000002, "sampler_name": "euler", "scheduler": "simple", "seed": 905108107799393, "steps": 20}
---

# 图片生成/文生图/Flux.1 Krea Dev 普通版图生图  新人必备_1952283213253259265.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.1 Krea Dev 普通版图生图  新人必备_1952283213253259265.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Output → Other

**节点**（24 个）：
- `ShowText|pysssss`
- `DeepTranslatorTextNode`
- `Anything Everywhere`
- `Seed Everywhere`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `CLIPTextEncode` ★核心
- `Anything Everywhere`
- `ConditioningZeroOut`
- `VAELoader`
- `PreviewImage`
- `DualCLIPLoader`
- `Anything Everywhere3`
- `ModelSamplingFlux`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `KSampler (Efficient)` ★核心
- `DeepTranslatorTextNode`
- `LoadImage`
- `SaveImage`
- `LayerFilter: HDREffects`
- `Note`

## 关键参数

- `seed` = `905108107799393`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.8500000000000002`

## 知识

覆盖率 **71%**（17/24）

**有卡**：`DeepTranslatorTextNode`、`Seed Everywhere`、`StringFunction|pysssss`、`CLIPTextEncode`、`ConditioningZeroOut`、`VAELoader`、`DualCLIPLoader`、`ModelSamplingFlux`、`LoraLoaderModelOnly`、`UNETLoader`、`VAEEncode`、`KSampler (Efficient)`、`LoadImage`、`SaveImage`、`LayerFilter: HDREffects`

**用到的条目**：VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、KSampler (Efficient)、Seed Everywhere
