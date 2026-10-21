---
key: 图片生成/图生图/F2K亚秒级商业产品白底精修V2.0｜带扣图开关_2092609760863543297.json
name: F2K亚秒级商业产品白底精修V2.0｜带扣图开关_2092609760863543297
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F2K亚秒级商业产品白底精修V2.0｜带扣图开关_2092609760863543297.json
hash: 9c61e31087c536a6
coverage: 0.8125
learned_at: 2026-10-21 00:39:02
nodes: [SetNode, ImpactInt, 孤海注释, VAEEncode, ReferenceLatent, ConditioningZeroOut, ReferenceLatent, GetImageSize, RandomNoise, CFGGuider, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, SaveImage, UNETLoader, UNETLoader, CLIPLoader, VAELoader, GetNode, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, CLIPTextEncode, GetNode, VAELoader, SamplerCustomAdvanced, VAEDecode, LoraLoaderModelOnly, easy imageRemBg, Image Comparer (rgthree), Fast Groups Bypasser (rgthree), SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/F2K亚秒级商业产品白底精修V2.0｜带扣图开关_2092609760863543297.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F2K亚秒级商业产品白底精修V2.0｜带扣图开关_2092609760863543297.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `SetNode`
- `ImpactInt`
- `孤海注释`
- `VAEEncode` ★核心
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
- `GetNode`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy imageRemBg`
- `Image Comparer (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`

## 知识

覆盖率 **81%**（26/32）

**有卡**：`ImpactInt`、`VAEEncode`、`ReferenceLatent`、`ConditioningZeroOut`、`GetImageSize`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`VAEDecode`、`easy imageRemBg`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
