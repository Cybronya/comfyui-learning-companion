---
name: unknown_workflow_sampler_clip_vae_25
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.846333
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Model Input Switch, Note Plus (mtb)]
members: [图片生成/文生图/1959536155693887489.json, 图片生成/文生图/1960034364899930114.json, 图片生成/文生图/1960059347424456705.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_25

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1959536155693887489.json、图片生成/文生图/1960034364899930114.json、图片生成/文生图/1960059347424456705.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 2/3 个有
- `Int` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ModelPatchTorchSettings` —— 2/3 个有
- `Note Plus (mtb)` —— 2/3 个有
- `NunchakuQwenImageDiTLoader` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `CR Model Input Switch` —— 1/3 个有
- `EmptyUnitGenerator_UTK` —— 1/3 个有
- `TorchCompileModel` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 3 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 3 | 53% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Model Input Switch、Note Plus (mtb)
