---
name: text_to_image_sampler_clip_unet_62
type: Text To Image
frequency: 8
level: weak
coverage: 0.859125
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/二次元-anima模型-文生图_2055198430875660289.json, 图片生成/文生图/写实 文生图_2068912035760529409.json, 图片生成/文生图/动漫专用模型文生图_2019252456521211906.json, 图片生成/文生图/太猛了！Z-image文生图新王-支持中文！_1995051018658492417.json, 图片生成/文生图/布谷boogu_image_turbo文生图_2074490110728560642.json, 图片生成/文生图/文生图_2028064937913880578.json, 图片生成/文生图/文生图。Zimage（支持真人的国产加速模型）_2028059294964387841.json, 图片生成/文生图/电商一键生成模特 Z-Image_2012713566901637122.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_62

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/二次元-anima模型-文生图_2055198430875660289.json、图片生成/文生图/写实 文生图_2068912035760529409.json、图片生成/文生图/动漫专用模型文生图_2019252456521211906.json、图片生成/文生图/太猛了！Z-image文生图新王-支持中文！_1995051018658492417.json、图片生成/文生图/布谷boogu_image_turbo文生图_2074490110728560642.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/8 个有
- `PrimitiveInt` —— 3/8 个有
- `JjkText` —— 2/8 个有
- `PrimitiveStringMultiline` —— 2/8 个有
- `EasyCache` —— 1/8 个有
- `ResolutionSelector` —— 1/8 个有
- `SaveAnimatedWEBP` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1180 | 832 - 2048 | 8 | 67% |
| 高度 | 1248 | 720 - 2280 | 8 | 64% |
| 采样步数 | 20 | 4 - 35 | 8 | 33% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 5.5 | 8 | 32% |
| 采样算法 | euler | - | 8 | 50% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1180，观测区间 832 - 2048，8 个样本
- 高度 中位数 1248，观测区间 720 - 2280，8 个样本
- 采样步数 中位数 20，观测区间 4 - 35，8 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 5.5，8 个样本，取值分散，一致性仅 32%
- 采样算法 最常用 euler，8 个样本，一致性 50%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
