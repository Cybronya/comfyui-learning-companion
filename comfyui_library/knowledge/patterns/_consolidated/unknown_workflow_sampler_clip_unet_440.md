---
name: unknown_workflow_sampler_clip_unet_440
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8955
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Color Panel, CR Text Replace, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize+, GrowMaskWithBlur, Image Blend, Image Comparer (rgthree), ImageColorMatch+, ImageComposite+, ImageCompositeMasked, Int, KSamplerSelect, LayerUtility: CropByMask, LayerUtility: ImageMaskScaleAs, LayerUtility: RestoreCropBox, LoadImage, PreviewImage, Primitive float [Crystools], RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageScaleDownToSize, easy imageSize, 取色器_孤海]
problems: []
missing: []
members: [图片生成/图生图/万物迁移增强版—饰品_服装等_2053702739301027841.json, 图片生成/图生图/电商产品替换（1）_2087469163865534466.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_440

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/万物迁移增强版—饰品_服装等_2053702739301027841.json、图片生成/图生图/电商产品替换（1）_2087469163865534466.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Color Panel`
- `CR Text Replace`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize+`
- `GrowMaskWithBlur`
- `Image Blend`
- `Image Comparer (rgthree)`
- `ImageColorMatch+`
- `ImageComposite+`
- `ImageCompositeMasked`
- `Int`
- `KSamplerSelect`
- `LayerUtility: CropByMask`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `PreviewImage`
- `Primitive float [Crystools]`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageScaleDownToSize`
- `easy imageSize`
- `取色器_孤海`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageReel` —— 1/2 个有
- `LayerUtility: ImageReelComposit` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
