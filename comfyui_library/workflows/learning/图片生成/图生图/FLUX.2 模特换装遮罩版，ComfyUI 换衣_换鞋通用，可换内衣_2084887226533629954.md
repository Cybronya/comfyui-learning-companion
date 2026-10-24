---
key: 图片生成/图生图/FLUX.2 模特换装遮罩版，ComfyUI 换衣_换鞋通用，可换内衣_2084887226533629954.json
name: FLUX.2 模特换装遮罩版，ComfyUI 换衣_换鞋通用，可换内衣_2084887226533629954
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2 模特换装遮罩版，ComfyUI 换衣_换鞋通用，可换内衣_2084887226533629954.json
hash: 98697e6775beda5a
coverage: 0.571429
learned_at: 2026-10-23 10:54:09
nodes: [GetNode, GetImageSize, CFGGuider, UNETLoader, CLIPLoader, VAELoader, SetNode, InpaintStitchImproved, LayerMask: LoadBiRefNetModelV2, GetNode, LayerMask: BiRefNetUltraV2, GetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, SamplerCustomAdvanced, KSamplerSelect, GetNode, PainterFluxImageEdit, GetNode, GetNode, SetNode, GrowMaskWithBlur, VAEDecode, ImageBatchToList, RepeatLatentBatch, GetNode, InpaintCropImproved, Flux2Scheduler, LayerUtility: CropByMask V2, SetNode, ImpactInt, SetNode, SetNode, SetNode, MaskFillHoles, SetNode, SetNode, GetNode, GetNode, GetNode, LoadImage, LoadImage, Note, LoadImage, ImpactInt, RandomNoise, SaveImage, Image Comparer (rgthree), Text]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.2 模特换装遮罩版，ComfyUI 换衣_换鞋通用，可换内衣_2084887226533629954.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2 模特换装遮罩版，ComfyUI 换衣_换鞋通用，可换内衣_2084887226533629954.json`

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
- `LoadImage`
- `LoadImage`
- `Note`
- `LoadImage`
- `ImpactInt`
- `RandomNoise`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Text`

## 知识

覆盖率 **57%**（28/49）

**有卡**：`GetImageSize`、`CFGGuider`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`InpaintStitchImproved`、`LayerMask: LoadBiRefNetModelV2`、`LayerMask: BiRefNetUltraV2`、`LayerUtility: ImageScaleByAspectRatio V2`、`SamplerCustomAdvanced`、`KSamplerSelect`、`PainterFluxImageEdit`、`GrowMaskWithBlur`、`VAEDecode`、`ImageBatchToList`、`RepeatLatentBatch`、`InpaintCropImproved`、`Flux2Scheduler`、`LayerUtility: CropByMask V2`、`ImpactInt`、`MaskFillHoles`、`LoadImage`、`RandomNoise`、`SaveImage`、`Text`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPLoader、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
