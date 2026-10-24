---
name: unknown_workflow_generic_851
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 1
common_nodes: [ImageCrop+, ImageTile+, LoadImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/6-宫格图拆分工作流_2038606289256845313.json, 图片生成/图生图/九宫格拆分成单图-标准版-（必收藏）_2052035279879450626.json, 图片生成/图生图/角色+场景+自动拆分单图_2054553084394778626.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_851

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/6-宫格图拆分工作流_2038606289256845313.json、图片生成/图生图/九宫格拆分成单图-标准版-（必收藏）_2052035279879450626.json、图片生成/图生图/角色+场景+自动拆分单图_2054553084394778626.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `ImageCrop+`
- `ImageTile+`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 2/3 个有
- `MathExpression|pysssss` —— 2/3 个有
- `RH_Nano_Banana2_Image2Image` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
