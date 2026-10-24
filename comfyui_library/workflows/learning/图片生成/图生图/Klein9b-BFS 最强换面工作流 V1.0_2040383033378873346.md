---
key: 图片生成/图生图/Klein9b-BFS 最强换面工作流 V1.0_2040383033378873346.json
name: Klein9b-BFS 最强换面工作流 V1.0_2040383033378873346
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Klein9b-BFS 最强换面工作流 V1.0_2040383033378873346.json
hash: 1d5a8b55b51b90df
coverage: 0.962963
learned_at: 2026-10-23 11:04:46
nodes: [VAEEncode, ConditioningZeroOut, ReferenceLatent, Flux2Scheduler, KSamplerSelect, CFGGuider, RandomNoise, SamplerCustomAdvanced, LayerUtility: PurgeVRAM V2, CLIPLoader, GetImageSize, ReferenceLatent, ReferenceLatent, VAEEncode, VAELoader, ImageScaleToTotalPixels, ImageScaleToTotalPixels, Seed (rgthree), EmptyFlux2LatentImage, ReferenceLatent, CLIPTextEncode, VAEDecode, UNETLoader, Image Comparer (rgthree), SaveImage, LoadImage, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/Klein9b-BFS 最强换面工作流 V1.0_2040383033378873346.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Klein9b-BFS 最强换面工作流 V1.0_2040383033378873346.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `ReferenceLatent`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `CLIPLoader`
- `GetImageSize`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `VAELoader`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `Seed (rgthree)`
- `EmptyFlux2LatentImage`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **96%**（26/27）

**有卡**：`VAEEncode`、`ConditioningZeroOut`、`ReferenceLatent`、`Flux2Scheduler`、`KSamplerSelect`、`CFGGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`LayerUtility: PurgeVRAM V2`、`CLIPLoader`、`GetImageSize`、`VAELoader`、`ImageScaleToTotalPixels`、`Seed (rgthree)`、`EmptyFlux2LatentImage`、`CLIPTextEncode`、`VAEDecode`、`UNETLoader`、`SaveImage`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
