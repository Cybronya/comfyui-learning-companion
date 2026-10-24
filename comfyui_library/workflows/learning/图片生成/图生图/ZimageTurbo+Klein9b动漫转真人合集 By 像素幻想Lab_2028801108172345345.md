---
key: 图片生成/图生图/ZimageTurbo+Klein9b动漫转真人合集 By 像素幻想Lab_2028801108172345345.json
name: ZimageTurbo+Klein9b动漫转真人合集 By 像素幻想Lab_2028801108172345345
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/ZimageTurbo+Klein9b动漫转真人合集 By 像素幻想Lab_2028801108172345345.json
hash: 459a819c21b26564
coverage: 0.888889
learned_at: 2026-10-23 11:33:03
nodes: [KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageReelComposit, LayerUtility: ImageReel, CLIPTextEncode, CFGGuider, KSamplerSelect, Flux2Scheduler, ConditioningZeroOut, RandomNoise, EmptyFlux2LatentImage, SamplerCustomAdvanced, Image Comparer (rgthree), LayerUtility: ImageReelComposit, LayerUtility: ImageReel, easy setNode, GetImageSize, CLIPTextEncode, VAEEncode, ConditioningZeroOut, LayerUtility: ImageReelComposit, VAEEncode, easy setNode, LayerUtility: ImageReel, easy getNode, easy setNode, easy getNode, KSamplerAdvanced, PreviewImage, VAEDecode, Image Comparer (rgthree), SaveImage, VAEDecode, SaveImage, VAEDecode, easy getNode, easy getNode, easy getNode, Any Switch (rgthree), Image Comparer (rgthree), SaveImage, Fast Groups Bypasser (rgthree), SaveImage, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, Image Comparer (rgthree), KSamplerAdvanced, easy setNode, VAEEncode, easy showAnything, ConditioningZeroOut, CLIPTextEncode, easy cleanGpuUsed, CR Text, Qwen3_VQA, Qwen3_VQA, easy cleanGpuUsed, VAELoader, CLIPLoader, UNETLoader, VAELoader, CLIPLoader, UNETLoader, VAELoader, CLIPLoader, UNETLoader, LoadImage, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ReferenceLatent, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SeedVR2LoadDiTModel, easy showAnything, KSamplerAdvanced, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "FlowMatchEulerDiscreteScheduler", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 图片生成/图生图/ZimageTurbo+Klein9b动漫转真人合集 By 像素幻想Lab_2028801108172345345.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/ZimageTurbo+Klein9b动漫转真人合集 By 像素幻想Lab_2028801108172345345.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（81 个）：
- `KSamplerAdvanced` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageReel`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `ConditioningZeroOut`
- `RandomNoise`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `Image Comparer (rgthree)`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageReel`
- `easy setNode`
- `GetImageSize`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `LayerUtility: ImageReelComposit`
- `VAEEncode` ★核心
- `easy setNode`
- `LayerUtility: ImageReel`
- `easy getNode`
- `easy setNode`
- `easy getNode`
- `KSamplerAdvanced` ★核心
- `PreviewImage`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `VAEDecode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `Any Switch (rgthree)`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `Image Comparer (rgthree)`
- `KSamplerAdvanced` ★核心
- `easy setNode`
- `VAEEncode` ★核心
- `easy showAnything`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `CR Text`
- `Qwen3_VQA`
- `Qwen3_VQA`
- `easy cleanGpuUsed`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ReferenceLatent`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SeedVR2LoadDiTModel`
- `easy showAnything`
- `KSamplerAdvanced` ★核心
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `FlowMatchEulerDiscreteScheduler`

## 知识

覆盖率 **89%**（72/81）

**有卡**：`KSamplerAdvanced`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`CLIPTextEncode`、`CFGGuider`、`KSamplerSelect`、`Flux2Scheduler`、`ConditioningZeroOut`、`RandomNoise`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`easy setNode`、`GetImageSize`、`VAEEncode`、`easy getNode`、`VAEDecode`、`SaveImage`、`easy cleanGpuUsed`、`CR Text`、`Qwen3_VQA`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoadImage`、`LoraLoaderModelOnly`、`ReferenceLatent`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
