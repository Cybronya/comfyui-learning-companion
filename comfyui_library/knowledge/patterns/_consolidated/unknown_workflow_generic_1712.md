---
name: unknown_workflow_generic_1712
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [LoadImage, RH_Sora2_I2V_Batch, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/全能视频S多任务并发文生视频，一次生成最大150s视频只要5-10分钟_1998962356308824066.json, 视频生成/文生视频/批量视频生成_2001610943249412097.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1712

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/全能视频S多任务并发文生视频，一次生成最大150s视频只要5-10分钟_1998962356308824066.json、视频生成/文生视频/批量视频生成_2001610943249412097.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `RH_Sora2_I2V_Batch`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `StringConstantMultiline` —— 1/2 个有
- `TextBox3` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
