---
key: 图片生成/图生图/Flux.1 IPAdapter 风格迁移_1994257493721284609.json
name: Flux.1 IPAdapter 风格迁移_1994257493721284609
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.1 IPAdapter 风格迁移_1994257493721284609.json
hash: 9f69711ddd46a9b1
coverage: 1
learned_at: 2026-10-23 10:58:39
nodes: [DualCLIPLoader, UNETLoader, EmptySD3LatentImage, VAEDecode, CLIPTextEncode, VAELoader, ApplyIPAdapterFlux, RH_Translator, LoadImage, IPAdapterFluxLoader, ConditioningZeroOut, KSampler, SaveImage, LoraLoaderModelOnly, ModelSamplingFlux]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 928073390997800, "steps": 30}
---

# 图片生成/图生图/Flux.1 IPAdapter 风格迁移_1994257493721284609.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.1 IPAdapter 风格迁移_1994257493721284609.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ApplyIPAdapterFlux`
- `RH_Translator`
- `LoadImage`
- `IPAdapterFluxLoader`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingFlux`

## 关键参数

- `seed` = `928073390997800`
- `steps` = `30`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`DualCLIPLoader`、`UNETLoader`、`EmptySD3LatentImage`、`VAEDecode`、`CLIPTextEncode`、`VAELoader`、`ApplyIPAdapterFlux`、`RH_Translator`、`LoadImage`、`IPAdapterFluxLoader`、`ConditioningZeroOut`、`KSampler`、`SaveImage`、`LoraLoaderModelOnly`、`ModelSamplingFlux`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
