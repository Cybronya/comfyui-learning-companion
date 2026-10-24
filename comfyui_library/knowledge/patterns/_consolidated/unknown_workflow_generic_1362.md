---
name: unknown_workflow_generic_1362
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [LoadImage, SaveImage, workflow>控制区]
problems: []
missing: []
members: [图片生成/图生图/去除人物AI感增强真实感工作流_2039606297762467841.json, 图片生成/图生图/高清2K换装-小红书FireRedTeam模型一键快速换服装（人物和场景统一不变）_2035023647248748545.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1362

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/去除人物AI感增强真实感工作流_2039606297762467841.json、图片生成/图生图/高清2K换装-小红书FireRedTeam模型一键快速换服装（人物和场景统一不变）_2035023647248748545.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `SaveImage`
- `workflow>控制区`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `EmptyLatentImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1152 | - | 1 | 100% |
| 高度 | 2048 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
