---
name: text_to_image_lora_sampler_clip_612
type: Text To Image
frequency: 2
level: weak
coverage: 0.764
common_nodes: [Bounded Image Crop, Bounded Image Crop with Mask, CLIPLoader, CLIPTextEncode, ColorMatchV2, ConditioningZeroOut, EmptyLatentImage, GetImageSize, GetNode, ImageSmartSharpen+, ImageToMask, Int, KSampler, LayerUtility: ImageBlend, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, NoiseFromImage+, ReferenceLatent, ResizeAndPadImage, ResizeImageMixlab, ResizeLongestToNode, SaveImage, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Klein_TTP放大-写实自用_2100514063276138498.json, 图片生成/图生图/Klein_TTP放大-写实（自用）_2100074942904750082.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_612

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Klein_TTP放大-写实自用_2100514063276138498.json、图片生成/图生图/Klein_TTP放大-写实（自用）_2100074942904750082.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `Bounded Image Crop`
- `Bounded Image Crop with Mask`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatchV2`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetImageSize`
- `GetNode`
- `ImageSmartSharpen+`
- `ImageToMask`
- `Int`
- `KSampler`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `NoiseFromImage+`
- `ReferenceLatent`
- `ResizeAndPadImage`
- `ResizeImageMixlab`
- `ResizeLongestToNode`
- `SaveImage`
- `SetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
