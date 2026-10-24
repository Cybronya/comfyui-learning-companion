---
key: 图片生成/图生图/组件系列8-FLUX.2-Klein单图编辑_2058753653384765441.json
name: 组件系列8-FLUX.2-Klein单图编辑_2058753653384765441
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/组件系列8-FLUX.2-Klein单图编辑_2058753653384765441.json
hash: bd4669f57cc69706
coverage: 0.826087
learned_at: 2026-10-23 13:21:34
nodes: [UNETLoader, VAELoader, CLIPLoader, ReferenceLatent, Seed (rgthree), RandomNoise, ConditioningZeroOut, CLIPTextEncode, ReferenceLatent, CFGGuider, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, SamplerCustomAdvanced, Flux2Scheduler, VAEEncode, LoadImage, Text, SetNode, GetNode, VAEDecode, Image Comparer (rgthree), SaveImage, PreviewImage]
patterns: []
missing: []
---

# 图片生成/图生图/组件系列8-FLUX.2-Klein单图编辑_2058753653384765441.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/组件系列8-FLUX.2-Klein单图编辑_2058753653384765441.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `ReferenceLatent`
- `Seed (rgthree)`
- `RandomNoise`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SamplerCustomAdvanced` ★核心
- `Flux2Scheduler`
- `VAEEncode` ★核心
- `LoadImage`
- `Text`
- `SetNode`
- `GetNode`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `PreviewImage`

## 知识

覆盖率 **83%**（19/23）

**有卡**：`UNETLoader`、`VAELoader`、`CLIPLoader`、`ReferenceLatent`、`Seed (rgthree)`、`RandomNoise`、`ConditioningZeroOut`、`CLIPTextEncode`、`CFGGuider`、`KSamplerSelect`、`LayerUtility: ImageScaleByAspectRatio V2`、`SamplerCustomAdvanced`、`Flux2Scheduler`、`VAEEncode`、`LoadImage`、`Text`、`VAEDecode`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
