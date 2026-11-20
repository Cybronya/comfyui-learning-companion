---
name: unknown_workflow_sampler_clip_unet_549
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.902
common_nodes: [Anything Everywhere3, BasicGuider, BasicScheduler, CLIPLoader_Any, CLIPTextEncode, ColorMatchV2, CropByMask, ImageCompositeMasked, ImageScale, ImageScaleToTotalPixelsX, ImageToMask, ImpactMakeAnyList, KSamplerSelect, LayerColor: BrightnessContrastV2, LayerMask: MaskGrow, LayerUtility: ColorImage V2, LayerUtility: ImageBlendAdvance, LoadImage, MaskPreview, Masks Add, PreviewImage, RandomNoise, ReferenceLatent, SAM3Segment, SamplerCustomAdvanced, SaveImage, Seed (rgthree), UNETLoader_Any, VAEDecode, VAEEncode, VAELoader_Any, easy mathInt, easy positive, easy promptReplace]
problems: []
missing: []
members: [平台全量/flux2-klein-9b-服装模特图-批量帽子迁移_2059498295654961153.json, 平台全量/flux2-klein-9b-服装模特图-批量鞋子迁移_2060636747519840257.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_549

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/flux2-klein-9b-服装模特图-批量帽子迁移_2059498295654961153.json、平台全量/flux2-klein-9b-服装模特图-批量鞋子迁移_2060636747519840257.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader_Any`
- `CLIPTextEncode`
- `ColorMatchV2`
- `CropByMask`
- `ImageCompositeMasked`
- `ImageScale`
- `ImageScaleToTotalPixelsX`
- `ImageToMask`
- `ImpactMakeAnyList`
- `KSamplerSelect`
- `LayerColor: BrightnessContrastV2`
- `LayerMask: MaskGrow`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageBlendAdvance`
- `LoadImage`
- `MaskPreview`
- `Masks Add`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SAM3Segment`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader_Any`
- `VAEDecode`
- `VAEEncode`
- `VAELoader_Any`
- `easy mathInt`
- `easy positive`
- `easy promptReplace`

**可变部分**（部分 workflow 才有）：
- `AILab_MaskCombiner` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
