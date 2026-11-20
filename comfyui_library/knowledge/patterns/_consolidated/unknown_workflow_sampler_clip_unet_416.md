---
name: unknown_workflow_sampler_clip_unet_416
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.909667
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Color Panel, CR Text Replace, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize+, GrowMaskWithBlur, Image Blend, Image Comparer (rgthree), ImageColorMatch+, ImageComposite+, ImageCompositeMasked, Int, KSamplerSelect, LayerUtility: CropByMask, LayerUtility: ImageMaskScaleAs, LayerUtility: RestoreCropBox, LoadImage, PreviewImage, Primitive float [Crystools], RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageScaleDownToSize, easy imageSize, 取色器_孤海]
problems: []
missing: []
members: [图片生成/图生图/万物迁移增强版—饰品_服装等_2053702739301027841.json, 图片生成/图生图/电商产品替换（1）_2087469163865534466.json, 平台全量/饰品穿戴仅供参考_2053351916347895809.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_416

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/万物迁移增强版—饰品_服装等_2053702739301027841.json、图片生成/图生图/电商产品替换（1）_2087469163865534466.json、平台全量/饰品穿戴仅供参考_2053351916347895809.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
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
- `LayerUtility: ImageReel` —— 2/3 个有
- `LayerUtility: ImageReelComposit` —— 2/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
