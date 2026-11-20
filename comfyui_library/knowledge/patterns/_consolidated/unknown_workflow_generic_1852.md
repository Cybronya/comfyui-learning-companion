---
name: unknown_workflow_generic_1852
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7915
common_nodes: [LoadImage, Qwen3_VQA, SaveImage, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/千问最强反推工作流_2050531267967496193.json, 平台全量/frkhgbsfjbrewgwer_2000409424734846978.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1852

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/千问最强反推工作流_2050531267967496193.json、平台全量/frkhgbsfjbrewgwer_2000409424734846978.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `Qwen3_VQA`
- `SaveImage`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Image Input Switch` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
