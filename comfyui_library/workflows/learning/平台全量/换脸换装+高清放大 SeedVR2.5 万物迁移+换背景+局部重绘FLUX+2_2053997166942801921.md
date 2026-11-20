---
key: 平台全量/换脸换装+高清放大 SeedVR2.5 万物迁移+换背景+局部重绘FLUX+2_2053997166942801921.json
name: 换脸换装+高清放大 SeedVR2.5 万物迁移+换背景+局部重绘FLUX+2_2053997166942801921
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/换脸换装+高清放大 SeedVR2.5 万物迁移+换背景+局部重绘FLUX+2_2053997166942801921.json
hash: fda24065cf991992
coverage: 0.75
learned_at: 2026-11-14 02:08:36
nodes: [KSamplerSelect, Flux2Scheduler, CFGGuider, SamplerCustomAdvanced, VAEDecode, RandomNoise, ConditioningZeroOut, EmptyFlux2LatentImage, GetImageSize, ReferenceLatent, ReferenceLatent, ReferenceLatent, ReferenceLatent, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, VAEEncode, easy imageScaleDownToSize, VAEEncode, Image Comparer (rgthree), SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, GetNode, CLIPTextEncode, GetNode, easy imageScaleDownToSize, LoraLoaderModelOnly, SaveImage, SaveImage, CR Text, ResizeImagesByLongerEdge, Image Comparer (rgthree), Note, easy clearCacheAll, easy cleanGpuUsed, easy int, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, SaveImage, LoadImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, LoadImage]
patterns: []
missing: []
---

# 平台全量/换脸换装+高清放大 SeedVR2.5 万物迁移+换背景+局部重绘FLUX+2_2053997166942801921.json

> 来源文件 `comfyui_library/workflows/平台全量/换脸换装+高清放大 SeedVR2.5 万物迁移+换背景+局部重绘FLUX+2_2053997166942801921.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
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
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
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
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `easy imageScaleDownToSize`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `SaveImage`
- `CR Text`
- `ResizeImagesByLongerEdge`
- `Image Comparer (rgthree)`
- `Note`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `easy int`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `SaveImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **75%**（39/52）

**有卡**：`KSamplerSelect`、`Flux2Scheduler`、`CFGGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`RandomNoise`、`ConditioningZeroOut`、`EmptyFlux2LatentImage`、`GetImageSize`、`ReferenceLatent`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`VAEEncode`、`easy imageScaleDownToSize`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`SaveImage`、`CR Text`、`ResizeImagesByLongerEdge`、`easy clearCacheAll`、`easy cleanGpuUsed`、`easy int`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
