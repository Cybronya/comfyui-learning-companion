---
key: 图片生成/图生图/FLUX.2_模特换装遮罩版，一键换衣_换鞋通用_2085639692602658817.json
name: FLUX.2_模特换装遮罩版，一键换衣_换鞋通用_2085639692602658817
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2_模特换装遮罩版，一键换衣_换鞋通用_2085639692602658817.json
hash: 673b6e93f61c9849
coverage: 0.571429
learned_at: 2026-10-21 00:39:07
nodes: [GetNode, GetImageSize, CFGGuider, UNETLoader, CLIPLoader, VAELoader, SetNode, InpaintStitchImproved, LayerMask: LoadBiRefNetModelV2, GetNode, LayerMask: BiRefNetUltraV2, GetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, SamplerCustomAdvanced, KSamplerSelect, GetNode, PainterFluxImageEdit, GetNode, GetNode, SetNode, GrowMaskWithBlur, VAEDecode, ImageBatchToList, RepeatLatentBatch, GetNode, InpaintCropImproved, Flux2Scheduler, LayerUtility: CropByMask V2, SetNode, ImpactInt, SetNode, SetNode, SetNode, MaskFillHoles, SetNode, SetNode, GetNode, GetNode, GetNode, Note, LoadImage, ImpactInt, RandomNoise, SaveImage, Image Comparer (rgthree), LoadImage, LoadImage, Text]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.2_模特换装遮罩版，一键换衣_换鞋通用_2085639692602658817.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2_模特换装遮罩版，一键换衣_换鞋通用_2085639692602658817.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `GetNode`
- `GetImageSize`
- `CFGGuider`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `InpaintStitchImproved`
- `LayerMask: LoadBiRefNetModelV2`
- `GetNode`
- `LayerMask: BiRefNetUltraV2`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `GetNode`
- `PainterFluxImageEdit`
- `GetNode`
- `GetNode`
- `SetNode`
- `GrowMaskWithBlur`
- `VAEDecode` ★核心
- `ImageBatchToList`
- `RepeatLatentBatch`
- `GetNode`
- `InpaintCropImproved`
- `Flux2Scheduler`
- `LayerUtility: CropByMask V2`
- `SetNode`
- `ImpactInt`
- `SetNode`
- `SetNode`
- `SetNode`
- `MaskFillHoles`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `LoadImage`
- `ImpactInt`
- `RandomNoise`
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoadImage`
- `Text`

## 知识

覆盖率 **57%**（28/49）

**有卡**：`GetImageSize`、`CFGGuider`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`InpaintStitchImproved`、`LayerMask: LoadBiRefNetModelV2`、`LayerMask: BiRefNetUltraV2`、`LayerUtility: ImageScaleByAspectRatio V2`、`SamplerCustomAdvanced`、`KSamplerSelect`、`PainterFluxImageEdit`、`GrowMaskWithBlur`、`VAEDecode`、`ImageBatchToList`、`RepeatLatentBatch`、`InpaintCropImproved`、`Flux2Scheduler`、`LayerUtility: CropByMask V2`、`ImpactInt`、`MaskFillHoles`、`LoadImage`、`RandomNoise`、`SaveImage`、`Text`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPLoader、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
