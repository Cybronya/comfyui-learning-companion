---
name: image_to_image_lora_sampler_clip_37
type: Image To Image
frequency: 9
level: moderate
coverage: 0.932778
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/V3-图像超分放大-精修_高清放大_2082292491298099201.json, 图片生成/图生图/V3-图像超分放大-精修_高清放大_2082295257340932098.json, 图片生成/图生图/image2.0高清修图615最优版_2066373652978950146.json, 图片生成/图生图/修复过拟合噪点_2087789964036755457.json, 图片生成/图生图/细节爆炸！让你的图片从“能看”到“震撼”！Klein+SeedVR2双重采样高清放大超分无损精修_1967301012027478018.json, 图片生成/图生图/细节爆炸！让你的图片从“能看”到“震撼”！Klein+SeedVR2双重采样高清放大超分无损精修_2114719218620002306.json, 平台全量/SeedVR2官流超分 + Klein细节修复_2082201077746851841.json, 平台全量/图像超分放大V3_2080293907216289794.json, 平台全量/豹豹喵呜制作：图像超分放大V3_2080220449409167361.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_37

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/V3-图像超分放大-精修_高清放大_2082292491298099201.json、图片生成/图生图/V3-图像超分放大-精修_高清放大_2082295257340932098.json、图片生成/图生图/image2.0高清修图615最优版_2066373652978950146.json、图片生成/图生图/修复过拟合噪点_2087789964036755457.json、图片生成/图生图/细节爆炸！让你的图片从“能看”到“震撼”！Klein+SeedVR2双重采样高清放大超分无损精修_1967301012027478018.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 9 个 workflow 都包含：
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
- `INTConstant` —— 7/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/9 个有
- `LayerUtility: ImageScaleRestore V2` —— 7/9 个有
- `MathExpression|pysssss` —— 7/9 个有
- `SeedVR2Conditioning` —— 7/9 个有
- `SeedVR2Preprocess` —— 7/9 个有
- `VAEEncodeTiled` —— 7/9 个有
- `easy imageColorMatch` —— 7/9 个有
- `PathchSageAttentionKJ` —— 6/9 个有
- `CheckpointLoaderSimple` —— 5/9 个有
- `ImageScaleToTotalPixels` —— 5/9 个有
- `SeedVR2PostProcessing` —— 5/9 个有
- `ImageResizeKJv2` —— 2/9 个有
- `KSamplerAdvanced` —— 2/9 个有
- `Label (rgthree)` —— 2/9 个有
- `LayerFilter: GaussianBlur` —— 2/9 个有
- `RHHiddenNodes` —— 2/9 个有
- `easy imageConcat` —— 2/9 个有
- `ColorMatchPro` —— 1/9 个有
- `GetNode` —— 1/9 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/9 个有
- `SetNode` —— 1/9 个有
- `ShunjingAIShade` —— 1/9 个有
- `easy showAnything` —— 1/9 个有
- `ttN seed` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1 | 1 - 4 | 9 | 25% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 78% |
| 调度器 | linear_quadratic | - | 9 | 44% |
| 重绘幅度 | 1 | 0.25 - 1 | 9 | 63% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 1，观测区间 1 - 4，9 个样本，取值分散，一致性仅 25%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 78%
- 调度器 最常用 linear_quadratic，9 个样本，一致性 44%
- 重绘幅度 中位数 1，观测区间 0.25 - 1，9 个样本
- 高发问题（16/9 个样本）：Steps较低可能导致细节不足
