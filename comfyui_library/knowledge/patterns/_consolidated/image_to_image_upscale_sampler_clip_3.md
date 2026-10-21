---
name: image_to_image_upscale_sampler_clip_3
type: Image To Image
frequency: 6
level: moderate
coverage: 0.729167
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-IMAGE-BASE大合集支持文生图 _ 图片洗图_2016207552249339905.json, 图片生成/文生图/Z-Image Base 极致写实+文生图_图生图洗图 SeedVR2.5 + TTP 高清放大_2016741486603276289.json, 图片生成/文生图/Z-Image-Base大合集+文生图+洗图_2016472904732516353.json, 图片生成/文生图/Z-Image文生图+洗图+seedVR2超清放大_1997890617130803201.json, 图片生成/文生图/☃️开源王者 Z-IMAGE-BASE大合集支持文生图 _ 图片洗图_2016340251035308033.json, 视频生成/文生视频/Z Image Base 极致写实+文生图_图生图洗图 SeedVR2.5 + TTP 高清放大_2016769190719393793.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_3

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Z-IMAGE-BASE大合集支持文生图 _ 图片洗图_2016207552249339905.json、图片生成/文生图/Z-Image Base 极致写实+文生图_图生图洗图 SeedVR2.5 + TTP 高清放大_2016741486603276289.json、图片生成/文生图/Z-Image-Base大合集+文生图+洗图_2016472904732516353.json、图片生成/文生图/Z-Image文生图+洗图+seedVR2超清放大_1997890617130803201.json、图片生成/文生图/☃️开源王者 Z-IMAGE-BASE大合集支持文生图 _ 图片洗图_2016340251035308033.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 5/6 个有
- `INTConstant` —— 5/6 个有
- `Image Filter Adjustments` —— 5/6 个有
- `ImageScaleBy` —— 5/6 个有
- `ImpactInt` —— 5/6 个有
- `ModelSamplingAuraFlow` —— 5/6 个有
- `PlaySound|pysssss` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `PrimitiveFloat` —— 5/6 个有
- `SomethingToString` —— 5/6 个有
- `ConditioningZeroOut` —— 1/6 个有
- `Float` —— 1/6 个有
- `KOOK_ImageCompression` —— 1/6 个有
- `KOOK_SaveJPGImage` —— 1/6 个有
- `easy clearCacheAll` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 9 - 25 | 6 | 73% |
| Prompt 约束强度(CFG) | 3 | 1 - 3 | 6 | 72% |
| 采样算法 | res_multistep | - | 6 | 83% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 0.9 - 1 | 6 | 96% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 9 - 25，6 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 3，6 个样本
- 采样算法 最常用 res_multistep，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.9 - 1，6 个样本，取值集中（一致性 96%）
