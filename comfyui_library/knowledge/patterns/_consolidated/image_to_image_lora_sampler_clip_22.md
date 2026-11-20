---
name: image_to_image_lora_sampler_clip_22
type: Image To Image
frequency: 11
level: strong
coverage: 0.870818
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, ImageListToBatch+, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TeaCache, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/Kontext 绝对无损放大_1964322385656729602.json, 平台全量/kontext 4k超高清放大_1965087677395685377.json, 平台全量/kontext_hires高清放大_1964533868026056705.json, 平台全量/kontext放大_1966335055926865922.json, 平台全量/全能图片V1-高清放大_1965584124150992897.json, 平台全量/千府AI_kontext_hires高清放大工作流_1967414688222941186.json, 平台全量/图片增强放大_1942871091381473282.json, 平台全量/图片葫芦娃Kontext高清放大_1977266445241470978.json, 平台全量/葫芦娃大佬一键4K高清放大工作流（Kontext+TTP）_1964253653546713090.json, 平台全量/葫芦版高清放大，无需反推_1978666717691924482.json, 平台全量/高清放大 kontext版本_1963553968231370753.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_22

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（平台全量/Kontext 绝对无损放大_1964322385656729602.json、平台全量/kontext 4k超高清放大_1965087677395685377.json、平台全量/kontext_hires高清放大_1964533868026056705.json、平台全量/kontext放大_1966335055926865922.json、平台全量/全能图片V1-高清放大_1965584124150992897.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageListToBatch+`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TeaCache`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 10/11 个有
- `LayerColor: ColorAdapter` —— 10/11 个有
- `LayerUtility: NumberCalculatorV2` —— 10/11 个有
- `LayerUtility: Seed` —— 9/11 个有
- `PrimitiveInt` —— 9/11 个有
- `ImpactImageBatchToImageList` —— 7/11 个有
- `LayerUtility: ImageMaskScaleAs` —— 5/11 个有
- `LayerUtility: ImageMaskScaleAsV2` —— 4/11 个有
- `ImageBatchToList+` —— 3/11 个有
- `ApplyFBCacheOnModel` —— 1/11 个有
- `Bjornulf_ShowInt` —— 1/11 个有
- `DF_Integer` —— 1/11 个有
- `EasyCache` —— 1/11 个有
- `PreviewImage` —— 1/11 个有
- `SimpleMath+` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 25 | 11 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 91% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 25，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
