---
name: image_to_image_sampler_clip_unet_65
type: Image To Image
frequency: 6
level: moderate
coverage: 0.931833
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/01-06-01-QwenImage图生图V1（文字自动修复）_1986833915342221314.json, 图片生成/图生图/3d卡通可爱系风格-klein_2042859666035712002.json, 图片生成/图生图/F2K 白模建筑参考图渲染（指定风格参考图）_2058049321479794689.json, 图片生成/图生图/Qwen-Image-2512图生图_1953010725393526786.json, 图片生成/图生图/产品换背景-klein_2042792273842282498.json, 图片生成/图生图/粉嫩皮肤 Klein 9B_2044917625544773634.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_65

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/01-06-01-QwenImage图生图V1（文字自动修复）_1986833915342221314.json、图片生成/图生图/3d卡通可爱系风格-klein_2042859666035712002.json、图片生成/图生图/F2K 白模建筑参考图渲染（指定风格参考图）_2058049321479794689.json、图片生成/图生图/Qwen-Image-2512图生图_1953010725393526786.json、图片生成/图生图/产品换背景-klein_2042792273842282498.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `ReferenceLatent` —— 4/6 个有
- `scale` —— 4/6 个有
- `Flux2KleinModelConfig_EditUtils` —— 3/6 个有
- `ModelSamplingAuraFlow` —— 3/6 个有
- `AdaptiveLongestEdge_EditUtils` —— 2/6 个有
- `EmptySD3LatentImage` —— 2/6 个有
- `Flux2KleinConfigPreparer_EditUtils` —— 2/6 个有
- `EditTextEncode_EditUtils` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `KSamplerAdvanced` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/6 个有
- `UnetLoaderGGUF` —— 1/6 个有
- `easy clearCacheAll` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 3 | 2 - 8 | 6 | 42% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 50% |
| 重绘幅度 | 1 | 0.3 - 1 | 6 | 64% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 3，观测区间 2 - 8，6 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，6 个样本
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
