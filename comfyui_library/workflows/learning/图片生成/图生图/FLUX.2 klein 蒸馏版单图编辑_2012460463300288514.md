---
key: 图片生成/图生图/FLUX.2 klein 蒸馏版单图编辑_2012460463300288514.json
name: FLUX.2 klein 蒸馏版单图编辑_2012460463300288514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2 klein 蒸馏版单图编辑_2012460463300288514.json
hash: 79ef55be908ace1b
coverage: 0.95
learned_at: 2026-10-23 10:54:07
nodes: [CLIPLoader, UNETLoader, VAELoader, ConditioningZeroOut, ReferenceLatent, VAEDecode, VAEEncode, ImageScaleToTotalPixels, KSamplerSelect, RandomNoise, Flux2Scheduler, CFGGuider, SamplerCustomAdvanced, CLIPTextEncode, GetImageSize, EmptyFlux2LatentImage, ReferenceLatent, LoadImage, SaveImage, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.2 klein 蒸馏版单图编辑_2012460463300288514.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2 klein 蒸馏版单图编辑_2012460463300288514.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `Flux2Scheduler`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `GetImageSize`
- `EmptyFlux2LatentImage`
- `ReferenceLatent`
- `LoadImage`
- `SaveImage`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`CLIPLoader`、`UNETLoader`、`VAELoader`、`ConditioningZeroOut`、`ReferenceLatent`、`VAEDecode`、`VAEEncode`、`ImageScaleToTotalPixels`、`KSamplerSelect`、`RandomNoise`、`Flux2Scheduler`、`CFGGuider`、`SamplerCustomAdvanced`、`CLIPTextEncode`、`GetImageSize`、`EmptyFlux2LatentImage`、`LoadImage`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
