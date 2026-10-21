---
name: image_to_image_sampler_clip_checkpoint_2
type: Image To Image
frequency: 4
level: moderate
coverage: 0.585
common_nodes: [CLIPTextEncode, CR SDXL Aspect Ratio, CheckpointLoaderSimple, ConditioningCombine, ConditioningSetTimestepRange, ConditioningZeroOut, Fast Groups Bypasser (rgthree), INTConstant, ImpactInt, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PlaySound|pysssss, PreviewImage, PrimitiveFloat, Qwen3_VQA, SaveImage, ShowText|pysssss, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/RED-Z-IMAGE-AIO-反推洗图_2002626517219831809.json, 图片生成/文生图/RED-Z-IMAGE-AIO-大合集_1998316097340342274.json, 图片生成/文生图/RED-Z-IMAGE-AIO-文生图 精准洗图!_1999684637897224193.json, 图片生成/文生图/Z-IMAGE 文生图 反推洗图_2010711633445785601.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_checkpoint_2

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/RED-Z-IMAGE-AIO-反推洗图_2002626517219831809.json、图片生成/文生图/RED-Z-IMAGE-AIO-大合集_1998316097340342274.json、图片生成/文生图/RED-Z-IMAGE-AIO-文生图 精准洗图!_1999684637897224193.json、图片生成/文生图/Z-IMAGE 文生图 反推洗图_2010711633445785601.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `CheckpointLoaderSimple`
- `ConditioningCombine`
- `ConditioningSetTimestepRange`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `ImpactInt`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PlaySound|pysssss`
- `PreviewImage`
- `PrimitiveFloat`
- `Qwen3_VQA`
- `SaveImage`
- `ShowText|pysssss`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `INPAINT_ExpandMask` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `ImageAndMaskPreview` —— 3/4 个有
- `ImageCompositeMasked` —— 3/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 9 - 10 | 4 | 95% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 3.5 | 4 | 62% |
| 采样算法 | dpmpp_2m_sde | - | 4 | 75% |
| 调度器 | karras | - | 4 | 75% |
| 重绘幅度 | 0.45 | 0.45 - 0.9 | 4 | 65% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 9 - 10，4 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 3.5，4 个样本
- 采样算法 最常用 dpmpp_2m_sde，4 个样本，一致性 75%
- 调度器 最常用 karras，4 个样本，一致性 75%
- 重绘幅度 中位数 0.45，观测区间 0.45 - 0.9，4 个样本
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
