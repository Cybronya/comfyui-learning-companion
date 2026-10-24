---
key: 图片生成/图生图/人物换脸，开源顶级一致性flux.2 klein_2016441047668236290.json
name: 人物换脸，开源顶级一致性flux.2 klein_2016441047668236290
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/人物换脸，开源顶级一致性flux.2 klein_2016441047668236290.json
hash: 61a8d420a1c5bcf0
coverage: 0.96
learned_at: 2026-10-23 12:10:38
nodes: [KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, VAEEncode, SamplerCustomAdvanced, VAEEncode, CFGGuider, RandomNoise, VAEDecode, ConditioningZeroOut, ReferenceLatent, ReferenceLatent, CLIPTextEncode, ReferenceLatent, LoadImage, SaveImage, Image Comparer (rgthree), LoraLoaderModelOnly, CLIPLoader, VAELoader, Get Image Size, LoadImage, RHHiddenNodes, UNETLoader, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/人物换脸，开源顶级一致性flux.2 klein_2016441047668236290.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/人物换脸，开源顶级一致性flux.2 klein_2016441047668236290.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `VAEEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `CFGGuider`
- `RandomNoise`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `ReferenceLatent`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `LoadImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `Get Image Size`
- `LoadImage`
- `RHHiddenNodes`
- `UNETLoader` ★核心
- `LoadImage`

## 知识

覆盖率 **96%**（24/25）

**有卡**：`KSamplerSelect`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`VAEEncode`、`SamplerCustomAdvanced`、`CFGGuider`、`RandomNoise`、`VAEDecode`、`ConditioningZeroOut`、`ReferenceLatent`、`CLIPTextEncode`、`LoadImage`、`SaveImage`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`Get Image Size`、`RHHiddenNodes`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
