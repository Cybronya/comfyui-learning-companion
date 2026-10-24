---
name: unknown_workflow_sampler_clip_unet_277
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8705
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, Flux2Scheduler, GrowMaskWithBlur, ImageCompositeMasked, ImageCrop+, KSamplerSelect, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX2去水印万能改图单图版保持原图不变_2059054774292664321.json, 图片生成/图生图/FLUX2去水印万能改图单图版保持原图不变_2062027536372166658.json, 图片生成/图生图/Flux2-Klein移除水印单图版V2（保持原图不变）_2014510703759069185.json, 图片生成/图生图/移除即梦水印单图版V2（保持原图不变）_2012487948297572353.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_277

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/FLUX2去水印万能改图单图版保持原图不变_2059054774292664321.json、图片生成/图生图/FLUX2去水印万能改图单图版保持原图不变_2062027536372166658.json、图片生成/图生图/Flux2-Klein移除水印单图版V2（保持原图不变）_2014510703759069185.json、图片生成/图生图/移除即梦水印单图版V2（保持原图不变）_2012487948297572353.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `GrowMaskWithBlur`
- `ImageCompositeMasked`
- `ImageCrop+`
- `KSamplerSelect`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `JjkText` —— 2/4 个有
- `SetLatentNoiseMask` —— 2/4 个有
- `easy imageSize` —— 2/4 个有
- `ImageConcanate` —— 1/4 个有
- `LayerUtility: ImageReel` —— 1/4 个有
- `LayerUtility: ImageReelComposit` —— 1/4 个有
- `MaskPreview` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
