---
name: unknown_workflow_sampler_unet_vae_187
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.873667
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, PrimitiveStringMultiline, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2 风格参考文生图_2073326532138987522.json, 图片生成/文生图/Krea2 风格融合图生图_2073326336202076162.json, 图片生成/文生图/Krea2-双图风格融合_2073323590434516993.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_187

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Krea2 风格参考文生图_2073326532138987522.json、图片生成/文生图/Krea2 风格融合图生图_2073326336202076162.json、图片生成/文生图/Krea2-双图风格融合_2073323590434516993.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `PrimitiveStringMultiline`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Krea2StyleSemanticFusion` —— 2/3 个有
- `ResizeImagesByLongerEdge` —— 2/3 个有
- `EmptyLatentImage` —— 1/3 个有
- `Krea2StyleSemanticConditioning` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `ResolutionSelector` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.5 | 0.5 - 1 | 3 | 65% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.5，观测区间 0.5 - 1，3 个样本
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
