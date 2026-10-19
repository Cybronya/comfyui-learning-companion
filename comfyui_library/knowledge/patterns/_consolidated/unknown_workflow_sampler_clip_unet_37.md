---
name: unknown_workflow_sampler_clip_unet_37
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.940857
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [Fans Prompt Styler Negative]
members: [图片生成/文生图/1951256026077188097.json, 图片生成/文生图/1951281909651419137.json, 图片生成/文生图/1951839776326537218.json, 图片生成/文生图/1951967199781179393.json, 图片生成/文生图/1952021213906415618.json, 图片生成/文生图/1959107680914845697.json, 图片生成/文生图/1960596890238746626.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_37

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1951256026077188097.json、图片生成/文生图/1951281909651419137.json、图片生成/文生图/1951839776326537218.json、图片生成/文生图/1951967199781179393.json、图片生成/文生图/1952021213906415618.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/7 个有
- `Image Comparer (rgthree)` —— 2/7 个有
- `Fans Prompt Styler Negative` —— 1/7 个有
- `FluxKontextImageScale` —— 1/7 个有
- `HYPIRImageRestoration` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 25 | 7 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 71% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 25，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Fans Prompt Styler Negative
