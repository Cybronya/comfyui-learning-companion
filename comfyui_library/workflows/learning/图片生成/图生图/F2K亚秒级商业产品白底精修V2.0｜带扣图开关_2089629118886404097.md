---
key: 图片生成/图生图/F2K亚秒级商业产品白底精修V2.0｜带扣图开关_2089629118886404097.json
name: F2K亚秒级商业产品白底精修V2.0｜带扣图开关_2089629118886404097.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F2K亚秒级商业产品白底精修V2.0｜带扣图开关_2089629118886404097.json
hash: 91e61dc16d3a3dd6
coverage: 0.741935
learned_at: 2026-10-09 22:19:26
nodes: [SetNode, ImpactInt, 孤海注释, VAEEncode, LoraLoaderModelOnly, ReferenceLatent, ConditioningZeroOut, ReferenceLatent, GetImageSize, RandomNoise, CFGGuider, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, SaveImage, UNETLoader, UNETLoader, CLIPLoader, VAELoader, GetNode, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, CLIPTextEncode, LayerMask: BiRefNetUltra, GetNode, Image Comparer (rgthree), VAELoader, SamplerCustomAdvanced, VAEDecode, Fast Groups Bypasser (rgthree)]
patterns: []
missing: [LayerMask: BiRefNetUltra, LayerUtility: ImageScaleByAspectRatio V2]
discoveries: [次要节点 `LayerMask: BiRefNetUltra` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/F2K亚秒级商业产品白底精修V2.0｜带扣图开关_2089629118886404097.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2089629118886404097.json`

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

覆盖率 **74%**（23/31）

**有卡**：`ImpactInt`、`VAEEncode`、`LoraLoaderModelOnly`、`ReferenceLatent`、`ConditioningZeroOut`、`GetImageSize`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`VAEDecode`

**缺卡**（2）：`LayerMask: BiRefNetUltra`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 学习发现

- 次要节点 `LayerMask: BiRefNetUltra` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
