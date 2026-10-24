---
name: image_to_image_upscale_lora_sampler_91
type: Image To Image
frequency: 2
level: weak
coverage: 0.588
common_nodes: [AddMask, CLIPLoader_Any, CLIPTextEncode, CR Image Input Switch (4 way), CR String To Number, CR Text Replace, ConditioningZeroOut, EmptyImage, GetImageSize, GetNode, GoohaiUniversalSlider, GrowMaskWithBlur, Image Comparer (rgthree), Image Overlay, ImageNoiseAugmentation, ImageResize+, ImageUpscaleWithModel, Int, JjkText, KSampler, KuwaharaBlur, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, Mask Switch (JPS), MaskPreview+, PreviewImage, ReferenceLatent, SaveImage, SetNode, SomethingToString, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, Text Concatenate (JPS), UNETLoader_Any, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader_Any, easy imageBatchToImageList, easy imageColorMatch, easy imageListToImageBatch, easy int, easy sam3ImageSegmentation, easy sam3ModelLoader, easy showAnything, 孤海注释, 忽略多组孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人像真实感放大_专业版_2098953207358771202.json, 图片生成/图生图/人像真实感放大_专业版_2099064909014323201.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_91

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/人像真实感放大_专业版_2098953207358771202.json、图片生成/图生图/人像真实感放大_专业版_2099064909014323201.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：59%

## 共有节点

全部 2 个 workflow 都包含：
- `AddMask`
- `CLIPLoader_Any`
- `CLIPTextEncode`
- `CR Image Input Switch (4 way)`
- `CR String To Number`
- `CR Text Replace`
- `ConditioningZeroOut`
- `EmptyImage`
- `GetImageSize`
- `GetNode`
- `GoohaiUniversalSlider`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `Image Overlay`
- `ImageNoiseAugmentation`
- `ImageResize+`
- `ImageUpscaleWithModel`
- `Int`
- `JjkText`
- `KSampler`
- `KuwaharaBlur`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Switch (JPS)`
- `MaskPreview+`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `SetNode`
- `SomethingToString`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `Text Concatenate (JPS)`
- `UNETLoader_Any`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader_Any`
- `easy imageBatchToImageList`
- `easy imageColorMatch`
- `easy imageListToImageBatch`
- `easy int`
- `easy sam3ImageSegmentation`
- `easy sam3ModelLoader`
- `easy showAnything`
- `孤海注释`
- `忽略多组孤海`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
