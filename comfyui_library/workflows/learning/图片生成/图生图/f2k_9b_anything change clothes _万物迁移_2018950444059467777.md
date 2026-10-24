---
key: 图片生成/图生图/f2k_9b_anything change clothes _万物迁移_2018950444059467777.json
name: f2k_9b_anything change clothes _万物迁移_2018950444059467777
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/f2k_9b_anything change clothes _万物迁移_2018950444059467777.json
hash: 1c1a0b6663ccc398
coverage: 0.75
learned_at: 2026-10-23 11:34:47
nodes: [LoadImage, KSamplerSelect, Flux2Scheduler, CFGGuider, SamplerCustomAdvanced, VAEDecode, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, GetImageSize, ReferenceLatent, ReferenceLatent, ReferenceLatent, ReferenceLatent, SetNode, SetNode, SetNode, LoadImage, GetNode, GetNode, GetNode, SaveImage, GetNode, VAEEncode, easy imageScaleDownToSize, VAEEncode, Image Comparer (rgthree), UNETLoader, CLIPLoader, VAELoader, LayerUtility: ImageReel, Fast Groups Bypasser (rgthree), GetNode, easy imageScaleDownToSize, RandomNoise, LayerUtility: ImageReelComposit, SaveImage, CR Text, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 图片生成/图生图/f2k_9b_anything change clothes _万物迁移_2018950444059467777.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/f2k_9b_anything change clothes _万物迁移_2018950444059467777.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `LoadImage`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `SaveImage`
- `GetNode`
- `VAEEncode` ★核心
- `easy imageScaleDownToSize`
- `VAEEncode` ★核心
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: ImageReel`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `easy imageScaleDownToSize`
- `RandomNoise`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **75%**（30/40）

**有卡**：`LoadImage`、`KSamplerSelect`、`Flux2Scheduler`、`CFGGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`CLIPTextEncode`、`ConditioningZeroOut`、`EmptyFlux2LatentImage`、`GetImageSize`、`ReferenceLatent`、`SaveImage`、`VAEEncode`、`easy imageScaleDownToSize`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LayerUtility: ImageReel`、`RandomNoise`、`LayerUtility: ImageReelComposit`、`CR Text`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
