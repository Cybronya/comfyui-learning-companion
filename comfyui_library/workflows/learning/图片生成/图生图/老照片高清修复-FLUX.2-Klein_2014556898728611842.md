---
key: 图片生成/图生图/老照片高清修复-FLUX.2-Klein_2014556898728611842.json
name: 老照片高清修复-FLUX.2-Klein_2014556898728611842
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/老照片高清修复-FLUX.2-Klein_2014556898728611842.json
hash: 4d9c816d3b2a15b1
coverage: 0.904762
learned_at: 2026-10-23 13:23:23
nodes: [ReferenceLatent, VAEEncode, ConditioningZeroOut, Image Comparer (rgthree), PrimitiveStringMultiline, ReferenceLatent, CLIPTextEncode, SaveImage, UNETLoader, CLIPLoader, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, SamplerCustomAdvanced, VAEDecode, PlaySound|pysssss, CFGGuider, KSamplerSelect, EmptyFlux2LatentImage, Flux2Scheduler, RandomNoise, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/老照片高清修复-FLUX.2-Klein_2014556898728611842.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/老照片高清修复-FLUX.2-Klein_2014556898728611842.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `PrimitiveStringMultiline`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `PlaySound|pysssss`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `RandomNoise`
- `LoadImage`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`ReferenceLatent`、`VAEEncode`、`ConditioningZeroOut`、`CLIPTextEncode`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`SamplerCustomAdvanced`、`VAEDecode`、`PlaySound|pysssss`、`CFGGuider`、`KSamplerSelect`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`RandomNoise`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
