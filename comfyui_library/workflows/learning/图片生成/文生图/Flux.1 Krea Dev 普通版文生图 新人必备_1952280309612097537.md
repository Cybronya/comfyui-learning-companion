---
key: 图片生成/文生图/Flux.1 Krea Dev 普通版文生图 新人必备_1952280309612097537.json
name: Flux.1 Krea Dev 普通版文生图 新人必备_1952280309612097537
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1 Krea Dev 普通版文生图 新人必备_1952280309612097537.json
hash: 027d9253e29dd3cd
coverage: 0.695652
learned_at: 2026-10-15 22:26:25
nodes: [ShowText|pysssss, DeepTranslatorTextNode, Anything Everywhere, Seed Everywhere, ShowText|pysssss, StringFunction|pysssss, CLIPTextEncode, EmptyLatentImage, Anything Everywhere, ConditioningZeroOut, VAELoader, PreviewImage, DualCLIPLoader, Anything Everywhere3, ModelSamplingFlux, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler (Efficient), UNETLoader, SaveImage, LayerFilter: HDREffects, DeepTranslatorTextNode, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 535577283025654, "steps": 20, "width": 800}
---

# 图片生成/文生图/Flux.1 Krea Dev 普通版文生图 新人必备_1952280309612097537.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.1 Krea Dev 普通版文生图 新人必备_1952280309612097537.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Output → Other

**节点**（23 个）：
- `ShowText|pysssss`
- `DeepTranslatorTextNode`
- `Anything Everywhere`
- `Seed Everywhere`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `Anything Everywhere`
- `ConditioningZeroOut`
- `VAELoader`
- `PreviewImage`
- `DualCLIPLoader`
- `Anything Everywhere3`
- `ModelSamplingFlux`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler (Efficient)` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `LayerFilter: HDREffects`
- `DeepTranslatorTextNode`
- `Note`

## 关键参数

- `width` = `800`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `535577283025654`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **70%**（16/23）

**有卡**：`DeepTranslatorTextNode`、`Seed Everywhere`、`StringFunction|pysssss`、`CLIPTextEncode`、`EmptyLatentImage`、`ConditioningZeroOut`、`VAELoader`、`DualCLIPLoader`、`ModelSamplingFlux`、`LoraLoaderModelOnly`、`KSampler (Efficient)`、`UNETLoader`、`SaveImage`、`LayerFilter: HDREffects`

**用到的条目**：VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、KSampler (Efficient)、Seed Everywhere
