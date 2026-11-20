---
name: image_to_image_upscale_lora_sampler_40
type: Image To Image
frequency: 5
level: strong
coverage: 0.6074
common_nodes: [AddMask, CLIPLoader_Any, CLIPTextEncode, CR Image Input Switch (4 way), CR String To Number, CR Text Replace, ConditioningZeroOut, GetImageSize, GetNode, GoohaiUniversalSlider, GrowMaskWithBlur, Image Comparer (rgthree), Image Overlay, ImageNoiseAugmentation, ImageUpscaleWithModel, Int, JjkText, KSampler, KuwaharaBlur, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LoadImage, LoraLoaderModelOnly, Mask Switch (JPS), PreviewImage, ReferenceLatent, SaveImage, SetNode, SomethingToString, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, Text Concatenate (JPS), UNETLoader_Any, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader_Any, easy imageBatchToImageList, easy imageColorMatch, easy imageListToImageBatch, easy int, easy sam3ImageSegmentation, easy sam3ModelLoader, easy showAnything, 孤海注释, 忽略多组孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人像真实感放大_专业版_2098953207358771202.json, 图片生成/图生图/人像真实感放大_专业版_2099064909014323201.json, 平台全量/三视图 4_3放大专用_2100485657675259905.json, 平台全量/人像真实感放大 _ 专业版_2093233122535108609.json, 平台全量/人像真实感放大 _ 专业版_2099501957500198914.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_40

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/人像真实感放大_专业版_2098953207358771202.json、图片生成/图生图/人像真实感放大_专业版_2099064909014323201.json、平台全量/三视图 4_3放大专用_2100485657675259905.json、平台全量/人像真实感放大 _ 专业版_2093233122535108609.json、平台全量/人像真实感放大 _ 专业版_2099501957500198914.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 5 个 workflow 都包含：
- `AddMask`
- `CLIPLoader_Any`
- `CLIPTextEncode`
- `CR Image Input Switch (4 way)`
- `CR String To Number`
- `CR Text Replace`
- `ConditioningZeroOut`
- `GetImageSize`
- `GetNode`
- `GoohaiUniversalSlider`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `Image Overlay`
- `ImageNoiseAugmentation`
- `ImageUpscaleWithModel`
- `Int`
- `JjkText`
- `KSampler`
- `KuwaharaBlur`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Switch (JPS)`
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

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `MaskPreview+` —— 4/5 个有
- `EmptyImage` —— 2/5 个有
- `Bounded Image Crop` —— 1/5 个有
- `ComfyMathExpression` —— 1/5 个有
- `Image Bounds` —— 1/5 个有
- `Image Remove Alpha JK` —— 1/5 个有
- `ImagePadForOutpaint` —— 1/5 个有
- `ImageScaleToMaxDimension` —— 1/5 个有
- `Inset Image Bounds` —— 1/5 个有
- `ZML_AnyTypeSwitchFiveBoolean` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
