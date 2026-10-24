---
name: image_to_image_sampler_clip_unet_132
type: Image To Image
frequency: 3
level: moderate
coverage: 0.867667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Image Comparer (rgthree), KSampler, LoadImage, PreviewImage, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX2-Klein高清图像4K放大增加细节8G显存可用_2013266120995770369.json, 图片生成/图生图/Z image参考图重绘+TTP放大_2013203346101899266.json, 图片生成/图生图/Z-Image 写实洗图，摄影风格_1994079561516335105.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_132

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/FLUX2-Klein高清图像4K放大增加细节8G显存可用_2013266120995770369.json、图片生成/图生图/Z image参考图重绘+TTP放大_2013203346101899266.json、图片生成/图生图/Z-Image 写实洗图，摄影风格_1994079561516335105.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
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
- `ImageUpscaleWithModel` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `ImageScaleBy` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `LG_Color_Match_V2` —— 1/3 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/3 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `ReferenceLatent` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 3 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.4 | 0.3 - 1 | 3 | 45% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.3 - 1，3 个样本，取值分散，一致性仅 45%
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
