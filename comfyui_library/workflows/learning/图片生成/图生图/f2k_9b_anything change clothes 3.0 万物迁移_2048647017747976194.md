---
key: 图片生成/图生图/f2k_9b_anything change clothes 3.0 万物迁移_2048647017747976194.json
name: f2k_9b_anything change clothes 3.0 万物迁移_2048647017747976194
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/f2k_9b_anything change clothes 3.0 万物迁移_2048647017747976194.json
hash: 4e96a3448ae1b85d
coverage: 0.75
learned_at: 2026-10-23 11:34:47
nodes: [LoadImage, KSamplerSelect, Flux2Scheduler, CFGGuider, SamplerCustomAdvanced, VAEDecode, RandomNoise, ConditioningZeroOut, EmptyFlux2LatentImage, GetImageSize, ReferenceLatent, ReferenceLatent, ReferenceLatent, ReferenceLatent, LoadImage, SaveImage, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, SaveImage, easy imageScaleDownToSize, VAEEncode, easy imageScaleDownToSize, VAEEncode, Image Comparer (rgthree), SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Fast Groups Bypasser (rgthree), UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, LoraLoaderModelOnly, CR Text, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 图片生成/图生图/f2k_9b_anything change clothes 3.0 万物迁移_2048647017747976194.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/f2k_9b_anything change clothes 3.0 万物迁移_2048647017747976194.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `LoadImage`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `RandomNoise`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `LoadImage`
- `SaveImage`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `easy imageScaleDownToSize`
- `VAEEncode` ★核心
- `easy imageScaleDownToSize`
- `VAEEncode` ★核心
- `Image Comparer (rgthree)`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **75%**（30/40）

**有卡**：`LoadImage`、`KSamplerSelect`、`Flux2Scheduler`、`CFGGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`RandomNoise`、`ConditioningZeroOut`、`EmptyFlux2LatentImage`、`GetImageSize`、`ReferenceLatent`、`SaveImage`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`easy imageScaleDownToSize`、`VAEEncode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
