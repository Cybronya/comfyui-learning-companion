---
key: 图片生成/图生图/FLUX.2-KLEIN-双图编辑-高清直出_2019989419784146946.json
name: FLUX.2-KLEIN-双图编辑-高清直出_2019989419784146946
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2-KLEIN-双图编辑-高清直出_2019989419784146946.json
hash: c11e22783429e8f2
coverage: 1
learned_at: 2026-10-23 10:54:11
nodes: [KSamplerSelect, CFGGuider, RandomNoise, Flux2Scheduler, EmptyFlux2LatentImage, VAELoader, ImageResizeKJv2, GetImageSize, ReferenceLatent, VAEEncode, ReferenceLatent, ReferenceLatent, ReferenceLatent, ConditioningZeroOut, VAEEncode, SamplerCustomAdvanced, VAEDecode, SaveImage, CLIPTextEncode, CLIPLoader, UNETLoader, Label (rgthree), LoadImage, ImageResizeKJv2, Text, SaveImage, LayerUtility: PurgeVRAM V2, SeedVR2, CustomAddLabel, SaveImage, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.2-KLEIN-双图编辑-高清直出_2019989419784146946.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2-KLEIN-双图编辑-高清直出_2019989419784146946.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `KSamplerSelect` ★核心
- `CFGGuider`
- `RandomNoise`
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `VAELoader`
- `ImageResizeKJv2`
- `GetImageSize`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `Label (rgthree)`
- `LoadImage`
- `ImageResizeKJv2`
- `Text`
- `SaveImage`
- `LayerUtility: PurgeVRAM V2`
- `SeedVR2`
- `CustomAddLabel`
- `SaveImage`
- `LoadImage`

## 知识

覆盖率 **100%**（31/31）

**有卡**：`KSamplerSelect`、`CFGGuider`、`RandomNoise`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`VAELoader`、`ImageResizeKJv2`、`GetImageSize`、`ReferenceLatent`、`VAEEncode`、`ConditioningZeroOut`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`CLIPLoader`、`UNETLoader`、`Label (rgthree)`、`LoadImage`、`Text`、`LayerUtility: PurgeVRAM V2`、`SeedVR2`、`CustomAddLabel`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
