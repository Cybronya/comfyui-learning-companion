---
name: unknown_workflow_inpaint_sampler_unet_5
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.571
common_nodes: [CFGGuider, CLIPLoader, Flux2Scheduler, GetImageSize, GetNode, GrowMaskWithBlur, Image Comparer (rgthree), ImageBatchToList, ImpactInt, InpaintCropImproved, InpaintStitchImproved, KSamplerSelect, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskFillHoles, PainterFluxImageEdit, RandomNoise, RepeatLatentBatch, SamplerCustomAdvanced, SaveImage, SetNode, Text, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX.2 模特换装遮罩版，ComfyUI 换衣_换鞋通用，可换内衣_2084887226533629954.json, 图片生成/图生图/FLUX.2_模特换装遮罩版，一键换衣_换鞋通用_2085630087579389954.json, 图片生成/图生图/FLUX.2_模特换装遮罩版，一键换衣_换鞋通用_2085639692602658817.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_unet_5

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/FLUX.2 模特换装遮罩版，ComfyUI 换衣_换鞋通用，可换内衣_2084887226533629954.json、图片生成/图生图/FLUX.2_模特换装遮罩版，一键换衣_换鞋通用_2085630087579389954.json、图片生成/图生图/FLUX.2_模特换装遮罩版，一键换衣_换鞋通用_2085639692602658817.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `Flux2Scheduler`
- `GetImageSize`
- `GetNode`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageBatchToList`
- `ImpactInt`
- `InpaintCropImproved`
- `InpaintStitchImproved`
- `KSamplerSelect`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskFillHoles`
- `PainterFluxImageEdit`
- `RandomNoise`
- `RepeatLatentBatch`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
