---
key: 图片生成/文生图/Flux.1 Krea Dev Nunchaku 文生图新人必备_1952287898248884225.json
name: Flux.1 Krea Dev Nunchaku 文生图新人必备_1952287898248884225
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1 Krea Dev Nunchaku 文生图新人必备_1952287898248884225.json
hash: adc73bc3fb5289cf
coverage: 0.727273
learned_at: 2026-10-15 22:26:25
nodes: [ShowText|pysssss, DeepTranslatorTextNode, Anything Everywhere, Anything Everywhere3, Seed Everywhere, ShowText|pysssss, StringFunction|pysssss, CLIPTextEncode, EmptyLatentImage, Anything Everywhere, KSampler (Efficient), ConditioningZeroOut, NunchakuTextEncoderLoaderV2, VAELoader, DeepTranslatorTextNode, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuFluxLoraLoader, ModelSamplingFlux, LayerFilter: HDREffects, SaveImage, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "normal", "seed": 535577283025654, "steps": 30, "width": 800}
---

# 图片生成/文生图/Flux.1 Krea Dev Nunchaku 文生图新人必备_1952287898248884225.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.1 Krea Dev Nunchaku 文生图新人必备_1952287898248884225.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Output → Other

**节点**（22 个）：
- `ShowText|pysssss`
- `DeepTranslatorTextNode`
- `Anything Everywhere`
- `Anything Everywhere3`
- `Seed Everywhere`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `Anything Everywhere`
- `KSampler (Efficient)` ★核心
- `ConditioningZeroOut`
- `NunchakuTextEncoderLoaderV2`
- `VAELoader`
- `DeepTranslatorTextNode`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxLoraLoader` ★核心
- `ModelSamplingFlux`
- `LayerFilter: HDREffects`
- `SaveImage`
- `Note`

## 关键参数

- `width` = `800`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `535577283025654`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **73%**（16/22）

**有卡**：`DeepTranslatorTextNode`、`Seed Everywhere`、`StringFunction|pysssss`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler (Efficient)`、`ConditioningZeroOut`、`NunchakuTextEncoderLoaderV2`、`VAELoader`、`NunchakuFluxDiTLoader`、`NunchakuFluxLoraLoader`、`ModelSamplingFlux`、`LayerFilter: HDREffects`、`SaveImage`

**用到的条目**：VAELoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、KSampler (Efficient)、Seed Everywhere、NunchakuTextEncoderLoaderV2、NunchakuFluxLoraLoader
