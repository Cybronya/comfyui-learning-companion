---
key: 图片生成/图生图/F2-klein-9B产品精修2.0_2027658019277905921.json
name: F2-klein-9B产品精修2.0_2027658019277905921
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F2-klein-9B产品精修2.0_2027658019277905921.json
hash: 441ae54c2df96135
coverage: 0.761905
learned_at: 2026-10-23 10:53:03
nodes: [SaveImage, LoadImage, KSamplerSelect, SamplerCustomAdvanced, RandomNoise, CLIPLoader, VAELoader, EmptyFlux2LatentImage, CFGGuider, Flux2Scheduler, CLIPTextEncode, ConditioningZeroOut, GetImageSize, ReferenceLatent, ReferenceLatent, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, CR Text, Fast Groups Bypasser (rgthree), easy imageScaleDownToSize, VAEEncode, VAEDecode, LoraLoaderModelOnly, Image Comparer (rgthree), SaveImage, SaveImage, Image Comparer (rgthree), SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, easy cleanGpuUsed, easy cleanGpuUsed, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, UNETLoader, LoraLoaderModelOnly, JWInteger]
patterns: []
missing: []
---

# 图片生成/图生图/F2-klein-9B产品精修2.0_2027658019277905921.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F2-klein-9B产品精修2.0_2027658019277905921.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `SaveImage`
- `LoadImage`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CLIPLoader`
- `VAELoader`
- `EmptyFlux2LatentImage`
- `CFGGuider`
- `Flux2Scheduler`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `GetImageSize`
- `ReferenceLatent`
- `ReferenceLatent`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `easy imageScaleDownToSize`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `JWInteger`

## 知识

覆盖率 **76%**（32/42）

**有卡**：`SaveImage`、`LoadImage`、`KSamplerSelect`、`SamplerCustomAdvanced`、`RandomNoise`、`CLIPLoader`、`VAELoader`、`EmptyFlux2LatentImage`、`CFGGuider`、`Flux2Scheduler`、`CLIPTextEncode`、`ConditioningZeroOut`、`GetImageSize`、`ReferenceLatent`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`CR Text`、`easy imageScaleDownToSize`、`VAEEncode`、`VAEDecode`、`LoraLoaderModelOnly`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`easy cleanGpuUsed`、`UNETLoader`、`JWInteger`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
