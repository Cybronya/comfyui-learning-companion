---
name: image_to_image_upscale_sampler_clip_22
type: Image To Image
frequency: 5
level: strong
coverage: 0.7626
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ConstrainImage|pysssss, Image Comparer (rgthree), ImageUpscaleWithModel, KSampler, LoadImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image-TTP高清_2075758139307282433.json, 图片生成/图生图/Z-image-万物高清_无损放大_1998610398515462146.json, 图片生成/图生图/万物高清_无损放大_保留细节去AI感_2020203737612034049.json, 图片生成/图生图/重绘放大-造相 Z-image -ttp分块放大_2003719931206221825.json, 图片生成/图生图/🤩重绘放大-造相 Z-image -ttp分块放大_高清修复_1982910130675167234.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_22

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Z-image-TTP高清_2075758139307282433.json、图片生成/图生图/Z-image-万物高清_无损放大_1998610398515462146.json、图片生成/图生图/万物高清_无损放大_保留细节去AI感_2020203737612034049.json、图片生成/图生图/重绘放大-造相 Z-image -ttp分块放大_2003719931206221825.json、图片生成/图生图/🤩重绘放大-造相 Z-image -ttp分块放大_高清修复_1982910130675167234.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ConstrainImage|pysssss`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
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
- `GetNode` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `SaveImage` —— 2/5 个有
- `easy imageSave` —— 2/5 个有
- `Anything Everywhere` —— 1/5 个有
- `Float` —— 1/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `Int` —— 1/5 个有
- `LGNoiseInjection` —— 1/5 个有
- `SaveImageJPG_GH` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | kl_optimal | - | 5 | 100% |
| 重绘幅度 | 0.65 | 0.65 - 0.65 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 kl_optimal，5 个样本，一致性 100%
- 重绘幅度 中位数 0.65，观测区间 0.65 - 0.65，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
