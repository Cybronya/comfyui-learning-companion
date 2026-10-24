---
key: 图片生成/图生图/FLUX.2 klein 蒸馏版双图编辑_2012462098781052930.json
name: FLUX.2 klein 蒸馏版双图编辑_2012462098781052930
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2 klein 蒸馏版双图编辑_2012462098781052930.json
hash: 3ebf341fc8de2f6e
coverage: 0.96
learned_at: 2026-10-23 10:54:08
nodes: [CLIPLoader, KSamplerSelect, ReferenceLatent, ReferenceLatent, ConditioningZeroOut, ImageScaleToTotalPixels, GetImageSize, ReferenceLatent, ReferenceLatent, ImageScaleToTotalPixels, VAEEncode, SamplerCustomAdvanced, Flux2Scheduler, VAEDecode, CFGGuider, EmptyFlux2LatentImage, VAEEncode, RandomNoise, CLIPTextEncode, LoadImage, LoadImage, PrimitiveStringMultiline, UNETLoader, VAELoader, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.2 klein 蒸馏版双图编辑_2012462098781052930.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2 klein 蒸馏版双图编辑_2012462098781052930.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `ReferenceLatent`
- `ReferenceLatent`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `Flux2Scheduler`
- `VAEDecode` ★核心
- `CFGGuider`
- `EmptyFlux2LatentImage`
- `VAEEncode` ★核心
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `VAELoader`
- `SaveImage`

## 知识

覆盖率 **96%**（24/25）

**有卡**：`CLIPLoader`、`KSamplerSelect`、`ReferenceLatent`、`ConditioningZeroOut`、`ImageScaleToTotalPixels`、`GetImageSize`、`VAEEncode`、`SamplerCustomAdvanced`、`Flux2Scheduler`、`VAEDecode`、`CFGGuider`、`EmptyFlux2LatentImage`、`RandomNoise`、`CLIPTextEncode`、`LoadImage`、`UNETLoader`、`VAELoader`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
