---
key: 图片生成/文生图/一键运行：Flux-Dev-SRPO-v1-fp8.safetensors文生图_1968862294623100929.json
name: 一键运行：Flux-Dev-SRPO-v1-fp8.safetensors文生图_1968862294623100929.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/一键运行：Flux-Dev-SRPO-v1-fp8.safetensors文生图_1968862294623100929.json
hash: 924dfeb4a51d06be
coverage: 0.578947
learned_at: 2026-10-09 02:01:38
nodes: [ShowText|pysssss, DeepTranslatorTextNode, ShowText|pysssss, EmptyLatentImage, Anything Everywhere, ConditioningZeroOut, PreviewImage, NunchakuFluxLoraLoader, CLIPTextEncode, DeepTranslatorTextNode, KSampler (Efficient), ModelSamplingFlux, DualCLIPLoader, Anything Everywhere, VAELoader, UNETLoader, Note, SaveImage, LayerFilter: HDREffects]
patterns: []
missing: [LayerFilter: HDREffects, KSampler (Efficient)]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "normal", "seed": 118556035633740, "steps": 30, "width": 800}
discoveries: [次要节点 `LayerFilter: HDREffects` 知识库中没有该节点类型的任何知识, 核心节点 `KSampler (Efficient)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/一键运行：Flux-Dev-SRPO-v1-fp8.safetensors文生图_1968862294623100929.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1968862294623100929.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Output → Other

**节点**（19 个）：
- `ShowText|pysssss`
- `DeepTranslatorTextNode`
- `ShowText|pysssss`
- `EmptyLatentImage` ★核心
- `Anything Everywhere`
- `ConditioningZeroOut`
- `PreviewImage`
- `NunchakuFluxLoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `DeepTranslatorTextNode`
- `KSampler (Efficient)` ★核心
- `ModelSamplingFlux`
- `DualCLIPLoader`
- `Anything Everywhere`
- `VAELoader`
- `UNETLoader` ★核心
- `Note`
- `SaveImage`
- `LayerFilter: HDREffects`

## 关键参数

- `width` = `800`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `118556035633740`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **58%**（11/19）

**有卡**：`DeepTranslatorTextNode`、`EmptyLatentImage`、`ConditioningZeroOut`、`NunchakuFluxLoraLoader`、`CLIPTextEncode`、`ModelSamplingFlux`、`DualCLIPLoader`、`VAELoader`、`UNETLoader`、`SaveImage`

**缺卡**（2）：`LayerFilter: HDREffects`、`KSampler (Efficient)`

**用到的条目**：VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、NunchakuFluxLoraLoader、DualCLIPLoader、ModelSamplingFlux

## 学习发现

- 次要节点 `LayerFilter: HDREffects` 知识库中没有该节点类型的任何知识
- 核心节点 `KSampler (Efficient)` 仅有 KSampler 的通用知识，没有该节点自己的说明
