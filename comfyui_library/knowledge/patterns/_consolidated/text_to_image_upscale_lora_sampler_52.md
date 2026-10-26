---
name: text_to_image_upscale_lora_sampler_52
type: Text To Image
frequency: 5
level: strong
coverage: 0.9308
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize, INTConstant, JjkText, KSampler, LayerColor: ColorAdapter, LayerFilter: GaussianBlur, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, RHHiddenNodes, SaveImage, SeedVR2Conditioning, SeedVR2Preprocess, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader, VOSR2ModelLoader, VOSR2Upscale, easy imageConcat, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/1分钟极速放大糊图变4K VOSR2+SeedVR2无损超分高清放大最快模型_2104762415798906881.json, 图片生成/图生图/SeedVR2 官方无损超分｜1分钟极速放大糊图文字变4K超清_2096883810347610113.json, 图片生成/图生图/SeedVR2官方无损超分放大 糊图文字极速变4K超清_2099183470638616577.json, 图片生成/图生图/SeedVR2官方无损超分流｜1分钟糊图变4K超清，文字不糊当前最快_2099464792846196738.json, 图片生成/图生图/VOSR2+SeedVR2双引擎高清放大｜糊图文字无损变4K超清，一分钟极速出图_2104479741754568705.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_52

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/1分钟极速放大糊图变4K VOSR2+SeedVR2无损超分高清放大最快模型_2104762415798906881.json、图片生成/图生图/SeedVR2 官方无损超分｜1分钟极速放大糊图文字变4K超清_2096883810347610113.json、图片生成/图生图/SeedVR2官方无损超分放大 糊图文字极速变4K超清_2099183470638616577.json、图片生成/图生图/SeedVR2官方无损超分流｜1分钟糊图变4K超清，文字不糊当前最快_2099464792846196738.json、图片生成/图生图/VOSR2+SeedVR2双引擎高清放大｜糊图文字无损变4K超清，一分钟极速出图_2104479741754568705.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize`
- `INTConstant`
- `JjkText`
- `KSampler`
- `LayerColor: ColorAdapter`
- `LayerFilter: GaussianBlur`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RHHiddenNodes`
- `SaveImage`
- `SeedVR2Conditioning`
- `SeedVR2Preprocess`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `easy imageConcat`
- `solarL_SaveImagesToZip`
- `孤海注释`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（10/5 个样本）：Steps较低可能导致细节不足
