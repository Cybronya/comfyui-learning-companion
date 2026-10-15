---
key: 图片生成/文生图/Flux.1 Krea Dev Nunchaku图生图  新人必备_1952289860134621185.json
name: Flux.1 Krea Dev Nunchaku图生图  新人必备_1952289860134621185
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1 Krea Dev Nunchaku图生图  新人必备_1952289860134621185.json
hash: dc61097e1a12f9a6
coverage: 0.73913
learned_at: 2026-10-15 22:26:25
nodes: [ShowText|pysssss, DeepTranslatorTextNode, Anything Everywhere, Anything Everywhere3, Seed Everywhere, ShowText|pysssss, StringFunction|pysssss, CLIPTextEncode, ConditioningZeroOut, NunchakuTextEncoderLoaderV2, VAELoader, Anything Everywhere, VAEEncode, DeepTranslatorTextNode, KSampler (Efficient), ModelSamplingFlux, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuFluxLoraLoader, LayerFilter: HDREffects, SaveImage, LoadImage, Note]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.7000000000000002, "sampler_name": "euler", "scheduler": "normal", "seed": 535577283025654, "steps": 30}
---

# 图片生成/文生图/Flux.1 Krea Dev Nunchaku图生图  新人必备_1952289860134621185.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.1 Krea Dev Nunchaku图生图  新人必备_1952289860134621185.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Output → Other

**节点**（23 个）：
- `ShowText|pysssss`
- `DeepTranslatorTextNode`
- `Anything Everywhere`
- `Anything Everywhere3`
- `Seed Everywhere`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `NunchakuTextEncoderLoaderV2`
- `VAELoader`
- `Anything Everywhere`
- `VAEEncode` ★核心
- `DeepTranslatorTextNode`
- `KSampler (Efficient)` ★核心
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxLoraLoader` ★核心
- `LayerFilter: HDREffects`
- `SaveImage`
- `LoadImage`
- `Note`

## 关键参数

- `seed` = `535577283025654`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `0.7000000000000002`

## 知识

覆盖率 **74%**（17/23）

**有卡**：`DeepTranslatorTextNode`、`Seed Everywhere`、`StringFunction|pysssss`、`CLIPTextEncode`、`ConditioningZeroOut`、`NunchakuTextEncoderLoaderV2`、`VAELoader`、`VAEEncode`、`KSampler (Efficient)`、`ModelSamplingFlux`、`NunchakuFluxDiTLoader`、`NunchakuFluxLoraLoader`、`LayerFilter: HDREffects`、`SaveImage`、`LoadImage`

**用到的条目**：VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、KSampler (Efficient)、Seed Everywhere、VAEEncode、NunchakuTextEncoderLoaderV2
