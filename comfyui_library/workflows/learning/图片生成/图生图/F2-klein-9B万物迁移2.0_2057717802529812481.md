---
key: 图片生成/图生图/F2-klein-9B万物迁移2.0_2057717802529812481.json
name: F2-klein-9B万物迁移2.0_2057717802529812481
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F2-klein-9B万物迁移2.0_2057717802529812481.json
hash: 7961a0d832d765a1
coverage: 0.761905
learned_at: 2026-10-23 10:53:02
nodes: [CLIPLoader, VAELoader, KSamplerSelect, Flux2Scheduler, CFGGuider, SamplerCustomAdvanced, VAEDecode, RandomNoise, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, GetImageSize, ReferenceLatent, ReferenceLatent, ReferenceLatent, ReferenceLatent, LayerUtility: ImageReelComposit, SaveImage, Fast Groups Bypasser (rgthree), VAEEncode, VAEEncode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, Int, SaveImage, LayerUtility: ImageReel, Image Comparer (rgthree), Int, easy imageScaleDownToSize, easy imageScaleDownToSize, LoadImage, LoadImage, CR Text]
patterns: []
missing: []
---

# 图片生成/图生图/F2-klein-9B万物迁移2.0_2057717802529812481.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F2-klein-9B万物迁移2.0_2057717802529812481.json`

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
- `Image Comparer (rgthree)`
- `Int`
- `easy imageScaleDownToSize`
- `easy imageScaleDownToSize`
- `LoadImage`
- `LoadImage`
- `CR Text`

## 知识

覆盖率 **76%**（32/42）

**有卡**：`CLIPLoader`、`VAELoader`、`KSamplerSelect`、`Flux2Scheduler`、`CFGGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`RandomNoise`、`CLIPTextEncode`、`ConditioningZeroOut`、`EmptyFlux2LatentImage`、`GetImageSize`、`ReferenceLatent`、`LayerUtility: ImageReelComposit`、`SaveImage`、`VAEEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`Int`、`LayerUtility: ImageReel`、`easy imageScaleDownToSize`、`LoadImage`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
