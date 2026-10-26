---
name: unknown_workflow_generic_1646
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.75
common_nodes: [LoadImage, RHLLMChatNode, ShowText|pysssss]
problems: []
missing: []
members: [图片生成/文生图/空白工作流rr_2078234563565940738.json, 数字人/数字人/空白工作流rr_2078413430951858178.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1646

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/空白工作流rr_2078234563565940738.json、数字人/数字人/空白工作流rr_2078413430951858178.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `RHLLMChatNode`
- `ShowText|pysssss`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 1/2 个有
- `SaveText` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
