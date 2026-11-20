---
name: unknown_workflow_sampler_unet_vae_301
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.85675
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, MiniMaxH3ImageConditioning, PrimitiveStringMultiline, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/Minimax-H3-image  文生图_2120392021948063745.json, 平台全量/Minimax-H3-image  文生图_2120409098842890241.json, 平台全量/Minimax-H3-image 官方版 _ 文生图_2120364083680735233.json, 平台全量/文生图-Minimax-H3-image_2121183852818427905.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_301

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/Minimax-H3-image  文生图_2120392021948063745.json、平台全量/Minimax-H3-image  文生图_2120409098842890241.json、平台全量/Minimax-H3-image 官方版 _ 文生图_2120364083680735233.json、平台全量/文生图-Minimax-H3-image_2121183852818427905.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `MiniMaxH3ImageConditioning`
- `PrimitiveStringMultiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 3/4 个有
- `CM_FloatToInt` —— 2/4 个有
- `ResolutionSelector` —— 2/4 个有
- `KOOK_SaveJPGImage` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 6 | 4 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 6，4 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
