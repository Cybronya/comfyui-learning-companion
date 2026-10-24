---
name: image_to_image_upscale_lora_sampler_107
type: Image To Image
frequency: 2
level: weak
coverage: 0.9035
common_nodes: [CLIPTextEncode, ConditioningZeroOut, ConstrainImage|pysssss, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageListToImageBatch, ImageScaleToTotalPixels, ImageUpscaleWithModel, ImpactImageBatchToImageList, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, ReferenceLatent, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/溶图打光Kontext-V2_2023704917680070658.json, 图片生成/图生图/🦖产品精修_2011619538990796802.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_107

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/溶图打光Kontext-V2_2023704917680070658.json、图片生成/图生图/🦖产品精修_2011619538990796802.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ConstrainImage|pysssss`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `ImpactImageBatchToImageList`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ColorMatchImage` —— 1/2 个有
- `DF_Get_image_size` —— 1/2 个有
- `GrowMaskWithBlur` —— 1/2 个有
- `Image Filter Adjustments` —— 1/2 个有
- `ImageComposite+` —— 1/2 个有
- `LayerUtility: HLFrequencyDetailRestore` —— 1/2 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/2 个有
- `MaskFastGrow` —— 1/2 个有
- `RMBG` —— 1/2 个有
- `孤海图像缩放按像素` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 27.5 | - | 2 | 91% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 27.5，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
