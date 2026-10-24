---
name: unknown_workflow_sampler_clip_unet_390
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.964667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, SaveImage, Seed (rgthree), SizeNode, UNETLoader, VAEDecode, VAELoader, easy promptLine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/z-image 去杂乱的噪点，保留细节_2005172510469615617.json, 图片生成/文生图/【LG】细节增强优化版_2004297248144064513.json, 图片生成/文生图/【LG】细节增强优化版_2015060948377149441.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_390

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/z-image 去杂乱的噪点，保留细节_2005172510469615617.json、图片生成/文生图/【LG】细节增强优化版_2004297248144064513.json、图片生成/文生图/【LG】细节增强优化版_2015060948377149441.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `Seed (rgthree)`
- `SizeNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 2/3 个有
- `GenerateNoise` —— 2/3 个有
- `LGNoiseInjectionLatent` —— 2/3 个有
- `BNK_InjectNoise` —— 1/3 个有
- `BNK_NoisyLatentImage` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `RescaleCFG` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 3 - 4 | 3 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 0.3 - 1 | 3 | 57% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 3 - 4，3 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，3 个样本
- 高发问题（8/3 个样本）：Steps较低可能导致细节不足
