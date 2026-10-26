---
key: 图片生成/图生图/Flux-2-Kelin亚秒级商业产品白底精修V2.0｜带扣图开关_2113822790381035521.json
name: Flux-2-Kelin亚秒级商业产品白底精修V2.0｜带扣图开关_2113822790381035521
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux-2-Kelin亚秒级商业产品白底精修V2.0｜带扣图开关_2113822790381035521.json
hash: b0097c672e0840d0
coverage: 0.806452
learned_at: 2026-10-26 22:01:42
nodes: [SetNode, ImpactInt, 孤海注释, VAEEncode, LoraLoaderModelOnly, ReferenceLatent, ConditioningZeroOut, ReferenceLatent, GetImageSize, RandomNoise, CFGGuider, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, SaveImage, UNETLoader, UNETLoader, CLIPLoader, VAELoader, GetNode, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, CLIPTextEncode, LayerMask: BiRefNetUltra, GetNode, Image Comparer (rgthree), VAELoader, SamplerCustomAdvanced, VAEDecode, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 图片生成/图生图/Flux-2-Kelin亚秒级商业产品白底精修V2.0｜带扣图开关_2113822790381035521.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux-2-Kelin亚秒级商业产品白底精修V2.0｜带扣图开关_2113822790381035521.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `SetNode`
- `ImpactInt`
- `孤海注释`
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `GetImageSize`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `SaveImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LayerMask: BiRefNetUltra`
- `GetNode`
- `Image Comparer (rgthree)`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **81%**（25/31）

**有卡**：`ImpactInt`、`VAEEncode`、`LoraLoaderModelOnly`、`ReferenceLatent`、`ConditioningZeroOut`、`GetImageSize`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`CLIPTextEncode`、`LayerMask: BiRefNetUltra`、`SamplerCustomAdvanced`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
