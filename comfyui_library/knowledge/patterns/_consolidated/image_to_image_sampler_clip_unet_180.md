---
name: image_to_image_sampler_clip_unet_180
type: Image To Image
frequency: 3
level: moderate
coverage: 0.657667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Float, GetNode, Image Comparer (rgthree), Int, KSampler, LoadImage, SaveImage, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageListToImageBatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image -ttp分块放大_高清修复_2005152050122031105.json, 图片生成/图生图/Z-image-TTP优化细节放大（自用）_2013095850817363969.json, 平台全量/Z-image-TTP优化细节放大_2010605475443777537.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_180

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Z-image -ttp分块放大_高清修复_2005152050122031105.json、图片生成/图生图/Z-image-TTP优化细节放大（自用）_2013095850817363969.json、平台全量/Z-image-TTP优化细节放大_2010605475443777537.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Float`
- `GetNode`
- `Image Comparer (rgthree)`
- `Int`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `SetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadFlorence2Model` —— 2/3 个有
- `Florence2Run` —— 2/3 个有
- `ImageUpscaleWithModel` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `easy compare` —— 2/3 个有
- `easy imageBatchToImageList` —— 2/3 个有
- `ConstrainImage|pysssss` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `easy int` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 10 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | kl_optimal | - | 3 | 33% |
| 重绘幅度 | 0.9 | 0.65 - 0.9 | 3 | 86% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 10，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 kl_optimal，3 个样本，一致性 33%
- 重绘幅度 中位数 0.9，观测区间 0.65 - 0.9，3 个样本，取值集中（一致性 86%）
