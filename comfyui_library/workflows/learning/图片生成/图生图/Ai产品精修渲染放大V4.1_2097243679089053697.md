---
key: 图片生成/图生图/Ai产品精修渲染放大V4.1_2097243679089053697.json
name: Ai产品精修渲染放大V4.1_2097243679089053697
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Ai产品精修渲染放大V4.1_2097243679089053697.json
hash: 7fe9204cc8af8922
coverage: 0.952381
learned_at: 2026-10-21 00:38:43
nodes: [UNETLoader, CLIPLoader, VAELoader, ReferenceLatent, Flux2Scheduler, GetImageSize, LoadImage, Image Comparer (rgthree), SaveImage, ConstrainImage|pysssss, VAEDecode, EmptyFlux2LatentImage, LoraLoaderModelOnly, ConditioningZeroOut, SamplerCustomAdvanced, RandomNoise, CFGGuider, KSamplerSelect, CLIPTextEncode, VAEEncode, ReferenceLatent]
patterns: []
missing: []
---

# 图片生成/图生图/Ai产品精修渲染放大V4.1_2097243679089053697.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Ai产品精修渲染放大V4.1_2097243679089053697.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ReferenceLatent`
- `Flux2Scheduler`
- `GetImageSize`
- `LoadImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `ConstrainImage|pysssss`
- `VAEDecode` ★核心
- `EmptyFlux2LatentImage`
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`ReferenceLatent`、`Flux2Scheduler`、`GetImageSize`、`LoadImage`、`SaveImage`、`ConstrainImage|pysssss`、`VAEDecode`、`EmptyFlux2LatentImage`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`SamplerCustomAdvanced`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`CLIPTextEncode`、`VAEEncode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
