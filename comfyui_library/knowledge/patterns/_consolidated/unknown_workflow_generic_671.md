---
name: unknown_workflow_generic_671
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.4005
common_nodes: [GetNode, LoadImage, RH_Nano_Banana2_Gemini31Flash, SaveImage, SetNode]
problems: []
missing: []
members: [图片生成/图生图/一键换装_2042786160912633857.json, 图片生成/图生图/一键提取服装_2042504590024773634.json, 图片生成/图生图/一键提取服装_2046059357334413314.json, 图片生成/文生图/全能图片V2_Neo_xlw_2028755810783858690.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_671

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/一键换装_2042786160912633857.json、图片生成/图生图/一键提取服装_2042504590024773634.json、图片生成/图生图/一键提取服装_2046059357334413314.json、图片生成/文生图/全能图片V2_Neo_xlw_2028755810783858690.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：40%

## 共有节点

全部 4 个 workflow 都包含：
- `GetNode`
- `LoadImage`
- `RH_Nano_Banana2_Gemini31Flash`
- `SaveImage`
- `SetNode`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `easy imageConcat` —— 3/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
