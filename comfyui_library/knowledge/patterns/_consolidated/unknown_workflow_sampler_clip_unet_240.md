---
name: unknown_workflow_sampler_clip_unet_240
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.933833
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/千问2512文生图海报、图片设计_2093310820385116161.json, 图片生成/文生图/小红书风格加黑丝_2003393169008041986.json, 图片生成/文生图/小腰精_01_2037141728938958849.json, 图片生成/文生图/小腰精_胸部_2103720016867848193.json, 图片生成/文生图/文生图  boogu_2067835171948290050.json, 图片生成/文生图/文生图(人像)_2006960061226164225.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_240

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/千问2512文生图海报、图片设计_2093310820385116161.json、图片生成/文生图/小红书风格加黑丝_2003393169008041986.json、图片生成/文生图/小腰精_01_2037141728938958849.json、图片生成/文生图/小腰精_胸部_2103720016867848193.json、图片生成/文生图/文生图  boogu_2067835171948290050.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 5/6 个有
- `EmptySD3LatentImage` —— 4/6 个有
- `LoraLoader` —— 4/6 个有
- `ConditioningZeroOut` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `QwenImageLatentAspectRatio` —— 2/6 个有
- `ConditioningCombine` —— 1/6 个有
- `ConditioningSetTimestepRange` —— 1/6 个有
- `VideoLinearCFGGuidance` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8.5 | 4 - 12 | 6 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 6 | 0% |
| 采样算法 | euler | - | 6 | 50% |
| 调度器 | simple | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 模型强度 | 1 | 0.8 - 1 | 4 | 91% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8.5，观测区间 4 - 12，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，6 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，6 个样本，一致性 50%
- 调度器 最常用 simple，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 0.8 - 1，4 个样本，取值集中（一致性 91%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/6 个样本）：Steps较低可能导致细节不足
