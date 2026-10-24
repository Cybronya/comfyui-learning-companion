---
key: 图片生成/图生图/FLUX.2-KLEIN-单图编辑-高清直出_2019989626764664833.json
name: FLUX.2-KLEIN-单图编辑-高清直出_2019989626764664833
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2-KLEIN-单图编辑-高清直出_2019989626764664833.json
hash: e0904a3bf12e2703
coverage: 1
learned_at: 2026-10-23 10:54:11
nodes: [RandomNoise, KSamplerSelect, Flux2Scheduler, CFGGuider, ReferenceLatent, ReferenceLatent, VAEEncode, ConditioningZeroOut, ImageResizeKJv2, Text, CLIPTextEncode, VAELoader, GetImageSize, EmptyFlux2LatentImage, SamplerCustomAdvanced, VAEDecode, LayerUtility: PurgeVRAM V2, SaveImage, Label (rgthree), CLIPLoader, UNETLoader, SaveImage, SaveImage, SeedVR2, CustomAddLabel, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.2-KLEIN-单图编辑-高清直出_2019989626764664833.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2-KLEIN-单图编辑-高清直出_2019989626764664833.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `RandomNoise`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `CFGGuider`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `ImageResizeKJv2`
- `Text`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `GetImageSize`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `SaveImage`
- `Label (rgthree)`
- `CLIPLoader`
- `UNETLoader` ★核心
- `SaveImage`
- `SaveImage`
- `SeedVR2`
- `CustomAddLabel`
- `LoadImage`

## 知识

覆盖率 **100%**（26/26）

**有卡**：`RandomNoise`、`KSamplerSelect`、`Flux2Scheduler`、`CFGGuider`、`ReferenceLatent`、`VAEEncode`、`ConditioningZeroOut`、`ImageResizeKJv2`、`Text`、`CLIPTextEncode`、`VAELoader`、`GetImageSize`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`SaveImage`、`Label (rgthree)`、`CLIPLoader`、`UNETLoader`、`SeedVR2`、`CustomAddLabel`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
