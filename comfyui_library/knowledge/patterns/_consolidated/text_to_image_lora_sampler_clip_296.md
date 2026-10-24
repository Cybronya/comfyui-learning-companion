---
name: text_to_image_lora_sampler_clip_296
type: Text To Image
frequency: 6
level: strong
coverage: 0.928833
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, INTConstant, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleRestore V2, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, ReferenceLatent, SaveImage, SeedVR2Conditioning, SeedVR2Preprocess, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Klein+SeedVR2双重采样 图片细节爆炸级高清放大超分无损精修_2104831073623568386.json, 图片生成/图生图/Klein+SeedVR2双重采样超分精修｜高清放大8K无损细节爆炸_2089445167932723202.json, 图片生成/图生图/Klein+SeedVR2双重采样｜高清放大超分精修 细节震撼无损_2089263939329810434.json, 图片生成/图生图/Klein加SeedVR2双重采样高清放大超分无损精修，细节爆炸图生图工具_2106098682989989889.json, 图片生成/图生图/V3-图像超分放大_精修_高清放大_2081985549186977794.json, 图片生成/图生图/细节爆炸让你的图片从能看到震撼 Klein加SeedVR2双重采样高清放大超分无损精修_2109694895496712194.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_296

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Klein+SeedVR2双重采样 图片细节爆炸级高清放大超分无损精修_2104831073623568386.json、图片生成/图生图/Klein+SeedVR2双重采样超分精修｜高清放大8K无损细节爆炸_2089445167932723202.json、图片生成/图生图/Klein+SeedVR2双重采样｜高清放大超分精修 细节震撼无损_2089263939329810434.json、图片生成/图生图/Klein加SeedVR2双重采样高清放大超分无损精修，细节爆炸图生图工具_2106098682989989889.json、图片生成/图生图/V3-图像超分放大_精修_高清放大_2081985549186977794.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `INTConstant`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleRestore V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2Conditioning`
- `SeedVR2Preprocess`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAEEncodeTiled`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 5/6 个有
- `JjkText` —— 5/6 个有
- `LayerFilter: GaussianBlur` —— 5/6 个有
- `RHHiddenNodes` —— 5/6 个有
- `easy imageConcat` —— 5/6 个有
- `孤海注释` —— 5/6 个有
- `SeedVR2PostProcessing` —— 3/6 个有
- `easy imageColorMatch` —— 3/6 个有
- `ColorMatchPro` —— 2/6 个有
- `MathExpression|pysssss` —— 2/6 个有
- `CR Prompt Text` —— 1/6 个有
- `ImageScaleToTotalPixels` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `ShunjingAIShade` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（18/6 个样本）：Steps较低可能导致细节不足
