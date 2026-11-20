---
name: text_to_image_upscale_lora_sampler_62
type: Text To Image
frequency: 4
level: strong
coverage: 0.891
common_nodes: [CLIPLoader, CLIPTextEncode, DF_Integer, EmptyLatentImage, Image Comparer (rgthree), ImageUpscaleWithModel, Int, JWFloat, JjkText, KSampler, LG_Color_Match_V2, LoadImage, LoraLoaderModelOnly, PreviewImage, RHHiddenNodes, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/产品专用无损放大｜反推提示词图生图｜商品细节放大不糊_2104814989918953474.json, 图片生成/图生图/人像专用无损放大｜图生图细节增强｜皮肤纹理不失真_2104786485156339714.json, 图片生成/图生图/无损放大人像专用图生图处理生成工作流工具_2102174442712555522.json, 图片生成/图生图/杂志级精修修图工作流，图生图质感高清还原_2111553319327064066.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_62

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/反推提示词/产品专用无损放大｜反推提示词图生图｜商品细节放大不糊_2104814989918953474.json、图片生成/图生图/人像专用无损放大｜图生图细节增强｜皮肤纹理不失真_2104786485156339714.json、图片生成/图生图/无损放大人像专用图生图处理生成工作流工具_2102174442712555522.json、图片生成/图生图/杂志级精修修图工作流，图生图质感高清还原_2111553319327064066.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DF_Integer`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `Int`
- `JWFloat`
- `JjkText`
- `KSampler`
- `LG_Color_Match_V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RHHiddenNodes`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GrowMask` —— 3/4 个有
- `InvertMask` —— 3/4 个有
- `JoinImageWithAlpha` —— 3/4 个有
- `LayerMask: BiRefNetUltraV2` —— 3/4 个有
- `LayerMask: LoadBiRefNetModelV2` —— 3/4 个有
- `Upscale Model Loader` —— 3/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `GetImageSize+` —— 2/4 个有
- `Latent Noise Injection` —— 2/4 个有
- `ModelSamplingAuraFlow` —— 2/4 个有
- `ResizeAndPadImage` —— 2/4 个有
- `SeedVR2LoadDiTModel` —— 2/4 个有
- `SeedVR2LoadVAEModel` —— 2/4 个有
- `SeedVR2VideoUpscaler` —— 2/4 个有
- `TTP_Image_Assy` —— 2/4 个有
- `TTP_Image_Tile_Batch` —— 2/4 个有
- `TTP_Tile_image_size` —— 2/4 个有
- `UpscaleModelLoader` —— 2/4 个有
- `VAEEncode` —— 2/4 个有
- `YUAN_TXTConvertAny` —— 2/4 个有
- `easy boolean` —— 2/4 个有
- `easy ifElse` —— 2/4 个有
- `easy imageBatchToImageList` —— 2/4 个有
- `easy imageScaleDownBy` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
