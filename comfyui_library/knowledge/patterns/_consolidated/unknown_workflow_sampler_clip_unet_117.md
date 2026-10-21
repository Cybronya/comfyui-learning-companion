---
name: unknown_workflow_sampler_clip_unet_117
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.9065
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-text-360_2080631673103937538.json, 图片生成/文生图/Qwen_Image_2512版4步加速出图_2006606275999703041.json, 图片生成/文生图/Qwen_Image_2512版4步加速出图_2019651247913046018.json, 图片生成/文生图/Z-image Tubro文生图工作流，没有AI味的模型！_2061058146243801090.json, 图片生成/文生图/Z-image-淡妆浓抹V3.0文生图_2026649178574688257.json, 图片生成/文生图/Zimage-base+turbo双剑合璧，提升速度&增加多样性&兼顾turbo美学。_2017455925828788225.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_117

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Qwen-text-360_2080631673103937538.json、图片生成/文生图/Qwen_Image_2512版4步加速出图_2006606275999703041.json、图片生成/文生图/Qwen_Image_2512版4步加速出图_2019651247913046018.json、图片生成/文生图/Z-image Tubro文生图工作流，没有AI味的模型！_2061058146243801090.json、图片生成/文生图/Z-image-淡妆浓抹V3.0文生图_2026649178574688257.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `ConditioningZeroOut` —— 3/6 个有
- `LayerUtility: PurgeVRAM V2` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `StringConcatenate` —— 1/6 个有
- `VAEEncode` —— 1/6 个有
- `easy positive` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7.5 | 4 - 20 | 6 | 43% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 6 | 25% |
| 采样算法 | euler | - | 6 | 67% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7.5，观测区间 4 - 20，6 个样本，取值分散，一致性仅 43%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，6 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 euler，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
