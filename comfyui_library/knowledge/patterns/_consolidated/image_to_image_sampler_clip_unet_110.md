---
name: image_to_image_sampler_clip_unet_110
type: Image To Image
frequency: 5
level: moderate
coverage: 0.9182
common_nodes: [CLIPLoader, CLIPTextEncode, Image Comparer (rgthree), KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/01-06-01-QwenImage图生图V1（文字自动修复）_1986833915342221314.json, 图片生成/图生图/3d卡通可爱系风格-klein_2042859666035712002.json, 图片生成/图生图/F2K 白模建筑参考图渲染（指定风格参考图）_2058049321479794689.json, 图片生成/图生图/产品换背景-klein_2042792273842282498.json, 图片生成/图生图/粉嫩皮肤 Klein 9B_2044917625544773634.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_110

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/01-06-01-QwenImage图生图V1（文字自动修复）_1986833915342221314.json、图片生成/图生图/3d卡通可爱系风格-klein_2042859666035712002.json、图片生成/图生图/F2K 白模建筑参考图渲染（指定风格参考图）_2058049321479794689.json、图片生成/图生图/产品换背景-klein_2042792273842282498.json、图片生成/图生图/粉嫩皮肤 Klein 9B_2044917625544773634.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/5 个有
- `ReferenceLatent` —— 4/5 个有
- `Flux2KleinModelConfig_EditUtils` —— 3/5 个有
- `scale` —— 3/5 个有
- `AdaptiveLongestEdge_EditUtils` —— 2/5 个有
- `EmptySD3LatentImage` —— 2/5 个有
- `Flux2KleinConfigPreparer_EditUtils` —— 2/5 个有
- `ModelSamplingAuraFlow` —— 2/5 个有
- `EditTextEncode_EditUtils` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `KSamplerAdvanced` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/5 个有
- `UnetLoaderGGUF` —— 1/5 个有
- `easy clearCacheAll` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 2 | 2 - 8 | 5 | 35% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 0.3 - 1 | 5 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 2，观测区间 2 - 8，5 个样本，取值分散，一致性仅 35%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，5 个样本
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
