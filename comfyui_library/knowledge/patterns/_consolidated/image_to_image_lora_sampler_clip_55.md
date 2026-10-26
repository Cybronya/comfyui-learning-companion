---
name: image_to_image_lora_sampler_clip_55
type: Image To Image
frequency: 5
level: moderate
coverage: 0.9524
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/V3-图像超分放大-精修_高清放大_2082292491298099201.json, 图片生成/图生图/V3-图像超分放大-精修_高清放大_2082295257340932098.json, 图片生成/图生图/image2.0高清修图615最优版_2066373652978950146.json, 图片生成/图生图/修复过拟合噪点_2087789964036755457.json, 图片生成/图生图/细节爆炸！让你的图片从“能看”到“震撼”！Klein+SeedVR2双重采样高清放大超分无损精修_1967301012027478018.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_55

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/V3-图像超分放大-精修_高清放大_2082292491298099201.json、图片生成/图生图/V3-图像超分放大-精修_高清放大_2082295257340932098.json、图片生成/图生图/image2.0高清修图615最优版_2066373652978950146.json、图片生成/图生图/修复过拟合噪点_2087789964036755457.json、图片生成/图生图/细节爆炸！让你的图片从“能看”到“震撼”！Klein+SeedVR2双重采样高清放大超分无损精修_1967301012027478018.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `easy imageColorMatch` —— 4/5 个有
- `CheckpointLoaderSimple` —— 3/5 个有
- `INTConstant` —— 3/5 个有
- `ImageScaleToTotalPixels` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `LayerUtility: ImageScaleRestore V2` —— 3/5 个有
- `MathExpression|pysssss` —— 3/5 个有
- `PathchSageAttentionKJ` —— 3/5 个有
- `SeedVR2Conditioning` —— 3/5 个有
- `SeedVR2Preprocess` —— 3/5 个有
- `VAEEncodeTiled` —— 3/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `KSamplerAdvanced` —— 2/5 个有
- `SeedVR2PostProcessing` —— 2/5 个有
- `ColorMatchPro` —— 1/5 个有
- `LayerFilter: GaussianBlur` —— 1/5 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有
- `easy imageConcat` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1 | 1 - 4 | 5 | 33% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 60% |
| 调度器 | linear_quadratic | - | 5 | 40% |
| 重绘幅度 | 1 | 0.25 - 1 | 5 | 48% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 1，观测区间 1 - 4，5 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 60%
- 调度器 最常用 linear_quadratic，5 个样本，一致性 40%
- 重绘幅度 中位数 1，观测区间 0.25 - 1，5 个样本，取值分散，一致性仅 48%
- 高发问题（8/5 个样本）：Steps较低可能导致细节不足
