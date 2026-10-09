---
key: 图片生成/文生图/Flux.1 Krea Dev 普通版图生图  新人必备_1952283213253259265.json
name: Flux.1 Krea Dev 普通版图生图  新人必备_1952283213253259265.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1 Krea Dev 普通版图生图  新人必备_1952283213253259265.json
hash: 00de43d0fe215fd3
coverage: 0.541667
learned_at: 2026-10-07 23:04:39
nodes: [ShowText|pysssss, DeepTranslatorTextNode, Anything Everywhere, Seed Everywhere, ShowText|pysssss, StringFunction|pysssss, CLIPTextEncode, Anything Everywhere, ConditioningZeroOut, VAELoader, PreviewImage, DualCLIPLoader, Anything Everywhere3, ModelSamplingFlux, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, VAEEncode, KSampler (Efficient), DeepTranslatorTextNode, LoadImage, SaveImage, LayerFilter: HDREffects, Note]
patterns: []
missing: [LayerFilter: HDREffects, StringFunction|pysssss, KSampler (Efficient), Seed Everywhere]
parameters: {"cfg": 1, "denoise": 0.8500000000000002, "sampler_name": "euler", "scheduler": "simple", "seed": 905108107799393, "steps": 20}
discoveries: [次要节点 `LayerFilter: HDREffects` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 核心节点 `KSampler (Efficient)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Flux.1 Krea Dev 普通版图生图  新人必备_1952283213253259265.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1952283213253259265.json`

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

覆盖率 **54%**（13/24）

**有卡**：`DeepTranslatorTextNode`、`CLIPTextEncode`、`ConditioningZeroOut`、`VAELoader`、`DualCLIPLoader`、`ModelSamplingFlux`、`LoraLoaderModelOnly`、`UNETLoader`、`VAEEncode`、`LoadImage`、`SaveImage`

**缺卡**（4）：`LayerFilter: HDREffects`、`StringFunction|pysssss`、`KSampler (Efficient)`、`Seed Everywhere`

**用到的条目**：VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、VAEEncode、DualCLIPLoader

## 学习发现

- 次要节点 `LayerFilter: HDREffects` 知识库中没有该节点类型的任何知识
- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
- 核心节点 `KSampler (Efficient)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明
