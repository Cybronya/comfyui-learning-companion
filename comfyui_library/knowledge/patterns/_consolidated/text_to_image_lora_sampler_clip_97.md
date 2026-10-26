---
name: text_to_image_lora_sampler_clip_97
type: Text To Image
frequency: 13
level: strong
coverage: 0.909769
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2026人像高清放大｜图生图老图秒变高清大图_2111355986270310402.json, 图片生成/图生图/Flux.2 Klein细节增强精修｜图生图质感细节双拉满_2106268265885552641.json, 图片生成/图生图/Flux2 Klein细节增强工作流，人物皮肤精修图生图处理工具_2106526010383622146.json, 图片生成/图生图/Krea2加Klein双采样高清放大工作流，图生图高清放大处理工具_2108321418625773570.json, 图片生成/图生图/Krea2高清修复4K细节｜去AI塑料感画质精修_2095954838394851330.json, 图片生成/图生图/Krea2高清修复工作流｜图生图还原真实质感_2090087487157915649.json, 图片生成/图生图/人物皮肤质感加克莱因高清 图片分辨率提升画质增强_2109005610992889857.json, 图片生成/图生图/新版人像高清放大 精修皮肤质感图生图处理工具_2114046970154274818.json, 图片生成/图生图/新版人像高清放大御川0721｜皮肤质感nice精修必备_2113896950406934530.json, 图片生成/图生图/最新4K高清修复｜Krea2细节精修放大工作流_2092885864887185410.json, 图片生成/图生图/男生大头优化4K｜图生图头像特写放大 细节皮肤都在线_2097564369910591489.json, 图片生成/图生图/高清修复4k细节Krea2最新工作流 图片分辨率提升画质增强_2109395790539087874.json, 图片生成/图生图/高清修复去除塑料感｜Krea2 4K细节精修图生图_2096246778885664770.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_97

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/2026人像高清放大｜图生图老图秒变高清大图_2111355986270310402.json、图片生成/图生图/Flux.2 Klein细节增强精修｜图生图质感细节双拉满_2106268265885552641.json、图片生成/图生图/Flux2 Klein细节增强工作流，人物皮肤精修图生图处理工具_2106526010383622146.json、图片生成/图生图/Krea2加Klein双采样高清放大工作流，图生图高清放大处理工具_2108321418625773570.json、图片生成/图生图/Krea2高清修复4K细节｜去AI塑料感画质精修_2095954838394851330.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `EditTextEncode_EditUtils` —— 11/13 个有
- `Flux2KleinConfigPreparer_EditUtils` —— 11/13 个有
- `Flux2KleinModelConfig_EditUtils` —— 11/13 个有
- `FluxKVCache` —— 11/13 个有
- `ImageUpscaleWithModel` —— 11/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/13 个有
- `PrimitiveFloat` —— 11/13 个有
- `UpscaleModelLoader` —— 11/13 个有
- `VAEDecodeTiled` —— 11/13 个有
- `VAEEncodeTiled` —— 11/13 个有
- `easy cleanGpuUsed` —— 11/13 个有
- `easy imageColorMatch` —— 11/13 个有
- `Image Comparer (rgthree)` —— 10/13 个有
- `Flux2KleinOutputExtractor_EditUtils` —— 9/13 个有
- `PreviewImage` —— 7/13 个有
- `LatentColorMatchSimple` —— 5/13 个有
- `Anything Everywhere3` —— 4/13 个有
- `CR Text` —— 2/13 个有
- `EmptyFlux2LatentImage` —— 2/13 个有
- `CheckpointLoaderSimple` —— 1/13 个有
- `ColorMatchPro` —— 1/13 个有
- `Fast Groups Bypasser (rgthree)` —— 1/13 个有
- `Flux2KleinEditTextEncode_EditUtils` —— 1/13 个有
- `INTConstant` —— 1/13 个有
- `LCSColorAnchor` —— 1/13 个有
- `LCSLoadData` —— 1/13 个有
- `LayerUtility: ImageScaleRestore V2` —— 1/13 个有
- `MemoryCleaner` —— 1/13 个有
- `PathchSageAttentionKJ` —— 1/13 个有
- `RHHiddenNodes` —— 1/13 个有
- `SeedVR2Conditioning` —— 1/13 个有
- `SeedVR2Preprocess` —— 1/13 个有
- `SimpleMath+` —— 1/13 个有
- `TTP_Image_Assy` —— 1/13 个有
- `TTP_Image_Tile_Batch` —— 1/13 个有
- `TTP_Tile_image_size` —— 1/13 个有
- `easy imageBatchToImageList` —— 1/13 个有
- `easy imageListToImageBatch` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 27/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（27/13 个样本）：Steps较低可能导致细节不足
