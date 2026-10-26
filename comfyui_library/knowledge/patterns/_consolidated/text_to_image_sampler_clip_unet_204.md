---
name: text_to_image_sampler_clip_unet_204
type: Text To Image
frequency: 3
level: moderate
coverage: 0.490333
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, CR Text Input Switch (4 way), ConditioningZeroOut, EmptyLatentImage, GetNode, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: PurgeVRAM V2, RH_LLMAPI_NODE, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader, easy seed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/【112】Qwen image 2512文生图_2007067400860078082.json, 图片生成/文生图/【115】Flux2 Klein文生图，和Z-Image对比_2012439100267175938.json, 图片生成/文生图/【117】Z-image base加速 Mean（自定义）、Distill（自动提示词）_2022674191740313601.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_204

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/【112】Qwen image 2512文生图_2007067400860078082.json、图片生成/文生图/【115】Flux2 Klein文生图，和Z-Image对比_2012439100267175938.json、图片生成/文生图/【117】Z-image base加速 Mean（自定义）、Distill（自动提示词）_2022674191740313601.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：49%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Input Switch (4 way)`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetNode`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: PurgeVRAM V2`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `Qwen3VL_Chat` —— 2/3 个有
- `easy int` —— 2/3 个有
- `CFGNorm` —— 1/3 个有
- `EmptyFlux2LatentImage` —— 1/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `Int` —— 1/3 个有
- `LayerUtility: ColorImage` —— 1/3 个有
- `MeanCache_ZImage` —— 1/3 个有
- `QWEN3_Text` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | 512 - 896 | 3 | 76% |
| 高度 | 1200 | 512 - 1200 | 3 | 67% |
| 采样步数 | 12 | 8 - 25 | 3 | 52% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 3 | 53% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 896，观测区间 512 - 896，3 个样本
- 高度 中位数 1200，观测区间 512 - 1200，3 个样本
- 采样步数 中位数 12，观测区间 8 - 25，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
