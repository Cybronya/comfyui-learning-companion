---
name: image_to_image_upscale_sampler_clip_40
type: Image To Image
frequency: 2
level: weak
coverage: 0.681
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Float, GetNode, Image Comparer (rgthree), ImageUpscaleWithModel, Int, KSampler, LoadImage, PreviewImage, SaveImage, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image -ttp分块放大_高清修复_2005152050122031105.json, 图片生成/图生图/Z-image-TTP优化细节放大（自用）_2013095850817363969.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_40

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Z-image -ttp分块放大_高清修复_2005152050122031105.json、图片生成/图生图/Z-image-TTP优化细节放大（自用）_2013095850817363969.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Float`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `Int`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `ConstrainImage|pysssss` —— 1/2 个有
- `DownloadAndLoadFlorence2Model` —— 1/2 个有
- `Florence2Run` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `easy compare` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | kl_optimal | - | 2 | 50% |
| 重绘幅度 | 0.775 | - | 2 | 84% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 kl_optimal，2 个样本，一致性 50%
- 重绘幅度 中位数 0.775，样本不足，未给区间，2 个样本，取值集中（一致性 84%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
