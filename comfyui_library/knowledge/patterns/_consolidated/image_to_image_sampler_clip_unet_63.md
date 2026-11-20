---
name: image_to_image_sampler_clip_unet_63
type: Image To Image
frequency: 7
level: strong
coverage: 0.847857
common_nodes: [CLIPLoader, CLIPTextEncode, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图像去噪_2078426606925864962.json, 图片生成/图生图/图像放大修复｜自动反推提示词｜zimage- CN Tile_2004312182915563521.json, 图片生成/图生图/电商产品全能化妆品场景美妆白底图精修_2042856879147196418.json, 图片生成/图生图/电商产品全能场景人物手臂手势白底图精修_2048960893014249473.json, 图片生成/图生图/电商产品全能珠宝首饰场景戒指项链手镯白底图精修_2043516708916301826.json, 图片生成/图生图/电商人物修图全能场景模特人像白底图精修_2050541837659713538.json, 图片生成/文生图/电商产品全能珠宝首饰场景戒指项链手镯白底图精修_2112371719381016577.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_63

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/图像去噪_2078426606925864962.json、图片生成/图生图/图像放大修复｜自动反推提示词｜zimage- CN Tile_2004312182915563521.json、图片生成/图生图/电商产品全能化妆品场景美妆白底图精修_2042856879147196418.json、图片生成/图生图/电商产品全能场景人物手臂手势白底图精修_2048960893014249473.json、图片生成/图生图/电商产品全能珠宝首饰场景戒指项链手镯白底图精修_2043516708916301826.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 6/7 个有
- `ReferenceLatent` —— 6/7 个有
- `ConditioningCombine` —— 5/7 个有
- `ConditioningZeroOut` —— 2/7 个有
- `ModelPatchLoader` —— 1/7 个有
- `Qwen3_VQA` —— 1/7 个有
- `QwenImageDiffsynthControlnet` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有
- `ttN concat` —— 1/7 个有
- `ttN text` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 7 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
