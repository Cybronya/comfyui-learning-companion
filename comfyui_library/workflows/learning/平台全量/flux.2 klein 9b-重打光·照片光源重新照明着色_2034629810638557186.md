---
key: 平台全量/flux.2 klein 9b-重打光·照片光源重新照明着色_2034629810638557186.json
name: flux.2 klein 9b-重打光·照片光源重新照明着色_2034629810638557186
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/flux.2 klein 9b-重打光·照片光源重新照明着色_2034629810638557186.json
hash: 52b98371b8dd59cc
coverage: 0.657143
learned_at: 2026-11-14 01:10:59
nodes: [Anything Everywhere, KSamplerSelect, VAELoader, CLIPLoader, EmptyFlux2LatentImage, ReferenceLatent, VAEEncode, RepeatLatentBatch, Flux2Scheduler, Anything Everywhere, ConditioningZeroOut, GetImageSize, CFGGuider, UNETLoader, CFGGuider, RandomNoise, Anything Everywhere, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, Image Comparer (rgthree), GetNode, CLIPTextEncode, RebatchLatents, SamplerCustomAdvanced, SetNode, LoraLoaderModelOnly, SaveImage, easy showAnything, SetNode, ImpactSwitch, GetNode, LoadImage, QwenMultiangleLightningNode]
patterns: []
missing: []
---

# 平台全量/flux.2 klein 9b-重打光·照片光源重新照明着色_2034629810638557186.json

> 来源文件 `comfyui_library/workflows/平台全量/flux.2 klein 9b-重打光·照片光源重新照明着色_2034629810638557186.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `Anything Everywhere`
- `KSamplerSelect` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyFlux2LatentImage`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `RepeatLatentBatch`
- `Flux2Scheduler`
- `Anything Everywhere`
- `ConditioningZeroOut`
- `GetImageSize`
- `CFGGuider`
- `UNETLoader` ★核心
- `CFGGuider`
- `RandomNoise`
- `Anything Everywhere`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `Image Comparer (rgthree)`
- `GetNode`
- `CLIPTextEncode` ★核心
- `RebatchLatents`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `easy showAnything`
- `SetNode`
- `ImpactSwitch`
- `GetNode`
- `LoadImage`
- `QwenMultiangleLightningNode`

## 知识

覆盖率 **66%**（23/35）

**有卡**：`KSamplerSelect`、`VAELoader`、`CLIPLoader`、`EmptyFlux2LatentImage`、`ReferenceLatent`、`VAEEncode`、`RepeatLatentBatch`、`Flux2Scheduler`、`ConditioningZeroOut`、`GetImageSize`、`CFGGuider`、`UNETLoader`、`RandomNoise`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`RebatchLatents`、`SamplerCustomAdvanced`、`LoraLoaderModelOnly`、`SaveImage`、`LoadImage`、`QwenMultiangleLightningNode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
