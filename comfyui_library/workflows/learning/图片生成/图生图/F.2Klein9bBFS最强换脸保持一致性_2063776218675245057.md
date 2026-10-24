---
key: 图片生成/图生图/F.2Klein9bBFS最强换脸保持一致性_2063776218675245057.json
name: F.2Klein9bBFS最强换脸保持一致性_2063776218675245057
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2Klein9bBFS最强换脸保持一致性_2063776218675245057.json
hash: 1321a0d2136a64aa
coverage: 0.9
learned_at: 2026-10-23 10:52:42
nodes: [VAEEncode, ConditioningZeroOut, ReferenceLatent, Flux2Scheduler, KSamplerSelect, CFGGuider, RandomNoise, SamplerCustomAdvanced, LayerUtility: PurgeVRAM V2, SaveImage, CLIPLoader, GetImageSize, ReferenceLatent, ReferenceLatent, VAEEncode, VAELoader, Seed (rgthree), EmptyFlux2LatentImage, ReferenceLatent, CLIPTextEncode, LoadImage, LoadImage, UNETLoader, PreviewAny, ImageScaleToTotalPixels, Image Comparer (rgthree), VAEDecode, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, Int]
patterns: []
missing: []
---

# 图片生成/图生图/F.2Klein9bBFS最强换脸保持一致性_2063776218675245057.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2Klein9bBFS最强换脸保持一致性_2063776218675245057.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `ReferenceLatent`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `SaveImage`
- `CLIPLoader`
- `GetImageSize`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `VAELoader`
- `Seed (rgthree)`
- `EmptyFlux2LatentImage`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `PreviewAny`
- `ImageScaleToTotalPixels`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`

## 知识

覆盖率 **90%**（27/30）

**有卡**：`VAEEncode`、`ConditioningZeroOut`、`ReferenceLatent`、`Flux2Scheduler`、`KSamplerSelect`、`CFGGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`LayerUtility: PurgeVRAM V2`、`SaveImage`、`CLIPLoader`、`GetImageSize`、`VAELoader`、`Seed (rgthree)`、`EmptyFlux2LatentImage`、`CLIPTextEncode`、`LoadImage`、`UNETLoader`、`ImageScaleToTotalPixels`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
