---
key: 平台全量/flux.2 klein 9b-重打光·照片光源重新照明着色_2027329955582976001.json
name: flux.2 klein 9b-重打光·照片光源重新照明着色_2027329955582976001
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/flux.2 klein 9b-重打光·照片光源重新照明着色_2027329955582976001.json
hash: 1f378abca666b944
coverage: 0.666667
learned_at: 2026-11-14 01:10:59
nodes: [Anything Everywhere, KSamplerSelect, VAELoader, CLIPLoader, EmptyFlux2LatentImage, ReferenceLatent, VAEEncode, RepeatLatentBatch, Flux2Scheduler, Anything Everywhere, ConditioningZeroOut, GetImageSize, CFGGuider, UNETLoader, CFGGuider, RandomNoise, Anything Everywhere, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, Image Comparer (rgthree), GetNode, CLIPTextEncode, RebatchLatents, SamplerCustomAdvanced, SetNode, LoraLoaderModelOnly, LoadImage, SaveImage, easy showAnything, QwenMultiangleLightningNode, CR Text, SetNode, ImpactSwitch, GetNode]
patterns: []
missing: []
---

# 平台全量/flux.2 klein 9b-重打光·照片光源重新照明着色_2027329955582976001.json

> 来源文件 `comfyui_library/workflows/平台全量/flux.2 klein 9b-重打光·照片光源重新照明着色_2027329955582976001.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
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
- `LoadImage`
- `SaveImage`
- `easy showAnything`
- `QwenMultiangleLightningNode`
- `CR Text`
- `SetNode`
- `ImpactSwitch`
- `GetNode`

## 知识

覆盖率 **67%**（24/36）

**有卡**：`KSamplerSelect`、`VAELoader`、`CLIPLoader`、`EmptyFlux2LatentImage`、`ReferenceLatent`、`VAEEncode`、`RepeatLatentBatch`、`Flux2Scheduler`、`ConditioningZeroOut`、`GetImageSize`、`CFGGuider`、`UNETLoader`、`RandomNoise`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`RebatchLatents`、`SamplerCustomAdvanced`、`LoraLoaderModelOnly`、`LoadImage`、`SaveImage`、`QwenMultiangleLightningNode`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
