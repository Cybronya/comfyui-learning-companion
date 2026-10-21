---
key: 图片生成/文生图/节点系列04-Fast Groups Bypasser (rgthree)节点介绍_2028724362504839170.json
name: 节点系列04-Fast Groups Bypasser (rgthree)节点介绍_2028724362504839170
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/节点系列04-Fast Groups Bypasser (rgthree)节点介绍_2028724362504839170.json
hash: 0a28bd2d7659d016
coverage: 0.793103
learned_at: 2026-10-20 23:22:19
nodes: [VAELoader, CLIPLoader, CLIPTextEncode, UNETLoader, Image Comparer (rgthree), ConditioningZeroOut, ReferenceLatent, ReferenceLatent, VAEEncode, RandomNoise, CFGGuider, KSamplerSelect, Flux2Scheduler, SamplerCustomAdvanced, Text, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Note, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), SeedVR2LoadDiTModel, VAEDecode, easy cleanGpuUsed, PreviewImage, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SaveImage, Fast Groups Muter (rgthree)]
patterns: []
missing: []
---

# 图片生成/文生图/节点系列04-Fast Groups Bypasser (rgthree)节点介绍_2028724362504839170.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/节点系列04-Fast Groups Bypasser (rgthree)节点介绍_2028724362504839170.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `Image Comparer (rgthree)`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `SamplerCustomAdvanced` ★核心
- `Text`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `SeedVR2LoadDiTModel`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `PreviewImage`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `Fast Groups Muter (rgthree)`

## 知识

覆盖率 **79%**（23/29）

**有卡**：`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`UNETLoader`、`ConditioningZeroOut`、`ReferenceLatent`、`VAEEncode`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`Flux2Scheduler`、`SamplerCustomAdvanced`、`Text`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`SeedVR2LoadDiTModel`、`VAEDecode`、`easy cleanGpuUsed`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
