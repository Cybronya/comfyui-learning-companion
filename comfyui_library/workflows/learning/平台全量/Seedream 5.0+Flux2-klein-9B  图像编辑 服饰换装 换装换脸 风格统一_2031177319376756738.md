---
key: 平台全量/Seedream 5.0+Flux2-klein-9B  图像编辑 服饰换装 换装换脸 风格统一_2031177319376756738.json
name: Seedream 5.0+Flux2-klein-9B  图像编辑 服饰换装 换装换脸 风格统一_2031177319376756738
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Seedream 5.0+Flux2-klein-9B  图像编辑 服饰换装 换装换脸 风格统一_2031177319376756738.json
hash: af1f6d313e788f94
coverage: 0.755556
learned_at: 2026-11-14 01:00:32
nodes: [SaveImage, RH_Jimeng4_Image2Image, Image Comparer (rgthree), KSamplerSelect, Flux2Scheduler, CFGGuider, SamplerCustomAdvanced, VAEDecode, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, GetImageSize, ReferenceLatent, ReferenceLatent, ReferenceLatent, ReferenceLatent, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, VAEEncode, easy imageScaleDownToSize, VAEEncode, CLIPLoader, VAELoader, LoraLoaderModelOnly, GetNode, easy imageScaleDownToSize, RandomNoise, LayerUtility: ImageReelComposit, LoraLoaderModelOnly, LayerUtility: ImageReel, Image Comparer (rgthree), CR Text, UNETLoader, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, SaveImage, SaveImage, LoadImage, LoadImage]
patterns: []
missing: []
---

# 平台全量/Seedream 5.0+Flux2-klein-9B  图像编辑 服饰换装 换装换脸 风格统一_2031177319376756738.json

> 来源文件 `comfyui_library/workflows/平台全量/Seedream 5.0+Flux2-klein-9B  图像编辑 服饰换装 换装换脸 风格统一_2031177319376756738.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `SaveImage`
- `RH_Jimeng4_Image2Image`
- `Image Comparer (rgthree)`
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
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEEncode` ★核心
- `easy imageScaleDownToSize`
- `VAEEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `easy imageScaleDownToSize`
- `RandomNoise`
- `LayerUtility: ImageReelComposit`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageReel`
- `Image Comparer (rgthree)`
- `CR Text`
- `UNETLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **76%**（34/45）

**有卡**：`SaveImage`、`RH_Jimeng4_Image2Image`、`KSamplerSelect`、`Flux2Scheduler`、`CFGGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`CLIPTextEncode`、`ConditioningZeroOut`、`EmptyFlux2LatentImage`、`GetImageSize`、`ReferenceLatent`、`VAEEncode`、`easy imageScaleDownToSize`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`RandomNoise`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`CR Text`、`UNETLoader`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
