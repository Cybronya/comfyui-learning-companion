---
key: 图片生成/图生图/F2-klein-9B万物迁移2.0_2025429156120498178.json
name: F2-klein-9B万物迁移2.0_2025429156120498178
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F2-klein-9B万物迁移2.0_2025429156120498178.json
hash: edd9a8faa5f38850
coverage: 0.761905
learned_at: 2026-10-23 10:53:02
nodes: [CLIPLoader, VAELoader, KSamplerSelect, Flux2Scheduler, CFGGuider, SamplerCustomAdvanced, VAEDecode, RandomNoise, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, GetImageSize, ReferenceLatent, ReferenceLatent, ReferenceLatent, ReferenceLatent, CR Text, LayerUtility: ImageReelComposit, SaveImage, Fast Groups Bypasser (rgthree), VAEEncode, VAEEncode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, Int, SaveImage, LayerUtility: ImageReel, LoadImage, Image Comparer (rgthree), LoadImage, Int, easy imageScaleDownToSize, easy imageScaleDownToSize]
patterns: []
missing: []
---

# 图片生成/图生图/F2-klein-9B万物迁移2.0_2025429156120498178.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F2-klein-9B万物迁移2.0_2025429156120498178.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `CLIPLoader`
- `VAELoader`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `CR Text`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Int`
- `SaveImage`
- `LayerUtility: ImageReel`
- `LoadImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `Int`
- `easy imageScaleDownToSize`
- `easy imageScaleDownToSize`

## 知识

覆盖率 **76%**（32/42）

**有卡**：`CLIPLoader`、`VAELoader`、`KSamplerSelect`、`Flux2Scheduler`、`CFGGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`RandomNoise`、`CLIPTextEncode`、`ConditioningZeroOut`、`EmptyFlux2LatentImage`、`GetImageSize`、`ReferenceLatent`、`CR Text`、`LayerUtility: ImageReelComposit`、`SaveImage`、`VAEEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`Int`、`LayerUtility: ImageReel`、`LoadImage`、`easy imageScaleDownToSize`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
