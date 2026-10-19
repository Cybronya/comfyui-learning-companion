---
name: unknown_workflow_sampler_checkpoint_vae_19
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CheckpointLoaderSimple, EmptyLatentImage, KSampler, LoadImage, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1976881433581178881.json, 图片生成/文生图/1978426223942635521.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_19

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1976881433581178881.json、图片生成/文生图/1978426223942635521.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | sa_solver | - | 2 | 50% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 744 | - | 2 | 97% |
| 高度 | 1312 | - | 2 | 98% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，2 个样本，一致性 50%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 744，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- 高度 中位数 1312，样本不足，未给区间，2 个样本，取值集中（一致性 98%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
