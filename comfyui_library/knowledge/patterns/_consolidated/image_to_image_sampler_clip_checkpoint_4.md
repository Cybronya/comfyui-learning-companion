---
name: image_to_image_sampler_clip_checkpoint_4
type: Image To Image
frequency: 6
level: moderate
coverage: 0.6405
common_nodes: [CLIPTextEncode, CR SDXL Aspect Ratio, CheckpointLoaderSimple, ConditioningCombine, ConditioningSetTimestepRange, ConditioningZeroOut, INTConstant, ImpactInt, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PrimitiveFloat, Qwen3_VQA, ShowText|pysssss, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/RED-Z-IMAGE-AIO洗图_2029881670488301569.json, 图片生成/图生图/Z-IMAGE-AIO_2056004983102951425.json, 图片生成/文生图/RED-Z-IMAGE-AIO-反推洗图_2002626517219831809.json, 图片生成/文生图/RED-Z-IMAGE-AIO-大合集_1998316097340342274.json, 图片生成/文生图/RED-Z-IMAGE-AIO-文生图 精准洗图!_1999684637897224193.json, 图片生成/文生图/Z-IMAGE 文生图 反推洗图_2010711633445785601.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_checkpoint_4

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/RED-Z-IMAGE-AIO洗图_2029881670488301569.json、图片生成/图生图/Z-IMAGE-AIO_2056004983102951425.json、图片生成/文生图/RED-Z-IMAGE-AIO-反推洗图_2002626517219831809.json、图片生成/文生图/RED-Z-IMAGE-AIO-大合集_1998316097340342274.json、图片生成/文生图/RED-Z-IMAGE-AIO-文生图 精准洗图!_1999684637897224193.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `CheckpointLoaderSimple`
- `ConditioningCombine`
- `ConditioningSetTimestepRange`
- `ConditioningZeroOut`
- `INTConstant`
- `ImpactInt`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PrimitiveFloat`
- `Qwen3_VQA`
- `ShowText|pysssss`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 5/6 个有
- `PlaySound|pysssss` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `SaveImage` —— 5/6 个有
- `INPAINT_ExpandMask` —— 4/6 个有
- `Image Comparer (rgthree)` —— 4/6 个有
- `ImageAndMaskPreview` —— 4/6 个有
- `ImageCompositeMasked` —— 4/6 个有
- `CompressImages` —— 1/6 个有
- `MemoryCleaner` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 9 - 10 | 6 | 95% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 3.5 | 6 | 56% |
| 采样算法 | dpmpp_2m_sde | - | 6 | 67% |
| 调度器 | karras | - | 6 | 67% |
| 重绘幅度 | 0.45 | 0.45 - 1 | 6 | 61% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 9 - 10，6 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 3.5，6 个样本
- 采样算法 最常用 dpmpp_2m_sde，6 个样本，一致性 67%
- 调度器 最常用 karras，6 个样本，一致性 67%
- 重绘幅度 中位数 0.45，观测区间 0.45 - 1，6 个样本
- 高发问题（4/6 个样本）：Steps较低可能导致细节不足
