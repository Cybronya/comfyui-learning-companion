---
key: 图片生成/图生图/【真人转动漫】FLUX.2.0_Klein9B_2032008428285075458.json
name: 【真人转动漫】FLUX.2.0_Klein9B_2032008428285075458
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【真人转动漫】FLUX.2.0_Klein9B_2032008428285075458.json
hash: d6a4ea55dfdcc9a6
coverage: 0.742857
learned_at: 2026-10-23 11:51:10
nodes: [CLIPLoader, VAELoader, SetNode, SetNode, ConditioningZeroOut, SetNode, UNETLoader, LoraLoaderModelOnly, CLIPTextEncode, ReferenceLatent, CFGGuider, KSamplerSelect, Flux2Scheduler, SamplerCustomAdvanced, RandomNoise, VAEDecode, easy cleanGpuUsed, GetNode, GetNode, GetNode, GetImageSize, EmptyFlux2LatentImage, ReferenceLatent, Image Comparer (rgthree), LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, SaveImage, SaveImage, GetNode, Int, CR Text, easy imageScaleDownToSize, VAEEncode, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 图片生成/图生图/【真人转动漫】FLUX.2.0_Klein9B_2032008428285075458.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【真人转动漫】FLUX.2.0_Klein9B_2032008428285075458.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `ConditioningZeroOut`
- `SetNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSize`
- `EmptyFlux2LatentImage`
- `ReferenceLatent`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `GetNode`
- `Int`
- `CR Text`
- `easy imageScaleDownToSize`
- `VAEEncode` ★核心
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **74%**（26/35）

**有卡**：`CLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`ReferenceLatent`、`CFGGuider`、`KSamplerSelect`、`Flux2Scheduler`、`SamplerCustomAdvanced`、`RandomNoise`、`VAEDecode`、`easy cleanGpuUsed`、`GetImageSize`、`EmptyFlux2LatentImage`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`LoadImage`、`SaveImage`、`Int`、`CR Text`、`easy imageScaleDownToSize`、`VAEEncode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
