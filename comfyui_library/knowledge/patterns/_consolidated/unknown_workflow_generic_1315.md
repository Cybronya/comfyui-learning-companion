---
name: unknown_workflow_generic_1315
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.379
common_nodes: [GetNode, LoadImage, SaveImage, SetNode]
problems: []
missing: []
members: [图片生成/图生图/九图合一_2021240272025292802.json, 图片生成/图生图/全能图片pro_Neo_xlw_2028742013948010498.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1315

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/九图合一_2021240272025292802.json、图片生成/图生图/全能图片pro_Neo_xlw_2028742013948010498.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：38%

## 共有节点

全部 2 个 workflow 都包含：
- `GetNode`
- `LoadImage`
- `SaveImage`
- `SetNode`

**可变部分**（部分 workflow 才有）：
- `NineGridMosaicNode` —— 1/2 个有
- `RH_Nano_Banana2_Image2Image` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
