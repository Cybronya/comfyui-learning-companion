---
name: unknown_workflow_generic_326
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.753375
common_nodes: [1hew_MaskBatchToList, Bjornulf_LoopBasicBatch, Eden_Save_Param_Dict, LoadImage, LoadSAM3Model, PreviewAny, PrimitiveFloat, PrimitiveString, SaveImageWithAlpha, easy saveText]
problems: []
missing: []
members: [数字人/数字人/sam3组件-multitle3_2036880850557603842.json, 数字人/数字人/sam3组件-multitle4_2037263503836323842.json, 数字人/数字人/sam3组件-multitle5_2037902728327860225.json, 数字人/数字人/sam3组件-multitle6_2041777046006796289.json, 数字人/数字人/sam3组件-multitle7_2042214581564608514.json, 数字人/数字人/sam3组件-multitle8_2046255489444487169.json, 数字人/数字人/sam3组件-multitle9_2046807394075811841.json, 数字人/数字人/sam3组件-multitle_2032354223064616961.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_326

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/sam3组件-multitle3_2036880850557603842.json、数字人/数字人/sam3组件-multitle4_2037263503836323842.json、数字人/数字人/sam3组件-multitle5_2037902728327860225.json、数字人/数字人/sam3组件-multitle6_2041777046006796289.json、数字人/数字人/sam3组件-multitle7_2042214581564608514.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 8 个 workflow 都包含：
- `1hew_MaskBatchToList`
- `Bjornulf_LoopBasicBatch`
- `Eden_Save_Param_Dict`
- `LoadImage`
- `LoadSAM3Model`
- `PreviewAny`
- `PrimitiveFloat`
- `PrimitiveString`
- `SaveImageWithAlpha`
- `easy saveText`

**可变部分**（部分 workflow 才有）：
- `easy sam3ImageSegmentation` —— 7/8 个有
- `easy sam3ModelLoader` —— 7/8 个有
- `EmptyImage` —— 5/8 个有
- `GetImage_(Width&Height) _O` —— 5/8 个有
- `SAM3Segmentation` —— 3/8 个有
- `preview_mask` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
