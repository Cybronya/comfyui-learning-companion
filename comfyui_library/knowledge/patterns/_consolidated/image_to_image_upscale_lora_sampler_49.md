---
name: image_to_image_upscale_lora_sampler_49
type: Image To Image
frequency: 3
level: strong
coverage: 0.827667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DF_Integer, GetImageSize+, Image Comparer (rgthree), ImageUpscaleWithModel, Int, JWFloat, KSampler, LG_Color_Match_V2, Latent Noise Injection, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, RHHiddenNodes, ResizeAndPadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy boolean, easy ifElse, easy imageBatchToImageList, easy imageScaleDownBy]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/无损放大（产品专用）_2099322829899649026.json, 图片生成/图生图/无损放大_2070443812324990977.json, 图片生成/图生图/杂志修图_2054000139198574593.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_49

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/无损放大（产品专用）_2099322829899649026.json、图片生成/图生图/无损放大_2070443812324990977.json、图片生成/图生图/杂志修图_2054000139198574593.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DF_Integer`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `Int`
- `JWFloat`
- `KSampler`
- `LG_Color_Match_V2`
- `Latent Noise Injection`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RHHiddenNodes`
- `ResizeAndPadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy boolean`
- `easy ifElse`
- `easy imageBatchToImageList`
- `easy imageScaleDownBy`

**可变部分**（部分 workflow 才有）：
- `GrowMask` —— 2/3 个有
- `InvertMask` —— 2/3 个有
- `JoinImageWithAlpha` —— 2/3 个有
- `LayerMask: BiRefNetUltraV2` —— 2/3 个有
- `LayerMask: LoadBiRefNetModelV2` —— 2/3 个有
- `Upscale Model Loader` —— 2/3 个有
- `YUAN_TXTConvertAny` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 5 - 5 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | kl_optimal | - | 3 | 100% |
| 重绘幅度 | 0.7 | 0.7 - 0.7 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 5 - 5，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 kl_optimal，3 个样本，一致性 100%
- 重绘幅度 中位数 0.7，观测区间 0.7 - 0.7，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
